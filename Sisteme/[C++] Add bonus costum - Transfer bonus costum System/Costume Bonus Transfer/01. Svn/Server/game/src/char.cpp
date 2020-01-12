// 1) Search: if ((GetExchange() || IsOpenSafebox() || GetShopOwner()) || IsCubeOpen() || IsAcceOpen())
// 2) After their declaration: {
// 3) Make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
				if (IsAttrTransferOpen())
				{
					pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("다른 거래중(창고,교환,상점)에는 개인상점을 사용할 수 없습니다."));
					return;
				}
#endif

// 1) Search: if ((pkChrCauser->GetExchange() || pkChrCauser->IsOpenSafebox() || pkChrCauser->GetMyShop() || pkChrCauser->GetShopOwner()) || pkChrCauser->IsCubeOpen())
// 2) After their declaration: {
// 3) Make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
				if (pkChrCauser->IsAttrTransferOpen())
				{
					pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("다른 거래중(창고,교환,상점)에는 개인상점을 사용할 수 없습니다."));
					return;
				}
#endif

// 1) Search: if ((GetExchange() || IsOpenSafebox() || IsCubeOpen() || IsAcceOpen()))
// 2) After their declaration: {
// 3) Make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
				if (IsAttrTransferOpen())
				{
					pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("상대방이 다른 거래를 하고 있는 중입니다."));
					return;
				}
#endif

// 1) Search: if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen() || IsAcceOpen())
// 2) After their declaration: {
// 3) Make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
		if (IsAttrTransferOpen())
		{
			if (bSendMsg)
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT("거래창,창고 등을 연 상태에서는 다른곳으로 이동,종료 할수 없습니다"));
			
			return true;
		}
#endif

// 1) Search: if (GetExchange() || GetMyShop() || IsOpenSafebox() || IsCubeOpen() || IsAcceOpen())
// 2) After their declaration: {
// 3) Make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
		if (IsAttrTransferOpen())
		{
			if (bSendMsg)
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT("거래창,창고 등을 연 상태에서는 다른곳으로 이동,종료 할수 없습니다"));
			
			return true;
		}
#endif

// 1) Search: if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen() || IsAcceOpen())
// 2) After their declaration: {
// 3) Make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
	if (IsAttrTransferOpen())
		return false;
#endif