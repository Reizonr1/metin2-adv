// Cauta
	//CHECK_FORKEDROAD_WAR
	if (IsPC())
	{
		if (CThreeWayWar::instance().IsThreeWayWarMapIndex(GetMapIndex()))
			isForked = true;
	}
	//END_CHECK_FORKEDROAD_WAR

// Adauga dupa
#ifdef ENABLE_BOSS_TRACKING
	if (!IsPC() && pkKiller && pkKiller->IsPC())
	{
		quest::CQuestManager& BTracking = quest::CQuestManager::instance();

		if (GetRaceNum() == 1192 && GetMapIndex() == 72)  // Güçlü Buz Cadisi ( 4 Saat )
		{
			if (g_bChannel == 1)
				BTracking.RequestSetEventFlagBR("newtracking","cadi1", get_global_time()+240*60);
			else if (g_bChannel == 2)
				BTracking.RequestSetEventFlagBR("newtracking","cadi2", get_global_time()+240*60);
			else if (g_bChannel == 3)
				BTracking.RequestSetEventFlagBR("newtracking","cadi3", get_global_time()+240*60);
			else if (g_bChannel == 4)
				BTracking.RequestSetEventFlagBR("newtracking","cadi4", get_global_time()+240*60);
			else if (g_bChannel == 5)
				BTracking.RequestSetEventFlagBR("newtracking","cadi5", get_global_time()+240*60);
			else if (g_bChannel == 6)
				BTracking.RequestSetEventFlagBR("newtracking","cadi6", get_global_time()+240*60);
		}
		if (GetRaceNum() == 2206 && GetMapIndex() == 62)  // Alev Kral ( 2 Saat )
		{
			if (g_bChannel == 1)
				BTracking.RequestSetEventFlagBR("newtracking","alevkral1", get_global_time()+120*60);
			else if (g_bChannel == 2)
				BTracking.RequestSetEventFlagBR("newtracking","alevkral2", get_global_time()+120*60);
			else if (g_bChannel == 3)
				BTracking.RequestSetEventFlagBR("newtracking","alevkral3", get_global_time()+120*60);
			else if (g_bChannel == 4)
				BTracking.RequestSetEventFlagBR("newtracking","alevkral4", get_global_time()+120*60);
			else if (g_bChannel == 5)
				BTracking.RequestSetEventFlagBR("newtracking","alevkral5", get_global_time()+120*60);
			else if (g_bChannel == 6)
				BTracking.RequestSetEventFlagBR("newtracking","alevkral6", get_global_time()+120*60);
		}
		if (GetRaceNum() == 2091 && GetMapIndex() == 104)  // Kralice Örümcek ( 1 Saat )
		{
			if (g_bChannel == 1)
				BTracking.RequestSetEventFlagBR("newtracking","kraliceormcek1", get_global_time()+120*60);
			else if (g_bChannel == 2)
				BTracking.RequestSetEventFlagBR("newtracking","kraliceormcek2", get_global_time()+120*60);
			else if (g_bChannel == 3)
				BTracking.RequestSetEventFlagBR("newtracking","kraliceormcek3", get_global_time()+120*60);
			else if (g_bChannel == 4)
				BTracking.RequestSetEventFlagBR("newtracking","kraliceormcek4", get_global_time()+120*60);
			else if (g_bChannel == 5)
				BTracking.RequestSetEventFlagBR("newtracking","kraliceormcek5", get_global_time()+120*60);
			else if (g_bChannel == 6)
				BTracking.RequestSetEventFlagBR("newtracking","kraliceormcek6", get_global_time()+120*60);
		}
		if (GetRaceNum() == 1304 && GetMapIndex() == 65)  // Sari Kaplan Hayaleti ( 1 Saat )
		{
			if (g_bChannel == 1)
				BTracking.RequestSetEventFlagBR("newtracking","sarikaplan1", get_global_time()+120*60);
			else if (g_bChannel == 2)
				BTracking.RequestSetEventFlagBR("newtracking","sarikaplan2", get_global_time()+120*60);
			else if (g_bChannel == 3)
				BTracking.RequestSetEventFlagBR("newtracking","sarikaplan3", get_global_time()+120*60);
			else if (g_bChannel == 4)
				BTracking.RequestSetEventFlagBR("newtracking","sarikaplan4", get_global_time()+120*60);
			else if (g_bChannel == 5)
				BTracking.RequestSetEventFlagBR("newtracking","sarikaplan5", get_global_time()+120*60);
			else if (g_bChannel == 6)
				BTracking.RequestSetEventFlagBR("newtracking","sarikaplan6", get_global_time()+120*60);
		}
		if (GetRaceNum() == 691 && GetMapIndex() == 64)  // Buz Kralicesi ( 4 Saat )
		{
			if (g_bChannel == 1)
				BTracking.RequestSetEventFlagBR("newtracking","buzkralice1", get_global_time()+20*60);
			else if (g_bChannel == 2)
				BTracking.RequestSetEventFlagBR("newtracking","buzkralice2", get_global_time()+20*60);
			else if (g_bChannel == 3)
				BTracking.RequestSetEventFlagBR("newtracking","buzkralice3", get_global_time()+20*60);
			else if (g_bChannel == 4)
				BTracking.RequestSetEventFlagBR("newtracking","buzkralice4", get_global_time()+20*60);
			else if (g_bChannel == 5)
				BTracking.RequestSetEventFlagBR("newtracking","buzkralice5", get_global_time()+20*60);
			else if (g_bChannel == 6)
				BTracking.RequestSetEventFlagBR("newtracking","buzkralice6", get_global_time()+20*60);
		}
		if (GetRaceNum() == 1901 && GetMapIndex() == 61)  // Dokuz Kuyruk ( 1 Saat )
		{
			if (g_bChannel == 1)
				BTracking.RequestSetEventFlagBR("newtracking","dokuzkuyruk1", get_global_time()+30*60);
			else if (g_bChannel == 2)
				BTracking.RequestSetEventFlagBR("newtracking","dokuzkuyruk2", get_global_time()+30*60);
			else if (g_bChannel == 3)
				BTracking.RequestSetEventFlagBR("newtracking","dokuzkuyruk3", get_global_time()+30*60);
			else if (g_bChannel == 4)
				BTracking.RequestSetEventFlagBR("newtracking","dokuzkuyruk4", get_global_time()+30*60);
			else if (g_bChannel == 5)
				BTracking.RequestSetEventFlagBR("newtracking","dokuzkuyruk5", get_global_time()+30*60);
			else if (g_bChannel == 6)
				BTracking.RequestSetEventFlagBR("newtracking","dokuzkuyruk6", get_global_time()+30*60);
		}
		if (GetRaceNum() == 2191 && GetMapIndex() == 63)  // Güçlü Buz Cadisi ( 4 Saat )
		{
			if (g_bChannel == 1)
				BTracking.RequestSetEventFlagBR("newtracking","colejderha1", get_global_time()+20*60);
			else if (g_bChannel == 2)
				BTracking.RequestSetEventFlagBR("newtracking","colejderha2", get_global_time()+20*60);
			else if (g_bChannel == 3)
				BTracking.RequestSetEventFlagBR("newtracking","colejderha3", get_global_time()+20*60);
			else if (g_bChannel == 4)
				BTracking.RequestSetEventFlagBR("newtracking","colejderha4", get_global_time()+20*60);
			else if (g_bChannel == 5)
				BTracking.RequestSetEventFlagBR("newtracking","colejderha5", get_global_time()+20*60);
			else if (g_bChannel == 6)
				BTracking.RequestSetEventFlagBR("newtracking","colejderha6", get_global_time()+20*60);
		}
		if (GetRaceNum() == 2307 && GetMapIndex() == 68)  // Güçlü Buz Cadisi ( 4 Saat )
		{
			if (g_bChannel == 1)
				BTracking.RequestSetEventFlagBR("newtracking","agac1", get_global_time()+150*60);
			else if (g_bChannel == 2)
				BTracking.RequestSetEventFlagBR("newtracking","agac2", get_global_time()+150*60);
			else if (g_bChannel == 3)
				BTracking.RequestSetEventFlagBR("newtracking","agac3", get_global_time()+150*60);
			else if (g_bChannel == 4)
				BTracking.RequestSetEventFlagBR("newtracking","agac4", get_global_time()+150*60);
			else if (g_bChannel == 5)
				BTracking.RequestSetEventFlagBR("newtracking","agac5", get_global_time()+150*60);
			else if (g_bChannel == 6)
				BTracking.RequestSetEventFlagBR("newtracking","agac6", get_global_time()+150*60);
		}
		if (GetRaceNum() == 2492 && GetMapIndex() == 73)  // Güçlü Buz Cadisi ( 4 Saat )
		{
			if (g_bChannel == 1)
				BTracking.RequestSetEventFlagBR("newtracking","komutan1", get_global_time()+60*60);
			else if (g_bChannel == 2)
				BTracking.RequestSetEventFlagBR("newtracking","komutan2", get_global_time()+60*60);
			else if (g_bChannel == 3)
				BTracking.RequestSetEventFlagBR("newtracking","komutan3", get_global_time()+60*60);
			else if (g_bChannel == 4)
				BTracking.RequestSetEventFlagBR("newtracking","komutan4", get_global_time()+60*60);
			else if (g_bChannel == 5)
				BTracking.RequestSetEventFlagBR("newtracking","komutan5", get_global_time()+60*60);
			else if (g_bChannel == 6)
				BTracking.RequestSetEventFlagBR("newtracking","komutan6", get_global_time()+60*60);
		}
		if (GetRaceNum() == 792 && GetMapIndex() == 65)  // Güçlü Buz Cadisi ( 4 Saat )
		{
			if (g_bChannel == 1)
				BTracking.RequestSetEventFlagBR("newtracking","karanlik1", get_global_time()+120*60);
			else if (g_bChannel == 2)
				BTracking.RequestSetEventFlagBR("newtracking","karanlik2", get_global_time()+120*60);
			else if (g_bChannel == 3)
				BTracking.RequestSetEventFlagBR("newtracking","karanlik3", get_global_time()+120*60);
			else if (g_bChannel == 4)
				BTracking.RequestSetEventFlagBR("newtracking","karanlik4", get_global_time()+120*60);
			else if (g_bChannel == 5)
				BTracking.RequestSetEventFlagBR("newtracking","karanlik5", get_global_time()+120*60);
			else if (g_bChannel == 6)
				BTracking.RequestSetEventFlagBR("newtracking","karanlik6", get_global_time()+120*60);
		}
	}
#endif