//Find
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_WEAPON_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_WEAPON_SYSTEM", 0);
#endif

///Add
#ifdef NEW_ADD_INVENTORY
	PyModule_AddIntConstant(poModule, "ADD_INVENTORY",	1);
#else
	PyModule_AddIntConstant(poModule, "ADD_INVENTORY",	0);
#endif