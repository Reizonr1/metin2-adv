Search:
#include "locale_service.h"

Add it under:
#include "desc_client.h"

https://puu.sh/sgHM8/e0e5c7f510.png

---

Search:
CShop::CShop()
	: m_dwVnum(0), m_dwNPCVnum(0), m_pkPC(NULL)

Change:
#ifdef __OFFLINE_SHOP__
CShop::CShop() : m_dwVnum(0), m_dwNPCVnum(0), m_pkPC(NULL), m_dwOwnerAID(0), m_dwOwnerPID(0), m_Money(0), m_bColor(0), m_bSize(0), m_bIsLocked(0)
#else
CShop::CShop() : m_dwVnum(0), m_dwNPCVnum(0), m_pkPC(NULL)
#endif

https://puu.sh/sgHNx/73152734d1.png

---

Search:
CShop::~CShop()
{
	TPacketGCShop pack;

	pack.header		= HEADER_GC_SHOP;
	pack.subheader	= SHOP_SUBHEADER_GC_END;
	pack.size		= sizeof(TPacketGCShop);

	Broadcast(&pack, sizeof(pack));

	GuestMapType::iterator it;

	it = m_map_guest.begin();

	while (it != m_map_guest.end())
	{
		LPCHARACTER ch = it->first;
		ch->SetShop(NULL);
		++it;
	}

	M2_DELETE(m_pGrid);
}

Change:

CShop::~CShop()
{
#ifdef __OFFLINE_SHOP__
	m_bIsLocked = true;

	if (HasOwner())
	{
		for (DWORD i = 0; i < m_itemVector.size() && i < SHOP_HOST_ITEM_MAX_NUM; ++i)
		{
			LPITEM item = m_itemVector[i].pkItem;

			if (item == NULL)
				continue;

			item->SetSkipSave(true);
			M2_DESTROY_ITEM(item);
		}
	}
#endif

	TPacketGCShop pack;

	pack.header		= HEADER_GC_SHOP;
	pack.subheader	= SHOP_SUBHEADER_GC_END;
	pack.size		= sizeof(TPacketGCShop);

	Broadcast(&pack, sizeof(pack));

	GuestMapType::iterator it;

	it = m_map_guest.begin();

	while (it != m_map_guest.end())
	{
		LPCHARACTER ch = it->first;
		ch->SetShop(NULL);
		++it;
	}

#ifdef __OFFLINE_SHOP__
	m_SoldItems.clear();
#endif
	M2_DELETE(m_pGrid);
}

https://puu.sh/sgHPv/27a8112adf.png

---

Search:
void CShop::SetPCShop(LPCHARACTER ch)
{
	m_pkPC = ch;
}

Change:
#ifdef __OFFLINE_SHOP__
void CShop::SetOwner(DWORD dwOwnerAID, DWORD dwOwnerPID)
{
	m_dwOwnerAID = dwOwnerAID;
	m_dwOwnerPID = dwOwnerPID;
}
#endif

https://puu.sh/sgHQP/a214ca04b9.png

---

Search:
	for (bItemCount = 0; bItemCount < SHOP_HOST_ITEM_MAX_NUM; ++bItemCount)
		if (0 == (pTable + bItemCount)->vnum)
			break;

	SetShopItems(pTable, bItemCount);

Change:
	for (bItemCount = 0; bItemCount < SHOP_HOST_ITEM_MAX_NUM; ++bItemCount)
		if (0 == (pTable + bItemCount)->vnum)
			break;

#ifdef __OFFLINE_SHOP__
	SetShopItems(NULL, pTable, bItemCount);
#else
	SetShopItems(pTable, bItemCount);
#endif

https://puu.sh/sgHTP/96c91a46e3.png

---

Search:
bool CShop::Create(DWORD dwVnum, DWORD dwNPCVnum, TShopItemTable * pTable)
{
	...
}

Add it under:
#ifdef __OFFLINE_SHOP__
bool CShop::Create(TOfflineShopTable* table)
{
	sys_log(1, "OFFLINESHOP PID %u (Shopkeeper)", table->dwPID);

	BYTE bGridTable[6][2] = {
		{ 5, 8 },{ 5, 10 },{ 6, 10 },{ 7, 10, },{ 8, 10 },{ 9, 10 }
	};
	BYTE* bSelectedGrid = bGridTable[table->dwSize];

	m_pGrid->Clear();
	M2_DELETE(m_pGrid);
	m_pGrid = M2_NEW CGrid(bSelectedGrid[0], bSelectedGrid[1]);
	m_pGrid->Clear();

	m_itemVector.resize(SHOP_HOST_ITEM_MAX_NUM);
	memset(&m_itemVector[0], 0, sizeof(SHOP_ITEM) * m_itemVector.size());

	DWORD dwExpireDate = table->dwInstallTime + table->dwDuration;
	DWORD dwNowTimestamp = get_global_time();
	sys_log(0, "Create Offlineshop Install time: %u Expire time: %u Now: %u", table->dwInstallTime, dwExpireDate, dwNowTimestamp);

	if (dwNowTimestamp > dwExpireDate)
	{
		sys_err("Create Offlineshop fail %s:%u cannot created. shop's time expired", table->szName, table->dwPID);
		return false;
	}

	for (int i = 0; i < SHOP_HOST_ITEM_MAX_NUM; ++i)
	{
		TPlayerItem* pkItemTable = &table->items[i];
		if (pkItemTable->id == 0)
			continue;

		LPITEM pkItem = NULL;
		if ((pkItem = ITEM_MANAGER::instance().CreateItem(pkItemTable->vnum, pkItemTable->count, pkItemTable->id)) == NULL)
		{
			sys_err("Create Offlineshop fail %s item[id:%u] cannot created. item can not loaded", table->szName, pkItemTable->id);
			continue;
		}

		pkItem->SetSkipSave(true);
		pkItem->SetSockets(pkItemTable->alSockets);
		pkItem->SetAttributes(pkItemTable->aAttr);

		pkItem->SetLastOwnerPID(pkItemTable->owner);

		pkItem->SetCell(NULL, i);
		pkItem->SetWindow(pkItemTable->window);

		const TItemTable* pkItemProto = pkItem->GetProto();		
		m_pGrid->Put(pkItemTable->pos, 1, pkItemProto->bSize);


		SHOP_ITEM & item = m_itemVector[pkItemTable->pos];
		item.pkItem = pkItem;
		item.itemid = pkItem->GetID();
		item.vnum = pkItem->GetVnum();
		item.count = pkItem->GetCount();
		item.price = table->price[i];
		item.price2 = table->price2[i];
		item.price3 = table->price3[i];
		item.price4 = table->price4[i];

		char name[36];
		snprintf(name, sizeof(name), "%-20s(#%-5d) (x %d)", pkItemProto->szName, (int)item.vnum, item.count);
		sys_log(1, "OFFLINE_SHOP_ITEM: %-36s PRICE %-5d", name, item.price);
	}

	m_Money = table->ullMoney;
	m_bColor = table->dwColor;
	m_bSize = table->dwSize;
	m_bIsLocked = false;

	return true;
}
#endif

