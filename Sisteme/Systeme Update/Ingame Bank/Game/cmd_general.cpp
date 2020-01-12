Search:
ACMD(do_detaillog)
{
	ch->DetailLog();
}

Add it under:
ACMD(do_ingame_bank)
{
	int Bar_First = 10000000; int Bar_Second = 100000000; int Bar_Third = 1000000000; /* Bar amounts */

	// Process args
	char arg1[256], arg2[256];
	two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));

	// First Argument 1; Yang to bar
	// First Argument 2; Bar to Yang

	// Check args
	if (!*arg1 || !*arg2){
		ch->ChatPacket(CHAT_TYPE_INFO, "Missing Argument");
		return;
	}

	if (!isdigit(*arg1)){
		ch->ChatPacket(CHAT_TYPE_INFO, "Wrong Argument");
		return;
	}

	int iArgFirst = 0;
	str_to_number(iArgFirst, arg1);

	// Check args
	if (iArgFirst != 1 && iArgFirst != 2){
		ch->ChatPacket(CHAT_TYPE_INFO, "Unknown Argument");
		return;
	}

	if (!isdigit(*arg2)){
		ch->ChatPacket(CHAT_TYPE_INFO, "Wrong Argument2");
		return;
	}

	int iArgSecond = 0; // yang from arg
	str_to_number(iArgSecond, arg2);

	// General checks
	if (iArgFirst == 1 && iArgSecond > ch->GetGold()){
		ch->ChatPacket(CHAT_TYPE_INFO, "Inadequate yang");
		return;
	}

	if (iArgSecond < Bar_First){
		ch->ChatPacket(CHAT_TYPE_INFO, "Yang amount is too low");
		return;
	}

	if (test_server)
		ch->ChatPacket(CHAT_TYPE_INFO, "Arg1: %d Arg2: %d", iArgFirst, iArgSecond);

	// Check flood
	int iFloodResult = ch->GetQuestFlag("ingame_bank.flood_check");
	if (iFloodResult){
		if (get_global_time() < iFloodResult + 30 /* limit */) {
			ch->ChatPacket(CHAT_TYPE_INFO, "You can not use too fast");
			return;
		}
	}

	// Get old bar amount from db
	std::auto_ptr<SQLMsg> get_old_bar_msg(DBManager::instance().DirectQuery("SELECT bank_bar_first, bank_bar_second, bank_bar_third FROM player.player WHERE name = '%s'", ch->GetName()));

	if (get_old_bar_msg->uiSQLErrno != 0) {
		sys_err("Get Old Bar Query Failed, Error code: %ld", get_old_bar_msg->uiSQLErrno);
		return;
	}
	if (!get_old_bar_msg->Get()->uiNumRows){
		sys_err("Get Old Bar Query Failed, Rows couldn't get");
		return;
	}

	MYSQL_ROW row = mysql_fetch_row(get_old_bar_msg->Get()->pSQLResult);

	const char * cMyFirstBar = row[0]; const char * cMySecondBar = row[1]; const char * cMyThirdBar = row[2];
	int iMyFirstBar = 0; int iMySecondBar = 0; int iMyThirdBar = 0;

	str_to_number(iMyFirstBar, cMyFirstBar); str_to_number(iMySecondBar, cMySecondBar); str_to_number(iMyThirdBar, cMyThirdBar);

	if (test_server)
		ch->ChatPacket(CHAT_TYPE_INFO, "My old bars; First: %d Second: %d Third: %d", iMyFirstBar, iMySecondBar, iMyThirdBar);

	// Process bank stuffs -> Gold to bar
	if (iArgFirst == 1){
		// Calc new bar amount
		int converted_money = iArgSecond;

		while (converted_money >= Bar_Third){
			iMyThirdBar += 1;
			converted_money -= Bar_Third;
		}

		while (converted_money >= Bar_Second){
			iMySecondBar += 1;
			converted_money -= Bar_Second;
		}

		while (converted_money >= Bar_First){
			iMyFirstBar += 1;
			converted_money -= Bar_First;
		}

		if (test_server)
			ch->ChatPacket(CHAT_TYPE_INFO, "New bars; First: %d Second : %d Third : %d", iMyFirstBar, iMySecondBar, iMyThirdBar);

		// Overflow check
		if (iMyFirstBar > static_cast<int64_t>(99999999999) || iMySecondBar > static_cast<int64_t>(99999999999) || iMyThirdBar > static_cast<int64_t>(99999999999)){
			ch->ChatPacket(CHAT_TYPE_INFO, "Bar overflow !");
			return;
		}

		// Set new bar amounts to db
		int iLosedGold = iArgSecond - converted_money;

		std::auto_ptr<SQLMsg> new_bar_msg(DBManager::instance().DirectQuery("UPDATE player.player SET bank_bar_first = %d, bank_bar_second = %d, bank_bar_third = %d WHERE name = '%s'", iMyFirstBar, iMySecondBar, iMyThirdBar, ch->GetName()));
		if (new_bar_msg->uiSQLErrno != 0) {
			sys_err("New Bar Query Failed, Error code: %ld", new_bar_msg->uiSQLErrno);
			return;
		}

		ch->PointChange(POINT_GOLD, -iLosedGold); //Decrease gold

		ch->SetQuestFlag("ingame_bank.flood_check", get_global_time()); // Set flood check time

		// Info
		ch->ChatPacket(CHAT_TYPE_INFO, "Your new bar amounts; x1000: %d, x100: %d, x10: %d", iMyThirdBar, iMySecondBar, iMyFirstBar);
		ch->ChatPacket(CHAT_TYPE_INFO, "You losed %d gold", iLosedGold);
		ch->ChatPacket(CHAT_TYPE_COMMAND, "RecvBarCount %d %d %d", iMyFirstBar, iMySecondBar, iMyThirdBar);

		//Log
		if (iMyFirstBar)
			LogManager::instance().QuestRewardLog("GOLD_TO_BAR_FIRST", ch->GetPlayerID(), ch->GetLevel(), iMyFirstBar, 0);
		if (iMySecondBar)
			LogManager::instance().QuestRewardLog("GOLD_TO_BAR_SECOND", ch->GetPlayerID(), ch->GetLevel(), iMySecondBar, 0);
		if (iMyThirdBar)
			LogManager::instance().QuestRewardLog("GOLD_TO_BAR_THIRD", ch->GetPlayerID(), ch->GetLevel(), iMyThirdBar, 0);

		LogManager::instance().QuestRewardLog("GOLD_TO_BAR_LOSE_GOLD", ch->GetPlayerID(), ch->GetLevel(), iLosedGold, 0);
	}
	else if (iArgFirst == 2){ /* Process bank stuffs -> Bar to gold */
		int iMyMoneyPriceForBarFirst = 0; int iMyMoneyPriceForBarSecond = 0; int iMyMoneyPriceForBarThird = 0; //Convert arg money to bar

		int converted_money = iArgSecond;
		while (converted_money >= Bar_Third){
			iMyMoneyPriceForBarThird += 1;
			converted_money -= Bar_Third;
		}

		while (converted_money >= Bar_Second){
			iMyMoneyPriceForBarSecond += 1;
			converted_money -= Bar_Second;
		}

		while (converted_money >= Bar_First){
			iMyMoneyPriceForBarFirst += 1;
			converted_money -= Bar_First;
		}

		// Check arg money qualification
		if (iMyMoneyPriceForBarFirst > iMyFirstBar){
			ch->ChatPacket(CHAT_TYPE_INFO, "You are doesn't have enough x10 bar.");
			return;
		}
		if (iMyMoneyPriceForBarSecond > iMySecondBar){
			ch->ChatPacket(CHAT_TYPE_INFO, "You are doesn't have enough x100 bar.");
			return;
		}
		if (iMyMoneyPriceForBarThird > iMyThirdBar){
			ch->ChatPacket(CHAT_TYPE_INFO, "You are doesn't have enough x1000 bar.");
			return;
		}

		// bind bar amounts to new total money veriable
		int64_t iAddedNewMoney = 0;
		iAddedNewMoney += iMyMoneyPriceForBarFirst * Bar_First;
		iAddedNewMoney += iMyMoneyPriceForBarSecond * Bar_Second;
		iAddedNewMoney += iMyMoneyPriceForBarThird * Bar_Third;

		// Overflow check
		const int64_t nTotalGold = static_cast<int64_t>(ch->GetGold()) + static_cast<int64_t>(iAddedNewMoney);

		if (nTotalGold > GOLD_MAX){
			ch->ChatPacket(CHAT_TYPE_INFO, "Yang overflow !");
			return;
		}

		// New bar count
		int iNewBarFirst = iMyFirstBar - iMyMoneyPriceForBarFirst;
		int iNewBarSecond = iMySecondBar - iMyMoneyPriceForBarSecond;
		int iNewBarThird = iMyThirdBar - iMyMoneyPriceForBarThird;

		if (test_server){
			ch->ChatPacket(CHAT_TYPE_INFO, "New bars; First: %d Second : %d Third : %d", iNewBarFirst, iNewBarSecond, iNewBarThird);
			ch->ChatPacket(CHAT_TYPE_INFO, "New gold: %lld", nTotalGold);
		}

		std::auto_ptr<SQLMsg> new_bar_msg(DBManager::instance().DirectQuery("UPDATE player.player SET bank_bar_first = %d, bank_bar_second = %d, bank_bar_third = %d WHERE name = '%s'", iNewBarFirst, iNewBarSecond, iNewBarThird, ch->GetName()));
		if (new_bar_msg->uiSQLErrno != 0) {
			sys_err("New Bar Query Failed, Error code: %ld", new_bar_msg->uiSQLErrno);
			return;
		}
		ch->PointChange(POINT_GOLD, iAddedNewMoney);

		ch->SetQuestFlag("ingame_bank.flood_check", get_global_time()); //Set flood check time

		//Info
		ch->ChatPacket(CHAT_TYPE_INFO, "You are get %lld gold", iAddedNewMoney);
		ch->ChatPacket(CHAT_TYPE_COMMAND, "RecvBarCount %d %d %d", iNewBarFirst, iNewBarSecond, iNewBarThird);

		// Log
		if (iMyMoneyPriceForBarFirst)
			LogManager::instance().QuestRewardLog("BAR_TO_GOLD_FIRST", ch->GetPlayerID(), ch->GetLevel(), iMyMoneyPriceForBarFirst, 0);
		if (iMyMoneyPriceForBarSecond)
			LogManager::instance().QuestRewardLog("BAR_TO_GOLD_SECOND", ch->GetPlayerID(), ch->GetLevel(), iMyMoneyPriceForBarSecond, 0);
		if (iMyMoneyPriceForBarThird)
			LogManager::instance().QuestRewardLog("BAR_TO_GOLD_THIRD", ch->GetPlayerID(), ch->GetLevel(), iMyMoneyPriceForBarThird, 0);

		LogManager::instance().QuestRewardLog("GOLD_TO_BAR_WIN_GOLD", ch->GetPlayerID(), ch->GetLevel(), iAddedNewMoney, 0);
	}
}
