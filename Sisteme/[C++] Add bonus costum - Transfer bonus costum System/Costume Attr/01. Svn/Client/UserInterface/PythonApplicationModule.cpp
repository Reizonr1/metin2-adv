// 1) Search: #ifdef ENABLE_COSTUME_SYSTEM
// 2) After their end make a new line and paste:
#ifdef ENABLE_COSTUME_ATTR_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_ATTR_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_ATTR_SYSTEM", 0);
#endif