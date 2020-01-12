
//Add this on last line in top 

#include <boost/algorithm/string.hpp>


//find and add new varibles
void CHARACTER::Initialize()
{
	[..]
#ifdef OFFLINE_SHOP
	m_pkRefreshShopEvent = NULL;
	bprivShop = 0;
	bprivShopOwner = 0;
	bprivShop = 0;
	bprivShopOwner = 0;
	dw_ShopTime = 0;
	m_mapshops.clear();
#endif
#ifdef GIFT_SYSTEM
	m_pkGiftRefresh = NULL;
	m_dwLastGiftPage = 0;
	m_mapGiftGrid.clear();
#endif
	[..]
}
//find and add new varibles
void CHARACTER::Destroy()
{
	[..]
#ifdef GIFT_SYSTEM
	event_cancel(&m_pkGiftRefresh);
	m_dwLastGiftPage = 0;
	m_mapGiftGrid.clear();
#endif
#ifdef OFFLINE_SHOP
	event_cancel(&m_pkRefreshShopEvent);
	bprivShop = 0;
	bprivShopOwner = 0;
	dw_ShopTime = 0;
	m_mapshops.clear();
#endif
	[..]
}



/*Find in function void CHARACTER::EncodeInsertPacket (LPENTITY entity) :

strlcpy (addPacket.name, GetName(), sizeof (addPacket.name)); 
and replace with this:
*/
	#if defined(SHOP_HIDE_NAME) && defined(OFFLINE_SHOP)
		if (IsPC() || GetRaceNum() != 30000 && !IsPrivShop())
	#endif
		strlcpy(addPacket.name, GetName(), sizeof(addPacket.name));


//find and replace function

void CHARACTER::OnClick(LPCHARACTER pkChrCauser)
{
	if (!pkChrCauser)
	{
		sys_err("OnClick %s by NULL", GetName());
		return;
	}

	DWORD vid = GetVID();
	//if (test_server)
		sys_log(0, "OnClick %s[vnum %d ServerUniqueID %d, pid %d] by %s", GetName(), GetRaceNum(), vid, GetPlayerID(), pkChrCauser->GetName());

	// ??? ???? ???? ??? ? ??.
	{
		// ?, ??? ??? ??? ??? ? ??.
		if (pkChrCauser->GetMyShop() && pkChrCauser != this)
		{
			if (test_server)
				sys_err("OnClick Fail (%s->%s) - pc has shop", pkChrCauser->GetName(), GetName());
			return;
		}
	}

	// ????? ???? ??? ? ??.
	{
		if (pkChrCauser->GetExchange())
		{
			if (test_server)
				sys_err("OnClick Fail (%s->%s) - pc is exchanging", pkChrCauser->GetName(), GetName());
			return;
		}
	}

#ifdef OFFLINE_SHOP
	if (IsPC() || IsNPC() && GetRaceNum() == 30000)
	{		
		if (!CTargetManager::instance().GetTargetInfo(pkChrCauser->GetPlayerID(), TARGET_TYPE_VID, GetVID()) || GetRaceNum() == 30000)
#else
			
	if (IsPC())
	{
		if (!CTargetManager::instance().GetTargetInfo(pkChrCauser->GetPlayerID(), TARGET_TYPE_VID, GetVID()))
#endif
		{
			// 2005.03.17.myevan.Ĺ¸°ŮŔĚ ľĆ´Ń °ćżě´Â °łŔÎ »óÁˇ Ăł¸® ±â´ÉŔ» ŔŰµż˝ĂĹ˛´Ů.
			if (GetMyShop())
			{
				if (pkChrCauser->IsDead() == true) return;

				//PREVENT_TRADE_WINDOW
				if (pkChrCauser == this) // ŔÚ±â´Â °ˇ´É
				{
					if ((GetExchange() || IsOpenSafebox() || GetShopOwner()) || IsCubeOpen())
					{
						pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´Ů¸Ą °Ĺ·ˇÁß(Ă˘°í,±łČŻ,»óÁˇ)żˇ´Â °łŔÎ»óÁˇŔ» »çżëÇŇ Ľö ľř˝Ŕ´Ď´Ů."));
						return;
					}
				}
				else // ´Ů¸Ą »ç¶÷ŔĚ Ĺ¬¸ŻÇßŔ»¶§
				{
					// Ĺ¬¸ŻÇŃ »ç¶÷ŔĚ ±łČŻ/Ă˘°í/°łŔÎ»óÁˇ/»óÁˇŔĚżëÁßŔĚ¶ó¸é şŇ°ˇ
					if ((pkChrCauser->GetExchange() || pkChrCauser->IsOpenSafebox() || pkChrCauser->GetMyShop() || pkChrCauser->GetShopOwner()) || pkChrCauser->IsCubeOpen())
					{
						pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´Ů¸Ą °Ĺ·ˇÁß(Ă˘°í,±łČŻ,»óÁˇ)żˇ´Â °łŔÎ»óÁˇŔ» »çżëÇŇ Ľö ľř˝Ŕ´Ď´Ů."));
						return;
					}

					// Ĺ¬¸ŻÇŃ ´ë»óŔĚ ±łČŻ/Ă˘°í/»óÁˇŔĚżëÁßŔĚ¶ó¸é şŇ°ˇ
					//if ((GetExchange() || IsOpenSafebox() || GetShopOwner()))
					if ((GetExchange() || IsOpenSafebox() || IsCubeOpen()))
					{
						pkChrCauser->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("»ó´ëąćŔĚ ´Ů¸Ą °Ĺ·ˇ¸¦ ÇĎ°í ŔÖ´Â ÁßŔÔ´Ď´Ů."));
						return;
					}
				}
				//END_PREVENT_TRADE_WINDOW
				#ifdef OFFLINE_SHOP
				if (GetMyShop()->IsLocked())
					return;
				#endif
				GetMyShop()->AddGuest(pkChrCauser, GetVID(), false);

				pkChrCauser->SetShopOwner(this);
				return;
			}

			if (test_server)
				sys_err("%s.OnClickFailure(%s) - target is PC", pkChrCauser->GetName(), GetName());

			return;
		}
	}
	pkChrCauser->SetQuestNPCID(GetVID());

	if (quest::CQuestManager::instance().Click(pkChrCauser->GetPlayerID(), this))
	{
		return;
	}


	// NPC ?? ?? ?? : ?? ?? ?
	if (!IsPC())
	{
		if (!m_triggerOnClick.pFunc)
		{
			return;
		}

		m_triggerOnClick.pFunc(this, pkChrCauser);
	}

}

