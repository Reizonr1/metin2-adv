Search:
#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_EQUIPMENT_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_EQUIPMENT_SYSTEM",	0);
#endif

Add it under:
#ifdef USER_SECURITY_GUARD
	PyModule_AddIntConstant(poModule, "ENABLE_USER_SECURITY_GUARD", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_USER_SECURITY_GUARD", 0);
#endif
