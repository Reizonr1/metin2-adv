
//find void config_init and add before
#ifdef OFFLINE_SHOP
std::map<DWORD, DWORD> g_ShopIndexCount;
std::map<int, TShopCost> g_ShopCosts;
#include <boost/algorithm/string.hpp>
void LoadShopConfig()
{
	SQLMsg * pkMsg(DBManager::instance().DirectQuery("SELECT `id`,`time`,`time_type`+0,`cost` from shop_cost"));
	SQLResult * pRes = pkMsg->Get();
	if (pRes->uiNumRows)
	{
		MYSQL_ROW row;
		g_ShopIndexCount.clear();
		while ((row = mysql_fetch_row(pRes->pSQLResult)))
		{
			int id;
			str_to_number(id, row[0]);
			TShopCost c;
			str_to_number(c.days, row[1]);
			BYTE type;
			str_to_number(type, row[2]);
			if (type == 1)
				c.time = 86400;
			else if (type == 2)
				c.time = 3600;
			else
				c.time = 0;
			str_to_number(c.price, row[3]);
			g_ShopCosts[id] = c;
		}
	}
	const DESC_MANAGER::DESC_SET & set = DESC_MANAGER::instance().GetClientSet();
	DESC_MANAGER::DESC_SET::const_iterator it = set.begin();

	while (it != set.end())
	{
		LPDESC d = *(it++);

		if (!d->GetCharacter())
			continue;
		d->GetCharacter()->SendShopCost();
	}

}
void LoadIndexShopLimit()
{
	SQLMsg * pkMsg(DBManager::instance().DirectQuery("SELECT map_index,shop_limit from `shop_limit` where channel=%d or channel=0", g_bChannel));
	SQLResult * pRes = pkMsg->Get();
	if (pRes->uiNumRows)
	{
		MYSQL_ROW row;
		g_ShopIndexCount.clear();
		while ((row = mysql_fetch_row(pRes->pSQLResult)))
		{

			int index, limit;
			str_to_number(index, row[0]);
			str_to_number(limit, row[1]);
			if (!map_allow_find(index))
				continue;
			g_ShopIndexCount.insert(std::make_pair(index,limit));
			sys_log(0, "Shop Map %d limit %d\n", index, limit);
		}
	}
	fprintf(stdout, "\n");


}
#endif



//find LoadStateUserCount(); and add after
#ifdef OFFLINE_SHOP
LoadShopConfig();
LoadIndexShopLimit();
#endif