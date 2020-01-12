Search:
	m_pkChrShopOwner	= NULL;

Add it under:
#ifdef __OFFLINE_SHOP__
	m_pkChrOfflineShopOwner = NULL;
#endif

http://i.imgur.com/JLZt6p6.png
---

Search:
	// MINING
	m_pkMiningEvent = NULL;
	// END_OF_MINING

Add it under:
#ifdef __OFFLINE_SHOP__
	m_pkExpireOfflineShopEvent = NULL;
#endif

http://i.imgur.com/nZWddtJ.png
---

Search:
	// MINING
	event_cancel(&m_pkMiningEvent);
	// END_OF_MINING

Add it under:
#ifdef __OFFLINE_SHOP__
	event_cancel(&m_pkExpireOfflineShopEvent);
#endif

http://i.imgur.com/x76ZWzH.png
---

Search:
void CHARACTER::OpenMyShop(const char * c_pszSign, TShopItemTable * pTable, BYTE bItemCount)
{
	...
}

Add it under:

#ifdef __OFFLINE_SHOP__
void CHARACTER::OpenOfflineShop(const char * c_pszSign, BYTE bType, BYTE bSize, BYTE bColor, TShopItemTable * pTable, BYTE bItemCount)
{
	if (GetMyShop())
		return;

	if (bType < 0 || bType > 5)
		return;
	if (bSize < 0 || bSize > 5)
		return;
	if (bColor < 0 || bColor > 5)
		return;
	if (bItemCount == 0)
		return;


	quest::PC * pPC = quest::CQuestManager::instance().GetPCForce(GetPlayerID());
	if (pPC->IsRunning())
		return;


	char szSign[SHOP_SIGN_MAX_LEN + 1];
	strlcpy(szSign, c_pszSign, sizeof(szSign));

	std::string strSign(szSign);
	if (strSign.length() == 0)
		return;

	if (CBanwordManager::instance().CheckString(strSign.c_str(), strSign.length()))
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("ºñ¼Ó¾î³ª Àº¾î°¡ Æ÷ÇÔµÈ »óÁ¡ ÀÌ¸§À¸·Î »óÁ¡À» ¿­ ¼ö ¾ø½À´Ï´Ù."));
		return;
	}


	LPSECTREE pSec = GetSectree();
	if (!pSec)
		return;

	if (HasNearOfflineShop(GetX(), GetY())) {
		ChatPacket(CHAT_TYPE_INFO, "You can not create your offline shop to near other offline shops!");
		return;
	}


	std::set<TItemPos> cont;
	for (BYTE i = 0; i < bItemCount; ++i)
	{
		if (cont.find((pTable + i)->pos) != cont.end())
		{
			sys_err("OFFSHOP: duplicate shop item detected! (name: %s)", GetName());
			return;
		}

		// ANTI_GIVE, ANTI_MYSHOP check
		LPITEM pkItem = GetItem((pTable + i)->pos);
		if (pkItem)
		{
			const TItemTable * item_table = pkItem->GetProto();
			if (item_table && (IS_SET(item_table->dwAntiFlags, ITEM_ANTIFLAG_GIVE | ITEM_ANTIFLAG_MYSHOP)))
			{
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT("À¯·áÈ­ ¾ÆÀÌÅÛÀº °³ÀÎ»óÁ¡¿¡¼­ ÆÇ¸ÅÇÒ ¼ö ¾ø½À´Ï´Ù."));
				return;
			}

			if (pkItem->IsEquipped() == true)
			{
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT("ÀåºñÁßÀÎ ¾ÆÀÌÅÛÀº °³ÀÎ»óÁ¡¿¡¼­ ÆÇ¸ÅÇÒ ¼ö ¾ø½À´Ï´Ù."));
				return;
			}

			if (true == pkItem->isLocked())
			{
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT("»ç¿ëÁßÀÎ ¾ÆÀÌÅÛÀº °³ÀÎ»óÁ¡¿¡¼­ ÆÇ¸ÅÇÒ ¼ö ¾ø½À´Ï´Ù."));
				return;
			}

			if (__OFFLINE_SHOP_ALLOW_COIN__ == 0)
				(pTable + i)->price2 = 0;
			if (__OFFLINE_SHOP_ALLOW_GOLDBAR__ == 0)
				(pTable + i)->price3 = 0;
			if (__OFFLINE_SHOP_ALLOW_WON__ == 0)
				(pTable + i)->price4 = 0;

			if ((pTable + i)->price == 0 && (pTable + i)->price2 == 0 && (pTable + i)->price3 == 0 && (pTable + i)->price4 == 0)
			{
				ChatPacket(CHAT_TYPE_INFO, "You need write at least 1 price type");
				return;
			}

			if ((pTable + i)->price2 > 10000 || (pTable + i)->price3 > 199 && (pTable + i)->price4 > 999)
				return;
		}

		cont.insert((pTable + i)->pos);
	}


	const static int iTimeArray[] = {
		0,
		60 * 60 * 6 * 1,	/* 6 HOURS */
		60 * 60 * 12 * 1,	/* 12 HOURS */
		60 * 60 * 18 * 1,	/* 18 HOURS */
		60 * 60 * 24 * 1,	/* 24 HOURS */
		60 * 60 * 24 * 2	/* 48 HOURS */
	};
	const static INT iPriceArray[] = {
		10000,
		100000,
		250000,
		500000,
		750000,
		2000000
	};

	if (GetGold() < iPriceArray[bType])
		return;

	if (CShopManager::instance().GetOfflineShopCount(GetPlayerID()) >= OFFLINE_SHOP_MAX_COUNT)
	{
		ChatPacket(CHAT_TYPE_INFO, "A player can open a maximum of %d offline shop.", OFFLINE_SHOP_MAX_COUNT);
		return;
	}

	if (CountSpecifyItem(71049)) {
	}
	else if (CountSpecifyItem(50200))
		RemoveSpecifyItem(50200, 1);
	else
		return; // º¸µû¸®°¡ ¾øÀ¸¸é Áß´Ü.


	if (m_pkExchange)
		m_pkExchange->Cancel();


	LPSHOP pkMyShop = CShopManager::instance().CreateOfflineShop(this, bSize, bColor, pTable, bItemCount);
	if (!pkMyShop)
		return; 

	PointChange(POINT_GOLD, -iPriceArray[bType], false);

	pkMyShop->GetPCShop()->SetShopSign(strSign);
	pkMyShop->GetPCShop()->SetupExpire(iTimeArray[bType]);
	pkMyShop->Apply();
	
	TPacketGCShopSign p;
	p.bHeader = HEADER_GC_SHOP_SIGN;
	p.dwVID = pkMyShop->GetPCShop()->GetVID();
	strlcpy(p.szSign, c_pszSign, sizeof(p.szSign));
	PacketAround(&p, sizeof(TPacketGCShopSign));
}

