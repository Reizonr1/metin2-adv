#include "stdafx.h"
#include "../../libgame/include/grid.h"
#include "constants.h"
#include "utils.h"
#include "config.h"
#include "offline_shop.h"
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
#include "desc_client.h"
#include "group_text_parse_tree.h"
#include <boost/algorithm/string/predicate.hpp>
#include <cctype>
#include "offlineshop_manager.h"
#include "p2p.h"
#include "entity.h"
#include "sectree_manager.h"
#include "offlineshop_config.h"


COfflineShopManager::COfflineShopManager()
{
}


COfflineShopManager::~COfflineShopManager()
{
}

struct FFindOfflineShop
{
	const char * szName;

	DWORD dwVID, dwRealOwner;
	FFindOfflineShop(const char * c_szName) : szName(c_szName), dwVID(0), dwRealOwner(0) {};

	void operator()(LPENTITY ent)
	{
		if (!ent)
			return;

		if (ent->IsType(ENTITY_CHARACTER))
		{
			LPCHARACTER ch = (LPCHARACTER)ent;
			if (ch->IsOfflineShopNPC() && !strcmp(szName, ch->GetName()))
			{
				dwVID = ch->GetVID();
				dwRealOwner = ch->GetOfflineShopRealOwner();
				M2_DESTROY_CHARACTER(ch);
			}
		}
	}
};

bool COfflineShopManager::StartShopping(LPCHARACTER pkChr, LPCHARACTER pkChrShopKeeper)
{
	if (pkChr->GetOfflineShopOwner() == pkChrShopKeeper)
		return false;

	if (pkChrShopKeeper->IsPC())
		return false;

	sys_log(0, "OFFLINE_SHOP: START: %s", pkChr->GetName());
	return true;
}

LPOFFLINESHOP COfflineShopManager::CreateOfflineShop(LPCHARACTER npc, DWORD dwOwnerPID)
{
	if (FindOfflineShop(npc->GetVID()))
		return NULL;

	LPOFFLINESHOP pkOfflineShop = M2_NEW COfflineShop;
	pkOfflineShop->SetOfflineShopNPC(npc);

	m_map_pkOfflineShopByNPC.insert(TShopMap::value_type(npc->GetVID(), pkOfflineShop));
	m_Map_pkOfflineShopByNPC2.insert(TOfflineShopMap::value_type(dwOwnerPID, npc->GetVID()));
	return pkOfflineShop;
}

LPOFFLINESHOP COfflineShopManager::FindOfflineShop(DWORD dwVID)
{
	TShopMap::iterator it = m_map_pkOfflineShopByNPC.find(dwVID);

	if (it == m_map_pkOfflineShopByNPC.end())
		return NULL;

	return it->second;
}