//find and replace function
void CHARACTER::CloseMyShop()
{
	if (GetMyShop())
	{
		
		m_stShopSign.clear();
		CShopManager::instance().DestroyPCShop(this);
		m_pkMyShop = NULL;

		TPacketGCShopSign p;

		p.bHeader = HEADER_GC_SHOP_SIGN;
		p.dwVID = GetVID();
		p.szSign[0] = '\0';

		PacketAround(&p, sizeof(p));

		#ifdef OFFLINE_SHOP
		if (IsPrivShop())
		{
			M2_DESTROY_CHARACTER(this);
			return;
		}
		#endif
		SetPolymorph(GetJob(), true);
	}
}
//add new function

#ifdef GIFT_SYSTEM
#include <boost/algorithm/string.hpp>
EVENTFUNC(gift_refresh_event)
{
	char_event_info* info = dynamic_cast<char_event_info*>(event->info);
	if (info == NULL)
	{
		sys_err("gift_refresh_event> <Factor> Null pointer");
		return 0;
	}

	LPCHARACTER	ch = info->ch;

	if (NULL == ch || ch->IsNPC())
		return 0;
	ch->RefreshGift();
	return PASSES_PER_SEC(5 * 60);
}
void CHARACTER::StartRefreshGift()
{
	if (m_pkGiftRefresh)
		return;
	char_event_info* info = AllocEventInfo<char_event_info>();

	info->ch = this;
	m_pkGiftRefresh = event_create(gift_refresh_event, info, PASSES_PER_SEC(1));	// 1o?
}
void SendGift(LPCHARACTER ch, TGiftItem item)
{
	char szSockets[1024] = { '\0' };
	char *tempSockets = szSockets;
	for (int soc = 0; soc < ITEM_SOCKET_MAX_NUM; soc++)
		tempSockets += sprintf(tempSockets, "%ld%s", item.alSockets[soc], (soc<ITEM_SOCKET_MAX_NUM - 1 ? "|" : ""));
	char szAttrs[1024] = { '\0' };
	char *tempAttrs = szAttrs;
	for (int attr = 0; attr < ITEM_ATTRIBUTE_MAX_NUM; attr++)
		tempAttrs += sprintf(tempAttrs, "%u,%d%s", item.aAttr[attr].bType, item.aAttr[attr].sValue, (attr<ITEM_ATTRIBUTE_MAX_NUM - 1 ? "|" : ""));
#ifdef FULL_YANG
	ch->ChatPacket(CHAT_TYPE_COMMAND, "gift_item %d %d %lld %d %d %s %s %s %s", item.id, item.vnum, item.count, item.pos, item.dwDateAdd, item.szFrom, item.szReason, szSockets, szAttrs);
#else
	ch->ChatPacket(CHAT_TYPE_COMMAND, "gift_item %d %d %d %d %d %s %s %s %s", item.id, item.vnum, item.count, item.pos, item.dwDateAdd, item.szFrom, item.szReason, szSockets, szAttrs);
#endif
}
void CHARACTER::LoadGiftPage(int page)
{
	page = MINMAX(1, page, m_mapGiftGrid.size());
	ChatPacket(CHAT_TYPE_COMMAND, "gift_clear");
	GIFT_MAP::iterator it = m_mapGiftGrid.find(page);
	if (it == m_mapGiftGrid.end())
		return;
	m_dwLastGiftPage = page;
	for (int i = 0; i < it->second.size(); i++)
		SendGift(this, it->second[i]);	
	ChatPacket(CHAT_TYPE_COMMAND, "gift_load");

}
static CGrid* grid;
void CHARACTER::AddGiftGrid(int page)
{
	if (m_mapGiftGrid.find(page) == m_mapGiftGrid.end())
	{
		std::vector<TGiftItem> vec;
		m_mapGiftGrid.insert(std::make_pair(page, vec));
	}

}
int CHARACTER::AddGiftGridItem( int page, int size)
{
	AddGiftGrid(page);
	int iPos = grid->FindBlank(1, size);

	if (iPos < 0)
		return -1;

	if (!grid->IsEmpty(iPos, 1, size))
		return -1;


	grid->Put(iPos, 1, size);
	return iPos;

}
void CHARACTER::RefreshGift()
{
	char szSockets[1024] = { '\0' };
	char *tempSockets = szSockets;
	for (int i = 0; i < ITEM_SOCKET_MAX_NUM; i++)
	{
		tempSockets += sprintf(tempSockets, "socket%d", i);

		if (i<ITEM_SOCKET_MAX_NUM - 1)
			tempSockets += sprintf(tempSockets, ",");
	}
	char szAttrs[1024] = { '\0' };
	char *tempAttrs = szAttrs;
	for (int i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; i++)
	{
		if (i < 7)
			tempAttrs += sprintf(tempAttrs, "attrtype%d,attrvalue%d", i, i);
		else
			tempAttrs += sprintf(tempAttrs, "applytype%d,applyvalue%d", i - 7, i - 7);
		if (i<ITEM_ATTRIBUTE_MAX_NUM - 1)
			tempAttrs += sprintf(tempAttrs, ",");
	}
	SQLMsg * pkMsg(DBManager::instance().DirectQuery("SELECT id,vnum,count,unix_timestamp(date_add),replace(reason,' ','_'),replace(`from`,' ','_'),%s,%s from player_gift where  owner_id = %d and status = 'WAIT' ORDER BY date_add ", szSockets, szAttrs, GetPlayerID()));
	SQLResult * pRes = pkMsg->Get();
	m_mapGiftGrid.clear();
	grid = M2_NEW CGrid(15, 8);
	grid->Clear();
	int page = 1;
	if (pRes->uiNumRows>0)
	{
		AddGiftGrid(page);
		MYSQL_ROW row;
		while ((row = mysql_fetch_row(pRes->pSQLResult)) != NULL)
		{
			int col = 0;
			TGiftItem item;
			memset(&item, 0, sizeof(item));
			str_to_number(item.id, row[col++]);
			str_to_number(item.vnum, row[col++]);
			str_to_number(item.count, row[col++]);
			str_to_number(item.dwDateAdd, row[col++]);
			strlcpy(item.szReason, row[col++], sizeof(item.szReason) - 1);
			strlcpy(item.szFrom, row[col++], sizeof(item.szFrom) - 1);
			for (int i = 0; i < ITEM_SOCKET_MAX_NUM; i++)
				str_to_number(item.alSockets[i], row[col++]);
			for (int i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; i++)
			{
				str_to_number(item.aAttr[i].bType, row[col++]);
				str_to_number(item.aAttr[i].sValue, row[col++]);
			}

			const TItemTable * item_table = ITEM_MANAGER::instance().GetTable(item.vnum);
			if (!item_table)
				continue;
			int iPos = AddGiftGridItem( page, item_table->bSize);
			if (iPos < 0)
			{
				page++;
				grid->Clear();
				iPos = AddGiftGridItem(page, item_table->bSize);
				if (iPos < 0)
				{
					sys_err("iPos <0");
					break;
				}
			}
			item.pos = iPos;
			m_mapGiftGrid[page].push_back(item);

		}
		M2_DELETE(grid);
	}
	if(GetGiftPages()>0)
		ChatPacket(CHAT_TYPE_COMMAND, "gift_info %d", GetGiftPages());
}
#endif

