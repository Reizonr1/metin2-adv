Search:
#include <boost/bind.hpp>

Add it under:
#ifdef USER_SECURITY_GUARD
#include "user_security_guard.h"
#endif


---

Search:
		if (!g_bAuthServer)
		{
			TPlayerCountPacket pack;
			pack.dwCount = DESC_MANAGER::instance().GetLocalUserCount();
			db_clientdesc->DBPacket(HEADER_GD_PLAYER_COUNT, 0, &pack, sizeof(TPlayerCountPacket));
		}

Add it upper:
#ifdef USER_SECURITY_GUARD
		if (g_bAuthServer)
			UserSecurityGuard_Log();
#endif
