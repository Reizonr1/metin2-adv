Search:
#include "locale_service.h"

Add it under:
#ifdef DEATHMATCH_MODE
#include "DeathMatch.h"
#endif

---

Search:
	if (pkChr->GetEmpire() != pkVictim->GetEmpire())
	{
		if ( pkChr->GetPKMode() == PK_MODE_PROTECT || pkVictim->GetPKMode() == PK_MODE_PROTECT )
		{
			return false;
		}

		return true;
	}

Add it under:
#ifdef DEATHMATCH_MODE
	if (pkChr->GetMapIndex() == DEATMATCH_MAP_INDEX)
		return true;
#endif
