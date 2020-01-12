Search:
	Set(HEADER_CG_MALL_CHECKOUT,			sizeof(TPacketCGSafeboxCheckout),	"MallCheckout",			true);

Add it under:
#ifdef __OFFLINE_SHOP__
	Set(HEADER_CG_SAFEBOX_MONEY,			sizeof(TPacketCGSafeboxMoney),		"TPacketCGSafeboxMoney", true);
#endif

https://puu.sh/sgHoD/f2586e4c3b.png