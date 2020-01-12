Arat ;
	Set(HEADER_CG_STATE_CHECKER, sizeof(BYTE), "ServerStateCheck", false);

Altına ekle ;
	Set(HEADER_CG_OFFLINE_SHOP, sizeof(TPacketCGShop), "OfflineShop", true);
	Set(HEADER_CG_MY_OFFLINE_SHOP, sizeof(TPacketCGMyOfflineShop), "MyOfflineShop", true);

	
	

Arat ;
	Set(HEADER_GG_CHECK_AWAKENESS,		sizeof(TPacketGGCheckAwakeness),	"CheckAwakeness",		false);

Altına ekle ;
	Set(HEADER_GG_REMOVE_OFFLINE_SHOP,		sizeof(TPacketGGRemoveOfflineShop),		"RemoveOfflineShop",	false);
	Set(HEADER_GG_CHANGE_OFFLINE_SHOP_TIME, sizeof(TPacketGGChangeOfflineShopTime), "ChangeOfflineShopTime",false);
