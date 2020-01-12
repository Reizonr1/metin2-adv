// 1) Search: PyObject * playerGetAutoPotionInfo(PyObject* poSelf, PyObject* poArgs)
// 2) After their function make a new line and paste:
PyObject * playerSetAcceInfo(PyObject* poSelf, PyObject* poArgs)
{
	CPythonPlayer* player = CPythonPlayer::InstancePtr();
	CPythonPlayer::SAcceInfo& acceInfo = player->GetAcceInfo();
	
	if (!PyTuple_GetBoolean(poArgs, 0, &acceInfo.bActivated))
		return Py_BadArgument();
	
	if (!PyTuple_GetLong(poArgs, 1, &acceInfo.inventorySlotIndex))
		return Py_BadArgument();
	
	return Py_BuildNone();
}

PyObject * playerGetAcceInfo(PyObject* poSelf, PyObject* poArgs)
{
	CPythonPlayer* player = CPythonPlayer::InstancePtr();
	CPythonPlayer::SAcceInfo& acceInfo = player->GetAcceInfo();
	
	return Py_BuildValue("bi", acceInfo.bActivated, int(acceInfo.inventorySlotIndex));
}

// 1) Search: {"SetAutoPotionInfo", playerSetAutoPotionInfo, METH_VARARGS},
// 2) After make a new line and paste:
		{"GetAcceInfo", playerGetAcceInfo, METH_VARARGS},
		{"SetAcceInfo", playerSetAcceInfo, METH_VARARGS},

// 1) Search: PyObject * playerCanDetach(PyObject * poSelf, PyObject * poArgs)
// 2) Delete their function and paste:
PyObject * playerCanDetach(PyObject * poSelf, PyObject * poArgs)
{
	int iScrollItemIndex;
	TItemPos TargetSlotIndex;
	switch (PyTuple_Size (poArgs))
	{
	case 2:
		if (!PyTuple_GetInteger(poArgs, 0, &iScrollItemIndex))
			return Py_BadArgument();
		if (!PyTuple_GetInteger(poArgs, 1, &TargetSlotIndex.cell))
			return Py_BadArgument();
		break;
	case 3:
		if (!PyTuple_GetInteger(poArgs, 0, &iScrollItemIndex))
			return Py_BadArgument();
		if (!PyTuple_GetInteger(poArgs, 1, &TargetSlotIndex.window_type))
			return Py_BadArgument();
		if (!PyTuple_GetInteger(poArgs, 2, &TargetSlotIndex.cell))
			return Py_BadArgument();
		break;
	default:
		return Py_BadArgument();
	}
	
	CItemManager::Instance().SelectItemData(iScrollItemIndex);
	CItemData * pScrollItemData = CItemManager::Instance().GetSelectedItemDataPointer();
	if (!pScrollItemData)
		return Py_BuildException("Can't find item data");
	int iScrollType = pScrollItemData->GetType();
	int iScrollSubType = pScrollItemData->GetSubType();
	if (iScrollType != CItemData::ITEM_TYPE_USE)
		return Py_BuildValue("i", DETACH_METIN_CANT);
	if (iScrollSubType != CItemData::USE_DETACHMENT)
		return Py_BuildValue("i", DETACH_METIN_CANT);
	
	int iTargetItemIndex = CPythonPlayer::Instance().GetItemIndex(TargetSlotIndex);
	CItemManager::Instance().SelectItemData(iTargetItemIndex);
	CItemData * pTargetItemData = CItemManager::Instance().GetSelectedItemDataPointer();
	if (!pTargetItemData)
		return Py_BuildException("Can't find item data");
	
	int iTargetType = pTargetItemData->GetType();
	if (iTargetType == CItemData::ITEM_TYPE_COSTUME)
	{
		const TItemData * pPlayerItem = CPythonPlayer::Instance().GetItemData(TargetSlotIndex);
		CItemData * pItemData = NULL;
		if (pPlayerItem && CItemManager::Instance().GetItemDataPointer(pPlayerItem->vnum, &pItemData))
		{
			for (int iAttrCount = 0; iAttrCount < ITEM_ATTRIBUTE_SLOT_MAX_NUM; ++iAttrCount)
				if (pPlayerItem->aAttr[iAttrCount].bType != 0)
				{
					return Py_BuildValue("i", DETACH_METIN_OK);
				}
		}
	}
	
	if (pTargetItemData->IsFlag(CItemData::ITEM_FLAG_REFINEABLE))
	{
		for (int iSlotCount = 0; iSlotCount < METIN_SOCKET_COUNT; ++iSlotCount)
			if (CPythonPlayer::Instance().GetItemMetinSocket(TargetSlotIndex, iSlotCount) > 2)
			{
				return Py_BuildValue("i", DETACH_METIN_OK);
			}
	}

	return Py_BuildValue("i", DETACH_METIN_CANT);
}