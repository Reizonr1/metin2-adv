Search:
#include "OXEvent.h"

Add it under:
#ifdef DEATHMATCH_MODE
#include "DeathMatch.h"
#endif

---

Search:
	if (GetMapIndex() == OXEVENT_MAP_INDEX)
		return false;

Add it under:
#ifdef DEATHMATCH_MODE
	if (GetMapIndex() == DEATMATCH_MAP_INDEX)
		return false;
#endif

---

Search:
	if (IS_SET(pkSk->dwFlag, SKILL_FLAG_SELFONLY))
		pkVictim = this;

Add it under:
#ifdef DEATHMATCH_MODE
	if (GetMapIndex() == DEATMATCH_MAP_INDEX){
		if (dwVnum == SKILL_HOSIN || dwVnum == SKILL_REFLECT || dwVnum == SKILL_GICHEON || dwVnum == SKILL_JEONGEOP || dwVnum == SKILL_KWAESOK || dwVnum == SKILL_JEUNGRYEOK)
			pkVictim = this;
	}
#endif

---
