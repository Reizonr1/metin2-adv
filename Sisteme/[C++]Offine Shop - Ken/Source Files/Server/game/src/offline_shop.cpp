/*
* Filename : offline_shop.cpp
* Version : 0.1
* Description : --
*/

#include "stdafx.h"
#include "../../libgame/include/grid.h"
#include "constants.h"
#include "utils.h"
#include "config.h"
#include "desc.h"
#include "desc_manager.h"
#include "char.h"
#include "char_manager.h"
#include "item.h"
#include "item_manager.h"
#include "buffer_manager.h"
#include "packet.h"
#include "log.h"
#include "db.h"
#include "questmanager.h"
#include "monarch.h"
#include "mob_manager.h"
#include "locale_service.h"
#include "offline_shop.h"
#include "p2p.h"


COfflineShop::COfflineShop() : m_pkOfflineShopNPC(NULL) {}


COfflineShop::~COfflineShop()
{
	TPacketGCShop pack;
	pack.header = HEADER_GC_OFFLINE_SHOP;
	pack.subheader = SHOP_SUBHEADER_GC_END;
	pack.size = sizeof(TPacketGCShop);

	Broadcast(&pack, sizeof(pack));

	for (GuestMapType::iterator it = m_map_guest.begin(); it != m_map_guest.end(); ++it)
	{
		LPCHARACTER ch = it->first;
		ch->SetOfflineShop(NULL);
	}
}

void COfflineShop::SetOfflineShopNPC(LPCHARACTER npc)
{
	m_pkOfflineShopNPC = npc;
}

bool COfflineShop::AddGuest(LPCHARACTER ch, LPCHARACTER npc)
{
	// If there is no ch, return false
	if (!ch)
		return false;

	// If ch is exchanging, return false
	if (ch->GetExchange())
		return false;

	// If target is shopping, return false
	if (ch->GetShop())
		return false;

	// If target is look at private shop, return false
	if (ch->GetMyShop())
		return false;

	// If target is look at offline shop, return false
	if (ch->GetOfflineShop())
		return false;
	
	// If the npc is nullptr, return false
	if (!npc)
		return false;

	// Start process
	ch->SetOfflineShop(this);
	m_map_guest.insert(GuestMapType::value_type(ch, false));

	TPacketGCShop pack;
	pack.header = HEADER_GC_OFFLINE_SHOP;
	pack.subheader = SHOP_SUBHEADER_GC_START;

	TPacketGCOfflineShopStart pack2;
	memset(&pack2, 0, sizeof(pack2));
	pack2.owner_vid = npc->GetVID();

	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT pos,count,vnum,price,socket0,socket1,socket2,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u", get_table_postfix(), npc->GetOfflineShopRealOwner()));
	if (pMsg->Get()->uiNumRows == 0)
	{
		DBManager::instance().DirectQuery("DELETE FROM player.offline_shop_npc WHERE owner_id = %u", npc->GetOfflineShopRealOwner());
		ch->SetOfflineShop(NULL);
		ch->SetOfflineShopOwner(NULL);
		M2_DESTROY_CHARACTER(npc);
		return false;
	}

	MYSQL_ROW row;
	while (NULL != (row = mysql_fetch_row(pMsg->Get()->pSQLResult)))
	{
		BYTE bPos = 0;
		str_to_number(bPos, row[0]);

		str_to_number(pack2.items[bPos].count, row[1]);
		str_to_number(pack2.items[bPos].vnum, row[2]);
		str_to_number(pack2.items[bPos].price, row[3]);

		DWORD alSockets[ITEM_SOCKET_MAX_NUM];
		for (int i = 0, n = 4; i < ITEM_SOCKET_MAX_NUM; ++i, n++)
			str_to_number(alSockets[i], row[n]);

		TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_MAX_NUM];
		for (int i = 0, iStartType = 7, iStartValue = 8; i < ITEM_ATTRIBUTE_MAX_NUM; ++i, iStartType += 2, iStartValue += 2)
		{
			str_to_number(aAttr[i].bType, row[iStartType]);
			str_to_number(aAttr[i].sValue, row[iStartValue]);
		}

		thecore_memcpy(pack2.items[bPos].alSockets, alSockets, sizeof(pack2.items[bPos].alSockets));
		thecore_memcpy(pack2.items[bPos].aAttr, aAttr, sizeof(pack2.items[bPos].aAttr));
	}

	pack.size = sizeof(pack) + sizeof(pack2);

	if (ch->GetDesc())
	{
		ch->GetDesc()->BufferedPacket(&pack, sizeof(TPacketGCShop));
		ch->GetDesc()->Packet(&pack2, sizeof(TPacketGCOfflineShopStart));
	}

	return true;
}

