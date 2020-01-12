/* @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */
// Dosyanýn sonuna eklenir. ( }'den önce )

#ifdef ENABLE_GM_AFFECTS
	PyModule_AddIntConstant(poModule, "ENABLE_GM_AFFECTS", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_GM_AFFECTS", 0);
#endif

/* @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ */