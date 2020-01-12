Arat ;
#ifdef USE_OPENID
	PyModule_AddIntConstant(poModule, "USE_OPENID",	1);
	if (openid_test)
		PyModule_AddIntConstant(poModule, "OPENID_TEST",	1);
	else
		PyModule_AddIntConstant(poModule, "OPENID_TEST",	0);
#else
	PyModule_AddIntConstant(poModule, "USE_OPENID",	0);
	PyModule_AddIntConstant(poModule, "OPENID_TEST",	0);
#endif /* USE_OPENID */


Altına Ekle ;
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_OFFLINE_SHOP_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_OFFLINE_SHOP_SYSTEM", 0);
#endif