//1.) Search:
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
	PyModule_AddIntConstant(poModule, "ENABLE_FEATURES_OXEVENT", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_FEATURES_OXEVENT", 0);
#endif