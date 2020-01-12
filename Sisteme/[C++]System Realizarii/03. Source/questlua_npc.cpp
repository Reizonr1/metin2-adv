// 1) Search for: void RegisterNPCFunctionTable()
// 2) Paste this above:

	int npc_is_metin(lua_State* L)
	{
		CQuestManager& q = CQuestManager::instance();
		LPCHARACTER npc = q.GetCurrentNPCCharacterPtr();
		if(!npc || npc->IsPC())
		{
			lua_pushboolean(L, false);
			return 1;
		}
		lua_pushboolean(L, npc->IsStone());
		return 1;
	}

	int npc_is_boss(lua_State* L)
	{
		CQuestManager& q = CQuestManager::instance();
		LPCHARACTER npc = q.GetCurrentNPCCharacterPtr();
		if(!npc || npc->IsPC())
		{
			lua_pushboolean(L, false);
			return 1;
		}
		lua_pushboolean(L, npc->GetMobRank() == MOB_RANK_BOSS);
		return 1;
	}
	
// 1) Search for: void RegisterNPCFunctionTable()
// 2) And paste this above { NULL,				NULL			    	}

			{ "is_boss",	npc_is_boss },
			{ "is_metin",	npc_is_metin },
