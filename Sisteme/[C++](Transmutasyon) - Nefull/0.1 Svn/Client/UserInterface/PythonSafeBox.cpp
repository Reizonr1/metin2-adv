// Search for:
void initsafebox()

// Add Before:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
PyObject * safeboxGetItemLook(PyObject * poSelf, PyObject * poArgs)
{
	int ipos;
	if (!PyTuple_GetInteger(poArgs, 0, &ipos))
		return Py_BadArgument();

	TItemData * pInstance;
	if (!CPythonSafeBox::Instance().GetItemDataPtr(ipos, &pInstance))
		return Py_BuildException();

	return Py_BuildValue("i", pInstance->dwVnum);
}

PyObject * safeboxGetMallItemLook(PyObject * poSelf, PyObject * poArgs)
{
	int ipos;
	if (!PyTuple_GetInteger(poArgs, 0, &ipos))
		return Py_BadArgument();

	TItemData * pInstance;
	if (!CPythonSafeBox::Instance().GetMallItemDataPtr(ipos, &pInstance))
		return Py_BuildException();

	return Py_BuildValue("i", pInstance->dwVnum);
}
#endif

// Search for:
		{ "GetMoney",					safeboxGetMoney,						METH_VARARGS },

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
		{ "GetItemLook",				safeboxGetItemLook,						METH_VARARGS },
		{ "GeMalltItemLook",			safeboxGetMallItemLook,					METH_VARARGS },
#endif