#ifdef OFFLINE_SHOP

extern std::map<DWORD, DWORD> g_ShopIndexCount;
extern std::map<int, TShopCost> g_ShopCosts;
void CHARACTER::OpenMyShop(const char * c_pszSign, TShopItemTable * pTable, BYTE bItemCount, DWORD id)
{

	if (g_ShopCosts.find(id) == g_ShopCosts.end())
	{
		sys_log(0, "Shop days error %s %d", c_pszSign, id);
		return;
	}
	int days = g_ShopCosts[id].days;
	long long price = g_ShopCosts[id].price;
	if (price > 0 && GetGold() < price)
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT( "SHOP_NEED_MONEY"), price);
		return;
	}
	if (days == 0 && GetPart(PART_MAIN) > 2)
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("°©żĘŔ» ąţľîľß °łŔÎ »óÁˇŔ» ż­ Ľö ŔÖ˝Ŕ´Ď´Ů."));
		return;
	}

	if (GetMyShop())
	{
		CloseMyShop();
		return;
	}


	int gShopMax = quest::CQuestManager::Instance().GetEventFlag("shop_max");
	if (m_mapshops.size() >= (gShopMax ? gShopMax : 2))
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT( "SHOP_MAX_ERR"));
		return;
	}


	if (g_ShopIndexCount.count(GetMapIndex())>0)
	{
		int shop_max = g_ShopIndexCount[GetMapIndex()];
		bool block = false;

#ifdef SHOP_ONLY_ALLOWED_INDEX
		if (shop_max > 0)
		{
#else
		if (shop_max == 0)
			block = true;
		else{
#endif
			std::auto_ptr<SQLMsg> pkMsg(DBManager::instance().DirectQuery("SELECT map_index from player_shop WHERE channel=%d and status='OK' and map_index=%d", g_bChannel, GetMapIndex()));
			SQLResult * pRes = pkMsg->Get();
			if (pRes->uiNumRows >= shop_max)
				block = true;
		}
		if (block)
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT( "SHOP_MAP_MAX"));
			return;
		}
	}
