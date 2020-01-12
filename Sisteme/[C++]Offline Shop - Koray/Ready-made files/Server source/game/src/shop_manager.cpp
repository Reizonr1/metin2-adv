#include "stdafx.h"
#include "../../libgame/include/grid.h"
#include "constants.h"
#include "utils.h"
#include "config.h"
#include "shop.h"
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
#include "shop_manager.h"
#include "group_text_parse_tree.h"
#include "shopEx.h"
#include <boost/algorithm/string/predicate.hpp>
#include "shop_manager.h"
#include <cctype>
#include "sectree_manager.h"
CShopManager::CShopManager()
{
}

CShopManager::~CShopManager()
{
	Destroy();
}

bool CShopManager::Initialize(TShopTable * table, int size)
{
	if (!m_map_pkShop.empty())
		return false;

	int i; 

	for (i = 0; i < size; ++i, ++table)
	{
		LPSHOP shop = M2_NEW CShop;

		if (!shop->Create(table->dwVnum, table->dwNPCVnum, table->items))
		{
			M2_DELETE(shop);
			continue;
		}

		m_map_pkShop.insert(TShopMap::value_type(table->dwVnum, shop));
		m_map_pkShopByNPCVnum.insert(TShopMap::value_type(table->dwNPCVnum, shop));
	}
	char szShopTableExFileName[256];

	snprintf(szShopTableExFileName, sizeof(szShopTableExFileName),
		"%s/shop_table_ex.txt", LocaleService_GetBasePath().c_str());

	return ReadShopTableEx(szShopTableExFileName);
}
#ifdef __OFFLINE_SHOP__
bool CShopManager::Initialize(TOfflineShopTable * table, int size)
{
	for (int i = 0; i < size; ++i, ++table)
	{
		if (table->dwChannel != g_bChannel)
			continue;

		LPSHOP pkShop = M2_NEW CShop;

		char szShopName[1024];
		sprintf(szShopName, "%s's Offline shop", table->szName);

		DWORD dwShopVnum = 30005 + table->dwColor; // Style adjusted shop vnum
		LPCHARACTER priv_shop = CHARACTER_MANAGER::instance().SpawnOffShop(dwShopVnum, szShopName, table->dwMapIndex, table->dwX, table->dwY, 0);
		if (!priv_shop)
			continue;

		pkShop->SetOwner(table->dwAID, table->dwPID);
		pkShop->SetPCShop(priv_shop);

		priv_shop->SetOfflineShopOwner((LPCHARACTER)-1);
		priv_shop->SetMyShop(pkShop);

		if (!pkShop->Create(table))
		{
			pkShop->Remove();
			M2_DESTROY_CHARACTER(priv_shop);
			M2_DELETE(pkShop);
			continue;
		}

		priv_shop->SetShopSign(table->szSign);

		DWORD dwNow = get_global_time();
		DWORD dwExpireDate = table->dwInstallTime + table->dwDuration;
		sys_log(0, "Now: %u Expire date: %u", dwNow, dwExpireDate);
		priv_shop->SetupExpire(dwExpireDate - dwNow);

		m_map_pkShopByPC.insert(TShopMap::value_type(priv_shop->GetVID(), pkShop));
		m_map_pkOfflineShop[table->dwPID].push_back(priv_shop->GetVID());
	}

	return true;
}
#endif
void CShopManager::Destroy()
{
	TShopMap::iterator it = m_map_pkShop.begin();

	while (it != m_map_pkShop.end())
	{
#ifdef __OFFLINE_SHOP__
		it->second->Apply();
#endif
		M2_DELETE(it->second);
		++it;
	}

	m_map_pkShop.clear();
}
#ifdef __OFFLINE_SHOP__
void CShopManager::GetOfflineShops(DWORD dwPID)
{
	if (m_map_pkOfflineShop.empty() || m_map_pkOfflineShop.begin() == m_map_pkOfflineShop.end())
		return;

	std::map<DWORD, std::vector<DWORD> >::iterator it;
	for (it = m_map_pkOfflineShop.begin(); it != m_map_pkOfflineShop.end(); ++it)
	{
		if (it->first != dwPID)
			continue;

		if (it->second.empty() || it->second.begin() == it->second.end())
			continue;

		for (DWORD i = 0; i < it->second.size(); ++i)
		{
			LPSHOP pkShop = FindPCShop(it->second[i]);
			if (!pkShop) {
				sys_err("loop vid: %u is null shop pointer", it->second[i]);
				continue;
			}

			// Is not offline shop
			if (!pkShop->GetPCShop() || pkShop->GetPCShop()->IsPC() || dwPID != pkShop->GetOwner())
				continue;

			long mapIdx = pkShop->GetPCShop()->GetMapIndex();
			LPCHARACTER ch = CHARACTER_MANAGER::instance().FindByPID(dwPID);
			if (ch) {
				DWORD dwVID = (DWORD)pkShop->GetPCShop()->GetVID();
				long getX = pkShop->GetPCShop()->GetX();
				long getY = pkShop->GetPCShop()->GetY();

				ch->ChatPacket(CHAT_TYPE_COMMAND, "offlineshop_info %s %u %d %d %d", pkShop->GetPCShop()->GetShopSign().c_str(), dwVID, mapIdx, getX, getY);
			}
		}
	}
}

