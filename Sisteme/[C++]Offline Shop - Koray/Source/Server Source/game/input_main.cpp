Search:
void CInputMain::SafeboxCheckout(LPCHARACTER ch, const char * c_pData, bool bMall)
{
	...
}

Add it under:

#ifdef __OFFLINE_SHOP__
void CInputMain::SafeboxMoney(LPCHARACTER ch, const char * data)
{
	CSafebox* sb = ch->GetSafebox();
	if (sb == NULL)
		return;

	TPacketCGSafeboxMoney * p = (TPacketCGSafeboxMoney *)data;

	if (p->lMoney < 0)
		return;

	switch (p->bState)
	{
		case SAFEBOX_MONEY_STATE_SAVE:
		{
			if (ch->GetGold() < p->lMoney)
				return;

			TSafeboxMoney pack;
			pack.dwAID = ch->GetAID();
			pack.bType = 1;
			pack.llAmount = p->lMoney;
			db_clientdesc->DBPacket(HEADER_GD_SAFEBOX_MONEY, 0, &pack, sizeof(pack));

			sys_log(0, "Safebox save money from: %u amount: %lld", ch->GetAID(), p->lMoney);
			ch->PointChange(POINT_GOLD, -p->lMoney);
		}
		break;

		case SAFEBOX_MONEY_STATE_WITHDRAW:
		{
			if (sb->GetGold() < p->lMoney)
				return;
			if (p->lMoney > GOLD_MAX)
				return;
			if (p->lMoney + ch->GetGold() > GOLD_MAX)
				return;

			TSafeboxMoney pack;
			pack.dwAID = ch->GetAID();
			pack.bType = 0;
			pack.llAmount = p->lMoney;
			db_clientdesc->DBPacket(HEADER_GD_SAFEBOX_MONEY, 0, &pack, sizeof(pack));

			sys_log(0, "Safebox withdraw money from: %u amount: %lld", ch->GetAID(), p->lMoney);
			ch->PointChange(POINT_GOLD, p->lMoney);
		}
		break;
	}
}
#endif

https://puu.sh/sgGQz/abf49ebc4d.png
https://puu.sh/sgGRb/71a4102361.png
---

Search:
int CInputMain::MyShop(LPCHARACTER ch, const char * c_pData, size_t uiBytes)
{
	TPacketCGMyShop * p = (TPacketCGMyShop *) c_pData;
	int iExtraLen = p->bCount * sizeof(TShopItemTable);

	if (uiBytes < sizeof(TPacketCGMyShop) + iExtraLen)
		return -1;

Add it under:

#ifdef __OFFLINE_SHOP__
	if (p->bType != 0)
	{
		int iBadMaps[] = { 113, 66 };
		for (int i = 0; i < sizeof(iBadMaps) / sizeof(iBadMaps[0]); i++) {
			if (ch && i == ch->GetMapIndex()) {
				ch->ChatPacket(CHAT_TYPE_INFO, "You can not create offline shop on this map!");
				return (iExtraLen);
			}
		}

		if (g_bChannel == 99) {
			ch->ChatPacket(CHAT_TYPE_INFO, "You can not create offline shop on this channel!");
			return (iExtraLen);
		}

		if (quest::CQuestManager::instance().GetEventFlag("block_offlineshop"))
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "Offline shop creation temporary disabled from server admin!");
			return (iExtraLen);
		}

		if (CShopManager::instance().GetOfflineShopCount() >= OFFLINE_SHOP_CHANNEL_LIMIT)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "More offline shop can not be created in this channel!");
			return (iExtraLen);
		}

		int iStyleLevelLimits[] = {0 /*aka. standart */, 20, 40, 60, 80, 99};
		if (ch->GetLevel() < iStyleLevelLimits[p->bColor])
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You can not use this shop style before than %d level!", iStyleLevelLimits[p->bColor]);
			return (iExtraLen);
		}

		int iGridLevelLimit[] = { 0 /*aka. standart */, 20, 40, 60, 80, 99 };
		if (ch->GetLevel() < iGridLevelLimit[p->bSize])
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "You can not use this shop size before than %d level!", iGridLevelLimit[p->bSize]);
			return (iExtraLen);
		}
	}
#endif

https://puu.sh/sgGTO/d6cd5f59df.png
---

Search:
	if (ch->GetGold() >= GOLD_MAX)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("¼ÒÀ¯ µ·ÀÌ 20¾ï³ÉÀ» ³Ñ¾î °Å·¡¸¦ ÇÛ¼ö°¡ ¾ø½À´Ï´Ù."));
		sys_log(0, "MyShop ==> OverFlow Gold id %u name %s ", ch->GetPlayerID(), ch->GetName());
		return (iExtraLen);
	}

Change:
#ifdef __OFFLINE_SHOP__
	if (p->bType == 0 && ch->GetGold() >= GOLD_MAX)
#else
	if (ch->GetGold() >= GOLD_MAX)
#endif
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("¼ÒÀ¯ µ·ÀÌ 20¾ï³ÉÀ» ³Ñ¾î °Å·¡¸¦ ÇÛ¼ö°¡ ¾ø½À´Ï´Ù."));
		sys_log(0, "MyShop ==> OverFlow Gold id %u name %s ", ch->GetPlayerID(), ch->GetName());
		return (iExtraLen);
	}

https://puu.sh/sgGUQ/e423d27158.png
---

Search:
	sys_log(0, "MyShop count %d", p->bCount);
	ch->OpenMyShop(p->szSign, (TShopItemTable *) (c_pData + sizeof(TPacketCGMyShop)), p->bCount);
	return (iExtraLen);
}

Change:
	sys_log(0, "MyShop count %d", p->bCount);

#ifdef __OFFLINE_SHOP__
	if (p->bType == 0)
		ch->OpenMyShop(p->szSign, (TShopItemTable *)(c_pData + sizeof(TPacketCGMyShop)), p->bCount);
	else
		ch->OpenOfflineShop(p->szSign, p->bType, p->bSize, p->bColor, (TShopItemTable *)(c_pData + sizeof(TPacketCGMyShop)), p->bCount);
#else
	ch->OpenMyShop(p->szSign, (TShopItemTable *) (c_pData + sizeof(TPacketCGMyShop)), p->bCount);
#endif

	return (iExtraLen);
}

https://puu.sh/sgGWh/6647e987f3.png
---

Search:
		case HEADER_CG_SAFEBOX_ITEM_MOVE:
			SafeboxItemMove(ch, c_pData);
			break;

Add it under:
#ifdef __OFFLINE_SHOP__
		case HEADER_CG_SAFEBOX_MONEY:
			SafeboxMoney(ch, c_pData);
			break;
#endif

https://puu.sh/sgGYF/f501953cc2.png

