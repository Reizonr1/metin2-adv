//1.0 suchen:
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif

//1.0 dahinter:
#ifdef ENABLE_VIP_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_VIP_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_VIP_SYSTEM",	0);
#endif