void CShopManager::GotoOfflineShop(DWORD dwPID, DWORD dwVID)
{
	if (m_map_pkOfflineShop.empty() || m_map_pkOfflineShop.begin() == m_map_pkOfflineShop.end())
		return;

	std::map<DWORD, std::vector<DWORD> >::iterator it;
	for (it = m_map_pkOfflineShop.begin(); it != m_map_pkOfflineShop.end(); ++it)
	{
		if (it->first != dwPID)
			continue;

		if (it->second.empty() || it->second.begin() == it->second.end())
			continue;

		for (DWORD i = 0; i < it->second.size(); ++i)
		{
			if (dwVID != it->second[i])
				continue;

			LPSHOP pkShop = FindPCShop(it->second[i]);
			if (!pkShop) {
				sys_err("loop vid: %u is null shop pointer", it->second[i]);
				continue;
			}

			// Is not offline shop
			if (!pkShop->GetPCShop() || pkShop->GetPCShop()->IsPC() || dwPID != pkShop->GetOwner())
				continue;

			LPCHARACTER ch = CHARACTER_MANAGER::instance().FindByPID(dwPID);
			if (ch)
			{
				long shopMapIdx = pkShop->GetPCShop()->GetMapIndex();
				long charMapIdx = ch->GetMapIndex();

				if (shopMapIdx != charMapIdx) {
					ch->ChatPacket(CHAT_TYPE_INFO, "You are not same map with offline shop!");
					return;
				}

				ch->Show(shopMapIdx, pkShop->GetPCShop()->GetX(), pkShop->GetPCShop()->GetY());
				ch->Stop();
			}
		}
	}
}