void COfflineShopManager::DestroyOfflineShop(LPCHARACTER ch, DWORD dwVID, bool bDestroyAll)
{
	if (dwVID == 0 && ch)
	{
		std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT mapIndex, channel FROM %soffline_shop_npc WHERE owner_id = %u", get_table_postfix(), ch->GetPlayerID()));
		if (pMsg->Get()->uiNumRows == 0)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You can't use this option because you don't have offline shop npc!");
			return;
		}

		ch->SetOfflineShopVID(0);
		ch->SetOfflineShopStatus(0);

		MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
		long lMapIndex = 0;
		str_to_number(lMapIndex, row[0]);

		TPacketGGRemoveOfflineShop p;
		p.bHeader = HEADER_GG_REMOVE_OFFLINE_SHOP;
		p.lMapIndex = lMapIndex;

		// Set offline shop name
		char szNpcName[CHARACTER_NAME_MAX_LEN + 1];
		snprintf(szNpcName, sizeof(szNpcName), "%s's offline shop", ch->GetName());
		strlcpy(p.szNpcName, szNpcName, sizeof(p.szNpcName));
		// End Of Set offline shop name

		P2P_MANAGER::instance().Send(&p, sizeof(TPacketGGRemoveOfflineShop));
		DBManager::instance().DirectQuery("UPDATE %soffline_shop_item SET status = 1 WHERE owner_id = %u and status = 0", get_table_postfix(), ch->GetPlayerID());
	}
	else if (dwVID && ch)
	{
		ch->SetOfflineShopVID(0);
		ch->SetOfflineShopStatus(0);

		LPCHARACTER npc = CHARACTER_MANAGER::instance().Find(dwVID);
		if (!npc)
			npc = CHARACTER_MANAGER::instance().Find(FindMyOfflineShop(ch->GetPlayerID()));
		
		if (!npc)
		{
			std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT mapIndex,channel FROM %soffline_shop_npc WHERE owner_id = %u", get_table_postfix(), ch->GetPlayerID()));
			if (pMsg->Get()->uiNumRows == 0)
			{
				ch->ChatPacket(CHAT_TYPE_INFO, "You can't use this option because you don't have offline shop npc!");
				return;
			}

			MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);

			long lMapIndex = 0;
			str_to_number(lMapIndex, row[0]);

			BYTE bChannel = 0;
			str_to_number(bChannel, row[1]);

			if (g_bChannel != bChannel)
			{
				ch->ChatPacket(CHAT_TYPE_INFO, "You can't close your offline shop from %d channel. You must login %d channel", g_bChannel, bChannel);
				return;
			}

			char szName[CHARACTER_NAME_MAX_LEN + 1];
			snprintf(szName, sizeof(szName), "%s's offline shop", ch->GetName());
			LPSECTREE_MAP pMap = SECTREE_MANAGER::instance().GetMap(lMapIndex);
			FFindOfflineShop offlineShop(szName);
			pMap->for_each(offlineShop);

			if (bDestroyAll)
			{
				DBManager::instance().DirectQuery("UPDATE %soffline_shop_item SET status = 1 WHERE owner_id = %u and status = 0", get_table_postfix(), ch->GetPlayerID());
				m_map_pkOfflineShopByNPC.erase(offlineShop.dwVID);
				m_Map_pkOfflineShopByNPC2.erase(offlineShop.dwRealOwner);
				DBManager::instance().DirectQuery("DELETE FROM %soffline_shop_npc WHERE owner_id = %u", get_table_postfix(), offlineShop.dwRealOwner);
				return;
			}
		}

		LPOFFLINESHOP pkOfflineShop = FindOfflineShop(dwVID);
		if (!pkOfflineShop)
			pkOfflineShop = FindOfflineShop(FindMyOfflineShop(ch->GetPlayerID()));
		
		if (!pkOfflineShop)
			return;

		if (npc->GetOfflineShopChannel() != g_bChannel)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You can't close your offline shop from %d channel. You must login %d channel", g_bChannel, npc->GetOfflineShopChannel());
			return;
		}

		if (bDestroyAll)
		{
			DBManager::instance().DirectQuery("UPDATE %soffline_shop_item SET status = 1 WHERE owner_id = %u and status = 0", get_table_postfix(), ch->GetPlayerID());
			pkOfflineShop->Destroy(npc);
		}

		m_map_pkOfflineShopByNPC.erase(npc->GetVID());
		m_Map_pkOfflineShopByNPC2.erase(npc->GetOfflineShopRealOwner());
	}
}

#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
void COfflineShopManager::AddItem(LPCHARACTER ch, BYTE bDisplayPos, BYTE bPos, long long llPrice)
#else
void COfflineShopManager::AddItem(LPCHARACTER ch, BYTE bDisplayPos, BYTE bPos, int iPrice)
#endif
{
	if (!ch)
		return;

	// Fixed bug 6.21.2015
	if (bDisplayPos >= OFFLINE_SHOP_HOST_ITEM_MAX_NUM)
	{
		sys_err("Overflow offline shop slot count [%s]", ch->GetName());
		return;
	}
	// End Of fixed bug 6.21.2015

#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
	if (llPrice >= GOLD_MAX)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You can't add this item because of the overflow gold max!");
		return;
	}
#else
	if (iPrice >= GOLD_MAX - 1)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You can't add this item because of the overflow gold max!");
		return;
	}
#endif
	
	// Check player has offline shop or not
	std::auto_ptr<SQLMsg> pmsg(DBManager::instance().DirectQuery("SELECT COUNT(*) FROM player.offline_shop_npc WHERE owner_id = %u", ch->GetPlayerID()));
	MYSQL_ROW row = mysql_fetch_row(pmsg->Get()->pSQLResult);
	
	BYTE bResult = 0;
	str_to_number(bResult, row[0]);
	
	if (!bResult)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You can't use this option because you don't have a offline shop!");
		return;
	}
	// End Of Check player has offline shop or not

	LPITEM pkItem = ch->GetInventoryItem(bPos);
	
	if (!pkItem)
		return;

	// Check
	const TItemTable * itemTable = pkItem->GetProto();
	if (IS_SET(itemTable->dwAntiFlags, ITEM_ANTIFLAG_GIVE | ITEM_ANTIFLAG_MY_OFFLINE_SHOP))
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "This item is not tradeable!");
		return;
	}

	if (pkItem->isLocked())
		return;

	if (pkItem->IsEquipped())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You can't sell equipped items!");
		return;
	}

	char szColumns[QUERY_MAX_LEN], szValues[QUERY_MAX_LEN];

	int iLen = snprintf(szColumns, sizeof(szColumns), "id,owner_id,pos,count,price,vnum");
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
	int iUpdateLen = snprintf(szValues, sizeof(szValues), "%u,%u,%d,%u,%lld,%u", pkItem->GetID(), ch->GetPlayerID(), bDisplayPos, pkItem->GetCount(), llPrice, pkItem->GetVnum());
