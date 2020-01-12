// Search :
#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_EQUIPMENT_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_EQUIPMENT_SYSTEM",	0);
#endif

// Add after :

#ifdef ENABLE_PENDANT
	PyModule_AddIntConstant(poModule, "ENABLE_PENDANT",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_PENDANT",	0);
#endif
