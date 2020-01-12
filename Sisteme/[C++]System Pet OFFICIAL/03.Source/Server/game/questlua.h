//Search in this file:
	extern void RegisterHorseFunctionTable();
	extern void RegisterPetFunctionTable();

//Add after:
#ifdef NEW_PET_SYSTEM
	extern void RegisterNewPetFunctionTable();
#endif