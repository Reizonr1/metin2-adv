// 1) Search:
	void RegisterPCFunctionTable()
// 2) Before this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	int pc_open_changelook(lua_State * L)
	{
		CQuestManager & qMgr = CQuestManager::instance();
		LPCHARACTER pkChar = qMgr.GetCurrentCharacterPtr();
		if (pkChar)
			pkChar->ChangeLookWindow(true);
		
		return 0;
	}
#endif


// 1) Search:
			{NULL, NULL}
// 2) Before this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
			{"open_changelook", pc_open_changelook},
#endif