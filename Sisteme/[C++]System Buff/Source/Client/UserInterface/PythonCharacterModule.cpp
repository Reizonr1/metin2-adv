//Find:
	PyModule_AddIntConstant(poModule, "NEW_AFFECT_MALL",					CInstanceBase::NEW_AFFECT_MALL);
//Add Below(up to it):
#ifdef ITEM_BUFF_SYSTEM
	PyModule_AddIntConstant(poModule, "AFFECT_RESIST_BUFF",					CInstanceBase::AFFECT_RESIST_BUFF);
	PyModule_AddIntConstant(poModule, "AFFECT_CRITICAL_BUFF",				CInstanceBase::AFFECT_CRITICAL_BUFF);
	PyModule_AddIntConstant(poModule, "AFFECT_REFLECT_BUFF",				CInstanceBase::AFFECT_REFLECT_BUFF);			
#endif