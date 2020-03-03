// 1) Search:
void initshop()
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
PyObject * shopGetItemTransmutation(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();
	
	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->transmutation);
	
	return Py_BuildValue("i", 0);
}
#endif


// 1) Search:
		{NULL, NULL, NULL},
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		{"GetItemTransmutation", shopGetItemTransmutation, METH_VARARGS},
#endif