EVENTFUNC(offshop_expire_event)
{
	char_event_info* info = dynamic_cast<char_event_info*>(event->info);
	if (info == NULL)
		return 0;

	LPCHARACTER	ch = info->ch;
	if (ch == NULL) { // <Factor>
		return 0;
	}

	ch->m_pkExpireOfflineShopEvent = NULL;

	if (ch->GetMyShop())
		ch->GetMyShop()->Remove();

	M2_DESTROY_CHARACTER(ch);
	return 0;
}

void CHARACTER::SetupExpire(int iSec)
{
	if (m_pkExpireOfflineShopEvent != NULL)
		event_cancel(&m_pkExpireOfflineShopEvent);

	char_event_info* info = AllocEventInfo<char_event_info>();
	info->ch = this;

	m_pkExpireOfflineShopEvent = event_create(offshop_expire_event, info, PASSES_PER_SEC(iSec));
}
#endif

http://i.imgur.com/s6NiAxy.png
---

Search:
	// Ã»¼Ò³âÀº Äù½ºÆ® ¸øÇÔ
	if (LC_IsNewCIBN())
	{
		if (pkChrCauser->IsOverTime(OT_3HOUR))
		{
			sys_log(0, "Teen OverTime : name = %s, hour = %d)", pkChrCauser->GetName(), 3);
			return;
		}
		else if (pkChrCauser->IsOverTime(OT_5HOUR))
		{
			sys_log(0, "Teen OverTime : name = %s, hour = %d)", pkChrCauser->GetName(), 5);
			return;
		}
	}

	pkChrCauser->SetQuestNPCID(GetVID());

	if (quest::CQuestManager::instance().Click(pkChrCauser->GetPlayerID(), this))
	{
		return;
	}

