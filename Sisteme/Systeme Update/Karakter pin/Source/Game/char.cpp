Find - Bul:
sys_log(0, "DISCONNECT: %s (%s)", GetName(), c_pszReason ? c_pszReason : "unset" );

Add it under- Altına ekle:
DBManager::instance().DirectQuery("UPDATE player.player SET pin_kontrol = '%d' WHERE name = '%s'", 0, GetName());


http://puu.sh/jRZtB/39e34da9df.png