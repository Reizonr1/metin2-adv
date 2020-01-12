Caută:
#include "questmanager.h"
Adaugă sub:
#define ENABLE_BLOCK_SKILL_OXEVENT
Caută:bool CHARACTER::UseSkill(DWORD dwVnum, LPCHARACTER pkVictim, bool bUseGrandMaster)
{
Adaugă sub:
#ifdef ENABLE_OX_SKILL_BLOCK
	DWORD dwFlagBlockSkill = quest::CQuestManager::instance().GetEventFlag("oxta_skill_engelle");

	if (dwFlagBlockSkill > 0)
	{
		if (GetMapIndex() == 113)
		{
			if (quest::CQuestManager::instance().GetEventFlag("oxevent_status") == 2)
			{
				return false;
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT("ox_skill_engel"));
			}
		}
	}
#endif

#ifdef ENABLE_BLOCK_SKILL_OXEVENT
	DWORD szFlagValue = quest::CQuestManager::instance().GetEventFlag("cannot_use_skill_ox");

	if (szFlagValue > 0 && GetMapIndex() == 113 && !IsGM())
	{
		if (quest::CQuestManager::instance().GetEventFlag("oxevent_status") != 0)
		{
			ChatPacket(CHAT_TYPE_NOTICE, LC_TEXT("ox_player_skill_block"));
			return false;
		}
	}
#endif