#ifdef SHOP_ONLY_ALLOWED_INDEX
	else
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT( "SHOP_CANNOT_OPEN_HERE"));
		return;
	}
#endif
	if (GetMyShop())	// AI1I 1YAI ?­·Á AÖA¸¸é ´Ý´Â´U.
	{
		CloseMyShop();
		return;
	}
#ifndef FULL_YANG
	int64_t nTotalMoney = 0;

	for (int n = 0; n < bItemCount; ++n)
	{
		nTotalMoney += static_cast<int64_t> ((pTable + n)->price);
	}

	nTotalMoney += static_cast<int64_t> (GetGold());

	if (GOLD_MAX <= nTotalMoney)
	{
		sys_err("[OVERFLOW_GOLD] Overflow (GOLD_MAX) id %u name %s", GetPlayerID(), GetName());
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("20ľď łÉŔ» ĂĘ°úÇĎż© »óÁˇŔ» ż­Ľö°ˇ ľř˝Ŕ´Ď´Ů"));
		return;
	}
#endif
#ifdef ACCE_FIX
	if(IsAcceOpen())
		Acce_close(this);
#endif
	quest::PC * pPC = quest::CQuestManager::instance().GetPCForce(GetPlayerID());
	if (pPC->IsRunning())
		return;
	std::vector<TShopItemTable *> map_shop;
	for (BYTE i = 0; i < bItemCount; ++i)
	{
		// ANTI_GIVE, ANTI_MYSHOP check
		LPITEM pkItem = GetItem((pTable + i)->pos);

		if (pkItem)
		{
			const TItemTable * item_table = pkItem->GetProto();

			if (item_table && (IS_SET(item_table->dwAntiFlags, ITEM_ANTIFLAG_GIVE | ITEM_ANTIFLAG_MYSHOP)))
			{
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT( "ŔŻ·áČ­ ľĆŔĚĹŰŔş °łŔÎ»óÁˇżˇĽ­ ĆÇ¸ĹÇŇ Ľö ľř˝Ŕ´Ď´Ů."));
				return;
			}

			if (pkItem->IsEquipped())
			{
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT( "ŔĺşńÁßŔÎ ľĆŔĚĹŰŔş °łŔÎ»óÁˇżˇĽ­ ĆÇ¸ĹÇŇ Ľö ľř˝Ŕ´Ď´Ů."));
				return;
			}

			if (pkItem->isLocked())
			{
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT( "»çżëÁßŔÎ ľĆŔĚĹŰŔş °łŔÎ»óÁˇżˇĽ­ ĆÇ¸ĹÇŇ Ľö ľř˝Ŕ´Ď´Ů."));
				return;
			}
			if (pkItem->GetOwner() != this)
			{
				return;
			}
