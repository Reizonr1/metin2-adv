Search:
#include "../../common/VnumHelper.h"

Add it under:
#include "shop.h"
#include "shop_manager.h"

https://puu.sh/sgGbH/ee803b15cb.png
---

Search:
ACMD(do_mall_close)
{
	if (ch->GetMall())
	{
		ch->SetMallLoadTime(thecore_pulse());
		ch->CloseMall();
		ch->Save();
	}
}

Add it under:
#ifdef __OFFLINE_SHOP__
ACMD(do_gather)
{
	if (!ch->GetSafebox())
		return;

	if (quest::CQuestManager::instance().GetEventFlag("block_offlineshopcollect")) {
		ch->ChatPacket(CHAT_TYPE_INFO, "Offline shop reward collect feature is disabled.");
		return;
	}

	DWORD PID = ch->GetPlayerID();
	db_clientdesc->DBPacket(HEADER_GD_COLLECT_OFFLINE_SHOP_ITEM, ch->GetDesc()->GetHandle(), &PID, sizeof(PID));
}

ACMD(do_myshops)
{
	if (!ch)
		return;

	if (CShopManager::instance().GetOfflineShopCount(ch->GetPlayerID()) <= 0)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You're have not any offline shop!");
		return;
	}

	CShopManager::instance().GetOfflineShops(ch->GetPlayerID());
}

ACMD(do_offlineshop_goto)
{
	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	if (!*arg1 || !isdigit(*arg1))
		return;

	if (!ch)
		return;

	if (CShopManager::instance().GetOfflineShopCount(ch->GetPlayerID()) <= 0)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You're have not any offline shop!");
		return;
	}

	int iFloodResult = ch->GetQuestFlag("goto_shop.flood_check");
	if (iFloodResult && get_global_time() < iFloodResult + 60) {
		ch->ChatPacket(CHAT_TYPE_INFO, "You can not use too fast");
		return;
	}

	DWORD dwVID = 0;
	str_to_number(dwVID, arg1);
	CShopManager::instance().GotoOfflineShop(ch->GetPlayerID(), dwVID);
	ch->SetQuestFlag("goto_shop.flood_check", get_global_time());
}

ACMD(do_offlineshop_warp)
{
	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	if (!*arg1 || !isdigit(*arg1))
		return;

	if (!ch)
		return;

	if (CShopManager::instance().GetOfflineShopCount(ch->GetPlayerID()) <= 0)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You're have not any offline shop!");
		return;
	}

	int iFloodResult = ch->GetQuestFlag("warp_shop.flood_check");
	if (iFloodResult && get_global_time() < iFloodResult + 60) {
		ch->ChatPacket(CHAT_TYPE_INFO, "You can not use too fast");
		return;
	}

	DWORD dwVID = 0;
	str_to_number(dwVID, arg1);
	CShopManager::instance().WarpOfflineShop(ch->GetPlayerID(), dwVID);
	ch->SetQuestFlag("warp_shop.flood_check", get_global_time());
}

ACMD(do_offlineshop_close)
{
	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	if (!*arg1 || !isdigit(*arg1))
		return;

	if (!ch)
		return;

	if (CShopManager::instance().GetOfflineShopCount(ch->GetPlayerID()) <= 0)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "You're have not any offline shop!");
		return;
	}

	DWORD dwVID = 0;
	str_to_number(dwVID, arg1);
	CShopManager::instance().CloseOfflineShop(ch->GetPlayerID(), dwVID);
}

static void RefreshMoveShopAffect(LPCHARACTER ch, long mapindex, long x, long y)
{
	ch->Show(mapindex, x, y);
	ch->Stop();
}

ACMD(do_reloadpos)
{
	if (!ch)
		return;
	RefreshMoveShopAffect(ch, ch->GetMapIndex(), ch->GetX(), ch->GetY());
}

