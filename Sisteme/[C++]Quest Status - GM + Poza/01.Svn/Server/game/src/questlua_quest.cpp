//Ara:
	int quest_get_current_quest_index(lua_State* L)
	{
		CQuestManager& q = CQuestManager::instance();
		PC* pPC = q.GetCurrentPC();

		int idx = q.GetQuestIndexByName(pPC->GetCurrentQuestName());
		lua_pushnumber(L, idx);
		return 1;
	}
//Altına Ekle:
	int quest_get_current_quest_name(lua_State* L)
	{
		CQuestManager& q = CQuestManager::instance();
		PC* pPC = q.GetCurrentPC();

		lua_pushstring(L, pPC->GetCurrentQuestName().c_str());
		return 1;
	}

//Ara:
 			{ "getcurrentquestindex",	quest_get_current_quest_index},
//Altına Ekle:
			{ "getcurrentquestname",	quest_get_current_quest_name},