#ifdef SOULBIND_SYSTEM
			if (pkItem->IsSoulBind())
			{
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT( "You can't sell in private shop item with soul bind."));
				return;
			}
#endif
		}
		if (days != 0)
			map_shop.push_back(pTable++);
	}
	if (days != 0 && map_shop.size() == 0)
		return;
	char szName[256];
	DBManager::instance().EscapeString(szName, 256, c_pszSign, strlen(c_pszSign));
	m_stShopSign = szName;
	boost::replace_all(m_stShopSign, "%", "%%");


	if (m_stShopSign.length()>30)
		m_stShopSign.resize(30);
	if (m_stShopSign.length() == 0)
		return;
#ifdef STRING_PROTECTION
	if (CBanwordManager::instance().CheckString(m_stShopSign.c_str(), m_stShopSign.length()) != "")
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT( "şńĽÓľîłŞ Ŕşľî°ˇ Ć÷ÇÔµČ »óÁˇ ŔĚ¸§Ŕ¸·Î »óÁˇŔ» ż­ Ľö ľř˝Ŕ´Ď´Ů."));
		return;
	}
#else
	if (CBanwordManager::instance().CheckString(m_stShopSign.c_str(), m_stShopSign.length()))
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT( "şńĽÓľîłŞ Ŕşľî°ˇ Ć÷ÇÔµČ »óÁˇ ŔĚ¸§Ŕ¸·Î »óÁˇŔ» ż­ Ľö ľř˝Ŕ´Ď´Ů."));
		return;
	}
#endif
	if (m_pkExchange)
		m_pkExchange->Cancel();
	if (price > 0)
#ifdef FULL_YANG_OWN
		ChangeGold(-price);
#else
		PointChange(POINT_GOLD, -price);
#endif
	if (days != 0)
	{
		CShopManager::instance().CreateOfflineShop(this, m_stShopSign.c_str(), map_shop, id);
		m_stShopSign.clear();
		return;
	}
	TPacketGCShopSign p;
	p.bHeader = HEADER_GC_SHOP_SIGN;
	p.dwVID = GetVID();
	strlcpy(p.szSign, m_stShopSign.c_str(), sizeof(p.szSign));

	PacketAround(&p, sizeof(TPacketGCShopSign));

	m_pkMyShop = CShopManager::instance().CreatePCShop(this, pTable, bItemCount);
	if (!m_pkMyShop)
	{
		sys_err("Cannot open normal shop %s %s", GetName(), m_stShopSign.c_str());
		return;
	}
	if (IsPolymorphed() == true)
	{
		RemoveAffect(AFFECT_POLYMORPH);
	}

	if (GetHorse())
	{
		HorseSummon(false, true);
	}
	else if (GetMountVnum())
	{
		RemoveAffect(AFFECT_MOUNT);
		RemoveAffect(AFFECT_MOUNT_BONUS);
	}

	SetPolymorph(30000, true);

}
void CHARACTER::SetShopSign(const char * name)
{
	m_stShopSign = name;
	TPacketGCShopSign p;
	p.bHeader = HEADER_GC_SHOP_SIGN;
	p.dwVID = GetVID();
	strlcpy(p.szSign, m_stShopSign.c_str(), sizeof(p.szSign));
	PacketAround(&p, sizeof(TPacketGCShopSign));
}

