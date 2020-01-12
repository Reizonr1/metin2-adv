// 1) Search: #ifdef ENABLE_COSTUME_SYSTEM
// 2) After their end make a new line and paste:
#ifdef ENABLE_ATTR_TRANSFER_SYSTEM
	PyModule_AddIntConstant(poModule, "ITEM_TYPE_TRANSFER_SCROLL", CItemData::ITEM_TYPE_TRANSFER_SCROLL);
#endif