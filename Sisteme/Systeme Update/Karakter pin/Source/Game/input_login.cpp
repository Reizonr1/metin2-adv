Find - Bul:
void CInputLogin::CharacterSelect(LPDESC d, const char * data)

Add it upper - Ustune ekle:
void CInputLogin::CharacterPin(LPDESC d, const char* data)
{
	struct command_player_pin * pinfo = (struct command_player_pin *) data;
	const TAccountTable & c_r = d->GetAccountTable();

	if (sizeof(pinfo->character_pin) > 9) {
		sys_err("Pin packet manipulation detected from: %s -> %s", c_r.login, c_r.players[pinfo->index].szName);
		return;
	}

	char gelenPin[16];
	snprintf(gelenPin, 16, "%d", pinfo->character_pin);

	char szQuery[1024 + 1];
	snprintf(szQuery, sizeof(szQuery), "SELECT pin FROM player.player WHERE name = '%s'", c_r.players[pinfo->index].szName);
	SQLMsg * tmpPin_msg = DBManager::instance().DirectQuery(szQuery);
	if (!tmpPin_msg->Get()->uiNumRows) return;
	
	MYSQL_ROW row = mysql_fetch_row(tmpPin_msg->Get()->pSQLResult);
	const char * cRealPin = row[0];

	//sys_err("CHAR: %s PIN: %s DOGRU PIN %s", c_r.players[pinfo->index].szName, gelenPin, cRealPin);
	if (strcmp(cRealPin, gelenPin)){
		sys_log(0, "[%d]%s Yanlis pin denemesi - IP: %s", c_r.players[pinfo->index].dwID, c_r.players[pinfo->index].szName, d->GetHostName()); // wrong pin experiment
		d->SetPhase(PHASE_CLOSE);
	}
	else{
		DBManager::instance().DirectQuery("UPDATE player.player SET pin_kontrol = '%d' WHERE name = '%s'", 1, c_r.players[pinfo->index].szName);
	}
	M2_DELETE(tmpPin_msg);
}


http://puu.sh/jRZwA/c6feccc9d1.png


Find - Bul:
if (g_noticeBattleZone)
{
	if (FN_is_battle_zone(ch))
	{
		ch->ChatPacket(CHAT_TYPE_NOTICE, LC_TEXT("이 맵에선 강제적인 대전이 있을수 도 있습니다."));
		ch->ChatPacket(CHAT_TYPE_NOTICE, LC_TEXT("이 조항에 동의하지 않을시"));
		ch->ChatPacket(CHAT_TYPE_NOTICE, LC_TEXT("본인의 주성 및 부성으로 돌아가시기 바랍니다."));
	}
}

Add it under- Altına ekle:
char szQuery1[1024 + 1];
snprintf(szQuery1, sizeof(szQuery1), "SELECT pin_kontrol FROM player.player WHERE name = '%s'", ch->GetName());
SQLMsg * tmpPinkontrol_msg = DBManager::instance().DirectQuery(szQuery1);

if (tmpPinkontrol_msg->Get()->uiNumRows){
	MYSQL_ROW row = mysql_fetch_row(tmpPinkontrol_msg->Get()->pSQLResult);
	const char * cPinKontrolResult = row[0];
	if (strcmp(cPinKontrolResult, "1")) {
		ch->ChatPacket(CHAT_TYPE_NOTICE, "Illegal giris tespit edildi"); // illegal login detected [ without pin ]
		LogManager::instance().HackLog("PIN_CONFLICT", ch);
		ch->GetDesc()->DelayedDisconnect(3);
	}
	M2_DELETE(tmpPinkontrol_msg);
}


http://puu.sh/jSDKR/537953a959.png


Find - Bul:
case HEADER_CG_CHARACTER_SELECT:
	CharacterSelect(d, c_pData);
	break;

Add it under- Altına ekle:
case HEADER_CG_PLAYER_PIN:
	CharacterPin(d, c_pData);
	break;
	
	
http://puu.sh/jRZLx/48da90306a.png



Find - Bul:
player_create_packet.account_index	= pinfo->index;

Add it under- Altına ekle:
if (sizeof(pinfo->character_pin) > 9) {
	sys_err("Pin packet manipulation detected from: %s", c_rAccountTable.login);
	d->Packet(&packFailure, sizeof(packFailure));
	return;
}
char chPin[9 + 1];
snprintf(chPin, sizeof(chPin), "%d", pinfo->character_pin);

char escpText[10 * 2 + 1];
DBManager::instance().EscapeString(escpText, sizeof(escpText), chPin, strlen(chPin));
strlcpy(player_create_packet.character_pin, escpText, sizeof(escpText));


http://puu.sh/jSOcW/cc47d4a13d.png
