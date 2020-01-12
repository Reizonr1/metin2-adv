[..]

#ifdef OFFLINE_SHOP
static LPEVENT s_pkShopEvent = NULL;
static LPEVENT s_pkFixShopEvent = NULL;

EVENTINFO(shop_event_info)
{
	// used to send command
	DWORD empty;
};
#include "shop.h"
EVENTFUNC(shop_event)
{
	LPCHARACTER pc;
	CharacterVectorInteractor i;

	if (CHARACTER_MANAGER::instance().GetCharactersByRaceNum(30000, i))
	{
		CharacterVectorInteractor::iterator it = i.begin();

		while (it != i.end()) {
			LPCHARACTER pc = *it++;
			if (pc)
			{
				LPSHOP shop;
				if ((shop = pc->GetMyShop())) {
					if (pc->GetShopTime() < get_global_time() || shop->GetItemCount() <= 0)
						pc->DeleteMyShop();
				}
				else
					M2_DESTROY_CHARACTER(pc);
			}

		}
	}

	return PASSES_PER_SEC(SHOP_TIME_REFRESH);
}

EVENTFUNC(fix_shop_event)
{
	char szSockets[1024] = { '\0' };
	char *tempSockets = szSockets;
	for (int i = 0; i < ITEM_SOCKET_MAX_NUM; i++)
	{
		tempSockets += sprintf(tempSockets, "ps.socket%d", i);

		if (i<ITEM_SOCKET_MAX_NUM - 1)
			tempSockets += sprintf(tempSockets, ",");
	}
	char szAttrs[1024] = { '\0' };
	char *tempAttrs = szAttrs;
	for (int i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; i++)
	{
		if (i < 7)
			tempAttrs += sprintf(tempAttrs, "ps.attrtype%d,attrvalue%d", i, i);
		else
			tempAttrs += sprintf(tempAttrs, "ps.applytype%d,applyvalue%d", i - 7, i - 7);
		if (i<ITEM_ATTRIBUTE_MAX_NUM - 1)
			tempAttrs += sprintf(tempAttrs, ",");
	}
	SQLMsg * pkMsg(DBManager::instance().DirectQuery("SELECT ps.id,ps.player_id,REPLACE('%s','#PLAYER_NAME#',p.name),ps.vnum,ps.count,ps.price,%s,%s FROM `player_shop_items` ps LEFT JOIN player p ON p.id=ps.player_id where not EXISTS(select name from player_shop WHERE id=ps.shop_id) and not ISNULL(p.name)", LC_TEXT("SHOP_NAME"), szSockets, szAttrs));
	SQLResult * pRes = pkMsg->Get();
	if (pRes->uiNumRows>0)
	{
		MYSQL_ROW row;
		while ((row = mysql_fetch_row(pRes->pSQLResult)) != NULL)
		{
			DWORD id,pid,vnum,count,socket[6],attr[7][2];
			int col = 0;
			str_to_number(id, row[col++]);
			str_to_number(pid, row[col++]);
			col++;

			str_to_number(vnum, row[col++]);
			str_to_number(count, row[col++]);
			for (int i = 0;i < ITEM_SOCKET_MAX_NUM;i++)
				str_to_number(socket[i], row[col++]);
			for (int i = 0;i < ITEM_ATTRIBUTE_MAX_NUM;i++)
			{
				str_to_number(attr[i][0], row[col++]);
				str_to_number(attr[i][1], row[col++]);
			}
			char query[1024];
			sprintf(query, "INSERT INTO player_gift SET owner_id=%d,vnum=%d,count=%d,reason='%s',`from`=replace(\"%s\",' ','_'),status='WAIT',date_add=NOW()",
				pid, vnum,count, LC_TEXT("SHOP_REASON"), row[3]);

			for (int s = 0; s < ITEM_SOCKET_MAX_NUM; s++)
			{
				sprintf(query, "%s, socket%d='%d'", query, s, socket[s]);

			}
			for (int ia = 0; ia < ITEM_ATTRIBUTE_MAX_NUM; ia++)
			{
				if (ia < 7)
				{
					sprintf(query, "%s, attrtype%d='%d'", query, ia, attr[ia][0]);
					sprintf(query, "%s, attrvalue%d='%d'", query, ia, attr[ia][1]);
				}
				else{
					sprintf(query, "%s, applytype%d='%d'", query, ia-7, attr[ia][0]);
					sprintf(query, "%s, applyvalue%d='%d'", query, ia-7, attr[ia][1]);
				}


			}
			DBManager::instance().DirectQuery(query);
			DBManager::instance().DirectQuery("delete from player_shop_items where id=%d",id);

		}
	}
	return PASSES_PER_SEC(SHOP_TIME_REFRESH*60);
}
void CreateShops()
{
	//sys_log(0,"Downloading shops list..");
	if (quest::CQuestManager::instance().GetEventFlag("shop_off") == 1)
		return;
	SQLMsg * pkMsg(DBManager::instance().DirectQuery("SELECT id,map_index from player_shop WHERE channel=%d and status='OK' and exists(select name from player where id=player_id)", g_bChannel));
	SQLResult * pRes = pkMsg->Get();
	if (pRes->uiNumRows>0)
	{
		MYSQL_ROW row;
		while ((row = mysql_fetch_row(pRes->pSQLResult)) != NULL)
		{
			long map_index;
			DWORD id, vid;
			str_to_number(id, row[0]);
			str_to_number(map_index, row[1]);
			//sys_log(0,"Find shop id %d map_index %d",id,map_index);
			if (!CShopManager::instance().FindPCShop(id))
			{

				//sys_log(0,"Creating offline shop id %d",id);
				CShopManager::instance().StartOfflineShop(id, true);
			}
		}
	}
	if (NULL == s_pkShopEvent)
	{
		shop_event_info* info = AllocEventInfo<shop_event_info>();
		s_pkShopEvent = event_create(shop_event, info,1);
	}
	if (NULL == s_pkFixShopEvent)
	{
		shop_event_info* info = AllocEventInfo<shop_event_info>();
		s_pkFixShopEvent = event_create(fix_shop_event, info,1);
	}
}
#endif
void CInputDB::Boot(const char* data)
{

	CMotionManager::instance().Build();
	
	#ifdef OFFLINE_SHOP
	CreateShops();
	#endif
}


