Search:
#include "belt_inventory_helper.h"

Add it under:
#ifdef DEATHMATCH_MODE
#include "Deathmatch.h"
#endif

---

Search:
	unsigned bodyPart = GetPart(PART_MAIN);

Add it under:
#ifdef DEATHMATCH_MODE
	if (GetMapIndex() == DEATMATCH_MAP_INDEX)
		return;
#endif

---

Search:
	if ( CArenaManager::instance().IsLimitedItem( GetMapIndex(), item->GetVnum() ) == true )
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´ë·Ã Áß¿¡´Â ÀÌ¿ëÇÒ ¼ö ¾ø´Â ¹°Ç°ÀÔ´Ï´Ù."));
		return false;
	}

Add it under:
#ifdef DEATHMATCH_MODE
	if (GetMapIndex() == DEATMATCH_MAP_INDEX){
		if (CDeathMatchManager::instance().IsLimitedItem(item->GetVnum()))
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´ë·Ã Áß¿¡´Â ÀÌ¿ëÇÒ ¼ö ¾ø´Â ¹°Ç°ÀÔ´Ï´Ù."));
			return false;
		}
	}
#endif

---

Search:
								if (quest::CQuestManager::instance().GetEventFlag("arena_potion_limit") > 0)
								{
									ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´ë·ÃÀå¿¡¼­ »ç¿ëÇÏ½Ç ¼ö ¾ø½À´Ï´Ù."));
									return false;
								}

Add it under:
#ifdef DEATHMATCH_MODE
								if (GetMapIndex() == DEATMATCH_MAP_INDEX)
									return false;
#endif

---

Search:
											if (CArenaManager::instance().IsArenaMap(pMarriage->ch1->GetMapIndex()) == true)
											{
												ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´ë·Ã Áß¿¡´Â ÀÌ¿ëÇÒ ¼ö ¾ø´Â ¹°Ç°ÀÔ´Ï´Ù."));
												break;
											}

Add it under:
#ifdef DEATHMATCH_MODE
											if (pMarriage->ch1->GetMapIndex() == DEATMATCH_MAP_INDEX)
												return false;
#endif

---

Search:
											if (CArenaManager::instance().IsArenaMap(pMarriage->ch2->GetMapIndex()) == true)
											{
												ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´ë·Ã Áß¿¡´Â ÀÌ¿ëÇÒ ¼ö ¾ø´Â ¹°Ç°ÀÔ´Ï´Ù."));
												break;
											}

Add it under:
#ifdef DEATHMATCH_MODE
											if (pMarriage->ch2->GetMapIndex() == DEATMATCH_MAP_INDEX)
												return false;
#endif

---

Search:
EffectPacket(SE_CHINA_FIREWORK);

Add it upper:
#ifdef DEATHMATCH_MODE
									if (GetMapIndex() == DEATMATCH_MAP_INDEX)
										return false;
#endif

---

Search:
EffectPacket(SE_SPIN_TOP);

Add it upper:
#ifdef DEATHMATCH_MODE
									if (GetMapIndex() == DEATMATCH_MAP_INDEX)
										return false;
#endif

---

Search:
							case FUCKING_BRAZIL_ITEM_AUTO_HP_RECOVERY_S:
								{
									if (CArenaManager::instance().IsArenaMap(GetMapIndex()) == true)
									{
										ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´ë·ÃÀå¿¡¼­ »ç¿ëÇÏ½Ç ¼ö ¾ø½À´Ï´Ù."));
										return false;
									}

Add it under:
#ifdef DEATHMATCH_MODE
									if (GetMapIndex() == DEATMATCH_MAP_INDEX)
										return false;
#endif

---

Search:
								switch (item->GetVnum())
								{
									case 70020 :
									case 71018 :
									case 71019 :

Add it upper:
#ifdef DEATHMATCH_MODE
								if (GetMapIndex() == DEATMATCH_MAP_INDEX)
									return false;
#endif

---

Search:
							// gm_guild_build, oxevent ¸Ê¿¡¼­ ±ÍÈ¯ºÎ ±ÍÈ¯±â¾ïºÎ ¸¦ »ç¿ë¸øÇÏ°Ô ¸·À½
							if (GetMapIndex() == 200 || GetMapIndex() == OXEVENT_MAP_INDEX)
							{
								ChatPacket(CHAT_TYPE_INFO, LC_TEXT("ÇöÀç À§Ä¡¿¡¼­ »ç¿ëÇÒ ¼ö ¾ø½À´Ï´Ù."));
								return false;
							}

Add it under:
#ifdef DEATHMATCH_MODE
							if (GetMapIndex() == DEATMATCH_MAP_INDEX)
							{
								ChatPacket(CHAT_TYPE_INFO, LC_TEXT("´ë·Ã Áß¿¡´Â ÀÌ¿ëÇÒ ¼ö ¾ø´Â ¹°Ç°ÀÔ´Ï´Ù."));
								return false;
							}
#endif

---

Search:
bool CHARACTER::ItemProcess_Polymorph(LPITEM item)
{
	if (IsPolymorphed())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("ÀÌ¹Ì µĞ°©ÁßÀÎ »óÅÂÀÔ´Ï´Ù."));
		return false;
	}

Add it under:
#ifdef DEATHMATCH_MODE
	if (GetMapIndex() == DEATMATCH_MAP_INDEX)
		return false;
#endif

---

Search:
			if (false == CArenaManager::instance().IsArenaMap(GetMapIndex()))
			{
				const long amount_of_used = pItem->GetSocket(idx_of_amount_of_used);
				const long amount_of_full = pItem->GetSocket(idx_of_amount_of_full);

Change:
#ifdef DEATHMATCH_MODE
			if (false == CArenaManager::instance().IsArenaMap(GetMapIndex()) && GetMapIndex() != DEATMATCH_MAP_INDEX)
#else
			if (false == CArenaManager::instance().IsArenaMap(GetMapIndex()))
#endif
			{
				const long amount_of_used = pItem->GetSocket(idx_of_amount_of_used);
				const long amount_of_full = pItem->GetSocket(idx_of_amount_of_full);


---