void CShopManager::WarpOfflineShop(DWORD dwPID, DWORD dwVID)
{
	if (m_map_pkOfflineShop.empty() || m_map_pkOfflineShop.begin() == m_map_pkOfflineShop.end())
		return;

	std::map<DWORD, std::vector<DWORD> >::iterator it;
	for (it = m_map_pkOfflineShop.begin(); it != m_map_pkOfflineShop.end(); ++it)
	{
		if (it->first != dwPID)
			continue;

		if (it->second.empty() || it->second.begin() == it->second.end())
			continue;

		for (DWORD i = 0; i < it->second.size(); ++i)
		{
			if (dwVID != it->second[i])
				continue;

			LPSHOP pkShop = FindPCShop(it->second[i]);
			if (!pkShop) {
				sys_err("loop vid: %u is null shop pointer", it->second[i]);
				continue;
			}

			// Is not offline shop
			if (!pkShop->GetPCShop() || pkShop->GetPCShop()->IsPC() || dwPID != pkShop->GetOwner())
				continue;

			LPCHARACTER ch = CHARACTER_MANAGER::instance().FindByPID(dwPID);
			if (ch)
			{
				long shopMapIdx = pkShop->GetPCShop()->GetMapIndex();
				long shopOldX = pkShop->GetPCShop()->GetX();
				long shopOldY = pkShop->GetPCShop()->GetY();
				long charMapIdx = ch->GetMapIndex();

				if (shopMapIdx != charMapIdx) {
					ch->ChatPacket(CHAT_TYPE_INFO, "You are not same map with offline shop!");
					return;
				}

				if (DISTANCE_APPROX(ch->GetX() - pkShop->GetPCShop()->GetX(), ch->GetY() - pkShop->GetPCShop()->GetY()) > 10000) {
					ch->ChatPacket(CHAT_TYPE_INFO, "You are so far to this offline shop!");
					return;
				}


				long playerX = ch->GetX();
				long playerY = ch->GetY();
				if (playerX <= 0 || playerY <= 0) {
					ch->ChatPacket(CHAT_TYPE_INFO, "You are can not warp your offline to here!");
					return;
				}

				PIXEL_POSITION pos2;
				if (!SECTREE_MANAGER::instance().GetMovablePosition(charMapIdx, playerX, playerY, pos2)) {
					ch->ChatPacket(CHAT_TYPE_INFO, "You can not move your offline shop to unavailable position!");
					return;
				}

				if (ch->HasNearOfflineShop(playerX, playerY)) {
					ch->ChatPacket(CHAT_TYPE_INFO, "You can not move your offline shop to near other offline shops!");
					return;
				}


				pkShop->SetLocked(true);

				pkShop->GetPCShop()->Show(charMapIdx, playerX, playerY);
				pkShop->GetPCShop()->Stop();

				char szQuery[QUERY_MAX_LEN + 1];
				sprintf(szQuery, "UPDATE player.offline_shop%s SET x=%u, y=%u WHERE pid=%u AND x=%u AND y=%u", get_table_postfix(), playerX, playerY, dwPID, shopOldX, shopOldY);

				std::auto_ptr<SQLMsg> pMsg(AccountDB::instance().DirectQuery(szQuery));
				if (pMsg->uiSQLErrno != 0) {
					sys_err("Move shop query failed, Error code: %u, %s: %s", pMsg->uiSQLErrno, ch->GetName(), szQuery);

					pkShop->Remove();
					M2_DESTROY_CHARACTER(pkShop->GetPCShop());
					// M2_DELETE(shop);
					return;
				}

				if (pMsg->Get()->uiAffectedRows == 0 || pMsg->Get()->uiAffectedRows == (uint32_t)-1) {
					sys_err("Move shop query NOT affected to any row! %s: %s", ch->GetName(), szQuery);

					pkShop->Remove();
					M2_DESTROY_CHARACTER(pkShop->GetPCShop());
					return;
				}

				// Complete
				pkShop->SetLocked(false);
			}
		}
	}
}

void CShopManager::CloseOfflineShop(DWORD dwPID, DWORD dwVID)
{
	if (m_map_pkOfflineShop.empty() || m_map_pkOfflineShop.begin() == m_map_pkOfflineShop.end())
		return;

	std::map<DWORD, std::vector<DWORD> >::iterator it;
	for (it = m_map_pkOfflineShop.begin(); it != m_map_pkOfflineShop.end(); ++it)
	{
		if (it->first != dwPID)
			continue;

		if (it->second.empty() || it->second.begin() == it->second.end())
			continue;

		for (DWORD i = 0; i < it->second.size(); ++i)
		{
			if (dwVID != it->second[i])
				continue;

			LPSHOP pkShop = FindPCShop(it->second[i]);
			if (!pkShop) {
				sys_err("loop vid: %u is null shop pointer", it->second[i]);
				continue;
			}

			// Is not offline shop
			if (!pkShop->GetPCShop() || pkShop->GetPCShop()->IsPC() || dwPID != pkShop->GetOwner())
				continue;

			LPCHARACTER ch = CHARACTER_MANAGER::instance().FindByPID(dwPID);
			if (ch->GetExchange() || ch->IsCubeOpen() /*|| ch->IsAcceOpen()*/)
				return;

			pkShop->Remove();
			M2_DESTROY_CHARACTER(pkShop->GetPCShop());
			// M2_DELETE(pkShop);
		}
	}
}
#endif
LPSHOP CShopManager::Get(DWORD dwVnum)
{
	TShopMap::const_iterator it = m_map_pkShop.find(dwVnum);

	if (it == m_map_pkShop.end())
		return NULL;

	return (it->second);
}

