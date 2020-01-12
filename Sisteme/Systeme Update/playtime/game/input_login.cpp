*input_login.cpp

Find - Bul:
	if (g_noticeBattleZone)
	{
		if (FN_is_battle_zone(ch))
		{
			ch->ChatPacket(CHAT_TYPE_NOTICE, LC_TEXT("ÀÌ ¸Ê¿¡¼± °­Á¦ÀûÀÎ ´ëÀüÀÌ ÀÖÀ»¼ö µµ ÀÖ½À´Ï´Ù."));
			ch->ChatPacket(CHAT_TYPE_NOTICE, LC_TEXT("ÀÌ Á¶Ç×¿¡ µ¿ÀÇÇÏÁö ¾ÊÀ»½Ã"));
			ch->ChatPacket(CHAT_TYPE_NOTICE, LC_TEXT("º»ÀÎÀÇ ÁÖ¼º ¹× ºÎ¼ºÀ¸·Î µ¹¾Æ°¡½Ã±â ¹Ù¶ø´Ï´Ù."));
		}
	}
	
Add it under- Altına ekle:
ch->InitCharLogonEvent();