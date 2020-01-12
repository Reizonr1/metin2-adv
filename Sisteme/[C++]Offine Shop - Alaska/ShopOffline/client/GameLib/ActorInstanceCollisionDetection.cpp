/*find 
BOOL CActorInstance::TestActorCollision(CActorInstance & rVictim)
{
	
and replace with
*/
#include "../UserInterface/Locale_inc.h"
BOOL CActorInstance::TestActorCollision(CActorInstance & rVictim)
{
#ifdef ENABLE_OFFLINE_SHOP
	if (rVictim.GetRace() == 30000)
		return FALSE;
#endif