Add it upper:

#ifdef __OFFLINE_SHOP__
	if (GetOfflineShopOwner())
	{
		if (pkChrCauser->IsDead())
			return;

		//PREVENT_TRADE_WINDOW
		{
			// Å¬¸¯ÇÑ »ç¶÷ÀÌ ±³È¯/Ã¢°í/°³ÀÎ»óÁ¡/»óÁ¡ÀÌ¿ëÁßÀÌ¶ó¸é ºÒ°¡
			if ((pkChrCauser->GetExchange() || pkChrCauser->IsOpenSafebox() || pkChrCauser->GetMyShop() || pkChrCauser->GetShopOwner()) || pkChrCauser->IsCubeOpen())
			{
				pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´Ù¸¥ °Å·¡Áß(Ã¢°í,±³È¯,»óÁ¡)¿¡´Â °³ÀÎ»óÁ¡À» »ç¿ëÇÒ ¼ö ¾ø½À´Ï´Ù."));
				return;
			}

			// Å¬¸¯ÇÑ ´ë»óÀÌ ±³È¯/Ã¢°í/»óÁ¡ÀÌ¿ëÁßÀÌ¶ó¸é ºÒ°¡
			//if ((GetExchange() || IsOpenSafebox() || GetShopOwner()))
			if ((GetExchange() || IsOpenSafebox() || IsCubeOpen()))
			{
				pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("»ó´ë¹æÀÌ ´Ù¸¥ °Å·¡¸¦ ÇÏ°í ÀÖ´Â ÁßÀÔ´Ï´Ù."));
				return;
			}
		}
		//END_PREVENT_TRADE_WINDOW

		if (pkChrCauser->GetShop())
		{
			pkChrCauser->GetShop()->RemoveGuest(pkChrCauser);
			pkChrCauser->SetShop(NULL);
		}

		GetMyShop()->AddGuest(pkChrCauser, GetVID(), false);
		pkChrCauser->SetShopOwner(this);
		return;
	}
#endif

http://i.imgur.com/ZT7tSa4.png
---

Search:
void CHARACTER::LoadSafebox(int iSize, DWORD dwGold, int iItemCount, TPlayerItem * pItems)

Change:
#ifdef __OFFLINE_SHOP__
void CHARACTER::LoadSafebox(int iSize, uint64_t dwGold, int iItemCount, TPlayerItem * pItems)
#else
void CHARACTER::LoadSafebox(int iSize, DWORD dwGold, int iItemCount, TPlayerItem * pItems)
#endif

http://i.imgur.com/1JIt5Vz.png
---

Search:
	TPacketCGSafeboxSize p;

	p.bHeader = HEADER_GC_SAFEBOX_SIZE;
	p.bSize = iSize;

	GetDesc()->Packet(&p, sizeof(TPacketCGSafeboxSize));

Add it under:
#ifdef __OFFLINE_SHOP__
	m_pkSafebox->SetGold(0);
#endif

http://i.imgur.com/JKtv0lN.png
---

Search:
	m_pkSafebox->Save();

Change:
#ifndef __OFFLINE_SHOP__
	m_pkSafebox->Save();
#endif

http://i.imgur.com/nG16y3F.png
---

Search:
	m_pkMall->Save();

Change:
#ifndef __OFFLINE_SHOP__
	m_pkMall->Save();
#endif

http://i.imgur.com/wd0utcy.png
---

Search:
void CHARACTER::UpdateDepositPulse()
{
	m_deposit_pulse = thecore_pulse() + PASSES_PER_SEC(60*5);	// 5ºĞ
}

bool CHARACTER::CanDeposit() const
{
	return (m_deposit_pulse == 0 || (m_deposit_pulse < thecore_pulse()));
}

Change:
void CHARACTER::UpdateDepositPulse()
{
#ifdef __OFFLINE_SHOP__
	m_deposit_pulse = thecore_pulse() + PASSES_PER_SEC(3);
#else
	m_deposit_pulse = thecore_pulse() + PASSES_PER_SEC(60*5);	// 5ºĞ
#endif
}

bool CHARACTER::CanDeposit() const
{
#ifdef __OFFLINE_SHOP__
	return (m_deposit_pulse < thecore_pulse());
#else
	return (m_deposit_pulse == 0 || (m_deposit_pulse < thecore_pulse()));
#endif
}

