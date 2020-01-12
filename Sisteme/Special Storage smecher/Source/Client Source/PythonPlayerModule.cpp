Cauta -----------

#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
PyObject * playerIsBeltInventorySlot(PyObject* poSelf, PyObject* poArgs)
{
	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iSlotIndex))
		return Py_BuildException();

	char Flag = CPythonPlayer::Instance().IsBeltInventorySlot(TItemPos(INVENTORY, iSlotIndex));

	return Py_BuildValue("i", Flag);
}
#endif

Adauga sub --------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
PyObject * playerIsSkillBookInventorySlot(PyObject* poSelf, PyObject* poArgs)
{
	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iSlotIndex))
		return Py_BuildException();

	char Flag = CPythonPlayer::Instance().IsSkillBookInventorySlot(TItemPos(INVENTORY, iSlotIndex));

	return Py_BuildValue("i", Flag);
}

PyObject * playerIsUpgradeItemsInventorySlot(PyObject* poSelf, PyObject* poArgs)
{
	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iSlotIndex))
		return Py_BuildException();

	char Flag = CPythonPlayer::Instance().IsUpgradeItemsInventorySlot(TItemPos(INVENTORY, iSlotIndex));

	return Py_BuildValue("i", Flag);
}

PyObject * playerIsStoneInventorySlot(PyObject* poSelf, PyObject* poArgs)
{
	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iSlotIndex))
		return Py_BuildException();

	char Flag = CPythonPlayer::Instance().IsStoneInventorySlot(TItemPos(INVENTORY, iSlotIndex));

	return Py_BuildValue("i", Flag);
}

PyObject * playerIsSandikInventorySlot(PyObject* poSelf, PyObject* poArgs)
{
	int iSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iSlotIndex))
		return Py_BuildException();

	char Flag = CPythonPlayer::Instance().IsSandikInventorySlot(TItemPos(INVENTORY, iSlotIndex));

	return Py_BuildValue("i", Flag);
}
#endif

Cauta -----------

#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
		{ "IsBeltInventorySlot",			playerIsBeltInventorySlot,			METH_VARARGS },
		{ "IsEquippingBelt",				playerIsEquippingBelt,				METH_VARARGS },
		{ "IsAvailableBeltInventoryCell",	playerIsAvailableBeltInventoryCell,	METH_VARARGS },
#endif

Adauga sub --------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
		{ "IsSkillBookInventorySlot",		playerIsSkillBookInventorySlot,		METH_VARARGS },
		{ "IsUpgradeItemsInventorySlot",	playerIsUpgradeItemsInventorySlot,	METH_VARARGS },
		{ "IsStoneInventorySlot",			playerIsStoneInventorySlot,			METH_VARARGS },
		{ "IsSandikInventorySlot",			playerIsSandikInventorySlot,			METH_VARARGS },
#endif

Cauta -----------

#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
	PyModule_AddIntConstant(poModule, "NEW_EQUIPMENT_SLOT_START",	c_New_Equipment_Start);
	PyModule_AddIntConstant(poModule, "NEW_EQUIPMENT_SLOT_COUNT",	c_New_Equipment_Count);
#endif

Adauga sub --------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	PyModule_AddIntConstant(poModule, "SKILL_BOOK_INVENTORY_SLOT_COUNT",	c_Skill_Book_Inventory_Slot_Count);
	PyModule_AddIntConstant(poModule, "UPGRADE_ITEMS_INVENTORY_SLOT_COUNT",	c_Upgrade_Items_Inventory_Slot_Count);
	PyModule_AddIntConstant(poModule, "STONE_INVENTORY_SLOT_COUNT",	c_Stone_Inventory_Slot_Count);
	PyModule_AddIntConstant(poModule, "SANDIK_INVENTORY_SLOT_COUNT",	c_Stone_Inventory_Slot_Count);
#endif

Cauta -----------

PyModule_AddIntConstant(poModule, "SLOT_TYPE_DRAGON_SOUL_INVENTORY",	SLOT_TYPE_DRAGON_SOUL_INVENTORY);

Adauga sub --------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	PyModule_AddIntConstant(poModule, "SLOT_TYPE_SKILL_BOOK_INVENTORY",		SLOT_TYPE_SKILL_BOOK_INVENTORY);
	PyModule_AddIntConstant(poModule, "SLOT_TYPE_UPGRADE_ITEMS_INVENTORY",	SLOT_TYPE_UPGRADE_ITEMS_INVENTORY);
	PyModule_AddIntConstant(poModule, "SLOT_TYPE_STONE_INVENTORY",			SLOT_TYPE_STONE_INVENTORY);
	PyModule_AddIntConstant(poModule, "SLOT_TYPE_SANDIK_INVENTORY",			SLOT_TYPE_SANDIK_INVENTORY);
#endif