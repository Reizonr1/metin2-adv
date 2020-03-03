// 1) Search: PyModule_AddIntConstant(poModule, "ITEM_ANTIFLAG_SAFEBOX", CItemData::ITEM_ANTIFLAG_SAFEBOX);
// 2) After make a new line and paste:
#ifdef ENABLE_NEW_ENCHANT_ATTR
	PyModule_AddIntConstant(poModule, "USE_CHANGE_ATTRIBUTE3", CItemData::USE_CHANGE_ATTRIBUTE3);
#endif