#else
	int iUpdateLen = snprintf(szValues, sizeof(szValues), "%u,%u,%d,%u,%d,%u", pkItem->GetID(), ch->GetPlayerID(), bDisplayPos, pkItem->GetCount(), iPrice, pkItem->GetVnum());
#endif

	if (g_bOfflineShopSocketMax == 3)
	{
		iLen += snprintf(szColumns + iLen, sizeof(szColumns) - iLen, ",socket0,socket1,socket2");
		iUpdateLen += snprintf(szValues + iUpdateLen, sizeof(szValues) - iUpdateLen, ",%ld,%ld,%ld", pkItem->GetSocket(0), pkItem->GetSocket(1), pkItem->GetSocket(2));
	}
	else if(g_bOfflineShopSocketMax == 4)
	{
		iLen += snprintf(szColumns + iLen, sizeof(szColumns) - iLen, ",socket0,socket1,socket2,socket3");
		iUpdateLen += snprintf(szValues + iUpdateLen, sizeof(szValues) - iUpdateLen, ",%ld,%ld,%ld,%ld", pkItem->GetSocket(0), pkItem->GetSocket(1), pkItem->GetSocket(2), pkItem->GetSocket(3));		
	}
	else if(g_bOfflineShopSocketMax == 5)
	{
		iLen += snprintf(szColumns + iLen, sizeof(szColumns) - iLen, ",socket0,socket1,socket2,socket3,socket4");
		iUpdateLen += snprintf(szValues + iUpdateLen, sizeof(szValues) - iUpdateLen, ",%ld,%ld,%ld,%ld,%ld", pkItem->GetSocket(0), pkItem->GetSocket(1), pkItem->GetSocket(2), pkItem->GetSocket(3), pkItem->GetSocket(4));		
	}
	else if(g_bOfflineShopSocketMax == 6)
	{
		iLen += snprintf(szColumns + iLen, sizeof(szColumns) - iLen, ",socket0,socket1,socket2,socket3,socket4,socket5");
		iUpdateLen += snprintf(szValues + iUpdateLen, sizeof(szValues) - iUpdateLen, ",%ld,%ld,%ld,%ld,%ld,%ld", pkItem->GetSocket(0), pkItem->GetSocket(1), pkItem->GetSocket(2), pkItem->GetSocket(3), pkItem->GetSocket(4), pkItem->GetSocket(5));		
	}

	iLen += snprintf(szColumns + iLen, sizeof(szColumns) - iLen, ",attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4");
	iUpdateLen += snprintf(szValues + iUpdateLen, sizeof(szValues) - iUpdateLen, ",%d,%d,%d,%d,%d,%d,%d,%d,%d,%d",
		pkItem->GetAttributeType(0), pkItem->GetAttributeValue(0),
		pkItem->GetAttributeType(1), pkItem->GetAttributeValue(1),
		pkItem->GetAttributeType(2), pkItem->GetAttributeValue(2),
		pkItem->GetAttributeType(3), pkItem->GetAttributeValue(3),
		pkItem->GetAttributeType(4), pkItem->GetAttributeValue(4));

	char szInsertQuery[QUERY_MAX_LEN];
	snprintf(szInsertQuery, sizeof(szInsertQuery), "INSERT INTO %soffline_shop_item (%s) VALUES (%s)", get_table_postfix(), szColumns, szValues);
	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery(szInsertQuery));
	ch->ChatPacket(CHAT_TYPE_INFO, "You added %s item in your offline-shop", pkItem->GetName());
	pkItem->RemoveFromCharacter();
	
	LPCHARACTER npc = CHARACTER_MANAGER::instance().Find(FindMyOfflineShop(ch->GetPlayerID()));
	if (!npc)
		return;

	LPOFFLINESHOP pkOfflineShop = FindOfflineShop(npc->GetVID());
	if (!pkOfflineShop)
		return;

	pkOfflineShop->BroadcastUpdateItem(bDisplayPos, ch->GetPlayerID());
	LogManager::instance().ItemLog(ch, pkItem, "ADD ITEM OFFLINE SHOP", "");
}

