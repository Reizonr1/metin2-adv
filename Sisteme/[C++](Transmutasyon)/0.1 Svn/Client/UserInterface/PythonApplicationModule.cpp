// Search: #ifdef ENABLE_COSTUME_SYSTEM

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_CHANGE_LOOK_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_CHANGE_LOOK_SYSTEM",	0);
#endif
