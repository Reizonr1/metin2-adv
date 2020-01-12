
[..]
//find and replace function
int CInputMain::MyShop(LPCHARACTER ch, const char * c_pData, size_t uiBytes)
{	
	TPacketCGMyShop * p = (TPacketCGMyShop *) c_pData;
	int iExtraLen = p->bCount * sizeof(TShopItemTable);
#ifdef SHOP_BLOCK_GAME99
	if (g_bChannel >= 99 & ch->GetGMLevel() <= 0) {
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT( "SHOP_OX_ERROR"));
		return (iExtraLen);
	}
#endif
#ifdef OFFLINE_SHOP
	if (quest::CQuestManager::instance().GetEventFlag("shop_off")==1)
		if (ch)
			{
				ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT( "SHOP_TEMP_OFF"));
				return (iExtraLen);
			}
#endif
#ifdef SHOP_GM_PRIVILEGES
	if (GM_PLAYER < ch->GetGMLevel() && SHOP_GM_PRIVILEGES >ch->GetGMLevel()) {
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("SHOP_PRIV_ERROR"));
		return (iExtraLen);
	}
#endif
	if (uiBytes < sizeof(TPacketCGMyShop) + iExtraLen)
		return -1;
	#ifndef FULL_YANG
 	if (ch->GetGold() >= GOLD_MAX)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("소유 돈이 20억냥을 넘어 거래를 핼수가 없습니다."));
		sys_log(0, "MyShop ==> OverFlow Gold id %u name %s ", ch->GetPlayerID(), ch->GetName());
		return (iExtraLen);
	}
	#endif
	if (ch->IsStun() || ch->IsDead())
		return (iExtraLen);

	if (ch->GetExchange() || ch->IsOpenSafebox() || ch->GetShopOwner() || ch->IsCubeOpen())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("다른 거래중일경우 개인상점을 열수가 없습니다."));
		return (iExtraLen);
	}

	sys_log(0, "MyShop count %d", p->bCount);
#ifdef OFFLINE_SHOP
	ch->OpenMyShop(p->szSign, (TShopItemTable *)(c_pData + sizeof(TPacketCGMyShop)), p->bCount, p->days);
#else
	ch->OpenMyShop(p->szSign, (TShopItemTable *)(c_pData + sizeof(TPacketCGMyShop)), p->bCount);
#endif
	return (iExtraLen);
}

[..]