void COfflineShop::RemoveGuest(LPCHARACTER ch)
{
	// If this offline shop is not equal to this, break it
	if (ch->GetOfflineShop() != this)
		return;

	m_map_guest.erase(ch);
	ch->SetOfflineShop(NULL);

	TPacketGCShop pack;
	pack.header = HEADER_GC_OFFLINE_SHOP;
	pack.subheader = SHOP_SUBHEADER_GC_END;
	pack.size = sizeof(TPacketGCShop);

	if (ch->GetDesc())
		ch->GetDesc()->Packet(&pack, sizeof(pack));
}

void COfflineShop::RemoveAllGuest()
{
	TPacketGCShop pack;
	pack.header = HEADER_GC_OFFLINE_SHOP;
	pack.subheader = SHOP_SUBHEADER_GC_END;
	pack.size = sizeof(TPacketGCShop);

	Broadcast(&pack, sizeof(pack));

	for (GuestMapType::iterator it = m_map_guest.begin(); it != m_map_guest.end(); ++it)
	{
		LPCHARACTER ch = it->first;
		ch->SetOfflineShop(NULL);
	}
}

void COfflineShop::Destroy(LPCHARACTER npc)
{
	DBManager::instance().Query("DELETE FROM %soffline_shop_npc WHERE owner_id = %u", get_table_postfix(), npc->GetOfflineShopRealOwner());
	RemoveAllGuest();
	M2_DESTROY_CHARACTER(npc);
}

int COfflineShop::Buy(LPCHARACTER ch, BYTE bPos)
{
	if (ch->GetOfflineShopOwner()->GetOfflineShopRealOwner() == ch->GetPlayerID())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You can't buy anything from your offline shop.");
		return SHOP_SUBHEADER_GC_OK;
	}

	if (bPos >= OFFLINE_SHOP_HOST_ITEM_MAX_NUM)
	{
		sys_log(0, "OfflineShop::Buy : invalid position %d : %s", bPos, ch->GetName());
		return SHOP_SUBHEADER_GC_INVALID_POS;
	}

	sys_log(0, "OfflineShop::Buy : name %s pos %d", ch->GetName(), bPos);

	GuestMapType::iterator it = m_map_guest.find(ch);
	if (it == m_map_guest.end())
		return SHOP_SUBHEADER_GC_END;

	char szQuery[1024];
	snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,price,socket0,socket1,socket2,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetOfflineShopOwner()->GetOfflineShopRealOwner(), bPos);
	std::auto_ptr<SQLMsg> pMsg(DBManager::Instance().DirectQuery(szQuery));

	MYSQL_ROW row;

#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
	long long llPrice = 0;
#else
	DWORD dwPrice = 0;
#endif
	DWORD dwItemVnum = 0;
	BYTE bCount = 0;
	DWORD alSockets[ITEM_SOCKET_MAX_NUM];
	TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_MAX_NUM];

	while (NULL != (row = mysql_fetch_row(pMsg->Get()->pSQLResult)))
	{
		str_to_number(bCount, row[1]);
		str_to_number(dwItemVnum, row[2]);
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
		str_to_number(llPrice, row[3]);
#else
		str_to_number(dwPrice, row[3]);
#endif

		// Set Sockets
		for (int i = 0, n = 4; i < ITEM_SOCKET_MAX_NUM; ++i, n++)
			str_to_number(alSockets[i], row[n]);
		// End Of Sockets

		// Set Attributes
		for (int i = 0, iStartAttributeType = 7, iStartAttributeValue = 8; i < ITEM_ATTRIBUTE_MAX_NUM; ++i, iStartAttributeType += 2, iStartAttributeValue += 2)
		{
			str_to_number(aAttr[i].bType, row[iStartAttributeType]);
			str_to_number(aAttr[i].sValue, row[iStartAttributeValue]);
		}
		// End Of Set Attributes
	}

