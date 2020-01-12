// 1) Search: #ifdef ENABLE_COSTUME_SYSTEM
// 2) Before this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_EFFECT_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_EFFECT_SYSTEM", 0);
#endif