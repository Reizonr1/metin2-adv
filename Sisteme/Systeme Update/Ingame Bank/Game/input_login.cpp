Search:
	// Áß¸³¸Ê¿¡ µé¾î°¬À»¶§ ¾È³»ÇÏ±â
	if (g_noticeBattleZone)
	{
		if (FN_is_battle_zone(ch))
		{
			ch->ChatPacket(CHAT_TYPE_NOTICE, LC_TEXT("ÀÌ ¸Ê¿¡¼± °­Á¦ÀûÀÎ ´ëÀüÀÌ ÀÖÀ»¼ö µµ ÀÖ½À´Ï´Ù."));
			ch->ChatPacket(CHAT_TYPE_NOTICE, LC_TEXT("ÀÌ Á¶Ç×¿¡ µ¿ÀÇÇÏÁö ¾ÊÀ»½Ã"));
			ch->ChatPacket(CHAT_TYPE_NOTICE, LC_TEXT("º»ÀÎÀÇ ÁÖ¼º ¹× ºÎ¼ºÀ¸·Î µ¹¾Æ°¡½Ã±â ¹Ù¶ø´Ï´Ù."));
		}
	}

Add it under:
	std::auto_ptr<SQLMsg> bar_msg(DBManager::instance().DirectQuery("SELECT bank_bar_first, bank_bar_second, bank_bar_third FROM player.player WHERE name = '%s'", ch->GetName()));
	if (bar_msg->uiSQLErrno != 0) {
		sys_err("Bar get Amount Query Failed, Error code: %ld", bar_msg->uiSQLErrno);
	}
	else{
		if (!bar_msg->Get()->uiNumRows){
			sys_err("Bar get Amount Failed, Rows couldn't get, Row count: %d", bar_msg->Get()->uiNumRows);
		}
		else{
			MYSQL_ROW row = mysql_fetch_row(bar_msg->Get()->pSQLResult);

			const char * cMyFirstBar = row[0];
			const char * cMySecondBar = row[1];
			const char * cMyThirdBar = row[2];

			ch->ChatPacket(CHAT_TYPE_COMMAND, "RecvBarCount %s %s %s", cMyFirstBar, cMySecondBar, cMyThirdBar);
		}
	}
