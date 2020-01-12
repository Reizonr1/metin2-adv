//Search in this file:
bool CActorInstance::IsNPC()
{
	if (TYPE_NPC==m_eActorType)
		return true;

	return false;
}

//Add after:

#define NEW_PET_SYSTEM
#ifdef NEW_PET_SYSTEM
bool CActorInstance::IsNewPet()
{
	if (34041 == m_eRace || 34042 == m_eRace || 34045 == m_eRace || 34046 == m_eRace || 34049 == m_eRace || 34050 == m_eRace || 34053 == m_eRace || 34054 == m_eRace)
		return true;

	return false;
}
#endif