//Search in this file:
	void operator() (LPENTITY ent)
	{
		if ( ent->IsType(ENTITY_CHARACTER) == true )
		{
			LPCHARACTER lpChar = (LPCHARACTER)ent;
			if ( lpChar->IsMonster() == true && !lpChar->IsPet())
				

//Replace with:


	void operator() (LPENTITY ent)
	{
		if ( ent->IsType(ENTITY_CHARACTER) == true )
		{
			LPCHARACTER lpChar = (LPCHARACTER)ent;
#ifdef NEW_PET_SYSTEM
			if (lpChar->IsMonster() == true && !lpChar->IsPet() && !lpChar->IsNewPet())
#else
			if ( lpChar->IsMonster() == true && !lpChar->IsPet())
#endif

//Search in this file
			if ( lpChar->IsNPC() == true && !lpChar->IsPet())

//Replace with:
#ifdef NEW_PET_SYSTEM
			if (lpChar->IsNPC() == true && !lpChar->IsPet() && !lpChar->IsNewPet())
#else
			if ( lpChar->IsNPC() == true && !lpChar->IsPet())
#endif