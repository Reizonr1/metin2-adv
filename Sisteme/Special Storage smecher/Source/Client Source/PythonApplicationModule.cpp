EN ALTTAK� } �ST�NE EKLEN�R 

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	PyModule_AddIntConstant(poModule, "WJ_SPLIT_INVENTORY_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "WJ_SPLIT_INVENTORY_SYSTEM", 0);
#endif