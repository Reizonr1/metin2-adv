// Search for:
void initshop()

// Add Before:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
PyObject* shopGetItemLookVnum(PyObject* poSelf, PyObject* poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();

	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->dwLookVnum);

	return Py_BuildValue("i", 0);
}
#endif

// Search for:
		{ "BuildPrivateShop",			shopBuildPrivateShop,			METH_VARARGS },

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
		{ "GetItemLookVnum",			shopGetItemLookVnum,			METH_VARARGS },
#endif
