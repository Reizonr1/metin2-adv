//1.0 suchen:
	void RegisterPCFunctionTable()
//1.0 davor:	
#ifdef ENABLE_VIP_SYSTEM
	int pc_set_vip(lua_State* L)
	{
		LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();
		if (!ch)
			return 1;

		BYTE viplevel = lua_isnumber(L, 1) ? lua_tonumber(L, 1) : 0;
		
		if (viplevel > 1)
			return 0;

		ch->SetVip(viplevel);
		ch->RefreshVip();
		ch->UpdatePacket();

		return 0;
	}

	int pc_reset_vip(lua_State* L)
	{
		LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();
		ch->ResetVip();
	}
	
	int pc_get_vip(lua_State* L)
	{
		lua_pushnumber(L, CQuestManager::instance().GetCurrentCharacterPtr()->GetVip());
		return 1;
	}

#endif
	
//1.1 suchen:
			{ NULL,			NULL			}
//1.1 davor:			
#ifdef ENABLE_VIP_SYSTEM
			{ "get_vip",	 	pc_get_vip },
			{ "set_vip",		pc_set_vip },
			{ "reset_vip",		pc_reset_vip },
#endif	