#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
	if (ch->GetGold() < static_cast<long long>(llPrice))
	{
		sys_log(1, "OfflineShop::Buy : Not enough money : %s has %u, price %lld", ch->GetName(), ch->GetGold(), llPrice);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}
#else
	if (ch->GetGold() < static_cast<int>(dwPrice))
	{
		sys_log(1, "OfflineShop::Buy : Not enough money : %s has %u, price %u", ch->GetName(), ch->GetGold(), dwPrice);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}
#endif

	LPITEM pItem = ITEM_MANAGER::Instance().CreateItem(dwItemVnum, bCount);
	if (!pItem)
		return SHOP_SUBHEADER_GC_SOLD_OUT;

	// Set Attributes, Sockets
	pItem->SetAttributes(aAttr);
	for (BYTE i = 0; i < ITEM_SOCKET_MAX_NUM; ++i)
		pItem->SetSocket(i, alSockets[i]);
	// End Of Set Attributes, Sockets

	// If item is a dragon soul item or normal item
	int iEmptyPos = 0;
	if (pItem->IsDragonSoul())
		iEmptyPos = ch->GetEmptyDragonSoulInventory(pItem);
	else
		iEmptyPos = ch->GetEmptyInventory(pItem->GetSize());

	// If iEmptyPos is less than 0, return inventory is full
	if (iEmptyPos < 0)
		return SHOP_SUBHEADER_GC_INVENTORY_FULL;

	// If item is a dragon soul, add this item in dragon soul inventory
	if (pItem->IsDragonSoul())
		pItem->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
	else
		pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));

	if (pItem)
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
		sys_log(0, "OFFLINE_SHOP: BUY: name %s %s(x %u):%u price %lld", ch->GetName(), pItem->GetName(), pItem->GetCount(), pItem->GetID(), llPrice);
#else
		sys_log(0, "OFFLINE_SHOP: BUY: name %s %s(x %u):%u price %u", ch->GetName(), pItem->GetName(), pItem->GetCount(), pItem->GetID(), dwPrice);
#endif


	// Check if the player is online
	LPCHARACTER tch = CHARACTER_MANAGER::instance().FindByPID(ch->GetOfflineShopOwner()->GetOfflineShopRealOwner());
	if (tch)
	{
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
		bool bIsOverFlow = tch->GetGold() + llPrice > GOLD_MAX - 1 ? true : false;
#else
		bool bIsOverFlow = tch->GetGold() + dwPrice > GOLD_MAX - 1 ? true : false;
#endif
		if (bIsOverFlow)
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
			DBManager::instance().Query("UPDATE player.player SET money = money + %lld WHERE id = %u", llPrice, ch->GetOfflineShopOwner()->GetOfflineShopRealOwner());
#else
			DBManager::instance().Query("UPDATE player.player SET money = money + %u WHERE id = %u", dwPrice, ch->GetOfflineShopOwner()->GetOfflineShopRealOwner());
#endif
		else
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
			tch->PointChange(POINT_GOLD, llPrice, false);
#else
			tch->PointChange(POINT_GOLD, dwPrice, false);
#endif
		tch->ChatPacket(CHAT_TYPE_INFO, "%s person bought %s from your offline shop.", ch->GetName(), pItem->GetName());
	}
	else
	{
		const CCI * pkCCI = P2P_MANAGER::Instance().FindByPID(ch->GetOfflineShopOwner()->GetOfflineShopRealOwner());
		if (!pkCCI || !pkCCI->pkDesc)
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
			DBManager::instance().Query("UPDATE player.player SET money = money + %lld WHERE id = %u", llPrice, ch->GetOfflineShopOwner()->GetOfflineShopRealOwner());
#else
			DBManager::instance().Query("UPDATE player.player SET money = money + %u WHERE id = %u", dwPrice, ch->GetOfflineShopOwner()->GetOfflineShopRealOwner());
#endif
		else
		{
			if (!pkCCI->pkDesc->GetCharacter())
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
				DBManager::instance().Query("UPDATE player.player SET money = money + %lld WHERE id = %u", llPrice, ch->GetOfflineShopOwner()->GetOfflineShopRealOwner());
#else
				DBManager::instance().Query("UPDATE player.player SET money = money + %u WHERE id = %u", dwPrice, ch->GetOfflineShopOwner()->GetOfflineShopRealOwner());
#endif
			else
			{
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP	
				bool bIsOverFlow = pkCCI->pkDesc->GetCharacter()->GetGold() + llPrice > GOLD_MAX - 1 ? true : false;
				if (bIsOverFlow)
					DBManager::instance().Query("UPDATE player.player SET money = money + %lld WHERE id = %u", llPrice, ch->GetOfflineShopOwner()->GetOfflineShopRealOwner());
				else
					pkCCI->pkDesc->GetCharacter()->PointChange(POINT_GOLD, llPrice, false);
#else
				bool bIsOverFlow = pkCCI->pkDesc->GetCharacter()->GetGold() + dwPrice > GOLD_MAX - 1 ? true : false;
				if (bIsOverFlow)
					DBManager::instance().Query("UPDATE player.player SET money = money + %u WHERE id = %u", dwPrice, ch->GetOfflineShopOwner()->GetOfflineShopRealOwner());
				else
					pkCCI->pkDesc->GetCharacter()->PointChange(POINT_GOLD, dwPrice, false);
#endif
				pkCCI->pkDesc->GetCharacter()->ChatPacket(CHAT_TYPE_INFO, "%s person bought %s from your offline shop.", ch->GetName(), pItem->GetName());
			}
		}
	}

	ITEM_MANAGER::instance().FlushDelayedSave(pItem);
	RemoveItem(ch->GetOfflineShopOwner()->GetOfflineShopRealOwner(), bPos);
	BroadcastUpdateItem(bPos, ch->GetOfflineShopOwner()->GetOfflineShopRealOwner(), true);
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
	ch->PointChange(POINT_GOLD, -llPrice, false);
