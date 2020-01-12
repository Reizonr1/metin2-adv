// 1) Search: #ifdef ENABLE_COSTUME_SYSTEM
// 2) After their end make a new line and paste:
#ifdef ENABLE_VIEW_TARGET_PLAYER_HP
	PyModule_AddIntConstant(poModule, "ENABLE_VIEW_TARGET_PLAYER_HP", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_VIEW_TARGET_PLAYER_HP", 0);
#endif

#ifdef ENABLE_VIEW_TARGET_DECIMAL_HP
	PyModule_AddIntConstant(poModule, "ENABLE_VIEW_TARGET_DECIMAL_HP", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_VIEW_TARGET_DECIMAL_HP", 0);
#endif