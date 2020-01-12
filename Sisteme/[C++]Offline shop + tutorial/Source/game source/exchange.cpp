Arat ;
	//PREVENT_TRADE_WINDOW
	if ( IsOpenSafebox() || GetShopOwner() || GetMyShop() || IsCubeOpen())
	{
		ChatPacket( CHAT_TYPE_INFO, LC_TEXT("´Ù¸¥ °Å·¡Ã¢ÀÌ ¿­·ÁÀÖÀ»°æ¿ì °Å·¡¸¦ ÇÒ¼ö ¾ø½À´Ï´Ù." ) );
		return false;
	}

	if ( victim->IsOpenSafebox() || victim->GetShopOwner() || victim->GetMyShop() || victim->IsCubeOpen() )
	{
		ChatPacket( CHAT_TYPE_INFO, LC_TEXT("»ó´ë¹æÀÌ ´Ù¸¥ °Å·¡ÁßÀÌ¶ó °Å·¡¸¦ ÇÒ¼ö ¾ø½À´Ï´Ù." ) );
		return false;
	}
	//END_PREVENT_TRADE_WINDOW
	int iDist = DISTANCE_APPROX(GetX() - victim->GetX(), GetY() - victim->GetY());

	
Değiştir ;
	//PREVENT_TRADE_WINDOW
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
	if ( IsOpenSafebox() || GetShopOwner() || GetMyShop() || IsCubeOpen() || GetOfflineShopOwner())
	{
		ChatPacket( CHAT_TYPE_INFO, LC_TEXT("´Ù¸¥ °Å·¡Ã¢ÀÌ ¿­·ÁÀÖÀ»°æ¿ì °Å·¡¸¦ ÇÒ¼ö ¾ø½À´Ï´Ù." ) );
		return false;
	}

	if ( victim->IsOpenSafebox() || victim->GetShopOwner() || victim->GetMyShop() || victim->IsCubeOpen() || victim->GetOfflineShopOwner())
	{
		ChatPacket( CHAT_TYPE_INFO, LC_TEXT("»ó´ë¹æÀÌ ´Ù¸¥ °Å·¡ÁßÀÌ¶ó °Å·¡¸¦ ÇÒ¼ö ¾ø½À´Ï´Ù." ) );
		return false;
	}
#else
	if (IsOpenSafebox() || GetShopOwner() || GetMyShop() || IsCubeOpen())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´Ù¸¥ °Å·¡Ã¢ÀÌ ¿­·ÁÀÖÀ»°æ¿ì °Å·¡¸¦ ÇÒ¼ö ¾ø½À´Ï´Ù."));
		return false;
	}

	if (victim->IsOpenSafebox() || victim->GetShopOwner() || victim->GetMyShop() || victim->IsCubeOpen())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("»ó´ë¹æÀÌ ´Ù¸¥ °Å·¡ÁßÀÌ¶ó °Å·¡¸¦ ÇÒ¼ö ¾ø½À´Ï´Ù."));
		return false;
	}
#endif
	//END_PREVENT_TRADE_WINDOW
	int iDist = DISTANCE_APPROX(GetX() - victim->GetX(), GetY() - victim->GetY());
