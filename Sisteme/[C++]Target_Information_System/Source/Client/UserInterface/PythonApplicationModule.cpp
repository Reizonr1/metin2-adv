// Search: #ifdef ENABLE_COSTUME_SYSTEM

// Add (Under):
#ifdef ENABLE_SEND_TARGET_INFO
	PyModule_AddIntConstant(poModule, "ENABLE_SEND_TARGET_INFO",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_SEND_TARGET_INFO",	0);
#endif