http://i.imgur.com/KRqta1Q.png
---

Search:
int	CHARACTER::GetSkillPowerByLevel(int level, bool bMob) const
{
	return CTableBySkill::instance().GetSkillPowerByLevelFromType(GetJob(), GetSkillGroup(), MINMAX(0, level, SKILL_MAX_LEVEL), bMob);
}

Add it under:
#ifdef __OFFLINE_SHOP__
struct FuncSearchNearShops
{
	long m_lNewX;
	long m_lNewY;
	bool m_bResult;
	LPCHARACTER m_ch;

	FuncSearchNearShops(LPCHARACTER ch, long lNewX, long lNewY) {
		m_ch = ch;
		m_bResult = false;
		m_lNewX = lNewX;
		m_lNewY = lNewY;
	}

	void operator() (LPENTITY ent)
	{
		if (ent->IsType(ENTITY_CHARACTER))
		{
			LPCHARACTER ch = (LPCHARACTER)ent;
			if (ch && ch != m_ch && ch->GetMyShop() && ch->GetMyShop()->GetPCShop() && !ch->GetMyShop()->GetPCShop()->IsPC()) {
				if (DISTANCE_APPROX(ch->GetX() - m_lNewX, ch->GetY() - m_lNewY) < 300)
					m_bResult = true;
			}
		}
	}
};


bool CHARACTER::HasNearOfflineShop(long newX, long newY)
{
	LPSECTREE pSec = GetSectree();
	if (!pSec) 
		return true;

	FuncSearchNearShops f(this, newX, newY);
	pSec->ForEachAround(f);
	if (f.m_bResult == true)
		return true;

	return false;
}

void CHARACTER::SetCoins(long val) {
	if (val < 0 || !isdigit(val)) {
		sys_err("Value format isn't valid, Value: %ld", val);
		return;
	}

	long value = val;
	std::auto_ptr<SQLMsg> msg(DBManager::instance().DirectQuery("UPDATE account.account SET cash = '%ld' WHERE id = '%d'", value, GetAID()));

	if (msg->uiSQLErrno != 0) {
		sys_err("SetCoins Query Failed, Error code: %ld", msg->uiSQLErrno);
		return;
	}

	sys_log(0, "NAME: %s Coins Set Event, Amount: %d", GetName(), val);
}

void CHARACTER::UpdateCoins(DWORD dwAID, long val) {
	if (val == 0) {
		sys_err("Value is empty");
		return;
	}

	DWORD dwTarget = dwAID ? dwAID : GetAID();
	char szQuery[1024 + 1];
	long value = abs(val);

	if (val > 0)
		sprintf(szQuery, "UPDATE account.account SET cash = cash + '%ld' WHERE id = '%u'", value, dwTarget);
	else
		sprintf(szQuery, "UPDATE account.account SET cash = cash - '%ld' WHERE id = '%u'", value, dwTarget);

	std::auto_ptr<SQLMsg> msg(DBManager::instance().DirectQuery(szQuery));

	if (msg->uiSQLErrno != 0) {
		sys_err("UpdateCoins Query Failed, Error code: %ld", msg->uiSQLErrno);
		return;
	}

	sys_log(0, "NAME: %s Coins Updated, Amount: %d", GetName(), val);
	if (val > 0)
		ChatPacket(CHAT_TYPE_INFO, "You won %d coin", value);
	else
		ChatPacket(CHAT_TYPE_INFO, "You lost %d coin", value);
}

long CHARACTER::GetCoins() {
	std::auto_ptr<SQLMsg> msg(DBManager::instance().DirectQuery("SELECT cash FROM account.account WHERE id = '%u'", GetAID()));

	if (msg->uiSQLErrno != 0) {
		sys_err("GetCoins Query Failed, Error code: %ld", msg->uiSQLErrno);
		return 0;
	}
	if (!msg->Get()->uiNumRows) {
		sys_err("GetCoins Query Failed, Rows couldn't get");
		return 0;
	}

	MYSQL_ROW row = mysql_fetch_row(msg->Get()->pSQLResult);
	const char * cMyCoins = row[0];

	long lMyCoins = 0;
	str_to_number(lMyCoins, cMyCoins);

	return lMyCoins;
}
#endif

