1)Mouse event doesn't appear in character create window use TAB or ENTER key for switch inputs
  Karakter oluşturma ekranında window olmadığı için fare değer girilen barları algılamıyor geçiş yapmak için TAB veya ENTER kullanın

2)input_login.cpp

Not:
If you add this lines and If user doesn't enter any pin kicked from game
Eğer aşağıdaki satırı eklerseniz oyuncu herhangi bir pin girmezse oyundan atılır

Part:
char szQuery1[1024 + 1];
snprintf(szQuery1, sizeof(szQuery1), "SELECT pin_kontrol FROM player.player WHERE name = '%s'", ch->GetName());
SQLMsg * tmpPinkontrol_msg = DBManager::instance().DirectQuery(szQuery1);

if (tmpPinkontrol_msg->Get()->uiNumRows){
	MYSQL_ROW row = mysql_fetch_row(tmpPinkontrol_msg->Get()->pSQLResult);
	const char * cPinKontrolResult = row[0];
	if (strcmp(cPinKontrolResult, "1")) {
		ch->ChatPacket(CHAT_TYPE_NOTICE, "Illegal giris tespit edildi");
		LogManager::instance().HackLog("PIN_CONFLICT", ch);
		ch->GetDesc()->DelayedDisconnect(3);
	}
	M2_DELETE(tmpPinkontrol_msg);
}
