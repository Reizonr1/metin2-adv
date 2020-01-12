//1.) Search:
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif
//2.) Add bellow:
#ifdef ENABLE_TITLE_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_TITLE_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_TITLE_SYSTEM",	0);
#endif
"""""""""""""""""""""""""""""""""""""""""