#ifdef OFFLINE_SHOP
#include "shop_manager.h"
void CInputDB::ShopClose(const char * c_pData)
{
	TPacketShopClose * p = (TPacketShopClose *)c_pData;
	if (p->pid)
	{
		LPCHARACTER owner = CHARACTER_MANAGER::instance().FindByPID(p->pid);
		if (owner)
		{
#ifdef GIFT_SYSTEM
			owner->RefreshGift();
#endif
			owner->RemovePrivShopTable(p->shop_id);
			owner->SendShops();
			owner->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("SHOP_SUCCESS_CLOSE"));
		}
		return;
	}

	LPCHARACTER pc;
	CharacterVectorInteractor i;

	if (CHARACTER_MANAGER::instance().GetCharactersByRaceNum(30000, i))
	{
		CharacterVectorInteractor::iterator it = i.begin();

		while (it != i.end()) {
			LPCHARACTER pc = *it++;
			if (pc)
				if (pc->GetPrivShop() == p->shop_id) {
					pc->DeleteMyShop();
					return;
				}

		}
	}
}
void CInputDB::ShopName(const char * c_pData)
{
	TPacketShopName * p = (TPacketShopName *)c_pData;


	LPCHARACTER pc;
	CharacterVectorInteractor i;

	if (CHARACTER_MANAGER::instance().GetCharactersByRaceNum(30000, i))
	{
		CharacterVectorInteractor::iterator it = i.begin();

		while (it != i.end()) {
			LPCHARACTER pc = *it++;
			if (pc)
			{
				if (pc->GetPrivShop() == p->shop_id) {
					pc->SetShopSign(p->szSign);
					return;
				}
			}

		}
	}
}
void CInputDB::ShopUpdateItem(const char * c_pData)
{
	TPacketShopUpdateItem * p = (TPacketShopUpdateItem *)c_pData;


	LPCHARACTER pc;
	CharacterVectorInteractor i;

	if (CHARACTER_MANAGER::instance().GetCharactersByRaceNum(30000, i))
	{
		CharacterVectorInteractor::iterator it = i.begin();

		while (it != i.end()) {
			LPCHARACTER pc = *it++;
			if (pc)
				if (pc->GetPrivShop() == p->shop_id) {
					if(p->shop_locked && pc->GetMyShop())
					{
						pc->GetMyShop()->SetLocked(p->shop_locked);
						pc->GetMyShop()->RemoveGuests();
					}
					else
						pc->UpdateShopItems();
					return;
				}

		}
	}
}
#endif

int CInputDB::Analyze(LPDESC d, BYTE bHeader, const char * c_pData)
{
	switch (bHeader)
	{
	case HEADER_DG_BOOT:
		Boot(c_pData);
		break;
#ifdef OFFLINE_SHOP
	case HEADER_DG_SHOP_NAME:
		ShopName(c_pData);
		break;
	case HEADER_DG_SHOP_CLOSE:
		ShopClose(c_pData);
		break;
	case HEADER_DG_SHOP_UPDATE_ITEM:
		ShopUpdateItem(c_pData);
		break;
#endif
	case HEADER_DG_LOGIN_SUCCESS:
		LoginSuccess(m_dwHandle, c_pData);
		break;
	}
	[..]
}
[..]