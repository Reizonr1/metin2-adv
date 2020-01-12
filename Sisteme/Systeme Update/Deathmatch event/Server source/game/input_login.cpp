Search:
#include "MarkManager.h"

Add it under:
#ifdef DEATHMATCH_MODE
#include "DeathMatch.h"
#endif

---

Search:
	else if (ch->GetMapIndex() == OXEVENT_MAP_INDEX)
	{
		// ox ÀÌº¥Æ® ¸Ê
		if (COXEventManager::instance().Enter(ch) == false)
		{
			// ox ¸Ê ÁøÀÔ Çã°¡°¡ ³ªÁö ¾ÊÀ½. ÇÃ·¹ÀÌ¾î¸é ¸¶À»·Î º¸³»ÀÚ
			if (ch->GetGMLevel() == GM_PLAYER)
				ch->WarpSet(EMPIRE_START_X(ch->GetEmpire()), EMPIRE_START_Y(ch->GetEmpire()));
		}
	}

Add it under:
#ifdef DEATHMATCH_MODE
	else if (ch->GetMapIndex() == DEATMATCH_MAP_INDEX)
	{
		// If disconnected from event send to empire
		if (ch->GetQuestFlag("qDeathMatchPanel.is_disconnected")){
			CDeathMatchManager::instance().ResetScore(ch);
			ch->WarpSet(EMPIRE_START_X(ch->GetEmpire()), EMPIRE_START_Y(ch->GetEmpire()));
		}

		// If player is spectator set observer flag
		if (ch->GetQuestFlag("qDeathMatchPanel.is_observer"))
			ch->SetObserverMode(true);

		// If player login without event is active send to empire
		if (!ch->IsObserverMode()){
			if (CDeathMatchManager::instance().Enter(ch) == false)
			{
				if (ch->GetGMLevel() == GM_PLAYER){
					ch->SetQuestFlag("qDeathMatchPanel.IsInLoginned", 0);
					ch->WarpSet(EMPIRE_START_X(ch->GetEmpire()), EMPIRE_START_Y(ch->GetEmpire()));
				}
			}
		}
	}
#endif

---

Search:
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
#ifdef DEATHMATCH_MODE
	if (ch->GetMapIndex() == DEATMATCH_MAP_INDEX){
		if (ch->GetParty()){
			LPPARTY pParty = ch->GetParty();

			if (pParty->GetMemberCount() == 2) {
				CPartyManager::instance().DeleteParty(pParty);
			}
			else {
				ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("<ÆÄÆ¼> ÆÄÆ¼¿¡¼­ ³ª°¡¼Ì½À´Ï´Ù."));
				pParty->Quit(ch->GetPlayerID());
			}
		}

		if (ch->GetMountVnum()){
			ch->RemoveAffect(AFFECT_MOUNT);
			ch->RemoveAffect(AFFECT_MOUNT_BONUS);
			if (ch->IsHorseRiding())
				ch->StopRiding();
		}

		if(!ch->IsObserverMode())
			CDeathMatchManager::instance().ResetScore(ch);
	}

	if (ch->GetMapIndex() != DEATMATCH_MAP_INDEX){
		if (ch->GetQuestFlag("qDeathMatchPanel.is_disconnected")){
			ch->SetQuestFlag("qDeathMatchPanel.is_disconnected", 0);
		}
	}
#endif

---