LPSHOP CShopManager::GetByNPCVnum(DWORD dwVnum)
{
	TShopMap::const_iterator it = m_map_pkShopByNPCVnum.find(dwVnum);

	if (it == m_map_pkShopByNPCVnum.end())
		return NULL;

	return (it->second);
}

/*
 * 인터페이스 함수들
 */

// 상점 거래를 시작
bool CShopManager::StartShopping(LPCHARACTER pkChr, LPCHARACTER pkChrShopKeeper, int iShopVnum)
{
	if (pkChr->GetShopOwner() == pkChrShopKeeper)
		return false;
	// this method is only for NPC
	if (pkChrShopKeeper->IsPC())
		return false;

	//PREVENT_TRADE_WINDOW
	if (pkChr->IsOpenSafebox() || pkChr->GetExchange() || pkChr->GetMyShop() || pkChr->IsCubeOpen())
	{
		pkChr->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("다른 거래창이 열린상태에서는 상점거래를 할수 가 없습니다."));
		return false;
	}
	//END_PREVENT_TRADE_WINDOW

	long distance = DISTANCE_APPROX(pkChr->GetX() - pkChrShopKeeper->GetX(), pkChr->GetY() - pkChrShopKeeper->GetY());

	if (distance >= SHOP_MAX_DISTANCE)
	{
		sys_log(1, "SHOP: TOO_FAR: %s distance %d", pkChr->GetName(), distance);
		return false;
	}

	LPSHOP pkShop;
#ifdef __OFFLINE_SHOP__
	LPCHARACTER pkOwner = pkChrShopKeeper->GetShopOwner();
#endif
	if (iShopVnum)
		pkShop = Get(iShopVnum);
#ifdef __OFFLINE_SHOP__
	else if (pkOwner)
		pkShop = FindPCShop(pkOwner->GetVID());
#endif
	else
		pkShop = GetByNPCVnum(pkChrShopKeeper->GetRaceNum());


	if (!pkShop)
	{
		sys_log(1, "SHOP: NO SHOP");
		return false;
	}

	bool bOtherEmpire = false;
#ifdef __OFFLINE_SHOP__
	if (!pkOwner && pkChr->GetEmpire() != pkChrShopKeeper->GetEmpire())
#else
	if (pkChr->GetEmpire() != pkChrShopKeeper->GetEmpire())
#endif
		bOtherEmpire = true;

	pkShop->AddGuest(pkChr, pkChrShopKeeper->GetVID(), bOtherEmpire);
	pkChr->SetShopOwner(pkChrShopKeeper);
	sys_log(0, "SHOP: START: %s", pkChr->GetName());
	return true;
}

LPSHOP CShopManager::FindPCShop(DWORD dwVID)
{
	TShopMap::iterator it = m_map_pkShopByPC.find(dwVID);

	if (it == m_map_pkShopByPC.end())
		return NULL;

	return it->second;
}

LPSHOP CShopManager::CreatePCShop(LPCHARACTER ch, TShopItemTable * pTable, BYTE bItemCount)
{
	if (FindPCShop(ch->GetVID()))
		return NULL;

	LPSHOP pkShop = M2_NEW CShop;
	pkShop->SetPCShop(ch);
#ifdef __OFFLINE_SHOP__
	pkShop->SetShopItems(NULL, pTable, bItemCount);
#else
	pkShop->SetShopItems(pTable, bItemCount);
#endif

	m_map_pkShopByPC.insert(TShopMap::value_type(ch->GetVID(), pkShop));
	return pkShop;
}

