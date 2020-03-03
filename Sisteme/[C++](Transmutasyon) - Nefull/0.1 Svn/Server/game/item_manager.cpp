// Search for:
LPITEM ITEM_MANAGER::CreateItem(DWORD vnum, DWORD count, DWORD id, bool bTryMagic, int iRarePct, bool bSkipSave)

// Replace their with:
#ifdef __CHANGE_LOOK_SYSTEM__
LPITEM ITEM_MANAGER::CreateItem(DWORD vnum, DWORD count, DWORD id, bool bTryMagic, int iRarePct, bool bSkipSave, DWORD dwLook)
#else
LPITEM ITEM_MANAGER::CreateItem(DWORD vnum, DWORD count, DWORD id, bool bTryMagic, int iRarePct, bool bSkipSave)
#endif

// Search for:
	item->SetMaskVnum(dwMaskVnum);

// Add Under:
#ifdef __CHANGE_LOOK_SYSTEM__
	item->SetItemLook(dwLook);
#endif

// Search for:
	t.vnum = item->GetOriginalVnum();

// Add Under:
#ifdef __CHANGE_LOOK_SYSTEM__
	t.dwVnum = item->GetItemLook();
#endif
