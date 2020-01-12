Search:
#include "skill.h"

Add it under:
#ifdef DEATHMATCH_MODE
#include "Deathmatch.h"
#endif


---

Search:
	if (CArenaManager::instance().IsArenaMap(GetMapIndex()) == true)
	{
		RemoveGoodAffect();
	}

Add it under:
#ifdef DEATHMATCH_MODE
	if (GetMapIndex() == DEATMATCH_MAP_INDEX)
		RemoveGoodAffect();
#endif


---

Search:
	// ¿ëÈ¥¼® ¼ÂÆÃ ·Îµå ¹× ÃÊ±âÈ­
	DragonSoul_Initialize();

Add it under:
#ifdef DEATHMATCH_MODE
	if (GetMapIndex() == DEATMATCH_MAP_INDEX){
		if (!IsAffectFlag(AFF_STUN) && !IsObserverMode() && !IsGM() && CDeathMatchManager::instance().GetStatus() != DEATHMATCH_STARTED)
			AddAffect(AFFECT_STUN, 0, 0, AFF_STUN, INFINITE_AFFECT_DURATION, 0, 0, 0);
	}
	else{
		if (IsAffectFlag(AFF_STUN)){
			CAffect* pStunAffect = FindAffect(AFFECT_STUN);
			if (pStunAffect){
				if (pStunAffect->lDuration > 60 * 365 * 24){
					RemoveAffect(AFFECT_STUN);
				}
			}
		}
	}
#endif