https://puu.sh/sgHWr/67eeec09f2.png

---

Search:
void CShop::SetShopItems(TShopItemTable * pTable, BYTE bItemCount)
{

Change:
#ifdef __OFFLINE_SHOP__
void CShop::SetShopItems(LPCHARACTER pkOwner, TShopItemTable * pTable, BYTE bItemCount)
#else
void CShop::SetShopItems(TShopItemTable * pTable, BYTE bItemCount)
#endif
{
#ifdef __OFFLINE_SHOP__
	if (!bItemCount) {
		sys_err("Offline shop init fail! Null item count.");

		LPCHARACTER owner = (pkOwner ? pkOwner : m_pkPC);
		if (owner)
			sys_err("Owner: %s[%u]", owner->GetName(), owner->GetPlayerID());
		return;
	}
#endif

https://puu.sh/sgHXZ/90fc3e8e95.png

---

Search:
	m_pGrid->Clear();

	m_itemVector.resize(SHOP_HOST_ITEM_MAX_NUM);
	memset(&m_itemVector[0], 0, sizeof(SHOP_ITEM) * m_itemVector.size());

Change:
#ifdef __OFFLINE_SHOP__
	BYTE bGridTable[6][2] = {
		{ 5, 8 },{ 5, 10 },{ 6, 10 },{ 7, 10, },{ 8, 10 },{ 9, 10 }
	};

	if (m_pkPC)
	{
		BYTE* bSelectedGrid = bGridTable[m_bSize];
		if (bItemCount > bSelectedGrid[0] * bSelectedGrid[1]) {
			sys_err("maximum item count from allocated grid count. item count: %d grid count: %d", bItemCount, bSelectedGrid[0] * bSelectedGrid[1]);
			return;
		}

		m_pGrid->Clear();
		M2_DELETE(m_pGrid);
		m_pGrid = M2_NEW CGrid(bSelectedGrid[0], bSelectedGrid[1]);
		m_pGrid->Clear();
	}
	else {
		if (bItemCount > 40)
			return;
	}
#else
	m_pGrid->Clear();
#endif

	m_itemVector.resize(SHOP_HOST_ITEM_MAX_NUM);
	memset(&m_itemVector[0], 0, sizeof(SHOP_ITEM) * m_itemVector.size());

https://puu.sh/sgHZF/c4f5add898.png

---

Search:
		if (m_pkPC)
		{
			pkItem = m_pkPC->GetItem(pTable->pos);

Change:
		if (m_pkPC)
		{
#ifdef __OFFLINE_SHOP__
			pkItem = (pkOwner ? pkOwner : m_pkPC)->GetItem(pTable->pos);
#else
			pkItem = m_pkPC->GetItem(pTable->pos);
#endif

https://puu.sh/sgI1i/3cddd9989f.png

---

Search:
			if (!pkItem)
			{
				sys_err("cannot find item on pos (%d, %d) (name: %s)", pTable->pos.window_type, pTable->pos.cell, m_pkPC->GetName());
				continue;
			}

Change:
			if (!pkItem)
			{
#ifdef __OFFLINE_SHOP__
				sys_err("cannot find item on pos (%d, %d) (name: %s)", pTable->pos.window_type, pTable->pos.cell, (pkOwner ? pkOwner : m_pkPC)->GetName());
#else
				sys_err("cannot find item on pos (%d, %d) (name: %s)", pTable->pos.window_type, pTable->pos.cell, m_pkPC->GetName());
#endif
				continue;
			}

https://puu.sh/sgI2U/4fd066dfde.png

---

Search:
			if (IsPCShop())
			{
				sys_err("not empty position for pc shop %s[%d]", m_pkPC->GetName(), m_pkPC->GetPlayerID());
			}
			else
			{
				sys_err("not empty position for npc shop");
			}

Change:
			if (IsPCShop())
			{
#ifdef __OFFLINE_SHOP__
				sys_err("not empty position for pc shop %s[%d]", (pkOwner ? pkOwner : m_pkPC)->GetName(), (pkOwner ? pkOwner : m_pkPC)->GetPlayerID());
#else
				sys_err("not empty position for pc shop %s[%d]", m_pkPC->GetName(), m_pkPC->GetPlayerID());
#endif
			}
			else
			{
				sys_err("not empty position for npc shop");
			}

https://puu.sh/sgI4I/92404e16cf.png
---

Search:
		m_pGrid->Put(iPos, 1, item_table->bSize);

		SHOP_ITEM & item = m_itemVector[iPos];

		item.pkItem = pkItem;
		item.itemid = 0;

Add it under:
#ifdef __OFFLINE_SHOP__
		if (pkItem)
		{
			if (pkOwner)
			{
				pkOwner->SyncQuickslot(QUICKSLOT_TYPE_ITEM, pkItem->GetCell(), 255);

				pkItem->SetSkipSave(true);
				pkItem->RemoveFromCharacter();

				pkItem->SetCell(NULL, iPos);
				pkItem->SetWindow(OFFLINE_SHOP);

				ITEM_MANAGER::instance().SaveSingleItem(pkItem);
			}

			item.itemid = pkItem->GetID();
			item.vnum = pkItem->GetVnum();
			item.count = pkItem->GetCount();
			item.price = pTable->price;
			item.price2 = pTable->price2;
			item.price3 = pTable->price3;
			item.price4 = pTable->price4;
		}
#else

https://puu.sh/sgI75/0d76c60394.png
---

Search:
		if (item.pkItem)
		{
			item.vnum = pkItem->GetVnum();
			item.count = pkItem->GetCount(); // PC ¼¥ÀÇ °æ¿ì ¾ÆÀÌÅÛ °³¼ö´Â ÁøÂ¥ ¾ÆÀÌÅÛÀÇ °³¼ö¿©¾ß ÇÑ´Ù.
			item.price = pTable->price; // °¡°İµµ »ç¿ëÀÚ°¡ Á¤ÇÑ´ë·Î..
			item.itemid	= pkItem->GetID();
		}
		else
		{
			item.vnum = pTable->vnum;
			item.count = pTable->count;

Change:
		if (item.pkItem)
		{
			item.vnum = pkItem->GetVnum();
			item.count = pkItem->GetCount(); // PC ¼¥ÀÇ °æ¿ì ¾ÆÀÌÅÛ °³¼ö´Â ÁøÂ¥ ¾ÆÀÌÅÛÀÇ °³¼ö¿©¾ß ÇÑ´Ù.
			item.price = pTable->price; // °¡°İµµ »ç¿ëÀÚ°¡ Á¤ÇÑ´ë·Î..
			item.itemid	= pkItem->GetID();
		}
#endif
		else
		{
			item.vnum = pTable->vnum;
			item.count = pTable->count;
#ifdef __OFFLINE_SHOP__
			item.price2 = pTable->price2;
			item.price3 = pTable->price3;
			item.price4 = pTable->price4;
#endif

https://puu.sh/sgI8M/1cd34c7f53.png

---

Search:
		sys_log(0, "SHOP_ITEM: %-36s PRICE %-5d", name, item.price);

Change:
#ifdef __OFFLINE_SHOP__
		sys_log(0, "SHOP_ITEM: %-36s PRICE %-5d PRICE2: %d PRICE3: %d PRICE4: %d", name, item.price, item.price2, item.price3, item.price4);
#else
		sys_log(0, "SHOP_ITEM: %-36s PRICE %-5d", name, item.price);
#endif
https://puu.sh/sgIaY/7ffa31e450.png

---

Search:
int CShop::Buy(LPCHARACTER ch, BYTE pos)
{

Add it under:
#ifdef __OFFLINE_SHOP__
	if (m_bIsLocked == true)
	{
		sys_log(0, "Shop::Buy : locked shop: %s", ch->GetName());
		return SHOP_SUBHEADER_GC_INVALID_POS;
	}

	if (IsPCShop() && ch && GetOwner() && ch->GetPlayerID() == GetOwner())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You can not buy item from your offline shop!");
		sys_log(0, "Shop::Buy : itself offline shop: %s", ch->GetName());
		return SHOP_SUBHEADER_GC_INVALID_POS;
	}
#endif

https://puu.sh/sgIcT/867672e65c.png

---

Search:
	if (r_item.price < 0)
	{
		LogManager::instance().HackLog("SHOP_BUY_GOLD_OVERFLOW", ch);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}

* OR *
	if (r_item.price <= 0)
	{
		LogManager::instance().HackLog("SHOP_BUY_GOLD_OVERFLOW", ch);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}

Add it under:
#ifdef __OFFLINE_SHOP__
	if (r_item.price2 < 0)
	{
		LogManager::instance().HackLog("SHOP_BUY_COIN_OVERFLOW", ch);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_COIN;
	}
	if (r_item.price3 < 0)
	{
		LogManager::instance().HackLog("SHOP_BUY_GOLDBAR_OVERFLOW", ch);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_GOLDBAR;
	}
	if (r_item.price4 < 0)
	{
		LogManager::instance().HackLog("SHOP_BUY_WON_OVERFLOW", ch);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_WON;
	}
#endif

https://puu.sh/sgIfQ/e1d42afe60.png

---

Search:
		if (!pkSelectedItem)
		{
			sys_log(0, "Shop::Buy : Critical: This user seems to be a hacker : invalid pcshop item : BuyerPID:%d SellerPID:%d",
					ch->GetPlayerID(),
					m_pkPC->GetPlayerID());

			return false;
		}

		if ((pkSelectedItem->GetOwner() != m_pkPC))
		{
			sys_log(0, "Shop::Buy : Critical: This user seems to be a hacker : invalid pcshop item : BuyerPID:%d SellerPID:%d",
					ch->GetPlayerID(),
					m_pkPC->GetPlayerID());

			return false;
		}
	}

Change:
		if (!pkSelectedItem)
		{
			sys_log(0, "Shop::Buy : Critical: This user seems to be a hacker : invalid pcshop item : BuyerPID:%d SellerPID:%d",
					ch->GetPlayerID(), m_pkPC->GetPlayerID());
			return SHOP_SUBHEADER_GC_SOLD_OUT;
		}
#ifdef __OFFLINE_SHOP__
		if ((pkSelectedItem->GetLastOwnerPID() && pkSelectedItem->GetLastOwnerPID() != GetOwner()))
		{
			sys_log(0, "Shop::Buy : Critical: This user seems to be a hacker : invalid pcshop item : BuyerPID:%d SellerPID:%d",
					ch->GetPlayerID(), m_pkPC->GetPlayerID());
			return SHOP_SUBHEADER_GC_SOLD_OUT;
		}
#else
		if ((pkSelectedItem->GetOwner() != m_pkPC))
		{
			sys_log(0, "Shop::Buy : Critical: This user seems to be a hacker : invalid pcshop item : BuyerPID:%d SellerPID:%d",
					ch->GetPlayerID(), m_pkPC->GetPlayerID());
			return SHOP_SUBHEADER_GC_SOLD_OUT;
		}
#endif

https://puu.sh/sgIji/da7639167b.png

---

Search:
	if (ch->GetGold() < (int) dwPrice)
	{
		sys_log(1, "Shop::Buy : Not enough money : %s has %d, price %d", ch->GetName(), ch->GetGold(), dwPrice);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}

Add it under:
#ifdef __OFFLINE_SHOP__
	DWORD dwPrice2 = r_item.price2; // coin
	if (ch->GetCoins() < (long)dwPrice2)
	{
		sys_log(1, "Shop::Buy : Not enough money price2 : %s has %d, price %d", ch->GetName(), ch->GetCoins(), dwPrice2);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_COIN;
	}

	DWORD dwPrice3 = r_item.price3; // goldbar
	if (ch->CountSpecifyItem(80007) < (int)dwPrice3)
	{
		sys_log(1, "Shop::Buy : Not enough money price3 : %s has %d, price %d", ch->GetName(), ch->CountSpecifyItem(80007), dwPrice3);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_GOLDBAR;
	}

	DWORD dwPrice4 = r_item.price4; // won
#ifdef ENABLE_CHEQUE_SYSTEM
	if (ch->GetPoint(POINT_CHEQUE) < dwPrice4)
	{
		sys_log(1, "Shop::Buy : Not enough money price4 : %s has %d, price %d", ch->GetName(), ch->GetPoint(POINT_CHEQUE), dwPrice4);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_WON;
	}
#endif
#endif

https://puu.sh/sgImA/e48b3a1e95.png

---

Search:
	ch->PointChange(POINT_GOLD, -dwPrice, false);

Add it under:
#ifdef __OFFLINE_SHOP__
	if (dwPrice2 > 0)
		ch->UpdateCoins(0, -dwPrice2);
	if (dwPrice3 > 0)
		ch->RemoveSpecifyItem(80007, dwPrice3);
#ifdef ENABLE_CHEQUE_SYSTEM
	if (dwPrice4 > 0)
		ch->PointChange(POINT_CHEQUE, -dwPrice4, true);
#endif
#endif

https://puu.sh/sgIpw/3f34ab456e.png

---

Remove:
	//¼¼±İ °è»ê
	DWORD dwTax = 0;
	int iVal = 0;

	if (LC_IsYMIR() ||  LC_IsKorea())
	{
		if (0 < (iVal = quest::CQuestManager::instance().GetEventFlag("trade_tax")))
		{
			if (iVal > 100)
				iVal = 100;

			dwTax = dwPrice * iVal / 100;
			dwPrice = dwPrice - dwTax;
		}
		else
		{
			iVal = 3;
			dwTax = dwPrice * iVal / 100;
			dwPrice = dwPrice - dwTax;			
		}
	}
	else
	{
		iVal = quest::CQuestManager::instance().GetEventFlag("personal_shop");

		if (0 < iVal)
		{
			if (iVal > 100)
				iVal = 100;

			dwTax = dwPrice * iVal / 100;
			dwPrice = dwPrice - dwTax;
		}
		else
		{
			iVal = 0;
			dwTax = 0;
		}
	}

	// »óÁ¡¿¡¼­ »ì‹š ¼¼±İ 5%
	if (!m_pkPC) 
	{
		CMonarch::instance().SendtoDBAddMoney(dwTax, ch->GetEmpire(), ch);
	}

---

Search:
	//¼¼±İ °è»ê
	DWORD dwTax = 0;
	int iVal = 0;

	if (LC_IsYMIR() ||  LC_IsKorea())
	{
		if (0 < (iVal = quest::CQuestManager::instance().GetEventFlag("trade_tax")))
		{
			if (iVal > 100)
				iVal = 100;

			dwTax = dwPrice * iVal / 100;
			dwPrice = dwPrice - dwTax;
		}
		else
		{
			iVal = 3;
			dwTax = dwPrice * iVal / 100;
			dwPrice = dwPrice - dwTax;			
		}
	}
	else
	{
		iVal = quest::CQuestManager::instance().GetEventFlag("personal_shop");

		if (0 < iVal)
		{
			if (iVal > 100)
				iVal = 100;

			dwTax = dwPrice * iVal / 100;
			dwPrice = dwPrice - dwTax;
		}
		else
		{
			iVal = 0;
			dwTax = 0;
		}
	}

	// »óÁ¡¿¡¼­ »ì‹š ¼¼±İ 5%
	if (!m_pkPC) 
	{
		CMonarch::instance().SendtoDBAddMoney(dwTax, ch->GetEmpire(), ch);
	}

	// ±ºÁÖ ½Ã½ºÅÛ : ¼¼±İ Â¡¼ö
	if (m_pkPC)
	{
		m_pkPC->SyncQuickslot(QUICKSLOT_TYPE_ITEM, item->GetCell(), 255);

		if (item->GetVnum() == 90008 || item->GetVnum() == 90009) // VCARD
		{
			VCardUse(m_pkPC, ch, item);
			item = NULL;
		}
		else
		{
			char buf[512];

			if (item->GetVnum() >= 80003 && item->GetVnum() <= 80007)
			{
				snprintf(buf, sizeof(buf), "%s FROM: %u TO: %u PRICE: %u", item->GetName(), ch->GetPlayerID(), m_pkPC->GetPlayerID(), dwPrice);
				LogManager::instance().GoldBarLog(ch->GetPlayerID(), item->GetID(), SHOP_BUY, buf);
				LogManager::instance().GoldBarLog(m_pkPC->GetPlayerID(), item->GetID(), SHOP_SELL, buf);
			}
			
			item->RemoveFromCharacter();
			if (item->IsDragonSoul())
				item->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
			else
				item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			ITEM_MANAGER::instance().FlushDelayedSave(item);
			

			snprintf(buf, sizeof(buf), "%s %u(%s) %u %u", item->GetName(), m_pkPC->GetPlayerID(), m_pkPC->GetName(), dwPrice, item->GetCount());
			LogManager::instance().ItemLog(ch, item, "SHOP_BUY", buf);

			snprintf(buf, sizeof(buf), "%s %u(%s) %u %u", item->GetName(), ch->GetPlayerID(), ch->GetName(), dwPrice, item->GetCount());
			LogManager::instance().ItemLog(m_pkPC, item, "SHOP_SELL", buf);
		}

		r_item.pkItem = NULL;
		BroadcastUpdateItem(pos);

		m_pkPC->PointChange(POINT_GOLD, dwPrice, false);

		if (iVal > 0)
			m_pkPC->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("ÆÇ¸Å±İ¾×ÀÇ %d %% °¡ ¼¼±İÀ¸·Î ³ª°¡°ÔµË´Ï´Ù"), iVal);

		CMonarch::instance().SendtoDBAddMoney(dwTax, m_pkPC->GetEmpire(), m_pkPC);
	}
	else
	{
		if (item->IsDragonSoul())
			item->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
		else
			item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
		ITEM_MANAGER::instance().FlushDelayedSave(item);
		LogManager::instance().ItemLog(ch, item, "BUY", item->GetName());

		if (item->GetVnum() >= 80003 && item->GetVnum() <= 80007)
		{
			LogManager::instance().GoldBarLog(ch->GetPlayerID(), item->GetID(), PERSONAL_SHOP_BUY, "");
		}

		DBManager::instance().SendMoneyLog(MONEY_LOG_SHOP, item->GetVnum(), -dwPrice);
	}

	if (item)
		sys_log(0, "SHOP: BUY: name %s %s(x %d):%u price %u", ch->GetName(), item->GetName(), item->GetCount(), item->GetID(), dwPrice);

    ch->Save();

    return (SHOP_SUBHEADER_GC_OK);


Change:
#ifdef __OFFLINE_SHOP__
	DWORD dwGoldbarCosts = 2000000; /* Default: 2.000.000 */
	TItemTable* rItem = ITEM_MANAGER::instance().GetTable(80007);
	if (rItem && rItem->dwGold)
		dwGoldbarCosts = rItem->dwGold;

	if (m_pkPC)
	{
		m_Money += dwPrice;
		if (dwPrice3)
			m_Money += dwGoldbarCosts * dwPrice3;

		GuestMapType::iterator it = m_map_guest.begin();
		GuestMapType::iterator it_end = m_map_guest.end();
		for (; it != it_end; ++it)
		{
			LPCHARACTER pkGuest = it->first;
			if (pkGuest->GetDesc() && pkGuest->GetPlayerID() == GetOwner())
			{
				TPacketGCShop pack;

				pack.header = HEADER_GC_SHOP;
				pack.subheader = SHOP_SUBHEADER_GC_UPDATE_MONEY;
				pack.size = sizeof(pack) + sizeof(m_Money);

				pkGuest->GetDesc()->BufferedPacket(&pack, sizeof(pack));
				pkGuest->GetDesc()->Packet(&m_Money, sizeof(m_Money));
				break;
			}
		}
	}

	if (HasOwner())
	{
		{
			item->SetSkipSave(false);
			item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			item->SetWindow(SAFEBOX_OFFLINE_SHOP); // Get new item to extra safebox
			ITEM_MANAGER::instance().SaveSingleItem(item); // Save item to extra safebox
			item->SetWindow(INVENTORY); // Set inventory window as temporary window
			ITEM_MANAGER::instance().SaveSingleItem(item); // Register delayed save request for inventory window

			char buf[512];

			snprintf(buf, sizeof(buf), "%s %u %u %u", item->GetName(), m_dwOwnerPID, dwPrice, item->GetCount());
			LogManager::instance().ItemLog(ch, item, "SHOP_BUY2", buf);

			snprintf(buf, sizeof(buf), "%s %u(%s) %u %u", item->GetName(), ch->GetPlayerID(), ch->GetName(), dwPrice, item->GetCount());
			LogManager::instance().ItemLog(m_dwOwnerPID, 0, 0, item->GetID(), "SHOP_SELL2", buf, "", item->GetVnum());
		}

		r_item.pkItem = NULL;

		SShopSoldData lpSoldData;
		lpSoldData.lpShop = this;
		lpSoldData.vnum = item->GetVnum();
		lpSoldData.Price = dwPrice;
		lpSoldData.Price2 = dwPrice2;
		lpSoldData.Price3 = dwPrice3;
		lpSoldData.Price4 = dwPrice4;
		lpSoldData.Count = item->GetCount();
		thecore_memcpy(lpSoldData.alSockets, item->GetSockets(), sizeof(lpSoldData.alSockets));
		thecore_memcpy(lpSoldData.aAttr, item->GetAttributes(), sizeof(lpSoldData.aAttr));
#if 0
		strlcpy(lpSoldData.newOwner, ch->GetName(), sizeof(lpSoldData.newOwner));
		lpSoldData.soldDate = get_global_time();
#endif
		m_SoldItems[pos] = lpSoldData;

		BroadcastUpdateItem(pos);

		TSafeboxMoney p;
		p.dwAID = m_dwOwnerAID;
		p.bType = 1;
		p.llAmount = dwPrice;
		db_clientdesc->DBPacket(HEADER_GD_SAFEBOX_MONEY, 0, &p, sizeof(p));

		if (dwPrice2 > 0)
			ch->UpdateCoins(m_dwOwnerAID, dwPrice2);

		if (dwPrice3 > 0) {
			TSafeboxMoney pBar;
			pBar.dwAID = m_dwOwnerAID;
			pBar.bType = 1;
			pBar.llAmount = dwPrice3 * dwGoldbarCosts;
			db_clientdesc->DBPacket(HEADER_GD_SAFEBOX_MONEY, 0, &pBar, sizeof(pBar));
		}

#ifdef ENABLE_CHEQUE_SYSTEM
		if (dwPrice4 > 0) {
			char szQuery[1024 + 1];
			sprintf(szQuery, "UPDATE player.player SET cheque = cheque + '%u' WHERE id = '%u'", dwPrice4, m_dwOwnerAID);
			std::auto_ptr<SQLMsg> msg(DBManager::instance().DirectQuery(szQuery));
		}
	}
#endif
	}
	else if (m_pkPC)
#else
	if (m_pkPC)
#endif
	{
		m_pkPC->SyncQuickslot(QUICKSLOT_TYPE_ITEM, item->GetCell(), 255);

		char buf[512];

		if (item->GetVnum() >= 80003 && item->GetVnum() <= 80007)
		{
			snprintf(buf, sizeof(buf), "%s FROM: %u TO: %u PRICE: %u", item->GetName(), ch->GetPlayerID(), m_pkPC->GetPlayerID(), dwPrice);
			LogManager::instance().GoldBarLog(ch->GetPlayerID(), item->GetID(), SHOP_BUY, buf);
			LogManager::instance().GoldBarLog(m_pkPC->GetPlayerID(), item->GetID(), SHOP_SELL, buf);
		}

		item->RemoveFromCharacter();
		if (item->IsDragonSoul())
			item->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
		else
			item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
		ITEM_MANAGER::instance().FlushDelayedSave(item);

#ifdef __OFFLINE_SHOP__
		snprintf(buf, sizeof(buf), "%s %u(%s) %u %u %u %u %u", item->GetName(), m_pkPC->GetPlayerID(), m_pkPC->GetName(), dwPrice, dwPrice2, dwPrice3, dwPrice4, item->GetCount());
#else
		snprintf(buf, sizeof(buf), "%s %u(%s) %u %u", item->GetName(), m_pkPC->GetPlayerID(), m_pkPC->GetName(), dwPrice, item->GetCount());
#endif
		LogManager::instance().ItemLog(ch, item, "SHOP_BUY", buf);

#ifdef __OFFLINE_SHOP__
		snprintf(buf, sizeof(buf), "%s %u(%s) %u %u %u %u %u", item->GetName(), ch->GetPlayerID(), ch->GetName(), dwPrice, dwPrice2, dwPrice3, dwPrice4, item->GetCount());
#else
		snprintf(buf, sizeof(buf), "%s %u(%s) %u %u", item->GetName(), ch->GetPlayerID(), ch->GetName(), dwPrice, item->GetCount());
#endif
		LogManager::instance().ItemLog(m_pkPC, item, "SHOP_SELL", buf);


		r_item.pkItem = NULL;
#ifdef __OFFLINE_SHOP__
		SShopSoldData lpSoldData;
		lpSoldData.lpShop = this;
		lpSoldData.vnum = item->GetVnum();
		lpSoldData.Price = dwPrice;
		lpSoldData.Price2 = dwPrice2;
		lpSoldData.Price3 = dwPrice3;
		lpSoldData.Price4 = dwPrice4;
		lpSoldData.Count = item->GetCount();
		thecore_memcpy(lpSoldData.alSockets, item->GetSockets(), sizeof(lpSoldData.alSockets));
		thecore_memcpy(lpSoldData.aAttr, item->GetAttributes(), sizeof(lpSoldData.aAttr));
#if 0
		strlcpy(lpSoldData.newOwner, ch->GetName(), sizeof(lpSoldData.newOwner));
		lpSoldData.soldDate = get_global_time();
#endif
		m_SoldItems[pos] = lpSoldData;
#endif

		BroadcastUpdateItem(pos);

		m_pkPC->PointChange(POINT_GOLD, dwPrice, false);

#ifdef __OFFLINE_SHOP__
		if (dwPrice2 > 0)
			m_pkPC->UpdateCoins(0, dwPrice2);

		if (dwPrice3 > 0) {
			DWORD dwGoldbarCosts = 2000000; /* Default: 2.000.000 */
			TItemTable* rItem = ITEM_MANAGER::instance().GetTable(80007);
			if (rItem && rItem->dwGold)
				dwGoldbarCosts = rItem->dwGold;

			TSafeboxMoney pBar;
			pBar.dwAID = m_dwOwnerAID;
			pBar.bType = 1;
			pBar.llAmount = dwPrice3 * dwGoldbarCosts;
			db_clientdesc->DBPacket(HEADER_GD_SAFEBOX_MONEY, 0, &pBar, sizeof(pBar));
		}

#ifdef ENABLE_CHEQUE_SYSTEM
		if (dwPrice4 > 0)
			m_pkPC->PointChange(POINT_CHEQUE, dwPrice4);
#endif

#endif
	}
	else
	{
		if (item->IsDragonSoul())
			item->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
		else
			item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
		ITEM_MANAGER::instance().FlushDelayedSave(item);
		LogManager::instance().ItemLog(ch, item, "BUY", item->GetName());

		if (item->GetVnum() >= 80003 && item->GetVnum() <= 80007)
		{
			LogManager::instance().GoldBarLog(ch->GetPlayerID(), item->GetID(), PERSONAL_SHOP_BUY, "");
		}

		DBManager::instance().SendMoneyLog(MONEY_LOG_SHOP, item->GetVnum(), -dwPrice);
	}

	if (item)
#ifdef __OFFLINE_SHOP__
		sys_log(0, "SHOP: BUY: name %s %s(x %d):%u price1 %u price2 %u price3 %u price4 %u", ch->GetName(), item->GetName(), item->GetCount(), item->GetID(), dwPrice, dwPrice2, dwPrice3, dwPrice4);
#else
		sys_log(0, "SHOP: BUY: name %s %s(x %d):%u price %u", ch->GetName(), item->GetName(), item->GetCount(), item->GetID(), dwPrice);
#endif

#ifdef __OFFLINE_SHOP__
	if (HasOwner())
	{
		char buf[1024] = { 0 };
		char itemlink[256];
		int len;
		int i;

		len = snprintf(itemlink, sizeof(itemlink), "item:%x:%x", item->GetVnum(), item->GetFlag());

		for (i = 0; i < ITEM_SOCKET_MAX_NUM; i++)
			len += snprintf(itemlink + len, sizeof(itemlink) - len, ":%d", item->GetSocket(i));

		for (i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; i++) {
			if (i >= item->GetAttributeCount())
				len += snprintf(itemlink + len, sizeof(itemlink) - len, ":0:0");
			else
				len += snprintf(itemlink + len, sizeof(itemlink) - len, ":%x:%d", item->GetAttributeType(i), item->GetAttributeValue(i));
		}

		//if (item->GetAttributeCount() > 0)
		snprintf(buf, sizeof(buf), "|cffffc700|H%s|h[%s]|h|r", itemlink, item->GetName());
		//else
		//	snprintf(buf, sizeof(buf), "|cfff1e6c0|H%s|h[%s]|h|r", itemlink, item->GetName());

		LPCHARACTER ownerch = CHARACTER_MANAGER::instance().FindByPID(m_dwOwnerPID);
		if (ownerch)
			ownerch->ChatPacket(CHAT_TYPE_INFO, "<Buy notice> %s bought %s with %u yang %u coin %u goldbar %u won from your offline shop.", ch->GetName(), buf, dwPrice, dwPrice2, dwPrice3, dwPrice4);
	}
#endif

	ch->Save();

#ifdef __OFFLINE_SHOP__
	if (HasOwner())
	{
		for (DWORD i = 0; i < SHOP_HOST_ITEM_MAX_NUM; ++i)
		{
			const SHOP_ITEM & item = m_itemVector[i];

			if (item.pkItem)
				break;

			if (i == SHOP_HOST_ITEM_MAX_NUM - 1)
			{
				Remove();
				M2_DESTROY_CHARACTER(m_pkPC);
			}
		}
	}
#endif

	return (SHOP_SUBHEADER_GC_OK);

---

Search:
	TPacketGCShopStart pack2;

	memset(&pack2, 0, sizeof(pack2));
	pack2.owner_vid = owner_vid;

Change:
	TPacketGCShopStart pack2;

	memset(&pack2, 0, sizeof(pack2));
#ifdef __OFFLINE_SHOP__
	pack2.vid = owner_vid;
#else
	pack2.owner_vid = owner_vid;
#endif

#ifdef __OFFLINE_SHOP__
	if (IsPCShop() || HasOwner())
		pack2.grid_type = m_bSize;
	else
		pack2.grid_type = 0;


	if (HasOwner())
	{
		if (ch->GetPlayerID() == m_dwOwnerPID)
			pack2.owner_vid = ch->GetVID();
		else
			pack2.owner_vid = -1;
	}
#endif

https://puu.sh/sgIFk/1829883b36.png

---

Search:
		if (m_pkPC && !item.pkItem)
			continue;

		pack2.items[i].vnum = item.vnum;

		if (bOtherEmpire) // no empire price penalty for pc shop
			pack2.items[i].price = item.price * 3;
		else
			pack2.items[i].price = item.price;

		pack2.items[i].count = item.count;

		if (item.pkItem)
		{
			thecore_memcpy(pack2.items[i].alSockets, item.pkItem->GetSockets(), sizeof(pack2.items[i].alSockets));
			thecore_memcpy(pack2.items[i].aAttr, item.pkItem->GetAttributes(), sizeof(pack2.items[i].aAttr));
		}
	}

Change:
		if (m_pkPC && !item.pkItem)
		{
#ifdef __OFFLINE_SHOP__
			DWORD dwVnum = GetSoldItemVnum(i);
			if (dwVnum)
			{
				pack2.items[i].vnum = dwVnum;
				long lGetPriceFromTempData = GetSoldPrice(i, 1);

				if (bOtherEmpire) // no empire price penalty for pc shop
					pack2.items[i].price = lGetPriceFromTempData * 3;
				else
					pack2.items[i].price = lGetPriceFromTempData;

				pack2.items[i].price2 = GetSoldPrice(i, 2);
				pack2.items[i].price3 = GetSoldPrice(i, 3);
				pack2.items[i].price4 = GetSoldPrice(i, 4);

				pack2.items[i].count = GetSoldCount(i);

				thecore_memcpy(pack2.items[i].alSockets, GetSoldSockets(i), sizeof(pack2.items[i].alSockets));
				thecore_memcpy(pack2.items[i].aAttr, GetSoldAttributes(i), sizeof(pack2.items[i].aAttr));
				pack2.items[i].isSold = 1;
			}
			else
#endif				
				continue;
		}

		else {
			pack2.items[i].vnum = item.vnum;

			if (bOtherEmpire) // no empire price penalty for pc shop
				pack2.items[i].price = item.price * 3;
			else
				pack2.items[i].price = item.price;

			pack2.items[i].count = item.count;
#ifdef __OFFLINE_SHOP__
			pack2.items[i].price2 = item.price2;
			pack2.items[i].price3 = item.price3;
			pack2.items[i].price4 = item.price4;
#endif
			if (item.pkItem)
			{
				thecore_memcpy(pack2.items[i].alSockets, item.pkItem->GetSockets(), sizeof(pack2.items[i].alSockets));
				thecore_memcpy(pack2.items[i].aAttr, item.pkItem->GetAttributes(), sizeof(pack2.items[i].aAttr));
			}
#ifdef __OFFLINE_SHOP__
			pack2.items[i].isSold = 0;
#endif
		}
	}


https://puu.sh/sgIIs/c5909d73b3.png
https://puu.sh/sgIJ7/48b896db74.png

---

Search:
	ch->GetDesc()->BufferedPacket(&pack, sizeof(TPacketGCShop));
	ch->GetDesc()->Packet(&pack2, sizeof(TPacketGCShopStart));

Add it under:
#ifdef __OFFLINE_SHOP__
	LPCHARACTER ownerch = CHARACTER_MANAGER::instance().FindByPID(m_dwOwnerPID);
	if (IsPCShop() && ownerch && ownerch != ch && ownerch->IsPC())
		ownerch->ChatPacket(CHAT_TYPE_INFO, "%s is looking to your offline shop!", ch->GetName());

	if (ch->GetPlayerID() == m_dwOwnerPID)
	{
		pack.subheader = SHOP_SUBHEADER_GC_UPDATE_MONEY;
		pack.size = sizeof(pack)+sizeof(m_Money);

		ch->GetDesc()->BufferedPacket(&pack, sizeof(pack));
		ch->GetDesc()->Packet(&m_Money, sizeof(m_Money));
	}
#endif

https://puu.sh/sgIKI/6977aabec4.png

---

Search:
void CShop::RemoveGuest(LPCHARACTER ch)
{
	if (ch->GetShop() != this)
		return;

Add it under:
#ifdef __OFFLINE_SHOP__
	LPCHARACTER ownerch = CHARACTER_MANAGER::instance().FindByPID(ch->GetShop()->GetOwner());
	if (IsPCShop() && ownerch && ownerch != ch && ownerch->IsPC())
		ownerch->ChatPacket(CHAT_TYPE_INFO, "%s is stopped look at to your offline shop!", ch->GetName());
#endif

https://puu.sh/sgIMK/90fb38bb8a.png

---

Search:
void CShop::Broadcast(const void * data, int bytes)
{
	...
}

Add it under:
#ifdef __OFFLINE_SHOP__
DWORD CShop::GetSoldItemVnum(BYTE pos)
{
	if (m_SoldItems.empty() || m_SoldItems.begin() == m_SoldItems.end())
		return NULL;

	std::map<BYTE, SShopSoldData>::iterator it;
	for (it = m_SoldItems.begin(); it != m_SoldItems.end(); ++it)
	{
		if (it->first != pos)
			continue;

		if (it->second.lpShop != this)
			continue;

		if (it->second.vnum == NULL)
			return NULL;

		return it->second.vnum;
	}
	return NULL;
}

long CShop::GetSoldPrice(BYTE pos, BYTE type)
{
	if (m_SoldItems.empty() || m_SoldItems.begin() == m_SoldItems.end())
		return NULL;

	std::map<BYTE, SShopSoldData>::iterator it;
	for (it = m_SoldItems.begin(); it != m_SoldItems.end(); ++it)
	{
		if (it->first != pos)
			continue;

		if (it->second.lpShop != this)
			continue;

		if (type == 1 && it->second.Price == NULL)
			return NULL;
		if (type == 2 && it->second.Price2 == NULL)
			return NULL;
		if (type == 3 && it->second.Price3 == NULL)
			return NULL;
		if (type == 4 && it->second.Price4 == NULL)
			return NULL;
		
		if (type == 4)
			return it->second.Price4;
		if (type == 3)
			return it->second.Price3;
		if (type == 2)
			return it->second.Price2;
		return it->second.Price;
	}
	return NULL;
}
BYTE CShop::GetSoldCount(BYTE pos)
{
	if (m_SoldItems.empty() || m_SoldItems.begin() == m_SoldItems.end())
		return NULL;

	std::map<BYTE, SShopSoldData>::iterator it;
	for (it = m_SoldItems.begin(); it != m_SoldItems.end(); ++it)
	{
		if (it->first != pos)
			continue;

		if (it->second.lpShop != this)
			continue;

		if (it->second.Count == NULL)
			return NULL;

		return it->second.Count;
	}
	return NULL;
}
const long* CShop::GetSoldSockets(BYTE pos)
{
	if (m_SoldItems.empty() || m_SoldItems.begin() == m_SoldItems.end())
		return NULL;

	std::map<BYTE, SShopSoldData>::iterator it;
	for (it = m_SoldItems.begin(); it != m_SoldItems.end(); ++it)
	{
		if (it->first != pos)
			continue;

		if (it->second.lpShop != this)
			continue;

		if (it->second.alSockets == NULL)
			return NULL;

		return it->second.alSockets;
	}
	return NULL;
}
const TPlayerItemAttribute* CShop::GetSoldAttributes(BYTE pos)
{
	if (m_SoldItems.empty() || m_SoldItems.begin() == m_SoldItems.end())
		return NULL;

	std::map<BYTE, SShopSoldData>::iterator it;
	for (it = m_SoldItems.begin(); it != m_SoldItems.end(); ++it)
	{
		if (it->first != pos)
			continue;

		if (it->second.lpShop != this)
			continue;

		if (it->second.aAttr == NULL)
			return NULL;

		return it->second.aAttr;
	}
	return NULL;
}
#endif

https://puu.sh/sgIOG/516f6e8faa.png
https://puu.sh/sgIOc/f70b0b1415.png

---

Search:
void CShop::BroadcastUpdateItem(BYTE pos)
{
	TPacketGCShop pack;
	TPacketGCShopUpdateItem pack2;

	TEMP_BUFFER	buf;

	pack.header		= HEADER_GC_SHOP;
	pack.subheader	= SHOP_SUBHEADER_GC_UPDATE_ITEM;
	pack.size		= sizeof(pack) + sizeof(pack2);

	pack2.pos		= pos;

	if (m_pkPC && !m_itemVector[pos].pkItem)
		pack2.item.vnum = 0;
	else
	{
		pack2.item.vnum	= m_itemVector[pos].vnum;
		if (m_itemVector[pos].pkItem)
		{
			thecore_memcpy(pack2.item.alSockets, m_itemVector[pos].pkItem->GetSockets(), sizeof(pack2.item.alSockets));
			thecore_memcpy(pack2.item.aAttr, m_itemVector[pos].pkItem->GetAttributes(), sizeof(pack2.item.aAttr));
		}
		else
		{
			memset(pack2.item.alSockets, 0, sizeof(pack2.item.alSockets));
			memset(pack2.item.aAttr, 0, sizeof(pack2.item.aAttr));
		}
	}

	pack2.item.price	= m_itemVector[pos].price;
	pack2.item.count	= m_itemVector[pos].count;

	buf.write(&pack, sizeof(pack));
	buf.write(&pack2, sizeof(pack2));

	Broadcast(buf.read_peek(), buf.size());
}

Change:
void CShop::BroadcastUpdateItem(BYTE pos)
{
	TPacketGCShop pack;
	TPacketGCShopUpdateItem pack2;

	pack.header		= HEADER_GC_SHOP;
	pack.subheader	= SHOP_SUBHEADER_GC_UPDATE_ITEM;
	pack.size		= sizeof(pack) + sizeof(pack2);

	pack2.pos		= pos;

	if (m_pkPC && !m_itemVector[pos].pkItem)
	{
#ifdef __OFFLINE_SHOP__
		DWORD dwVnum = GetSoldItemVnum(pos);
		if (dwVnum)
		{
			pack2.item.vnum = dwVnum;
			thecore_memcpy(pack2.item.alSockets, GetSoldSockets(pos), sizeof(pack2.item.alSockets));
			thecore_memcpy(pack2.item.aAttr, GetSoldAttributes(pos), sizeof(pack2.item.aAttr));
			pack2.item.isSold = 1;
		}
		else
#endif
			pack2.item.vnum = m_itemVector[pos].vnum;
	}
	else
	{
		pack2.item.vnum	= m_itemVector[pos].vnum;
		if (m_itemVector[pos].pkItem)
		{
			thecore_memcpy(pack2.item.alSockets, m_itemVector[pos].pkItem->GetSockets(), sizeof(pack2.item.alSockets));
			thecore_memcpy(pack2.item.aAttr, m_itemVector[pos].pkItem->GetAttributes(), sizeof(pack2.item.aAttr));
		}
		else
		{
			memset(pack2.item.alSockets, 0, sizeof(pack2.item.alSockets));
			memset(pack2.item.aAttr, 0, sizeof(pack2.item.aAttr));
		}
#ifdef __OFFLINE_SHOP__
		pack2.item.isSold = 0;
#endif
	}

	pack2.item.price	= m_itemVector[pos].price;
#ifdef __OFFLINE_SHOP__
	pack2.item.price2	= m_itemVector[pos].price2;
	pack2.item.price3	= m_itemVector[pos].price3;
	pack2.item.price4	= m_itemVector[pos].price4;
#endif
	pack2.item.count	= m_itemVector[pos].count;

	TEMP_BUFFER	buf;
	buf.write(&pack, sizeof(pack));
	buf.write(&pack2, sizeof(pack2));

	Broadcast(buf.read_peek(), buf.size());
}


https://puu.sh/sgIQX/291da3a38d.png
https://puu.sh/sgIRn/36998354a0.png

---

Search:
bool CShop::IsSellingItem(DWORD itemID)
{
	...
}

Add it under:
#ifdef __OFFLINE_SHOP__
void CShop::Apply()
{
	if (!HasOwner())
		return;

	TOfflineShopTable p;
	memset(&p, 0, sizeof(p));

	p.dwAID = m_dwOwnerAID;
	p.dwPID = m_dwOwnerPID;

	p.dwX = m_pkPC->GetX();
	p.dwY = m_pkPC->GetY();
	p.dwMapIndex = m_pkPC->GetMapIndex();

	p.dwChannel = g_bChannel;

	p.dwDuration = event_time(m_pkPC->m_pkExpireOfflineShopEvent) / passes_per_sec;

	p.ullMoney = m_Money;
	p.dwSize = m_bSize;
	p.dwColor = m_bColor;

	strlcpy(p.szSign, m_pkPC->GetShopSign().c_str(), sizeof(p.szSign));

	for (DWORD i = 0; i < m_itemVector.size() && i < SHOP_HOST_ITEM_MAX_NUM; ++i)
	{
		const SHOP_ITEM & item = m_itemVector[i];

		if (item.pkItem == NULL)
			continue;

		p.items2[i] = item.itemid;
		p.price[i] = item.price;
		p.price2[i] = item.price2;
		p.price3[i] = item.price3;
		p.price4[i] = item.price4;
	}

	db_clientdesc->DBPacket(HEADER_GD_OFFLINE_SHOP_ENTRY, 0, &p, sizeof(p));
}

void CShop::Remove()
{
	if (!HasOwner())
		return;

	m_bIsLocked = true;

	TOfflineShopTable p;
	memset(&p, 0, sizeof(p));

	p.dwAID = m_dwOwnerAID;
	p.dwPID = m_dwOwnerPID;

	p.dwX = m_pkPC->GetX();
	p.dwY = m_pkPC->GetY();
	p.dwMapIndex = m_pkPC->GetMapIndex();

	p.dwChannel = g_bChannel;

	p.ullMoney = m_Money;
	p.dwSize = m_bSize;
	p.dwColor = m_bColor;

	strlcpy(p.szSign, m_pkPC->GetShopSign().c_str(), sizeof(p.szSign));

	for (DWORD i = 0; i < m_itemVector.size() && i < SHOP_HOST_ITEM_MAX_NUM; ++i)
	{
		SHOP_ITEM& item = m_itemVector[i];

		if (item.pkItem == NULL)
			continue;

		p.items2[i] = item.itemid;
		p.price[i] = item.price;
		p.price2[i] = item.price2;
		p.price3[i] = item.price3;
		p.price4[i] = item.price4;

		item.pkItem->SetWindow(SAFEBOX_OFFLINE_SHOP);
		ITEM_MANAGER::instance().SaveSingleItem(item.pkItem);

		item.pkItem->SetSkipSave(true);
		M2_DESTROY_ITEM(item.pkItem);

		memset(&item, 0, sizeof(item));
	}

	db_clientdesc->DBPacket(HEADER_GD_OFFLINE_SHOP_REMOVE, 0, &p, sizeof(p));
}
#endif

