Search:
#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_EQUIPMENT_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_EQUIPMENT_SYSTEM",	0);
#endif

Add it under:
#ifdef __OFFLINE_SHOP__
	PyModule_AddIntConstant(poModule, "ENABLE_OFFLINE_SHOP", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_OFFLINE_SHOP", 0);
#endif