void COfflineShopManager::RemoveItem(LPCHARACTER ch, BYTE bPos)
{
	if (!ch)
		return;

	if (bPos >= OFFLINE_SHOP_HOST_ITEM_MAX_NUM)
	{
		sys_log(0, "OfflineShopManager::RemoveItem - Overflow slot! [%s]", ch->GetName());
		return;
	}

	LPCHARACTER npc = CHARACTER_MANAGER::instance().Find(FindMyOfflineShop(ch->GetPlayerID()));

	// Check npc
	if (!npc)
	{
		char szQuery[1024];
		
		if (g_bOfflineShopSocketMax == 3)
			snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,socket0,socket1,socket2,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);
		else if(g_bOfflineShopSocketMax == 4)
			snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,socket0,socket1,socket2,socket3,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);			
		else if(g_bOfflineShopSocketMax == 5)
			snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,socket0,socket1,socket2,socket3,socket4,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);			
		else if(g_bOfflineShopSocketMax == 6)
			snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,socket0,socket1,socket2,socket3,socket4,socket5,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);			
			
		std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery(szQuery));
		if (pMsg->Get()->uiNumRows == 0)
		{
			sys_log(0, "OfflineShopManager::RemoveItem - This slot is empty! [%s]", ch->GetName());
			return;
		}

		TPlayerItem item;
		int rows;
		if (!(rows = mysql_num_rows(pMsg->Get()->pSQLResult)))
			return;

		for (int i = 0; i < rows; ++i)
		{
			MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
			int cur = 0;

			str_to_number(item.pos, row[cur++]);
			str_to_number(item.count, row[cur++]);
			str_to_number(item.vnum, row[cur++]);
			for (BYTE a = 0; a < ITEM_SOCKET_MAX_NUM; a++)
				str_to_number(item.alSockets[a], row[cur++]);

			for (int j = 0; j < ITEM_ATTRIBUTE_MAX_NUM; j++)
			{
				str_to_number(item.aAttr[j].bType, row[cur++]);
				str_to_number(item.aAttr[j].sValue, row[cur++]);
			}
		}

		LPITEM pItem = ITEM_MANAGER::instance().CreateItem(item.vnum, item.count);
		if (!pItem)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "There is problem in the system at the moment. Please try again!");
			return;
		}

		pItem->SetAttributes(item.aAttr);
		pItem->SetSockets(item.alSockets);

		int iEmptyPos;
		if (pItem->IsDragonSoul())
			iEmptyPos = ch->GetEmptyDragonSoulInventory(pItem);
		else
			iEmptyPos = ch->GetEmptyInventory(pItem->GetSize());

		if (iEmptyPos < 0)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You don't have enough space for store the item!");
			return;
		}

		if (pItem->IsDragonSoul())
			pItem->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
		else
			pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));

		DBManager::instance().DirectQuery("DELETE FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);
		LogManager::instance().ItemLog(ch, pItem, "DELETE OFFLINE SHOP ITEM", "");
		ch->ChatPacket(CHAT_TYPE_INFO, "You removed %s item in your offline-shop.", pItem->GetName());
	}
	else
	{
		LPOFFLINESHOP pkOfflineShop = npc->GetOfflineShop();

		// Check pkOfflineShop
		if (!pkOfflineShop)
			return;
		
		char szQuery[1024];
		if (g_bOfflineShopSocketMax == 3)
			snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,socket0,socket1,socket2,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);
		else if(g_bOfflineShopSocketMax == 4)
			snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,socket0,socket1,socket2,socket3,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);
		else if(g_bOfflineShopSocketMax == 5)
			snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,socket0,socket1,socket2,socket3,socket4,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);
		else if(g_bOfflineShopSocketMax == 6)
			snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,socket0,socket1,socket2,socket3,socket4,socket5,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);

		std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery(szQuery));
		if (pMsg->Get()->uiNumRows == 0)
		{
			sys_log(0, "OfflineShopManager::RemoveItem - This slot is empty! [%s]", ch->GetName());
			return;
		}

		TPlayerItem item;
		int rows;
		if (!(rows = mysql_num_rows(pMsg->Get()->pSQLResult)))
			return;

		for (int i = 0; i < rows; ++i)
		{
			MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
			int cur = 0;

			str_to_number(item.pos, row[cur++]);
			str_to_number(item.count, row[cur++]);
			str_to_number(item.vnum, row[cur++]);
			for (BYTE a = 0; a < ITEM_SOCKET_MAX_NUM; a++)
				str_to_number(item.alSockets[a], row[cur++]);

			for (int j = 0; j < ITEM_ATTRIBUTE_MAX_NUM; j++)
			{
				str_to_number(item.aAttr[j].bType, row[cur++]);
				str_to_number(item.aAttr[j].sValue, row[cur++]);
			}
		}

		LPITEM pItem = ITEM_MANAGER::instance().CreateItem(item.vnum, item.count);
		if (!pItem)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "There is problem in the system at the moment. Please try again!");
			return;
		}

		pItem->SetAttributes(item.aAttr);
		pItem->SetSockets(item.alSockets);

		int iEmptyPos;
		if (pItem->IsDragonSoul())
			iEmptyPos = ch->GetEmptyDragonSoulInventory(pItem);
		else
			iEmptyPos = ch->GetEmptyInventory(pItem->GetSize());

		if (iEmptyPos < 0)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You don't have enough space for store the item!");
			return;
		}

		if (pItem->IsDragonSoul())
			pItem->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
		else
			pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));

		DBManager::instance().DirectQuery("DELETE FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);
		pkOfflineShop->BroadcastUpdateItem(bPos, ch->GetPlayerID(), true);

		if (LeftItemCount(ch) == 0)	
			pkOfflineShop->Destroy(npc);
		
		LogManager::instance().ItemLog(ch, pItem, "DELETE OFFLINE SHOP ITEM", "");
		ch->ChatPacket(CHAT_TYPE_INFO, "You removed %s item in your offline-shop.", pItem->GetName());
	}
}

