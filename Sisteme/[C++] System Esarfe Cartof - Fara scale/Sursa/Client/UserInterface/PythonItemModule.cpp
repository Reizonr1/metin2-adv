// 1) Search: #ifdef ENABLE_COSTUME_SYSTEM
// 2) Delete from ifdef to endif and paste:
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ITEM_TYPE_COSTUME", CItemData::ITEM_TYPE_COSTUME);
	PyModule_AddIntConstant(poModule, "COSTUME_TYPE_BODY", CItemData::COSTUME_BODY);
	PyModule_AddIntConstant(poModule, "COSTUME_TYPE_HAIR", CItemData::COSTUME_HAIR);
	PyModule_AddIntConstant(poModule, "COSTUME_TYPE_ACCE", CItemData::COSTUME_ACCE);
	PyModule_AddIntConstant(poModule, "COSTUME_SLOT_START", c_Costume_Slot_Start);
	PyModule_AddIntConstant(poModule, "COSTUME_SLOT_COUNT", c_Costume_Slot_Count);
	PyModule_AddIntConstant(poModule, "COSTUME_SLOT_BODY", c_Costume_Slot_Body);
	PyModule_AddIntConstant(poModule, "COSTUME_SLOT_HAIR", c_Costume_Slot_Hair);
	PyModule_AddIntConstant(poModule, "COSTUME_SLOT_ACCE", c_Costume_Slot_Acce);
	PyModule_AddIntConstant(poModule, "COSTUME_SLOT_MOUNT", c_Costume_Slot_Mount);
	PyModule_AddIntConstant(poModule, "COSTUME_SLOT_END", c_Costume_Slot_End);
#endif