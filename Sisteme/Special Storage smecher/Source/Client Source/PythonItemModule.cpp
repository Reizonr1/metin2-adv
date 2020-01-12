Cauta ---------------

PyModule_AddIntConstant(poModule, "WEAPON_SWORD", CItemData::WEAPON_SWORD);



ÜSTÜNE EKLENÝR ----------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	PyModule_AddIntConstant(poModule, "SKILL_BOOK_INVENTORY_SLOT_START",	c_Skill_Book_Inventory_Slot_Start);
	PyModule_AddIntConstant(poModule, "UPGRADE_ITEMS_INVENTORY_SLOT_START",	c_Upgrade_Items_Inventory_Slot_Start);
	PyModule_AddIntConstant(poModule, "STONE_INVENTORY_SLOT_START",	c_Stone_Inventory_Slot_Start);
	PyModule_AddIntConstant(poModule, "SANDIK_INVENTORY_SLOT_START",	c_Sandik_Inventory_Slot_Start);
#endif