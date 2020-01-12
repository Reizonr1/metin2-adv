//SEarch in this file:
bool __IsNPCRace(unsigned race)
{
	if (race > 9000)
		return true;

	return false;
}
//Add after:
#define NEW_PET_SYSTEM
#ifdef NEW_PET_SYSTEM
bool __IsNewPetRace(unsigned race)
{
	if (race >= 34001 && race <= 34060)
		return true;
	
	return false;
}
#endif

//Search in this file:
		if (race >= 30000)
		{

//Add after:
#ifdef NEW_PET_SYSTEM
			if (__IsNewPetRace(race))
				vec_stPathes.push_back("d:/ymir work/npc_pet/");
#endif
