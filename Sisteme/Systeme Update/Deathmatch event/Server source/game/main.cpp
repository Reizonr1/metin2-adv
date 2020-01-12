Search:
#include <boost/bind.hpp>

Add it under:
#ifdef DEATHMATCH_MODE
#include "DeathMatch.h"
#endif

---

Search:
	CHorseNameManager horsename_manager;

Add it under:
#ifdef DEATHMATCH_MODE
	CDeathMatchManager deathmatch_manager;
#endif

---

Search:
	if (speed_server)
		CSpeedServerManager::instance().Initialize();

Add it under:
#ifdef DEATHMATCH_MODE
	deathmatch_manager.Initialize();
#endif

---

Search:
	sys_log(0, "<shutdown> Destroying COXEventManager...");
	OXEvent_manager.Destroy();

Add it under:
#ifdef DEATHMATCH_MODE
	sys_log(0, "<shutdown> Destroying CDeathMatchManager...");
	deathmatch_manager.Destroy();
#endif

---

