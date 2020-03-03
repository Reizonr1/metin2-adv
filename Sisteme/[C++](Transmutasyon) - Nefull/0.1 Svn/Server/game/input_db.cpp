// Search for:
		LPITEM item = ITEM_MANAGER::instance().CreateItem(p->vnum, p->count, p->id);

// Replace their function with:
#ifdef __CHANGE_LOOK_SYSTEM__
		LPITEM item = ITEM_MANAGER::instance().CreateItem(p->vnum, p->count, p->id, false, -1, false, p->dwVnum);
#else
		LPITEM item = ITEM_MANAGER::instance().CreateItem(p->vnum, p->count, p->id);
#endif
