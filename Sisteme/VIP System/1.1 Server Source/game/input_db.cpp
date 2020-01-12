//1.0 suchen:
		char buf[51];
		snprintf(buf, sizeof(buf), "%s %d %d %ld %d", 
				inet_ntoa(ch->GetDesc()->GetAddr().sin_addr), ch->GetGold(), g_bChannel, ch->GetMapIndex(), ch->GetAlignment());
		LogManager::instance().CharLog(ch, 0, "LOGIN", buf);
//1.0 anpassen:
#ifdef ENABLE_VIP_SYSTEM
	char buf[51];
		snprintf(buf, sizeof(buf), "%s %d %d %ld %d %d", 
				inet_ntoa(ch->GetDesc()->GetAddr().sin_addr), ch->GetGold(), g_bChannel, ch->GetMapIndex(), ch->GetAlignment(), ch->GetVip());
		LogManager::instance().CharLog(ch, 0, "LOGIN", buf);	
#else		
	char buf[51];
		snprintf(buf, sizeof(buf), "%s %d %d %ld %d", 
				inet_ntoa(ch->GetDesc()->GetAddr().sin_addr), ch->GetGold(), g_bChannel, ch->GetMapIndex(), ch->GetAlignment());
		LogManager::instance().CharLog(ch, 0, "LOGIN", buf);
#endif		