#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
void COfflineShopManager::ChangePrice(LPCHARACTER ch, BYTE bPos, long long llPrice)
#else
void COfflineShopManager::ChangePrice(LPCHARACTER ch, BYTE bPos, DWORD dwPrice)
#endif
{
	if (!ch)
		return;

	if (bPos >= OFFLINE_SHOP_HOST_ITEM_MAX_NUM)
	{
		sys_err("Offlineshop overflow slot count [%s][%d]", ch->GetName(), bPos);
		return;
	}

#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
	if (llPrice >= GOLD_MAX)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You can't change price of the item because of the overflow gold max!");
		return;
	}
#else
	if (dwPrice >= GOLD_MAX - 1)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You can't change price of the item because of the overflow gold max!");
		return;
	}
#endif

	LPOFFLINESHOP pkOfflineShop = FindOfflineShop(FindMyOfflineShop(ch->GetPlayerID()));
	if (pkOfflineShop)
	{
		pkOfflineShop->RemoveAllGuest();
#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
		pkOfflineShop->BroadcastUpdatePrice(bPos, llPrice);
#else
		pkOfflineShop->BroadcastUpdatePrice(bPos, dwPrice);
#endif
	}

#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
	DBManager::instance().DirectQuery("UPDATE %soffline_shop_item SET price = %lld WHERE owner_id = %u and pos = %d", get_table_postfix(), llPrice, ch->GetPlayerID(), bPos);
#else
	DBManager::instance().DirectQuery("UPDATE %soffline_shop_item SET price = %u WHERE owner_id = %u and pos = %d", get_table_postfix(), dwPrice, ch->GetPlayerID(), bPos);
#endif
}

void COfflineShopManager::Refresh(LPCHARACTER ch)
{
	if (!ch)
		return;

	LPCHARACTER npc = CHARACTER_MANAGER::instance().Find(FindMyOfflineShop(ch->GetPlayerID()));
	if (!npc)
	{
		TPacketGCShop pack;
		pack.header = HEADER_GC_OFFLINE_SHOP;
		pack.subheader = SHOP_SUBHEADER_GC_UPDATE_ITEM2;

		TPacketGCOfflineShopStart pack2;
		memset(&pack2, 0, sizeof(pack2));
		pack2.owner_vid = 0;

		char szQuery[1024];
		if (g_bOfflineShopSocketMax == 3)
			snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,price,socket0,socket1,socket2,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and status = 0", get_table_postfix(), ch->GetPlayerID());
		else if(g_bOfflineShopSocketMax == 4)
			snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,price,socket0,socket1,socket2,socket3,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and status = 0", get_table_postfix(), ch->GetPlayerID());
		else if(g_bOfflineShopSocketMax == 5)
			snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,price,socket0,socket1,socket2,socket3,socket4,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and status = 0", get_table_postfix(), ch->GetPlayerID());
		else if(g_bOfflineShopSocketMax == 6)
			snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,price,socket0,socket1,socket2,socket3,socket4,socket5,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and status = 0", get_table_postfix(), ch->GetPlayerID());

		std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery(szQuery));

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
	else
	{
		LPOFFLINESHOP pkOfflineShop = npc->GetOfflineShop();
		if (!pkOfflineShop)
			return;

		pkOfflineShop->Refresh(ch);
	}
}

void COfflineShopManager::RefreshMoney(LPCHARACTER ch)
{
	if (!ch)
		return;

	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT money FROM player.player WHERE id = %u", ch->GetPlayerID()));

	TPacketGCShop p;
	TPacketGCOfflineShopMoney p2;

	p.header = HEADER_GC_OFFLINE_SHOP;
	p.subheader = SHOP_SUBHEADER_GC_REFRESH_MONEY;

	if (pMsg->Get()->uiNumRows == 0)
	{
		p2.llMoney = 0;
		p.size = sizeof(p) + sizeof(p2);
		if (ch->GetDesc())
		{
			ch->GetDesc()->BufferedPacket(&p, sizeof(TPacketGCShop));
			ch->GetDesc()->Packet(&p2, sizeof(TPacketGCOfflineShopMoney));
		}
	}
	else
	{
		MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
		str_to_number(p2.llMoney, row[0]);
		p.size = sizeof(p) + sizeof(p2);
		if (ch->GetDesc())
		{
			ch->GetDesc()->BufferedPacket(&p, sizeof(TPacketGCShop));
			ch->GetDesc()->Packet(&p2, sizeof(TPacketGCOfflineShopMoney));
		}
	}
}	

