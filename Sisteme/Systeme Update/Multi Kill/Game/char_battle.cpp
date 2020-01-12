Search:
	// BOSS_KILL_LOG
	if (GetMobRank() >= MOB_RANK_BOSS && pkKiller && pkKiller->IsPC())
	{
		char buf[51];
		snprintf(buf, sizeof(buf), "%d %ld", g_bChannel, pkKiller->GetMapIndex());
		if (IsStone())
			LogManager::instance().CharLog(pkKiller, GetRaceNum(), "STONE_KILL", buf);
		else
			LogManager::instance().CharLog(pkKiller, GetRaceNum(), "BOSS_KILL", buf);
	}
	// END_OF_BOSS_KILL_LOG
	
Add it under:
	if (pkKiller){
		if (IsPC() && pkKiller->IsPC())
		{
			if (get_global_time() < pkKiller->GetQuestFlag("2x_kill")){
				pkKiller->SetQuestFlag("2x_kill", 0);
				pkKiller->SetQuestFlag("3x_kill", get_global_time() + 6);
				pkKiller->ChatPacket(CHAT_TYPE_COMMAND, "2x_kill");
			}
			else if (get_global_time() < pkKiller->GetQuestFlag("3x_kill")){
				pkKiller->SetQuestFlag("3x_kill", 0);
				pkKiller->SetQuestFlag("4x_kill", get_global_time() + 6);
				pkKiller->ChatPacket(CHAT_TYPE_COMMAND, "3x_kill");
			}
			else if (get_global_time() < pkKiller->GetQuestFlag("4x_kill")){
				pkKiller->SetQuestFlag("4x_kill", 0);
				pkKiller->SetQuestFlag("5x_kill", get_global_time() + 6);
				pkKiller->ChatPacket(CHAT_TYPE_COMMAND, "4x_kill");
			}
			else if (get_global_time() < pkKiller->GetQuestFlag("5x_kill")){
				pkKiller->SetQuestFlag("5x_kill", 0);
				pkKiller->SetQuestFlag("6x_kill", get_global_time() + 6);
				pkKiller->ChatPacket(CHAT_TYPE_COMMAND, "5x_kill");
			}
			else if (get_global_time() < pkKiller->GetQuestFlag("6x_kill")){
				pkKiller->SetQuestFlag("6x_kill", 0);
				pkKiller->SetQuestFlag("6x_kill", get_global_time() + 6);
				pkKiller->ChatPacket(CHAT_TYPE_COMMAND, "6x_kill");
			}
			else{
				pkKiller->SetQuestFlag("1x_kill", get_global_time() + 6);
				pkKiller->ChatPacket(CHAT_TYPE_COMMAND, "1x_kill");
			}
		}
	}