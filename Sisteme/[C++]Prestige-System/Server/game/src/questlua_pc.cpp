#define MAX_PRESTIGE 12
// Suche :
	int pc_set_level(lua_State * L)  
// Füge nach der Funktion das ein :
#ifdef __PRESTIGE_SYSTEM__ 
	int pc_set_prestige(lua_State* L)
	{
		LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();
		if (!ch)
			return 1;

		BYTE prestigelevel = lua_isnumber(L, 1) ? lua_tonumber(L, 1) : 0;
		
		if (prestigelevel > MAX_PRESTIGE)
			return 0;

		ch->SetPrestigeLevel(prestigelevel);

		return 0;
	}

	int pc_get_prestige(lua_State* L)
	{
		LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();
		if (!ch)
		{
			lua_pushnumber(L, 0);
			return 1;
		}

		lua_pushnumber(L, ch->GetPrestigeLevel());

		return 0;
	}
#endif
// Suche :
			{ "set_level",		pc_set_level		},
// Füge darunter das ein :
#ifdef __PRESTIGE_SYSTEM__
			{ "get_prestige",	pc_get_prestige },
			{ "set_prestige",	pc_set_prestige },
#endif