#else
	ch->PointChange(POINT_GOLD, -dwPrice, false);
#endif
	ch->Save();
	LogManager::instance().ItemLog(ch, pItem, "BUY ITEM FROM OFFLINE SHOP", "");

	BYTE bLeftItemCount = GetLeftItemCount(ch->GetOfflineShopOwner()->GetOfflineShopRealOwner());
	if (bLeftItemCount == 0)
		Destroy(ch->GetOfflineShopOwner());

	return (SHOP_SUBHEADER_GC_OK);
}

void COfflineShop::BroadcastUpdateItem(BYTE bPos, DWORD dwPID, bool bDestroy)
{
	TPacketGCShop pack;
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
	TPacketGCOfflineShopUpdateItem pack2;
#else
	TPacketGCShopUpdateItem pack2;
#endif

	TEMP_BUFFER buf;

	pack.header = HEADER_GC_OFFLINE_SHOP;
	pack.subheader = SHOP_SUBHEADER_GC_UPDATE_ITEM;
	pack.size = sizeof(pack) + sizeof(pack2);
	pack2.pos = bPos;

	if (bDestroy)
	{
		pack2.item.vnum = 0;
		pack2.item.count = 0;
		pack2.item.price = 0;
		memset(pack2.item.alSockets, 0, sizeof(pack2.item.alSockets));
		memset(pack2.item.aAttr, 0, sizeof(pack2.item.aAttr));
	}
	else
	{
		char szQuery[1024];
		snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,price,socket0,socket1,socket2,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), dwPID, bPos);
		std::auto_ptr<SQLMsg> pMsg(DBManager::Instance().DirectQuery(szQuery));
		MYSQL_ROW row;
		while (NULL != (row = mysql_fetch_row(pMsg->Get()->pSQLResult)))
		{
			str_to_number(pack2.item.count, row[1]);
			str_to_number(pack2.item.vnum, row[2]);
			str_to_number(pack2.item.price, row[3]);

			// Set Sockets
			for (int i = 0, n = 4; i < ITEM_SOCKET_MAX_NUM; ++i, n++)
				str_to_number(pack2.item.alSockets[i], row[n]);
			// End Of Sockets

			// Set Attributes
			for (int i = 0, iStartAttributeType = 7, iStartAttributeValue = 8; i < ITEM_ATTRIBUTE_MAX_NUM; ++i, iStartAttributeType += 2, iStartAttributeValue += 2)
			{
				str_to_number(pack2.item.aAttr[i].bType, row[iStartAttributeType]);
				str_to_number(pack2.item.aAttr[i].sValue, row[iStartAttributeValue]);
			}
			// End Of Set Attributes
		}
	}

	buf.write(&pack, sizeof(pack));
	buf.write(&pack2, sizeof(pack2));
	Broadcast(buf.read_peek(), buf.size());
}

