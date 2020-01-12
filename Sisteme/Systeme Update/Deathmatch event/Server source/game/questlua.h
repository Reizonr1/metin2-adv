Search:
	extern void RegisterOXEventFunctionTable();

Add it under:
#ifdef DEATHMATCH_MODE
	extern void RegisterDeathMatchFunctionTable();
#endif
