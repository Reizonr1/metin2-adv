// Search for:
		len = snprintf(itemlink, sizeof(itemlink), "item:%x:%x:%x:%x:%x",

// Replace their function with:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
		DWORD dwLookVnum = CPythonPlayer::Instance().GetItemLook(TItemPos(INVENTORY, Cell.cell));

		len = snprintf(itemlink, sizeof(itemlink), "item:%x|%d:%x:%x:%x:%x",
#else
		len = snprintf(itemlink, sizeof(itemlink), "item:%x:%x:%x:%x:%x",
#endif

// Search for:
				pPlayerItem->vnum, pPlayerItem->flags,

// Replace their function with:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
				pPlayerItem->vnum, dwLookVnum, pPlayerItem->flags,
#else
				pPlayerItem->vnum, pPlayerItem->flags,
#endif

// Search for:
	PyModule_AddIntConstant(poModule, "GROUND",								GROUND);

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	enum NewTypes
	{
		SHOP = 10,
		TRADE_OWNER = 11,
		TRADE_TARGET = 12,
		GLASS = 13,
	};

	PyModule_AddIntConstant(poModule, "SHOP",								SHOP);
	PyModule_AddIntConstant(poModule, "TRADE_OWNER",						TRADE_OWNER);
	PyModule_AddIntConstant(poModule, "TRADE_TARGET",						TRADE_TARGET);
	PyModule_AddIntConstant(poModule, "GLASS",								GLASS);
#endif

// Search for:
void initPlayer()

// Add before:

#ifdef ENABLE_CHANGE_LOOK_SYSTEM
PyObject * playerSetChangeLookActivedItemSlot(PyObject * poSelf, PyObject * poArgs)
{
	int ChangeLookSlot;
	if (!PyTuple_GetInteger(poArgs, 0, &ChangeLookSlot))
		return Py_BuildException();

	int itemPos;
	if (!PyTuple_GetInteger(poArgs, 1, &itemPos))
		return Py_BuildException();

	CPythonPlayer::Instance().SetActivedChangeLookSlot(ChangeLookSlot, itemPos);
	return Py_BuildNone();
}

PyObject * playerFindActivedChangeLookSlot(PyObject * poSelf, PyObject * poArgs)
{
	int ChangeLookSlot;
	if (!PyTuple_GetInteger(poArgs, 0, &ChangeLookSlot))
		return Py_BuildException();

	return Py_BuildValue("i", CPythonPlayer::Instance().FindActivedChangeLookSlot(ChangeLookSlot));
}

PyObject * playerFindUsingChangeLookSlot(PyObject * poSelf, PyObject * poArgs)
{
	int ChangeLookSlot;
	if (!PyTuple_GetInteger(poArgs, 0, &ChangeLookSlot))
		return Py_BuildException();

	return Py_BuildValue("i", CPythonPlayer::Instance().FindUsingChangeLookSlot(ChangeLookSlot));
}

PyObject * playerGetItemLook(PyObject* poSelf, PyObject* poArgs)
{
	switch (PyTuple_Size(poArgs))
	{
		case 1:
		{
			int iSlotIndex;
			if (!PyTuple_GetInteger(poArgs, 0, &iSlotIndex))
				return Py_BuildException();
			
			DWORD dwVnum = CPythonPlayer::Instance().GetItemLook(TItemPos(INVENTORY, iSlotIndex));
			return Py_BuildValue("i", dwVnum);
		}
		case 2:
		{
			TItemPos Cell;
			if (!PyTuple_GetByte(poArgs, 0, &Cell.window_type))
				return Py_BuildException();
			
			if (!PyTuple_GetInteger(poArgs, 1, &Cell.cell))
				return Py_BuildException();
			
			DWORD dwVnum = CPythonPlayer::Instance().GetItemLook(Cell);
			return Py_BuildValue("i", dwVnum);
		}
		default:
			return Py_BuildException();
	}
}
#endif

// Search for:
		{ "SendDragonSoulRefine",		playerSendDragonSoulRefine,			METH_VARARGS },

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
		{ "SetChangeLookActivedItemSlot",	playerSetChangeLookActivedItemSlot,		METH_VARARGS },
		{ "FindActivedChangeLookSlot",		playerFindActivedChangeLookSlot,		METH_VARARGS },
		{ "FindUsingChangeLookSlot",		playerFindUsingChangeLookSlot,			METH_VARARGS },

		{ "GetItemLook",					playerGetItemLook,						METH_VARARGS },
#endif
