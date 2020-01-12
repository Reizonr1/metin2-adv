// 1) Search: #ifdef ENABLE_COSTUME_SYSTEM
// 2) After the endif make a new line and paste:
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
	PyModule_AddIntConstant(poModule, "COSTUME_TYPE_WEAPON", CItemData::COSTUME_WEAPON);
	PyModule_AddIntConstant(poModule, "COSTUME_SLOT_WEAPON", c_Costume_Slot_Weapon);
#endif