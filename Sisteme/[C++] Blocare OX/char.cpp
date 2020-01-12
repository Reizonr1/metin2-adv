Caută:
if (GetGuild())
		GetGuild()->LogoutMember(this);
		
Adaugă sub:
#ifdef ENABLE_OX_INVISIBILITY_SYSTEM
	if (IsAffectFlag(AFF_INVISIBILITY) && GetMapIndex() == 113)
		RemoveAffect(AFFECT_INVISIBILITY);
#endif

Caută:
#include "DragonSoul.h"
Adaugă sub:
#ifdef ENABLE_OX_INVISIBILITY_SYSTEM
#include "OXEvent.h"
#endif