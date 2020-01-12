// 1) Search: if (IsCubeOpen() || DragonSoul_RefineWindow_GetOpener() != NULL)
// 2) After their declaration: return false;
// 3) Make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
	if (IsAttrTransferOpen())
		return false;
#endif

// 1) Search: if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
// 2) After their declaration: {
// 3) Make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
		if (IsAttrTransferOpen())
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("거래창,창고 등을 연 상태에서는 귀환부,귀환기억부 를 사용할수 없습니다."));
			return false;
		}
#endif

// 1) Search: if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
// 2) After their declaration: {
// 3) Make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
		if (IsAttrTransferOpen())
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("거래창,창고 등을 연 상태에서는 보따리,비단보따리를 사용할수 없습니다."));
			return false;
		}
#endif