void COfflineShopManager::RefreshUnsoldItems(LPCHARACTER ch)
{
	TPacketGCShop pack;
	pack.header = HEADER_GC_OFFLINE_SHOP;
	pack.subheader = SHOP_SUBHEADER_GC_UPDATE_ITEM2;

	TPacketGCOfflineShopStart pack2;
	memset(&pack2, 0, sizeof(pack2));
	pack2.owner_vid = 0;

	char szQuery[1024];
	if (g_bOfflineShopSocketMax == 3)
		snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,price,socket0,socket1,socket2,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and status = 1", get_table_postfix(), ch->GetPlayerID());
	else if (g_bOfflineShopSocketMax == 4)
		snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,price,socket0,socket1,socket2,socket3,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and status = 1", get_table_postfix(), ch->GetPlayerID());
	else if (g_bOfflineShopSocketMax == 5)
		snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,price,socket0,socket1,socket2,socket3,socket4,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and status = 1", get_table_postfix(), ch->GetPlayerID());
	else if (g_bOfflineShopSocketMax == 6)
		snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,price,socket0,socket1,socket2,socket3,socket4,socket5,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and status = 1", get_table_postfix(), ch->GetPlayerID());

	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery(szQuery));

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

void COfflineShopManager::TakeItem(LPCHARACTER ch, BYTE bPos)
{
	if (bPos >= OFFLINE_SHOP_HOST_ITEM_MAX_NUM)
		return;

	if (ch->GetOfflineShop() || ch->GetOfflineShopOwner())
		return;

	char szQuery[1024];

	if (g_bOfflineShopSocketMax == 3)
		snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,socket0,socket1,socket2,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);
	else if (g_bOfflineShopSocketMax == 4)
		snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,socket0,socket1,socket2,socket3,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);
	else if (g_bOfflineShopSocketMax == 5)
		snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,socket0,socket1,socket2,socket3,socket4,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);
	else if (g_bOfflineShopSocketMax == 6)
		snprintf(szQuery, sizeof(szQuery), "SELECT pos,count,vnum,socket0,socket1,socket2,socket3,socket4,socket5,attrtype0,attrvalue0,attrtype1,attrvalue1,attrtype2,attrvalue2,attrtype3,attrvalue3,attrtype4,attrvalue4,attrtype5,attrvalue5,attrtype6,attrvalue6 FROM %soffline_shop_item WHERE owner_id = %u and pos = %d", get_table_postfix(), ch->GetPlayerID(), bPos);

	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery(szQuery));
	if (pMsg->Get()->uiNumRows == 0)
	{
		sys_log(0, "OfflineShopManager::RemoveItem - This slot is empty! [%s]", ch->GetName());
		return;
	}

	TPlayerItem item;
	int rows;
	if (!(rows = mysql_num_rows(pMsg->Get()->pSQLResult)))
		return;

	for (int i = 0; i < rows; ++i)
	{
		MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
		int cur = 0;

		str_to_number(item.pos, row[cur++]);
		str_to_number(item.count, row[cur++]);
		str_to_number(item.vnum, row[cur++]);
		for (BYTE a = 0; a < ITEM_SOCKET_MAX_NUM; a++)
			str_to_number(item.alSockets[a], row[cur++]);

		for (int j = 0; j < ITEM_ATTRIBUTE_MAX_NUM; j++)
		{
			str_to_number(item.aAttr[j].bType, row[cur++]);
			str_to_number(item.aAttr[j].sValue, row[cur++]);
		}
	}

	LPITEM pItem = ITEM_MANAGER::instance().CreateItem(item.vnum, item.count);
	if (!pItem)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "There is problem in the system at the moment. Please try again!");
		return;
	}

	pItem->SetAttributes(item.aAttr);
	pItem->SetSockets(item.alSockets);

	int iEmptyPos;
	if (pItem->IsDragonSoul())
		iEmptyPos = ch->GetEmptyDragonSoulInventory(pItem);
	else
		iEmptyPos = ch->GetEmptyInventory(pItem->GetSize());

	if (iEmptyPos < 0)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You don't have enough space for store the item!");
		return;
	}

	if (pItem->IsDragonSoul())
		pItem->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
	else
		pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));

	DBManager::instance().DirectQuery("DELETE FROM %soffline_shop_item WHERE owner_id = %u and pos = %d and status = 1", get_table_postfix(), ch->GetPlayerID(), bPos);
	LogManager::instance().ItemLog(ch, pItem, "TAKE OFFLINE SHOP ITEM", "");
	ch->ChatPacket(CHAT_TYPE_INFO, "You take %s item in your offline-shop.", pItem->GetName());
}

DWORD COfflineShopManager::FindMyOfflineShop(DWORD dwPID)
{
	TOfflineShopMap::iterator it = m_Map_pkOfflineShopByNPC2.find(dwPID);
	if (m_Map_pkOfflineShopByNPC2.end() == it)
		return 0;
	
	return it->second;
}