#ifdef __OFFLINE_SHOP__
LPSHOP CShopManager::CreateOfflineShop(LPCHARACTER ch, BYTE bSize, BYTE bColor, TShopItemTable * pTable, BYTE bItemCount)
{
	if (FindPCShop(ch->GetVID()))
		return NULL;

	char szShopName[1024];
	sprintf(szShopName, "%s's Offline shop", ch->GetName());

	int iShopVnum = 30005 + bColor;
	LPCHARACTER priv_shop = CHARACTER_MANAGER::instance().SpawnOffShopRange(iShopVnum, szShopName, ch->GetMapIndex(),
		ch->GetX() - 250, ch->GetY() - 250, ch->GetX() + 250, ch->GetY() + 250, true, false);
	if (!priv_shop)
		return NULL;

	LPSHOP pkShop = M2_NEW CShop;
	pkShop->SetShopSize(bSize);
	pkShop->SetOwner(ch->GetAID(), ch->GetPlayerID());
	pkShop->SetPCShop(priv_shop);
	pkShop->SetShopColor(bColor);
	pkShop->SetShopItems(ch, pTable, bItemCount);

	priv_shop->SetOfflineShopOwner(ch);
	priv_shop->SetMyShop(pkShop);

	m_map_pkShopByPC.insert(TShopMap::value_type(priv_shop->GetVID(), pkShop));
	m_map_pkOfflineShop[ch->GetPlayerID()].push_back(priv_shop->GetVID());
	return pkShop;
}
#endif
void CShopManager::DestroyPCShop(LPCHARACTER ch)
{
	LPSHOP pkShop = FindPCShop(ch->GetVID());

	if (!pkShop)
		return;

	//PREVENT_ITEM_COPY;
	ch->SetMyShopTime();
	//END_PREVENT_ITEM_COPY
#ifdef __OFFLINE_SHOP__
	std::vector<DWORD>::iterator it = m_map_pkOfflineShop[pkShop->GetOwner()].begin();
	std::vector<DWORD>::iterator it_end = m_map_pkOfflineShop[pkShop->GetOwner()].end();

	for (; it != it_end; ++it)
	{
		if (*it == ch->GetVID())
		{
			m_map_pkOfflineShop[pkShop->GetOwner()].erase(it);

			if (m_map_pkOfflineShop[pkShop->GetOwner()].size() == 0)
				m_map_pkOfflineShop.erase(pkShop->GetOwner());
			break;
		}
	}
#endif
	m_map_pkShopByPC.erase(ch->GetVID());
	M2_DELETE(pkShop);
}

// 상점 거래를 종료
void CShopManager::StopShopping(LPCHARACTER ch)
{
	LPSHOP shop;

	if (!(shop = ch->GetShop()))
		return;

	//PREVENT_ITEM_COPY;
	ch->SetMyShopTime();
	//END_PREVENT_ITEM_COPY
	
	shop->RemoveGuest(ch);
	sys_log(0, "SHOP: END: %s", ch->GetName());
}

// 아이템 구입
void CShopManager::Buy(LPCHARACTER ch, BYTE pos)
{
	if (!ch->GetShop())
		return;

	if (!ch->GetShopOwner())
		return;

	if (DISTANCE_APPROX(ch->GetX() - ch->GetShopOwner()->GetX(), ch->GetY() - ch->GetShopOwner()->GetY()) > 2000)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("상점과의 거리가 너무 멀어 물건을 살 수 없습니다."));
		return;
	}

	CShop* pkShop = ch->GetShop();

	if (!pkShop->IsPCShop())
	{
		//if (pkShop->GetVnum() == 0)
		//	return;
		//const CMob* pkMob = CMobManager::instance().Get(pkShop->GetNPCVnum());
		//if (!pkMob)
		//	return;

		//if (pkMob->m_table.bType != CHAR_TYPE_NPC)
		//{
		//	return;
		//}
	}
	else
	{
	}

	//PREVENT_ITEM_COPY
	ch->SetMyShopTime();
	//END_PREVENT_ITEM_COPY

	int ret = pkShop->Buy(ch, pos);

	if (SHOP_SUBHEADER_GC_OK != ret) // 문제가 있었으면 보낸다.
	{
		TPacketGCShop pack;

		pack.header	= HEADER_GC_SHOP;
		pack.subheader	= ret;
		pack.size	= sizeof(TPacketGCShop);

		ch->GetDesc()->Packet(&pack, sizeof(pack));
	}
}

