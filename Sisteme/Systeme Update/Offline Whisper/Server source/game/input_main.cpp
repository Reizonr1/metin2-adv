Search:
void CInputMain::ScriptButton(LPCHARACTER ch, const void* c_pData)
{
	TPacketCGScriptButton * p = (TPacketCGScriptButton *) c_pData;
	sys_log(0, "QUEST ScriptButton pid %d idx %u", ch->GetPlayerID(), p->idx);

	quest::PC* pc = quest::CQuestManager::instance().GetPCForce(ch->GetPlayerID());
	if (pc && pc->IsConfirmWait())
	{
		quest::CQuestManager::instance().Confirm(ch->GetPlayerID(), quest::CONFIRM_TIMEOUT);
	}
	else if (p->idx & 0x80000000)
	{
		//Äù½ºÆ® Ã¢¿¡¼­ Å¬¸¯½Ã(__SelectQuest) ¿©±â·Î
		quest::CQuestManager::Instance().QuestInfo(ch->GetPlayerID(), p->idx & 0x7fffffff);
	}
	else
	{
		quest::CQuestManager::Instance().QuestButton(ch->GetPlayerID(), p->idx);
	}
}

Add it under:
#ifdef OFFLINE_MESSAGE
void CInputMain::OfflineWhisper(LPCHARACTER ch, const char* data)
{
	TPacketCGOfflineMessage * p = (TPacketCGOfflineMessage *)data;

	if (!ch)
		return;

	if (!p->szTargetName){
		ch->ChatPacket(CHAT_TYPE_INFO, "Bad format - 0x01");
		sys_err("Target name not defined in offline message packet. From: %u", ch->GetPlayerID());
		return;
	}

	if (!p->szText){
		ch->ChatPacket(CHAT_TYPE_INFO, "Bad format - 0x02");
		sys_err("Message not defined in offline message packet. From: %u", ch->GetPlayerID());
		return;
	}

	if (strlen(p->szTargetName) < 2){
		ch->ChatPacket(CHAT_TYPE_INFO, "Bad format - 0x03");
		sys_err("Target name too short in offline message packet. From: %u", ch->GetPlayerID());
		return;
	}

	if (strstr(p->szTargetName, "DROP") || strstr(p->szTargetName, "TRUNCATE") || strstr(p->szText, "DROP") || strstr(p->szText, "TRUNCATE")){
		sys_err("HACKER: %s Name: %s Text: %s", ch->GetName(), p->szTargetName, p->szText);
		return;
	}


	int GetLastMsgTime = ch->GetQuestFlag("offline_msg.flood_check");
	if (GetLastMsgTime) {
		if (get_global_time() < GetLastMsgTime + 15 /* limit */) {
			ch->ChatPacket(CHAT_TYPE_INFO, "You can not use too fast");
			return;
		}
	}


	char szEscapedTargetName[CHARACTER_NAME_MAX_LEN * 2 + 1];
	DBManager::instance().EscapeString(szEscapedTargetName, sizeof(szEscapedTargetName), p->szTargetName, strlen(p->szTargetName));

	char szEscapedMessage[CHAT_MAX_LEN * 2 + 1];
	DBManager::instance().EscapeString(szEscapedMessage, sizeof(szEscapedMessage), p->szText, strlen(p->szText));


	LPCHARACTER pTarget = CHARACTER_MANAGER::instance().FindPC(szEscapedTargetName);
	if (pTarget){
		if (pTarget->GetDesc()){
			ch->ChatPacket(CHAT_TYPE_INFO, "Player %s already online", szEscapedTargetName);
			sys_err("Offline message Failed, Player already online. From: %s To: %s", ch->GetName(), szEscapedTargetName);
			return;
		}
	}

	if (!strcmp(szEscapedTargetName, ch->GetName())){
		ch->ChatPacket(CHAT_TYPE_INFO, "You can not send offline message to yourself");
		return;
	}


	std::auto_ptr<SQLMsg> pOwnerQuery(DBManager::instance().DirectQuery("SELECT id FROM player.player WHERE name = '%s'", szEscapedTargetName));

	if (pOwnerQuery->uiSQLErrno != 0) {
		ch->ChatPacket(CHAT_TYPE_INFO, "Offline message doesn't send, unknown error");
		sys_err("Offline message Query Failed, Error code: %ld", pOwnerQuery->uiSQLErrno);
		return;
	}
	if (!pOwnerQuery->Get()->uiNumRows){
		ch->ChatPacket(CHAT_TYPE_INFO, "Target user couldn't found");
		sys_err("Offline message Query Failed, Rows couldn't get. Target user couldn't found");
		return;
	}

	MYSQL_ROW row = mysql_fetch_row(pOwnerQuery->Get()->pSQLResult);
	const char * cTargetPID = row[0];

	DWORD dwTargetPID = 0;
	str_to_number(dwTargetPID, cTargetPID);

	sys_log(0, "Offline message requested, From: [%u]%s To: [%u]%s Msg: %s", ch->GetPlayerID(), ch->GetName(), dwTargetPID, szEscapedTargetName, szEscapedMessage);


	char szOffMsgFormatted[CHAT_MAX_LEN * 2];
	sprintf(szOffMsgFormatted, "%s_%d_%s", ch->GetName(), get_global_time(), szEscapedMessage);


	ch->SaveOfflineMessage(szOffMsgFormatted, dwTargetPID);
	ch->SetQuestFlag("offline_msg.flood_check", get_global_time());

	if (test_server)
		sys_err("Offline message saved. To: %u Msg: %s", dwTargetPID, szOffMsgFormatted);
}
#endif

---

Search:
		case HEADER_CG_SCRIPT_BUTTON:
			ScriptButton(ch, c_pData);
			break;

Add it under:
#ifdef OFFLINE_MESSAGE
		case HEADER_CG_OFFLINE_WHISPER:
			OfflineWhisper(ch, c_pData);
			break;
#endif
