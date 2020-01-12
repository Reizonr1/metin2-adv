// search this ::

if (true == SpamBlockCheck(ch, buf, buflen))
	{
		return iExtraLen;
	}
	
	
	
// change like this 
	
	if (true == SpamBlockCheck(ch, buf, buflen))
	{
		return iExtraLen;
	}

[..] // ----

	char chatbuf[CHAT_MAX_LEN + 1];
	int len;
	
#ifdef ENABLE_GLOBAL_CHAT
	len = snprintf(chatbuf, sizeof(chatbuf), "[CH%d][|cFF00FF00Lv. %d|r] %s : %s", g_bChannel, ch->GetLevel(), ch->GetName(), buf);
#else
	len = snprintf(chatbuf, sizeof(chatbuf), "%s : %s", ch->GetName(), buf);
#endif

[..] // ----

	if (CHAT_TYPE_SHOUT == pinfo->type)
	{
		LogManager::instance().ShoutLog(g_bChannel, ch->GetEmpire(), chatbuf);
	}
	
//################################################################################

// search this ::

	if (thecore_heart->pulse - (int) ch->GetLastShoutPulse() < passes_per_sec * 15)
			return (iExtraLen);

		ch->SetLastShoutPulse(thecore_heart->pulse);
		
		
// change like this 
	
	if (thecore_heart->pulse - (int) ch->GetLastShoutPulse() < passes_per_sec * 15)
			return (iExtraLen);

		ch->SetLastShoutPulse(thecore_heart->pulse);

[..] //----
		char chatbuf_global[CHAT_MAX_LEN + 1];

#ifdef ENABLE_GLOBAL_CHAT
		
		const char* kingdoms[3] = {"1     ","2     ","3     "};
		
		if(ch->GetEmpire() > 0 && ch->GetEmpire() == 1 or ch->GetEmpire() == 2 or ch->GetEmpire() == 3 ) 
		{
			int len_global = snprintf(chatbuf_global, sizeof(chatbuf_global), "%s [CH%d][|cFF00FF00Lv. %d|r] %s : %s",kingdoms[ch->GetEmpire()-1], g_bChannel, ch->GetLevel(), ch->GetName(), buf);
		}
		else 
		{
			int len_global = snprintf(chatbuf_global, sizeof(chatbuf_global), "%s : %s",ch->GetName(), buf);
		}

#else

[..] // ----

		TPacketGGShout p;
 
		p.bHeader = HEADER_GG_SHOUT;
		p.bEmpire = ch->GetEmpire();
		strlcpy(p.szText, chatbuf_global, sizeof(p.szText));
 
		P2P_MANAGER::instance().Send(&p, sizeof(TPacketGGShout));
 
		SendShout(chatbuf_global, ch->GetEmpire());

		return (iExtraLen);
	}