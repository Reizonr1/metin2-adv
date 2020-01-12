Search:
#include <cctype>

Add it under:
#include "sectree_manager.h"

https://puu.sh/sgJ7W/aeecdac5e3.png

---

Search:
bool CShopManager::Initialize(TShopTable * table, int size)
{
	...
}

Add it under:
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


https://puu.sh/sgJaD/4f8640c1d4.png
https://puu.sh/sgJbD/d5ac9a1213.png

---

Search:
void CShopManager::Destroy()
{
	TShopMap::iterator it = m_map_pkShop.begin();

	while (it != m_map_pkShop.end())
	{

Add it under:
#ifdef __OFFLINE_SHOP__
		it->second->Apply();
#endif

https://puu.sh/sgJcQ/17a73ae955.png

---

Search:
void CShopManager::Destroy()
{
	...
}

Add it under:

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


https://puu.sh/sgJeh/c21554d165.png
https://puu.sh/sgJfA/7449411867.png

---

Search:
	if (distance >= SHOP_MAX_DISTANCE)
	{
		sys_log(1, "SHOP: TOO_FAR: %s distance %d", pkChr->GetName(), distance);
		return false;
	}

	LPSHOP pkShop;

Add it under:
#ifdef __OFFLINE_SHOP__
	LPCHARACTER pkOwner = pkChrShopKeeper->GetShopOwner();
#endif

https://puu.sh/sgJh2/68bfca7bb0.png

--

Search:
	if (iShopVnum)
		pkShop = Get(iShopVnum);
	else
		pkShop = GetByNPCVnum(pkChrShopKeeper->GetRaceNum());

Change:
	if (iShopVnum)
		pkShop = Get(iShopVnum);
#ifdef __OFFLINE_SHOP__
	else if (pkOwner)
		pkShop = FindPCShop(pkOwner->GetVID());
#endif
	else
		pkShop = GetByNPCVnum(pkChrShopKeeper->GetRaceNum());


https://puu.sh/sgJi3/68a9f4b785.png

---

Search:
	bool bOtherEmpire = false;

	if (pkChr->GetEmpire() != pkChrShopKeeper->GetEmpire())
		bOtherEmpire = true;

Change:
	bool bOtherEmpire = false;
#ifdef __OFFLINE_SHOP__
	if (!pkOwner && pkChr->GetEmpire() != pkChrShopKeeper->GetEmpire())
#else
	if (pkChr->GetEmpire() != pkChrShopKeeper->GetEmpire())
#endif
		bOtherEmpire = true;

https://puu.sh/sgJjw/4f3b7ab70d.png

---

Search:
	LPSHOP pkShop = M2_NEW CShop;
	pkShop->SetPCShop(ch);
	pkShop->SetShopItems(pTable, bItemCount);

Change:
	LPSHOP pkShop = M2_NEW CShop;
	pkShop->SetPCShop(ch);
#ifdef __OFFLINE_SHOP__
	pkShop->SetShopItems(NULL, pTable, bItemCount);
#else
	pkShop->SetShopItems(pTable, bItemCount);
#endif

https://puu.sh/sgJl5/f29c4f7a24.png

---

Search:
LPSHOP CShopManager::CreatePCShop(LPCHARACTER ch, TShopItemTable * pTable, BYTE bItemCount)
{
	...
}

Add it under:

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

https://puu.sh/sgJlP/8226df8c27.png
https://puu.sh/sgJmi/ede89bdd88.png

---

Search:
void CShopManager::DestroyPCShop(LPCHARACTER ch)
{
	LPSHOP pkShop = FindPCShop(ch->GetVID());

	if (!pkShop)
		return;

	//PREVENT_ITEM_COPY;
	ch->SetMyShopTime();
	//END_PREVENT_ITEM_COPY

Add it under:
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

https://puu.sh/sgJop/9f8d3ba646.png



