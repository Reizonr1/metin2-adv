// 1) Search:
void AuctionManager::LoadAuctionItem()
// 2) Inside this func search:
	char szQuery[512];
// 2) Replace with:
#ifdef __CHANGELOOK_SYSTEM__
	char szQuery[512 + 15];
#else
	char szQuery[512];
#endif


// 1) Search:
void AuctionManager::LoadAuctionItem()
// 2) Inside this func search:
	"vnum, "
// 3) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
		"transmutation, "
#endif
// 4) Example of result:
	snprintf(szQuery, sizeof(szQuery), 
		"SELECT "
		"id, "
		"owner_id, "
		"count, "
		"vnum, "
#ifdef __CHANGELOOK_SYSTEM__
		"transmutation, "
#endif
		"socket0, "
		"socket1, "
		"socket2, "
		"attrtype0, "
		"attrvalue0, "
		"attrtype1, "
		"attrvalue1, "
		"attrtype2, "
		"attrvalue2, "
		"attrtype3, "
		"attrvalue3, "
		"attrtype4, "
		"attrvalue4, "
		"attrtype5, "
		"attrvalue5, "
		"attrtype6, "
		"attrvalue6 "
		"FROM item WHERE window = 'AUCTION'");


// 1) Search:
		str_to_number(item.vnum, row[cur++]);
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
		str_to_number(item.transmutation, row[cur++]);
#endif