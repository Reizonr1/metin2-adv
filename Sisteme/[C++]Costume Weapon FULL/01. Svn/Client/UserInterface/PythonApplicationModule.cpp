// 1) Search: #ifdef ENABLE_COSTUME_SYSTEM
// 2) After the endif make a new line and paste:
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_WEAPON_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_WEAPON_SYSTEM", 0);
#endif