void CShopManager::Sell(LPCHARACTER ch, BYTE bCell, BYTE bCount)
{
	if (!ch->GetShop())
		return;

	if (!ch->GetShopOwner())
		return;

	if (!ch->CanHandleItem())
		return;

	if (ch->GetShop()->IsPCShop())
		return;

	if (DISTANCE_APPROX(ch->GetX()-ch->GetShopOwner()->GetX(), ch->GetY()-ch->GetShopOwner()->GetY())>2000)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("상점과의 거리가 너무 멀어 물건을 팔 수 없습니다."));
		return;
	}
	
	LPITEM item = ch->GetInventoryItem(bCell);

	if (!item)
		return;

	if (item->IsEquipped() == true)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("착용 중인 아이템은 판매할 수 없습니다."));
		return;
	}

	if (true == item->isLocked())
	{
		return;
	}

	if (IS_SET(item->GetAntiFlag(), ITEM_ANTIFLAG_SELL))
		return;

	DWORD dwPrice;

	if (bCount == 0 || bCount > item->GetCount())
		bCount = item->GetCount();

	dwPrice = item->GetShopBuyPrice();

	if (IS_SET(item->GetFlag(), ITEM_FLAG_COUNT_PER_1GOLD))
	{
		if (dwPrice == 0)
			dwPrice = bCount;
		else
			dwPrice = bCount / dwPrice;
	}
	else
		dwPrice *= bCount;

	dwPrice /= 5;
	
	//세금 계산
	DWORD dwTax = 0;
	int iVal = 3;
	
	if (LC_IsYMIR() ||  LC_IsKorea())
	{
		dwTax = dwPrice * iVal / 100;
		dwPrice -= dwTax;
	}
	else
	{
		dwTax = dwPrice * iVal/100;
		dwPrice -= dwTax;
	}

	if (test_server)
		sys_log(0, "Sell Item price id %d %s itemid %d", ch->GetPlayerID(), ch->GetName(), item->GetID());

	const int64_t nTotalMoney = static_cast<int64_t>(ch->GetGold()) + static_cast<int64_t>(dwPrice);

	if (GOLD_MAX <= nTotalMoney)
	{
		sys_err("[OVERFLOW_GOLD] id %u name %s gold %u", ch->GetPlayerID(), ch->GetName(), ch->GetGold());
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("20억냥이 초과하여 물품을 팔수 없습니다."));
		return;
	}

	// 20050802.myevan.상점 판매 로그에 아이템 ID 추가
	sys_log(0, "SHOP: SELL: %s item name: %s(x%d):%u price: %u", ch->GetName(), item->GetName(), bCount, item->GetID(), dwPrice);

	if (iVal > 0)
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("판매금액의 %d %% 가 세금으로 나가게됩니다"), iVal);

	DBManager::instance().SendMoneyLog(MONEY_LOG_SHOP, item->GetVnum(), dwPrice);

	if (bCount == item->GetCount())
	{
		// 한국에는 아이템을 버리고 복구해달라는 진상유저들이 많아서
		// 상점 판매시 속성로그를 남긴다.
		if (LC_IsYMIR())
			item->AttrLog();

		ITEM_MANAGER::instance().RemoveItem(item, "SELL");
	}
	else
		item->SetCount(item->GetCount() - bCount);

	//군주 시스템 : 세금 징수
	CMonarch::instance().SendtoDBAddMoney(dwTax, ch->GetEmpire(), ch);

	ch->PointChange(POINT_GOLD, dwPrice, false);
}

