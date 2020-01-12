// 1) Search: void AuctionManager::LoadAuctionItem()
// 2) Delete their function and paste:
void AuctionManager::LoadAuctionItem()
{
	char szQuery[512];
	snprintf(szQuery, sizeof(szQuery), 
		"SELECT id,	owner_id, count, vnum, socket0, socket1, socket2,"
		"attrtype0, attrvalue0,"
		"attrtype1, attrvalue1,"
		"attrtype2, attrvalue2,"
		"attrtype3, attrvalue3,"
		"attrtype4, attrvalue4,"
		"attrtype5, attrvalue5,"
		"attrtype6, attrvalue6,"
		"applytype0, applyvalue0,"
		"applytype1, applyvalue1,"
		"applytype2, applyvalue2,"
		"applytype3, applyvalue3,"
		"applytype4, applyvalue4,"
		"applytype5, applyvalue5,"
		"applytype6, applyvalue6,"
		"applytype7, applyvalue7"
		"FROM item WHERE window = 'AUCTION'");

	SQLMsg *msg = CDBManager::instance().DirectQuery(szQuery);
	MYSQL_RES *res = msg->Get()->pSQLResult;
	
	if (!res)
	{
		return;
	}
	
	int rows;
	if ((rows = mysql_num_rows(res)) <= 0)
	{
		return;
	}
	
	for (int i = 0; i < rows; ++i)
	{
		MYSQL_ROW row = mysql_fetch_row(res);
		TPlayerItem item;
		
		int cur = 0;
		str_to_number(item.id, row[cur++]);
		str_to_number(item.owner, row[cur++]);
		item.window = AUCTION;
		str_to_number(item.count, row[cur++]);
		str_to_number(item.vnum, row[cur++]);
		str_to_number(item.alSockets[0], row[cur++]);
		str_to_number(item.alSockets[1], row[cur++]);
		str_to_number(item.alSockets[2], row[cur++]);
		
		for (int j = 0; j < ITEM_ATTRIBUTE_MAX_NUM; j++)
		{
			str_to_number(item.aAttr[j].bType, row[cur++]);
			str_to_number(item.aAttr[j].sValue, row[cur++]);
		}
		InsertItemCache(&item, true);
	}
	
	return;
}