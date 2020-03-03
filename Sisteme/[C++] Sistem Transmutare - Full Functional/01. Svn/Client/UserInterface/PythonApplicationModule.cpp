// 1) Search:
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_CHANGELOOK_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_CHANGELOOK_SYSTEM", 0);
#endif