bool CompareShopItemName(const SShopItemTable& lhs, const SShopItemTable& rhs)
{
	TItemTable* lItem = ITEM_MANAGER::instance().GetTable(lhs.vnum);
	TItemTable* rItem = ITEM_MANAGER::instance().GetTable(rhs.vnum);
	if (lItem && rItem)
		return strcmp(lItem->szLocaleName, rItem->szLocaleName) < 0;
	else
		return true;
}

bool ConvertToShopItemTable(IN CGroupNode* pNode, OUT TShopTableEx& shopTable)
{
	if (!pNode->GetValue("vnum", 0, shopTable.dwVnum))
	{
		sys_err("Group %s does not have vnum.", pNode->GetNodeName().c_str());
		return false;
	}

	if (!pNode->GetValue("name", 0, shopTable.name))
	{
		sys_err("Group %s does not have name.", pNode->GetNodeName().c_str());
		return false;
	}
	
	if (shopTable.name.length() >= SHOP_TAB_NAME_MAX)
	{
		sys_err("Shop name length must be less than %d. Error in Group %s, name %s", SHOP_TAB_NAME_MAX, pNode->GetNodeName().c_str(), shopTable.name.c_str());
		return false;
	}

	std::string stCoinType;
	if (!pNode->GetValue("cointype", 0, stCoinType))
	{
		stCoinType = "Gold";
	}
	
	if (boost::iequals(stCoinType, "Gold"))
	{
		shopTable.coinType = SHOP_COIN_TYPE_GOLD;
	}
	else if (boost::iequals(stCoinType, "SecondaryCoin"))
	{
		shopTable.coinType = SHOP_COIN_TYPE_SECONDARY_COIN;
	}
	else
	{
		sys_err("Group %s has undefine cointype(%s).", pNode->GetNodeName().c_str(), stCoinType.c_str());
		return false;
	}

	CGroupNode* pItemGroup = pNode->GetChildNode("items");
	if (!pItemGroup)
	{
		sys_err("Group %s does not have 'group items'.", pNode->GetNodeName().c_str());
		return false;
	}

	int itemGroupSize = pItemGroup->GetRowCount();
	std::vector <TShopItemTable> shopItems(itemGroupSize);
	if (itemGroupSize >= SHOP_HOST_ITEM_MAX_NUM)
	{
		sys_err("count(%d) of rows of group items of group %s must be smaller than %d", itemGroupSize, pNode->GetNodeName().c_str(), SHOP_HOST_ITEM_MAX_NUM);
		return false;
	}

	for (int i = 0; i < itemGroupSize; i++)
	{
		if (!pItemGroup->GetValue(i, "vnum", shopItems[i].vnum))
		{
			sys_err("row(%d) of group items of group %s does not have vnum column", i, pNode->GetNodeName().c_str());
			return false;
		}
		
		if (!pItemGroup->GetValue(i, "count", shopItems[i].count))
		{
			sys_err("row(%d) of group items of group %s does not have count column", i, pNode->GetNodeName().c_str());
			return false;
		}
		if (!pItemGroup->GetValue(i, "price", shopItems[i].price))
		{
			sys_err("row(%d) of group items of group %s does not have price column", i, pNode->GetNodeName().c_str());
			return false;
		}
	}
	std::string stSort;
	if (!pNode->GetValue("sort", 0, stSort))
	{
		stSort = "None";
	}

	if (boost::iequals(stSort, "Asc"))
	{
		std::sort(shopItems.begin(), shopItems.end(), CompareShopItemName);
	}
	else if(boost::iequals(stSort, "Desc"))
	{
		std::sort(shopItems.rbegin(), shopItems.rend(), CompareShopItemName);
	}

	CGrid grid = CGrid(5, 9);
	int iPos;

	memset(&shopTable.items[0], 0, sizeof(shopTable.items));

	for (int i = 0; i < shopItems.size(); i++)
	{
		TItemTable * item_table = ITEM_MANAGER::instance().GetTable(shopItems[i].vnum);
		if (!item_table)
		{
			sys_err("vnum(%d) of group items of group %s does not exist", shopItems[i].vnum, pNode->GetNodeName().c_str());
			return false;
		}

		iPos = grid.FindBlank(1, item_table->bSize);

		grid.Put(iPos, 1, item_table->bSize);
		shopTable.items[iPos] = shopItems[i];
	}

	shopTable.byItemCount = shopItems.size();
	return true;
}