void COfflineShopManager::ChangeOfflineShopTime(LPCHARACTER ch, BYTE bTime)
{
	if (!ch)
		return;

	// Remember
	DWORD dwOfflineShopVID = FindMyOfflineShop(ch->GetPlayerID());

	if (!dwOfflineShopVID)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You can't use this option because you don't have offline shop yet!");
		return;
	}

	LPCHARACTER npc = CHARACTER_MANAGER::instance().Find(FindMyOfflineShop(ch->GetPlayerID()));
	if (npc)
	{
		if (npc->GetOfflineShopTimer() == 0 && bTime == 4)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "Your offline shop timer is already unlimited!");
			return;
		}
		
		if (g_wCoinsForUnlimited > 0 && bTime == 4)
		{
			std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT coins FROM account.account WHERE id = %u", ch->GetAID()));
			if (pMsg->Get()->uiNumRows == 0) return;
			MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
			long lCoins = 0;
			str_to_number(lCoins, row[0]);

			if (lCoins < static_cast<long>(g_wCoinsForUnlimited))
			{
				ch->ChatPacket(CHAT_TYPE_INFO, "You can't open an offline shop. You need to %d coins to open an offline shop!", g_wCoinsForUnlimited);
				return;
			}

			DBManager::instance().DirectQuery("UPDATE account.account SET coins = coins - %d where id = %u", g_wCoinsForUnlimited, ch->GetAID());
		}

		if (bTime == 4)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You changed time of your offline shop via Unlimited!");
			npc->StopOfflineShopUpdateEvent();
		}
		else
		{
			int iTime = 0;
			switch (bTime)
			{
				case 1:
					iTime = 1 * 60 * 60;
					break;
				case 2:
					iTime = 2 * 60 * 60;
					break;
				case 3:
					iTime = 4 * 60 * 60;
					break;
			}
			std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("UPDATE %soffline_shop_npc SET time = %d WHERE owner_id = %u", get_table_postfix(), iTime, ch->GetPlayerID()));
			npc->StopOfflineShopUpdateEvent();
			npc->SetOfflineShopTimer(iTime);
			npc->StartOfflineShopUpdateEvent();
			LogManager::instance().CharLog(ch, 0, "OFFLINE SHOP", "CHANGE TIME");
			ch->ChatPacket(CHAT_TYPE_INFO, "You changed time of your offline-shop. New expired time is %d hour(s)", iTime / 60 / 60);
		}
	}
	else
	{
		if (g_wCoinsForUnlimited > 0 && bTime == 4)
		{
			std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT coins FROM account.account WHERE id = %u", ch->GetAID()));
			if (pMsg->Get()->uiNumRows == 0) return;
			MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
			long lCoins = 0;
			str_to_number(lCoins, row[0]);

			if (lCoins < static_cast<long>(g_wCoinsForUnlimited))
			{
				ch->ChatPacket(CHAT_TYPE_INFO, "You can't open an offline shop. You need to %d coins to open an offline shop!", g_wCoinsForUnlimited);
				return;
			}

			DBManager::instance().DirectQuery("UPDATE account.account SET coins = coins - %d where id = %u", g_wCoinsForUnlimited, ch->GetAID());
		}

		TPacketGGChangeOfflineShopTime p;
		p.bHeader = HEADER_GG_CHANGE_OFFLINE_SHOP_TIME;
		p.bTime = bTime;		
		std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT mapIndex FROM %soffline_shop_npc WHERE owner_id = %u", get_table_postfix(), ch->GetPlayerID()));
		if (pMsg->Get()->uiNumRows == 0)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You can't use this option!");
			return;
		}
		
		MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
		str_to_number(p.lMapIndex, row[0]);		
		p.dwOwnerPID = ch->GetPlayerID();
		P2P_MANAGER::instance().Send(&p, sizeof(TPacketGGChangeOfflineShopTime));
		if (bTime != 4)
			ch->ChatPacket(CHAT_TYPE_INFO, "You changed time of your offline-shop.");
		else
			ch->ChatPacket(CHAT_TYPE_INFO, "You changed time of your offline-shop via Unlimited!");
	}
}

void COfflineShopManager::StopShopping(LPCHARACTER ch)
{
	LPOFFLINESHOP pkOfflineShop;

	if (!(pkOfflineShop = ch->GetOfflineShop()))
		return;

	pkOfflineShop->RemoveGuest(ch);
	sys_log(0, "OFFLINE_SHOP: END: %s", ch->GetName());

	///
	TPacketGCShop pack;
	pack.header = HEADER_GC_OFFLINE_SHOP;
	pack.subheader = SHOP_SUBHEADER_GC_UPDATE_ITEM2;

	TPacketGCOfflineShopStart pack2;
	memset(&pack2, 0, sizeof(pack2));
	pack2.owner_vid = 0;
	for (BYTE i = 0; i < OFFLINE_SHOP_HOST_ITEM_MAX_NUM; ++i)
		pack2.items[i].vnum = 0;

	pack.size = sizeof(pack) + sizeof(pack2);
	
	if (ch->GetDesc())
	{
		ch->GetDesc()->BufferedPacket(&pack, sizeof(TPacketGCShop));
		ch->GetDesc()->Packet(&pack2, sizeof(TPacketGCOfflineShopStart));
	}
}

