// 1) Search:
		char itemlink[256];
// 2) Replace with:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		char itemlink[256 + 12];
#else
		char itemlink[256];
#endif


// 1) Search:
		len = snprintf(itemlink, sizeof(itemlink), "item:%x:%x:%x:%x:%x", pPlayerItem->vnum, pPlayerItem->flags, pPlayerItem->alSockets[0], pPlayerItem->alSockets[1], pPlayerItem->alSockets[2]);
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		len += snprintf(itemlink + len, sizeof(itemlink) - len, ":%x", pPlayerItem->transmutation);
#endif


// 1) Search:
	if (pTargetItemData->IsFlag(CItemData::ITEM_FLAG_REFINEABLE))
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	if (pScrollItemData->GetValue(0) == CL_CLEAN_ATTR_VALUE0)
	{
		const TItemData * pPlayerItem = CPythonPlayer::Instance().GetItemData(TargetSlotIndex);
		if (pPlayerItem)
		{
			if (pPlayerItem->transmutation == 0)
				return Py_BuildValue("i", DETACH_METIN_CANT);
			else
				return Py_BuildValue("i", DETACH_METIN_OK);
		}
		else
			return Py_BuildValue("i", DETACH_METIN_OK);
	}
#endif


// 1) Search:
void initPlayer()
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
PyObject * playerGetItemTransmutation(PyObject* poSelf, PyObject* poArgs)
{
	switch (PyTuple_Size(poArgs))
	{
		case 1:
		{
			int iSlotIndex;
			if (!PyTuple_GetInteger(poArgs, 0, &iSlotIndex))
				return Py_BuildException();
			
			DWORD dwTransmutation = CPythonPlayer::Instance().GetItemTransmutation(TItemPos(INVENTORY, iSlotIndex));
			return Py_BuildValue("i", dwTransmutation);
		}
		case 2:
		{
			TItemPos Cell;
			if (!PyTuple_GetByte(poArgs, 0, &Cell.window_type))
				return Py_BuildException();
			
			if (!PyTuple_GetInteger(poArgs, 1, &Cell.cell))
				return Py_BuildException();
			
			DWORD dwTransmutation = CPythonPlayer::Instance().GetItemTransmutation(Cell);
			return Py_BuildValue("i", dwTransmutation);
		}
		default:
			return Py_BuildException();
	}
}
#endif


// 1) Search:
		{NULL, NULL, NULL},
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		{"GetItemTransmutation", playerGetItemTransmutation, METH_VARARGS},
#endif