void COfflineShop::BroadcastUpdatePrice(BYTE bPos, DWORD dwPrice)
{
	TPacketGCShop pack;
	TPacketGCShopUpdatePrice pack2;

	TEMP_BUFFER buf;

	pack.header = HEADER_GC_OFFLINE_SHOP;
	pack.subheader = SHOP_SUBHEADER_GC_UPDATE_PRICE;
	pack.size = sizeof(pack) + sizeof(pack2);

	pack2.bPos = bPos;
	pack2.iPrice = dwPrice;

	buf.write(&pack, sizeof(pack));
	buf.write(&pack2, sizeof(pack2));

	Broadcast(buf.read_peek(), buf.size());
}

void COfflineShop::Refresh(LPCHARACTER ch)
{
	TPacketGCShop pack;
	pack.header = HEADER_GC_OFFLINE_SHOP;
	pack.subheader = SHOP_SUBHEADER_GC_UPDATE_ITEM2;

	TPacketGCOfflineShopStart pack2;
	memset(&pack2, 0, sizeof(pack2));
	pack2.owner_vid = 0;

	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT pos,count,vnum,price,socket0,socket1,socket2,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u", get_table_postfix(), ch->GetPlayerID()));

	MYSQL_ROW row;
	while (NULL != (row = mysql_fetch_row(pMsg->Get()->pSQLResult)))
	{
		BYTE bPos = 0;
		str_to_number(bPos, row[0]);

		str_to_number(pack2.items[bPos].count, row[1]);
		str_to_number(pack2.items[bPos].vnum, row[2]);
		str_to_number(pack2.items[bPos].price, row[3]);

		DWORD alSockets[ITEM_SOCKET_MAX_NUM];
		for (int i = 0, n = 4; i < ITEM_SOCKET_MAX_NUM; ++i, n++)
			str_to_number(alSockets[i], row[n]);

		TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_MAX_NUM];
		for (int i = 0, iStartType = 7, iStartValue = 8; i < ITEM_ATTRIBUTE_MAX_NUM; ++i, iStartType += 2, iStartValue += 2)
		{
			str_to_number(aAttr[i].bType, row[iStartType]);
			str_to_number(aAttr[i].sValue, row[iStartValue]);
		}

		thecore_memcpy(pack2.items[bPos].alSockets, alSockets, sizeof(pack2.items[bPos].alSockets));
		thecore_memcpy(pack2.items[bPos].aAttr, aAttr, sizeof(pack2.items[bPos].aAttr));
	}

	pack.size = sizeof(pack) + sizeof(pack2);

	if (ch->GetDesc())
	{
		ch->GetDesc()->BufferedPacket(&pack, sizeof(TPacketGCShop));
		ch->GetDesc()->Packet(&pack2, sizeof(TPacketGCOfflineShopStart));
	}
}

bool COfflineShop::RemoveItem(DWORD dwVID, BYTE bPos)
{
	DBManager::instance().Query("DELETE FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), dwVID, bPos);
	return true;
}

BYTE COfflineShop::GetLeftItemCount(DWORD dwPID)
{
	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT COUNT(*) FROM %soffline_shop_item WHERE owner_id = %u and status = 0", get_table_postfix(), dwPID));
	if (pMsg->Get()->uiNumRows == 0)
		return 0;

	MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
	BYTE bCount = 0;
	str_to_number(bCount, row[0]);
	return bCount;
}

void COfflineShop::Broadcast(const void * data, int bytes)
{
	sys_log(1, "OfflineShop::Broadcast %p %d", data, bytes);

	for (GuestMapType::iterator it = m_map_guest.begin(); it != m_map_guest.end(); ++it)
	{
		LPCHARACTER ch = it->first;
		if (ch->GetDesc())
			ch->GetDesc()->Packet(data, bytes);
	}
}
