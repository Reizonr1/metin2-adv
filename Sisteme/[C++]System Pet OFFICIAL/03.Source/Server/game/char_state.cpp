//Search in cahr_state.cpp :
//In function: void CHARACTER::__StateIdle_NPC()
//This
	if (IsPet())

//Replace with:

#ifdef NEW_PET_SYSTEM
	if (IsPet() || IsNewPet())
#else
	if (IsPet())
#endif