void COfflineShopManager::Buy(LPCHARACTER ch, BYTE pos)
{
	if (!ch->GetOfflineShop())
		return;

	if (!ch->GetOfflineShopOwner())
		return;

	if (DISTANCE_APPROX(ch->GetX() - ch->GetOfflineShopOwner()->GetX(), ch->GetY() - ch->GetOfflineShopOwner()->GetY()) > 1500)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("상점과의 거리가 너무 멀어 물건을 살 수 없습니다."));
		return;
	}
	
	LPOFFLINESHOP pkOfflineShop = ch->GetOfflineShop();

	if (!pkOfflineShop)
		return;

	int ret = pkOfflineShop->Buy(ch, pos);

	// The result is not equal to SHOP_SUBHEADER_GC_OK, send the error to the character.
	if (SHOP_SUBHEADER_GC_OK != ret)
	{
		TPacketGCShop pack;
		pack.header = HEADER_GC_OFFLINE_SHOP;
		pack.subheader	= ret;
		pack.size	= sizeof(TPacketGCShop);
		
		if (ch->GetDesc())		
			ch->GetDesc()->Packet(&pack, sizeof(pack));
	}
}

void COfflineShopManager::WithdrawMoney(LPCHARACTER ch, long long llRequiredMoney)
{
	if (llRequiredMoney < 0)
		return;

	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT money FROM player.player WHERE id = %u", ch->GetPlayerID()));
	if (pMsg->Get()->uiNumRows == 0)
		return;

	long long llCurrentMoney = 0;
	MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
	str_to_number(llCurrentMoney, row[0]);

	if (llRequiredMoney > llCurrentMoney)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You can't enter big number than current money!");
		return;
	}

#ifdef ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
	bool isOverFlow = static_cast<long long>(ch->GetGold()) + llRequiredMoney > GOLD_MAX - 1 ? true : false;
#else
	bool isOverFlow = ch->GetGold() + llRequiredMoney > GOLD_MAX - 1 ? true : false;
#endif

	if (isOverFlow)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You can't withdraw this money at the moment!");
		return;
	}

	ch->PointChange(POINT_GOLD, llRequiredMoney, false);
	ch->ChatPacket(CHAT_TYPE_INFO, "You received %lld yang", llRequiredMoney);
	DBManager::instance().DirectQuery("UPDATE player.player SET money = money - %lld WHERE id = %u", llRequiredMoney, ch->GetPlayerID());
	LogManager::instance().CharLog(ch, 0, "OFFLINE SHOP", "WITHDRAW MONEY");
}

BYTE COfflineShopManager::LeftItemCount(LPCHARACTER ch)
{
	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT COUNT(*) FROM %soffline_shop_item WHERE owner_id = %u", get_table_postfix(), ch->GetPlayerID()));
	if (pMsg->Get()->uiNumRows == 0)
		return 0;

	MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
	BYTE bCount = 0;
	str_to_number(bCount, row[0]);
	return bCount;
}

bool COfflineShopManager::HasOfflineShop(LPCHARACTER ch)
{
	BYTE bHasOfflineShop = 0;
	TPacketGCShop p;
	p.header = HEADER_GC_OFFLINE_SHOP;
	p.subheader = SHOP_SUBHEADER_GC_CHECK_RESULT;
	p.size = sizeof(p);

	if (ch->GetOfflineShopVID())
	{
		bHasOfflineShop = 1;
		ch->SetOfflineShopStatus(2);
		if (ch->GetDesc())
		{
			ch->GetDesc()->Packet(&p, sizeof(p));
			ch->GetDesc()->Packet(&bHasOfflineShop, sizeof(BYTE));
		}
		return true;
	}
	else
	{
		std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT owner_id FROM %soffline_shop_npc WHERE owner_id = %u", get_table_postfix(), ch->GetPlayerID()));
		if (pMsg->Get()->uiNumRows == 0)
		{
			ch->SetOfflineShopStatus(bHasOfflineShop);
			if (ch->GetDesc())
			{
				ch->GetDesc()->Packet(&p, sizeof(p));
				ch->GetDesc()->Packet(&bHasOfflineShop, sizeof(BYTE));
			}
			return false;
		}
		else
		{
			bHasOfflineShop = 1;
			ch->SetOfflineShopStatus(2);
			if (ch->GetDesc())
			{
				ch->GetDesc()->Packet(&p, sizeof(p));
				ch->GetDesc()->Packet(&bHasOfflineShop, sizeof(BYTE));
			}
			return true;
		}
	}
	return false;
}