Search:
	PyModule_AddIntConstant(poModule, "NAMECOLOR_EXTRA", CInstanceBase::NAMECOLOR_EXTRA);

Add it under:
#ifdef __OFFLINE_SHOP__
	PyModule_AddIntConstant(poModule, "NAMECOLOR_OFFSHOP", CInstanceBase::NAMECOLOR_OFFSHOP);
#endif