// 1) Search:
	void RegisterITEMFunctionTable()
// 2) Before this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	int item_is_transmulated(lua_State* L)
	{
		CQuestManager & qMgr = CQuestManager::instance();
		LPITEM pkItem = qMgr.GetCurrentItem();
		if (pkItem)
		{
			if (pkItem->GetTransmutation() > 0)
				lua_pushboolean(L, true);
			else
				lua_pushboolean(L, false);
		}
		else
			lua_pushboolean(L, false);
		
		return 1;
	}
	
	int item_set_transmutation(lua_State* L)
	{
		CQuestManager & qMgr = CQuestManager::instance();
		LPITEM pkItem = qMgr.GetCurrentItem();
		if ((pkItem) && (lua_isnumber(L, 1)))
		{
			DWORD dwTransmutation = (DWORD) lua_tonumber(L, 1);
			pkItem->SetTransmutation(dwTransmutation);
		}
		
		return 0;
	}
	
	int item_get_transmutation(lua_State* L)
	{
		CQuestManager & qMgr = CQuestManager::instance();
		LPITEM pkItem = qMgr.GetCurrentItem();
		if (pkItem)
			lua_pushnumber(L, pkItem->GetTransmutation());
		else
			lua_pushnumber(L, 0);
		
		return 1;
	}
#endif


// 1) Search:
			{NULL, NULL}
// 2) Before this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
			{"is_transmulated", item_is_transmulated},
			{"set_transmutation", item_set_transmutation},
			{"get_transmutation", item_get_transmutation},
#endif