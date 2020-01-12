//1.) Search for:
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif
//2.) Add after:
#ifdef WJ_SHOW_STROKE_INFO
	PyModule_AddIntConstant(poModule, "WJ_SHOW_STROKE_INFO",	1);
#else
	PyModule_AddIntConstant(poModule, "WJ_SHOW_STROKE_INFO",	0);
#endif