ACMD(do_moveshop)
{
	if (!ch) {
		sys_err("Move shop triggered null character pointer!");
		return;
	}

	long oldmyx = ch->GetX(), oldmyy = ch->GetY(), oldmyindex = ch->GetMapIndex();

	if (quest::CQuestManager::instance().GetEventFlag("block_offlineshopmove")) {
		ch->ChatPacket(CHAT_TYPE_INFO, "Offline shop move feature is disabled.");
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}

	int iFloodResult = ch->GetQuestFlag("move_shop.flood_check");
	if (iFloodResult && get_global_time() < iFloodResult + 60){
		ch->ChatPacket(CHAT_TYPE_INFO, "You can not use too fast");
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}

	char arg1[256], arg2[256];
	const char* line = two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));

	if (!*arg1 || !*arg2)
		return;

	long newx = 0, newy = 0;
	str_to_number(newx, arg1);
	str_to_number(newy, arg2);

	if (newx <= 0 || newy <= 0) {
		sys_err("New positions is wrong (%u-%u)", newx, newy);
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}

	if (!ch->GetShop()) {
		sys_err("Move shop triggered null shop pointer!");
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}

	LPCHARACTER chofshop = ch->GetShop()->GetPCShop();
	if (!chofshop) {
		sys_err("Move shop triggered null pcshop pointer!");
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}
	long oldshopx = chofshop->GetX(), oldshopy = chofshop->GetY();

	if (oldshopx <= 0 || oldshopy <= 0) {
		sys_err("Old shop's positions is wrong (%u-%u)", oldshopx, oldshopy);
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}

	if (chofshop->IsPC()) {
		sys_err("Shop is not offline shop!");
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}

	if (ch->GetPlayerID() != ch->GetShop()->GetOwner() && ch->GetGMLevel() != GM_IMPLEMENTOR) {
		sys_err("Function caller is not shop's owner!");
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}

	if (oldmyindex != chofshop->GetMapIndex()) {
		sys_err("Shop and owner is not in same map");
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}

	if (DISTANCE_APPROX(ch->GetX() - oldshopx, ch->GetY() - oldshopy) > 10000) {
		ch->ChatPacket(CHAT_TYPE_INFO, "You are too far to your offline shop!");
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}


	LPSECTREE pSec = chofshop->GetSectree();
	if (!pSec) {
		sys_err("Move shop triggered null sectree pointer!");
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}

	PIXEL_POSITION pos;
	if (!SECTREE_MANAGER::instance().GetMapBasePosition(oldmyx, oldmyy, pos)) {
		sys_err("Move shop GetMapBasePosition fail");
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}

	// Calculate new pos
	newx += pos.x / 100;
	newy += pos.y / 100;

	newx *= 100;
	newy *= 100;

	PIXEL_POSITION pos2;
	if (!SECTREE_MANAGER::instance().GetMovablePosition(oldmyindex, newx, newy, pos2)) {
		ch->ChatPacket(CHAT_TYPE_INFO, "You can not move your offline shop to unavailable position!");
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}

	if (chofshop->HasNearOfflineShop(newx, newy)) {
		ch->ChatPacket(CHAT_TYPE_INFO, "You can not move your offline shop to near other offline shops!");
		RefreshMoveShopAffect(ch, oldmyindex, oldmyx, oldmyy);
		return;
	}

	ch->GetShop()->SetLocked(true);

	// Warp shop to new pos
	chofshop->Show(oldmyindex, newx, newy);
	chofshop->Stop();

	// Change from mysql
	char szQuery[QUERY_MAX_LEN + 1];
	sprintf(szQuery, "UPDATE player.offline_shop%s SET x=%u, y=%u WHERE pid=%u AND x=%u AND y=%u", get_table_postfix(), newx, newy, ch->GetPlayerID(), oldshopx, oldshopy);

	std::auto_ptr<SQLMsg> pMsg(AccountDB::instance().DirectQuery(szQuery));
	if (pMsg->uiSQLErrno != 0) {
		sys_err("Move shop query failed, Error code: %u, %s: %s", pMsg->uiSQLErrno, ch->GetName(), szQuery);

		ch->GetShop()->Remove();
		M2_DESTROY_CHARACTER(ch->GetShop()->GetPCShop());
		return;
	}

	if (pMsg->Get()->uiAffectedRows == 0 || pMsg->Get()->uiAffectedRows == (uint32_t)-1) {
		sys_err("Move shop query NOT affected to any row! %s: %s", ch->GetName(), szQuery);

		ch->GetShop()->Remove();
		M2_DESTROY_CHARACTER(ch->GetShop()->GetPCShop());
		return;
	}

	// Complete
	ch->GetShop()->SetLocked(false);
	ch->SetQuestFlag("move_shop.flood_check", get_global_time());
	ch->ChatPacket(CHAT_TYPE_INFO, "Your offline shop succesfuly to new position!");
}
#endif

https://puu.sh/sgGh8/1d206b5f44.png
https://puu.sh/sgGgP/afefd30361.png
---

Search:
ACMD(do_close_shop)
{
	if (ch->GetMyShop())
	{
		ch->CloseMyShop();
		return;
	}
}

Change:
#ifdef __OFFLINE_SHOP__
ACMD(do_close_shop)
{
	if (ch->GetMyShop())
	{
		ch->CloseMyShop();
	}
	else if (ch->GetShop() && !ch->GetShop()->GetPCShop()->IsPC())
	{
		if (ch->GetPlayerID() == ch->GetShop()->GetOwner() || ch->GetGMLevel() > GM_PLAYER)
		{
			ch->GetShop()->Remove();
			M2_DESTROY_CHARACTER(ch->GetShop()->GetPCShop());
		}
	}
}
#else
ACMD(do_close_shop)
{
	if (ch->GetMyShop())
	{
		ch->CloseMyShop();
		return;
	}
}
#endif

https://puu.sh/sgGgr/a0ac390505.png