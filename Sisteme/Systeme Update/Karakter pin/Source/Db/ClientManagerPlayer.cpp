Find - Bul:
sys_log(0, "PlayerCreate accountid %d name %s level %d gold %d, st %d ht %d job %d",

Add it upper - Üstüne ekle:
char pinQuery[512];
snprintf(pinQuery, 512, "UPDATE player.player SET pin = '%s' WHERE name = '%s'", packet->character_pin, packet->player_table.name);


http://puu.sh/jSOse/8f1ecc1141.png


Find - Bul:
std::auto_ptr<SQLMsg> pMsg2(CDBManager::instance().DirectQuery(queryStr));
if (g_test_server)
	sys_log(0, "Create_Player queryLen[%d] TEXT[%s]", queryLen, text);
	
Add it under- Altına ekle:
CDBManager::instance().DirectQuery(pinQuery);


http://puu.sh/jSOwA/1af7483229.png