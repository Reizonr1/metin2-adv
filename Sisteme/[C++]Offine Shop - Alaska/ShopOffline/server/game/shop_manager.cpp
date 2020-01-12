[..]


//find function DestroyPCShop and replace with this
#include <boost/algorithm/string/replace.hpp>
#ifdef OFFLINE_SHOP
extern std::map<int, TShopCost> g_ShopCosts;
bool CShopManager::CreateOfflineShop(LPCHARACTER owner, const char *szSign, const std::vector<TShopItemTable *> pTable, DWORD id)
{
	if (g_ShopCosts.find(id) == g_ShopCosts.end())
	{
		sys_log(0, "CreateOfflineShop:Shop days error %d", id);
		return false;
	}

	DWORD map_index = owner->GetMapIndex();
	long x = (owner->GetX() + number(50, 200));
	long y = (owner->GetY() + number(50, 200));
	long z = owner->GetZ();
	char szQuery[4096];
	DWORD date_close = get_global_time() + (g_ShopCosts[id].time * g_ShopCosts[id].days);
	sprintf(szQuery, "insert into player_shop set item_count=%d,player_id=%d,name=\"%s\",map_index=%d,x=%ld,y=%ld,z=%ld,ip='%s',date=NOW(),date_close=FROM_UNIXTIME(%d),channel=%d",
		pTable.size(), owner->GetPlayerID(), szSign, map_index, x, y, z, inet_ntoa(owner->GetDesc()->GetAddr().sin_addr), date_close, g_bChannel);
	SQLMsg * pkMsg(DBManager::instance().DirectQuery(szQuery));
	SQLResult * pRes = pkMsg->Get();
	DWORD shop_id = pRes->uiInsertID;
	if (shop_id>0)
	{
		for (int i = 0;i < pTable.size();i++)
		{
			LPITEM item = owner->GetItem(pTable[i]->pos);
			if (item)
			{
				
				char query[1024];
				sprintf(query, "INSERT INTO player_shop_items SET");
				sprintf(query, "%s player_id='%d'", query, owner->GetPlayerID());
				sprintf(query, "%s, shop_id='%d'", query, shop_id);
				sprintf(query, "%s, vnum='%d'", query, item->GetVnum());
				sprintf(query, "%s, count='%d'", query, item->GetCount());
#ifdef FULL_YANG
				sprintf(query, "%s, price='%lld'", query, pTable[i]->price);
#else
				sprintf(query, "%s, price='%d'", query, pTable[i]->price);
#endif
				sprintf(query, "%s, display_pos='%u'", query, pTable[i]->display_pos);
				for (int s = 0; s < ITEM_SOCKET_MAX_NUM; s++)
				{
					sprintf(query, "%s, socket%d='%ld'", query, s, item->GetSocket(s));
					
				}
				for (int ia = 0; ia < ITEM_ATTRIBUTE_MAX_NUM; ia++)
				{
					const TPlayerItemAttribute& attr = item->GetAttribute(ia);
					if (ia < 7)
					{
						sprintf(query, "%s, attrtype%d='%u'", query, ia, attr.bType);
						sprintf(query, "%s, attrvalue%d='%d'", query, ia, attr.sValue);
					}
					else{
						sprintf(query, "%s, applytype%d='%u'", query, ia - 7, attr.bType);
						sprintf(query, "%s, applyvalue%d='%d'", query, ia - 7, attr.sValue);
					}


				}
				DBManager::instance().DirectQuery(query);
				ITEM_MANAGER::Instance().RemoveItem(item, "Priv shop");
			}
		}
		StartOfflineShop(shop_id);
		owner->SendShops();
		return true;
	}
	return false;
}

bool CShopManager::StartOfflineShop(DWORD id, bool onboot)
{

	std::string name;
	std::string shop_name(LC_TEXT("SHOP_NAME"));
	DWORD pid,time;
	long map_index, x, y, z;
	SQLMsg * pkMsg(DBManager::instance().DirectQuery("SELECT player_shop.name,player_shop.player_id,player.name as player_name,player_shop.map_index,player_shop.x,player_shop.y,player_shop.z,UNIX_TIMESTAMP(player_shop.date_close),player_shop.id from player_shop left join player on player.id=player_shop.player_id where player_shop.id='%d'", id));
	SQLResult * pRes = pkMsg->Get();
	if (pRes->uiNumRows>0)
	{
		MYSQL_ROW row;
		while ((row = mysql_fetch_row(pRes->pSQLResult)) != NULL)
		{
			name = row[0];
			str_to_number(pid, row[1]);
			boost::replace_all(shop_name, "#PLAYER_NAME#", row[2]);
			str_to_number(map_index, row[3]);
			str_to_number(x, row[4]);
			str_to_number(y, row[5]);
			str_to_number(z, row[6]);
			str_to_number(time, row[7]);
		}
	}
	if (map_index <= 0 || x <= 0 || y <= 0)
	{
		sys_err("location is null %d", id);
		return false;
	}

	LPCHARACTER ch = CHARACTER_MANAGER::Instance().SpawnMob(30000, map_index, x, y, z, true, 0, false);
	if (ch)
	{
		ch->SetName(shop_name.c_str());
		ch->SetPrivShop(id);
		ch->SetPrivShopOwner(pid);
		ch->SetShopTime(time);
		ch->Show(map_index, x, y, z);
		ch->OpenShop(id, name.c_str(), onboot);

		DBManager::instance().DirectQuery("UPDATE player_shop SET shop_vid=%d WHERE id=%d", (DWORD)ch->GetVID(), id);
		LPCHARACTER owner = CHARACTER_MANAGER::instance().FindByPID(ch->GetPrivShopOwner());
		if (owner)
			owner->LoadPrivShops();
		return true;
	}
	return false;
}

LPSHOP CShopManager::CreateNPCShop(LPCHARACTER ch, std::vector<TShopItemTable *> map_shop)
{
	if (FindPCShop(ch->GetPrivShop()))
		return NULL;

	LPSHOP pkShop = M2_NEW CShop;
	pkShop->SetPCShop(ch);
	pkShop->SetPrivShopItems(map_shop);
	pkShop->SetLocked(false);
	m_map_pkShopByPC.insert(TShopMap::value_type(ch->GetPrivShop(), pkShop));
	return pkShop;
}
void CShopManager::DestroyPCShop(LPCHARACTER ch)
{
	LPSHOP pkShop = FindPCShop(ch->IsPrivShop() && ch->GetRaceNum() == 30000 ? ch->GetPrivShop() : ch->GetVID());

	if (!pkShop)
		return;

	//PREVENT_ITEM_COPY;
	ch->SetMyShopTime();
	//END_PREVENT_ITEM_COPY

	m_map_pkShopByPC.erase(ch->IsPrivShop() && ch->GetRaceNum() == 30000 ? ch->GetPrivShop() : ch->GetVID());
	M2_DELETE(pkShop);
}
#else

void CShopManager::DestroyPCShop(LPCHARACTER ch)
{
	LPSHOP pkShop = FindPCShop(ch->GetVID());

	if (!pkShop)
		return;

	//PREVENT_ITEM_COPY;
	ch->SetMyShopTime();
	//END_PREVENT_ITEM_COPY

	m_map_pkShopByPC.erase(ch->GetVID());
	M2_DELETE(pkShop);
}
#endif