// 1) Search: #ifdef ENABLE_COSTUME_SYSTEM
// 2) After their end make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_TITLE_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_TITLE_SYSTEM", 0);
#endif