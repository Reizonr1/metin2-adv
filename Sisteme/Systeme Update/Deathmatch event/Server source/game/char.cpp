Search:
#include "OXEvent.h"

Add it under:
#ifdef DEATHMATCH_MODE
#include "Deathmatch.h"
#endif

---

Search:
	pack.sAlignment	= m_iAlignment / 10;
	pack.dwLevel = GetLevel();
	pack.bPKMode	= m_bPKMode;

Add it under:
#ifdef DEATHMATCH_MODE
	if (GetMapIndex() == DEATMATCH_MAP_INDEX){
		if (IsGM())
			m_bPKMode = PK_MODE_PROTECT;
		else
			m_bPKMode = PK_MODE_FREE;
	}
#endif


---

Search:
MessengerManager::instance().Logout(GetName());

Add it under:
#ifdef DEATHMATCH_MODE
	if (GetMapIndex() == DEATMATCH_MAP_INDEX){
		SetQuestFlag("qDeathMatchPanel.is_disconnected", 1); // Set as disconnected
		if (!IsObserverMode())
			CDeathMatchManager::instance().RemoveFromEvent(this); // Remove from attender list

		RemoveBadAffect(); // Remove stun affect
	}
#endif


---

Search:
	else if (pchLeader->GetDungeon())
		return PERR_DUNGEON;

Add it under:
#ifdef DEATHMATCH_MODE
	else if (pchLeader->GetMapIndex() == DEATMATCH_MAP_INDEX)
		return PERR_DUNGEON;
#endif

---