TPrivShop CHARACTER::GetPrivShopTable(DWORD id)
{
	TPrivShop shop;
	memset(&shop, 0, sizeof(TPrivShop));
	PSHOP_MAP::iterator it = m_mapshops.find(id);
	if (it != m_mapshops.end())
		return it->second;
	return shop;

}
void CHARACTER::UpdatePrivShopTable(DWORD id, TPrivShop shop)
{
	if (m_mapshops.find(id) != m_mapshops.end())
		m_mapshops[id]=shop;
	SendShops();
}
void CHARACTER::RemovePrivShopTable(DWORD id)
{
	if (m_mapshops.find(id) != m_mapshops.end())
		m_mapshops.erase(m_mapshops.find(id));
	SendShops();
}
void CHARACTER::UpdateShopItems()
{
	LPSHOP npcshop = GetMyShop();
	LPCHARACTER owner = CHARACTER_MANAGER::instance().FindByPID(GetPrivShopOwner());
	if (!npcshop || !IsPrivShop())
		return;
	npcshop->RemoveGuests(owner);
	npcshop->SetLocked(true);
	npcshop->ClearItems();
	std::vector<TShopItemTable *> map_shop;
	char szSockets[1024] = { '\0' };
	char *tempSockets = szSockets;
	for (int i = 0; i < ITEM_SOCKET_MAX_NUM; i++)
	{
		tempSockets += sprintf(tempSockets, "socket%d", i);

		if (i<ITEM_SOCKET_MAX_NUM - 1)
			tempSockets += sprintf(tempSockets, ",");
	}
	char szAttrs[1024] = { '\0' };
	char *tempAttrs = szAttrs;
	for (int i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; i++)
	{
		if (i < 7)
			tempAttrs += sprintf(tempAttrs, "attrtype%d,attrvalue%d", i, i);
		else
			tempAttrs += sprintf(tempAttrs, "applytype%d,applyvalue%d", i - 7, i - 7);
		if (i<ITEM_ATTRIBUTE_MAX_NUM - 1)
			tempAttrs += sprintf(tempAttrs, ",");
	}
	SQLMsg * Msg(DBManager::instance().DirectQuery("SELECT id,vnum,count,display_pos,price,%s,%s from player_shop_items where shop_id='%d'",szSockets,szAttrs, GetPrivShop()));
	SQLResult * Res = Msg->Get();
	if (Res->uiNumRows > 0)
	{
		MYSQL_ROW row;
		while ((row = mysql_fetch_row(Res->pSQLResult)) != NULL)
		{

			int col = 0;



			TShopItemTable *shop = new TShopItemTable;
			memset(shop, 0, sizeof(TShopItemTable));
			DWORD id;
			shop->pos.window_type = INVENTORY;
			str_to_number(id, row[col++]);
			str_to_number(shop->vnum, row[col++]);
			str_to_number(shop->count, row[col++]);
			str_to_number(shop->display_pos, row[col++]);
			//col++;
			str_to_number(shop->price, row[col++]);

			const TItemTable * item_table = ITEM_MANAGER::instance().GetTable(shop->vnum);


			if (!item_table)
			{
				sys_err("Shop: no item table by item vnum #%d", shop->vnum);
				continue;
			}
			for (int i = 0; i < INVENTORY_MAX_NUM; ++i)
			{
				if (NULL != GetInventoryItem(i) && GetInventoryItem(i)->GetRealID() == id)
					GetInventoryItem(i)->RemoveFromCharacter();
			}
			LPITEM item = ITEM_MANAGER::instance().CreateItem(shop->vnum, shop->count, id, false, -1, true);
			if (-1 == (shop->pos.cell = GetEmptyInventory(item_table->bSize)))
			{
				sys_err("no empty position in npc inventory");
				return;
			}
			if (item)
			{
				item->ClearAttribute();
				item->SetRealID(id);
				for (int s = 0;s<ITEM_SOCKET_MAX_NUM;s++)
				{
					DWORD soc;
					str_to_number(soc, row[col++]);
					item->SetSocket(s, soc, false);
				}
				for (int at = 0;at<ITEM_ATTRIBUTE_MAX_NUM;at++)
				{
					DWORD attr;
					long val;
					str_to_number(attr, row[col++]);
					str_to_number(val, row[col++]);
					item->SetForceAttribute(at, attr, val);
				}

				item->AddToCharacter(this, shop->pos);
			}
			else
			{
				sys_err("%d is not item", shop->vnum);
				continue;
			}
			map_shop.push_back(shop);
		}
	}



	if (map_shop.size() == 0 || map_shop.size() > SHOP_HOST_ITEM_MAX_NUM)
	{
		DeleteMyShop();
		return;
	}
	npcshop->SetPrivShopItems(map_shop);
	npcshop->SetLocked(false);
	for (int i = 0;i < SHOP_HOST_ITEM_MAX_NUM;i++)
		npcshop->BroadcastUpdateItem(i);
	
	if (owner)
	{
		owner->LoadPrivShops();
		owner->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("SHOP_EDIT_SUCCESS"));
	}
}
void CHARACTER::LoadPrivShops()
{
	m_mapshops.clear();
	SQLMsg * pkMsg(DBManager::instance().DirectQuery("SELECT id,shop_vid,replace(replace(name,' ','\\\\'),'#','_'),gold,item_count,(select count(id) from player_shop_items where shop_id=player_shop.id),DATEDIFF(date_close,now()) AS days,UNIX_TIMESTAMP(date_close) from player_shop WHERE player_id=%d", GetPlayerID()));
	SQLResult * pRes = pkMsg->Get();
	if (pRes->uiNumRows>0)
	{

		MYSQL_ROW row;
		while ((row = mysql_fetch_row(pRes->pSQLResult)) != NULL)
		{
			int col = 0;
			TPrivShop shop;
			memset(&shop, 0, sizeof(TPrivShop));
			str_to_number(shop.shop_id, row[col++]);
			str_to_number(shop.shop_vid, row[col++]);
			strlcpy(shop.szSign, row[col++], sizeof(shop.szSign));
			str_to_number(shop.gold, row[col++]);
			str_to_number(shop.item_count, row[col++]);
			str_to_number(shop.rest_count, row[col++]);
			str_to_number(shop.days, row[col++]);
			str_to_number(shop.date_close, row[col++]);
			m_mapshops.insert(std::make_pair(shop.shop_id, shop));
		}
	}
	SendShops();
}
void CHARACTER::SendShops(bool isGm)
{
	ChatPacket(CHAT_TYPE_COMMAND, "shop_clear");
	PSHOP_MAP::iterator it = m_mapshops.begin();
	while (it != m_mapshops.end())
	{
		ChatPacket(CHAT_TYPE_COMMAND, "shop_add %d %d %s %lld %d %d %d %d", it->second.shop_id, it->second.shop_vid, it->second.szSign, it->second.gold, it->second.item_count, it->second.rest_count, it->second.days, it->second.date_close);
		it++;
	}

	
}
void CHARACTER::SendShopCost()
{
	extern std::map<int, TShopCost> g_ShopCosts;
	ChatPacket(CHAT_TYPE_COMMAND, "shop_cost_clear");
	std::map<int, TShopCost>::iterator it = g_ShopCosts.begin();
	while (it != g_ShopCosts.end())
	{
		ChatPacket(CHAT_TYPE_COMMAND, "shop_cost %d %d %d %lld", it->first,it->second.days, it->second.time, it->second.price);
		it++;
	}


}
void CHARACTER::OpenShop(DWORD id, const char *name, bool onboot)
{
	if (GetMyShop())
	{
		CloseMyShop();
		return;
	}
	if (IsPC())
		return;
	char szSockets[1024] = { '\0' };
	char *tempSockets = szSockets;
	for (int i = 0; i < ITEM_SOCKET_MAX_NUM; i++)
	{
		tempSockets += sprintf(tempSockets, "socket%d", i);

		if (i<ITEM_SOCKET_MAX_NUM - 1)
			tempSockets += sprintf(tempSockets, ",");
	}
	char szAttrs[1024] = { '\0' };
	char *tempAttrs = szAttrs;
	for (int i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; i++)
	{
		if (i < 7)
			tempAttrs += sprintf(tempAttrs, "attrtype%d,attrvalue%d", i, i);
		else
			tempAttrs += sprintf(tempAttrs, "applytype%d,applyvalue%d", i - 7, i - 7);
		if (i<ITEM_ATTRIBUTE_MAX_NUM - 1)
			tempAttrs += sprintf(tempAttrs, ",");
	}
	SQLMsg * pkMsg(DBManager::instance().DirectQuery("SELECT id,vnum,count,display_pos,price,%s,%s from player_shop_items where shop_id='%d'",szSockets,szAttrs, id));

	SQLResult * pRes = pkMsg->Get();
	BYTE bItemCount = pRes->uiNumRows;

	TShopItemTable * m_pShopTable = new TShopItemTable[bItemCount];
	memset(&m_pShopTable[0], 0, sizeof(TShopItemTable) * bItemCount);

	std::vector<TShopItemTable *> map_shop;

	if (bItemCount>0)
	{
		bItemCount = 0;
		MYSQL_ROW row;
		int c = 0;
		while ((row = mysql_fetch_row(pRes->pSQLResult)) != NULL)
		{
			int col = 0;



			TShopItemTable *shop = new TShopItemTable;
			memset(shop, 0, sizeof(TShopItemTable));
			DWORD id;
			shop->pos.window_type = INVENTORY;
			str_to_number(id, row[col++]);
			str_to_number(shop->vnum, row[col++]);
			str_to_number(shop->count, row[col++]);
			str_to_number(shop->display_pos, row[col++]);
			//col++;
			str_to_number(shop->price, row[col++]);

			const TItemTable * item_table = ITEM_MANAGER::instance().GetTable(shop->vnum);


			if (!item_table)
			{
				sys_err("Shop: no item table by item vnum #%d", shop->vnum);
				continue;
			}
			if (-1 == (shop->pos.cell = GetEmptyInventory(item_table->bSize)))
			{
				sys_err("no empty position in npc inventory");
				return;
			}
			
			LPITEM item = ITEM_MANAGER::instance().CreateItem(shop->vnum, shop->count, 0, false, -1, true);

			if (item)
			{
				item->ClearAttribute();
				item->SetSkipSave(true);
				item->SetRealID(id);
				for (int s = 0;s<ITEM_SOCKET_MAX_NUM;s++)
				{
					DWORD soc;
					str_to_number(soc, row[col++]);
					item->SetSocket(s, soc, false);
				}
				for (int at = 0;at<ITEM_ATTRIBUTE_MAX_NUM;at++)
				{
					DWORD attr;
					long val;
					str_to_number(attr, row[col++]);
					str_to_number(val, row[col++]);
					item->SetForceAttribute(at, attr, val);
				}
				

				item->AddToCharacter(this, shop->pos);
			}
			else
			{
				sys_err("%d is not item", shop->vnum);
				continue;
			}

			map_shop.push_back(shop);
			++bItemCount;
		}
	}



	if (bItemCount == 0 && !onboot || bItemCount > SHOP_HOST_ITEM_MAX_NUM)
		return;


	m_stShopSign = name;

	if (m_stShopSign.length()>30)
		m_stShopSign.resize(30);
	if (m_stShopSign.length() == 0)
		return;


	TPacketGCShopSign p;

	p.bHeader = HEADER_GC_SHOP_SIGN;
	p.dwVID = GetVID();
	strlcpy(p.szSign, m_stShopSign.c_str(), sizeof(p.szSign));

	PacketAround(&p, sizeof(TPacketGCShopSign));

	m_pkMyShop = CShopManager::instance().CreateNPCShop(this, map_shop);

}
void CHARACTER::DeleteMyShop()
{
	if (GetMyShop())
	{
		SQLMsg * pkMsg(DBManager::instance().DirectQuery("SELECT gold FROM player_shop where id='%d'", GetPrivShop()));
		SQLResult * pRes = pkMsg->Get();
		if (pRes->uiNumRows>0)
		{
			MYSQL_ROW row;
			while ((row = mysql_fetch_row(pRes->pSQLResult)) != NULL)
			{
				long long gold;
				str_to_number(gold, row[0]);
				if (gold>0)
				{
					char query[1024];
					sprintf(query, "INSERT INTO player_gift SET \
					owner_id=%d,vnum=1,count='%s',reason=\"%s\",`from`=replace(\"%s\",' ','_'),status='WAIT',date_add=NOW()",
					GetPrivShopOwner(), row[0], LC_TEXT("SHOP_REASON"), GetName());
					DBManager::instance().DirectQuery(query);
				}

			}
			GetMyShop()->GetItems();
			LPCHARACTER owner = CHARACTER_MANAGER::instance().FindByPID(GetPrivShopOwner());
			if (owner)
			{
#ifdef GIFT_SYSTEM
				owner->RefreshGift();
#endif
				owner->RemovePrivShopTable(GetPrivShop());
				owner->SendShops();
				owner->ChatPacket(CHAT_TYPE_INFO, LC_TEXT( "SHOP_SUCCESS_CLOSE"));
			}
			else{
				TPacketShopClose packet;
				packet.shop_id = GetPrivShop();
				packet.pid = GetPrivShopOwner();
				db_clientdesc->DBPacket(HEADER_GD_SHOP_CLOSE, 0, &packet, sizeof(packet));
			}

			DBManager::instance().DirectQuery("delete from player_shop where id='%d'", GetPrivShop());
			CloseMyShop();
		}
		return;
	}
	M2_DESTROY_CHARACTER(this);
}



EVENTFUNC(RefreshShopEvent)
{
	char_event_info* info = dynamic_cast<char_event_info*>(event->info);
	if (info == NULL)
	{
		sys_err("ishop_refresh_event> <Factor> Null pointer");
		return 0;
	}

	LPCHARACTER	ch = info->ch;

	if (NULL == ch)
		return 0;


	ch->SendShops();
	ch->SendShopCost();
	if(ch->GetGiftPages()>0)
		ch->ChatPacket(CHAT_TYPE_COMMAND, "gift_info %d", ch->GetGiftPages());
	return PASSES_PER_SEC(10);
}
void CHARACTER::StartRefreshShopEvent()
{
	if (m_pkRefreshShopEvent)
		return;

	char_event_info* info = AllocEventInfo<char_event_info>();

	info->ch = this;

	m_pkRefreshShopEvent = event_create(RefreshShopEvent, info, PASSES_PER_SEC(1));	// 1o?
}
#endif
