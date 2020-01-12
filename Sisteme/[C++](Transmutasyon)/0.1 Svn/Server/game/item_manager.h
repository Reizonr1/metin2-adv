// Search for:
		LPITEM			CreateItem(DWORD vnum, DWORD count = 1, DWORD id = 0, bool bTryMagic = false, int iRarePct = -1, bool bSkipSave = false);

// Replace their with:
#ifdef __CHANGE_LOOK_SYSTEM__
		LPITEM                  CreateItem(DWORD vnum, DWORD count = 1, DWORD dwID = 0, bool bTryMagic = false, int iRarePct = -1, bool bSkipSave = false, DWORD dwLook = 0);
#else
		LPITEM                  CreateItem(DWORD vnum, DWORD count = 1, DWORD dwID = 0, bool bTryMagic = false, int iRarePct = -1, bool bSkipSave = false);
#endif
