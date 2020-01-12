Search:
#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
	PyModule_AddIntConstant(poModule, ENABLE_NEW_EQUIPMENT_SYSTEM,	1);
#else
	PyModule_AddIntConstant(poModule, ENABLE_NEW_EQUIPMENT_SYSTEM,	0);
#endif

Add it under:
#ifdef OFFLINE_MESSAGE
	PyModule_AddIntConstant(poModule, "OFFLINE_MESSAGE", 1);
#else
	PyModule_AddIntConstant(poModule, "OFFLINE_MESSAGE", 0);
#endif
