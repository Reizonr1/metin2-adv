// Search :

	PyModule_AddIntConstant(poModule, "FISH_ALIVE",							CItemData::FISH_ALIVE);

	
// Add below :

#ifdef ENABLE_PENDANT
	PyModule_AddIntConstant(poModule, "EQUIPMENT_PENDANT",					c_Equipment_Pendant);
	PyModule_AddIntConstant(poModule, "ARMOR_PENDANT",						CItemData::ARMOR_PENDANT);
#endif

