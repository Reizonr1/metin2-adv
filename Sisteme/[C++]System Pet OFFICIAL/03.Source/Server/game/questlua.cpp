//Search in this file:
#ifdef __PET_SYSTEM__
		RegisterPetFunctionTable();
#endif

//Add after:
#ifdef NEW_PET_SYSTEM
		RegisterNewPetFunctionTable();
#endif