bool CShopManager::ReadShopTableEx(const char* stFileName)
{
	// file 유무 체크.
	// 없는 경우는 에러로 처리하지 않는다.
	FILE* fp = fopen(stFileName, "rb");
	if (NULL == fp)
		return true;
	fclose(fp);

	CGroupTextParseTreeLoader loader;
	if (!loader.Load(stFileName))
	{
		sys_err("%s Load fail.", stFileName);
		return false;
	}

	CGroupNode* pShopNPCGroup = loader.GetGroup("shopnpc");
	if (NULL == pShopNPCGroup)
	{
		sys_err("Group ShopNPC is not exist.");
		return false;
	}

	typedef std::multimap <DWORD, TShopTableEx> TMapNPCshop;
	TMapNPCshop map_npcShop;
	for (int i = 0; i < pShopNPCGroup->GetRowCount(); i++)
	{
		DWORD npcVnum;
		std::string shopName;
		if (!pShopNPCGroup->GetValue(i, "npc", npcVnum) || !pShopNPCGroup->GetValue(i, "group", shopName))
		{
			sys_err("Invalid row(%d). Group ShopNPC rows must have 'npc', 'group' columns", i);
			return false;
		}
		std::transform(shopName.begin(), shopName.end(), shopName.begin(), (int(*)(int))std::tolower);
		CGroupNode* pShopGroup = loader.GetGroup(shopName.c_str());
		if (!pShopGroup)
		{
			sys_err("Group %s is not exist.", shopName.c_str());
			return false;
		}
		TShopTableEx table;
		if (!ConvertToShopItemTable(pShopGroup, table))
		{
			sys_err("Cannot read Group %s.", shopName.c_str());
			return false;
		}
		if (m_map_pkShopByNPCVnum.find(npcVnum) != m_map_pkShopByNPCVnum.end())
		{
			sys_err("%d cannot have both original shop and extended shop", npcVnum);
			return false;
		}
		
		map_npcShop.insert(TMapNPCshop::value_type(npcVnum, table));	
	}

	for (TMapNPCshop::iterator it = map_npcShop.begin(); it != map_npcShop.end(); ++it)
	{
		DWORD npcVnum = it->first;
		TShopTableEx& table = it->second;
		if (m_map_pkShop.find(table.dwVnum) != m_map_pkShop.end())
		{
			sys_err("Shop vnum(%d) already exists", table.dwVnum);
			return false;
		}
		TShopMap::iterator shop_it = m_map_pkShopByNPCVnum.find(npcVnum);
		
		LPSHOPEX pkShopEx = NULL;
		if (m_map_pkShopByNPCVnum.end() == shop_it)
		{
			pkShopEx = M2_NEW CShopEx;
			pkShopEx->Create(0, npcVnum);
			m_map_pkShopByNPCVnum.insert(TShopMap::value_type(npcVnum, pkShopEx));
		}
		else
		{
			pkShopEx = dynamic_cast <CShopEx*> (shop_it->second);
			if (NULL == pkShopEx)
			{
				sys_err("WTF!!! It can't be happend. NPC(%d) Shop is not extended version.", shop_it->first);
				return false;
			}
		}

		if (pkShopEx->GetTabCount() >= SHOP_TAB_COUNT_MAX)
		{
			sys_err("ShopEx cannot have tab more than %d", SHOP_TAB_COUNT_MAX);
			return false;
		}

		if (pkShopEx->GetVnum() != 0 && m_map_pkShop.find(pkShopEx->GetVnum()) != m_map_pkShop.end())
		{
			sys_err("Shop vnum(%d) already exist.", pkShopEx->GetVnum());
			return false;
		}
		m_map_pkShop.insert(TShopMap::value_type (pkShopEx->GetVnum(), pkShopEx));
		pkShopEx->AddShopTable(table);
	}

	return true;
}
