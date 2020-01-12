//find PyObject * poModule = Py_InitModule("chrmgr", s_methods); and add new line
#ifdef ENABLE_OFFLINE_SHOP
	PyModule_AddIntConstant(poModule, "NAMECOLOR_SHOP", CInstanceBase::NAMECOLOR_SHOP);
#endif

