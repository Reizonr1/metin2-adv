Arat:
	int pc_get_vid(lua_State* L)
	{
		lua_pushnumber(L, CQuestManager::instance().GetCurrentCharacterPtr()->GetVID());
		return 1;
	}
	
Üstüne ekle:
	int pc_is_afk(lua_State* L)
	{
		if (CQuestManager::instance().GetCurrentCharacterPtr()->IsAfk())
			lua_pushboolean(L, true);
		else
			lua_pushboolean(L, false);

		return 1;
	}

	int pc_set_afk(lua_State* L)
	{
		CQuestManager::instance().GetCurrentCharacterPtr()->SetAfk();
		return 1;
	}

	int pc_del_afk(lua_State* L)
	{
		CQuestManager::instance().GetCurrentCharacterPtr()->DelAfk();
		return 1;
	}
	
	int pc_is_open_shop(lua_State* L)
	{
		lua_pushboolean(L, CQuestManager::instance().GetCurrentCharacterPtr()->GetShopOwner());
		return 1;
	}

	
	
Arat:
{ "charge_cash",		pc_charge_cash		},

Altýna ekle:
			{ "is_afk",				pc_is_afk			},
			{ "set_afk",			pc_set_afk			},
			{ "del_afk",			pc_del_afk			},
			{ "is_open_shop",		pc_is_open_shop		},			
			
			
http://puu.sh/koHcH/4e3c1351f1.png