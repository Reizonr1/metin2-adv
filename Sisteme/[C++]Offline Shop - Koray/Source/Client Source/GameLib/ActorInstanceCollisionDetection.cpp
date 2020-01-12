Search:
BOOL CActorInstance::TestActorCollision(CActorInstance & rVictim)
{
/*
	if (m_pkHorse)
	{
		if (m_pkHorse->TestActorCollision(rVictim))
			return TRUE;

		return FALSE;
	}
*/

	if (rVictim.IsDead())
		return FALSE;

Add it under:
#ifdef __OFFLINE_SHOP__
	if (rVictim.GetRace() >= 30005 && rVictim.GetRace() <= 30010)
		return FALSE;
#endif


https://puu.sh/sgK46/5673244d96.png