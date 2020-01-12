Search:
void ITEM_MANAGER::SaveSingleItem(LPITEM item)
{
	if (!item->GetOwner())


Change:
void ITEM_MANAGER::SaveSingleItem(LPITEM item)
{
	BYTE window = item->GetWindow();
#ifdef __OFFLINE_SHOP__
	if (!item->GetOwner() && window != OFFLINE_SHOP && window != SAFEBOX_OFFLINE_SHOP)
#else
	if (!item->GetOwner())
#endif

https://puu.sh/sgH6B/8ed90678da.png
---

Search:
	sys_log(1, "ITEM_SAVE %s:%d in %s window %d", item->GetName(), item->GetID(), item->GetOwner()->GetName(), item->GetWindow());

Change:
#ifdef __OFFLINE_SHOP__
	sys_log(1, "ITEM_SAVE %s:%u in window %d last owner pid %u", item->GetName(), item->GetID(), item->GetWindow(), item->GetLastOwnerPID());
#else
	sys_log(1, "ITEM_SAVE %s:%u in %s window %d", item->GetName(), item->GetID(), item->GetOwner()->GetName(), item->GetWindow());
#endif

https://puu.sh/sgH7A/4a810e3776.png
---

Search:
	TPlayerItem t;

	t.id = item->GetID();
	t.window = item->GetWindow();
	t.pos = t.window == EQUIPMENT ? item->GetCell() - INVENTORY_MAX_NUM : item->GetCell();
	t.count = item->GetCount();
	t.vnum = item->GetOriginalVnum();
	t.owner = (t.window == SAFEBOX || t.window == MALL) ? item->GetOwner()->GetDesc()->GetAccountTable().id : item->GetOwner()->GetPlayerID();

Change:
	TPlayerItem t;

	t.id = item->GetID();
	t.window = window;
	t.pos = ((window == EQUIPMENT) ? (item->GetCell() - INVENTORY_MAX_NUM) : item->GetCell());
	t.count = item->GetCount();
	t.vnum = item->GetOriginalVnum();

#ifdef __OFFLINE_SHOP__
	if (window == OFFLINE_SHOP || window == SAFEBOX_OFFLINE_SHOP)
		t.owner = item->GetLastOwnerPID();
	else if (window == SAFEBOX || window == MALL)
		t.owner = item->GetOwner()->GetAID();
	else
		t.owner = item->GetOwner()->GetPlayerID();
#else
	t.owner = (t.window == SAFEBOX || t.window == MALL) ? item->GetOwner()->GetDesc()->GetAccountTable().id : item->GetOwner()->GetPlayerID();
#endif

https://puu.sh/sgH9E/f83792aa14.png