// 1) Search: #ifdef ENABLE_COSTUME_SYSTEM
// 2) After their end make a new line and paste:
#ifdef ENABLE_NEW_ENCHANT_ATTR
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_ENCHANT_ATTR", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_ENCHANT_ATTR", 0);
#endif