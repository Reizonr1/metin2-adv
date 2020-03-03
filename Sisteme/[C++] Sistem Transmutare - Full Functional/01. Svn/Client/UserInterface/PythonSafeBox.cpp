// 1) Search:
void initsafebox()
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
PyObject * safeboxGetItemTransmutation(PyObject * poSelf, PyObject * poArgs)
{
	int iPos;
	if (!PyTuple_GetInteger(poArgs, 0, &iPos))
		return Py_BadArgument();
	
	TItemData * pInstance;
	if (!CPythonSafeBox::Instance().GetItemDataPtr(iPos, &pInstance))
		return Py_BuildException();
	
	return Py_BuildValue("i", pInstance->transmutation);
}

PyObject * safeboxGetMallItemTransmutation(PyObject * poSelf, PyObject * poArgs)
{
	int iPos;
	if (!PyTuple_GetInteger(poArgs, 0, &iPos))
		return Py_BadArgument();
	
	TItemData * pInstance;
	if (!CPythonSafeBox::Instance().GetMallItemDataPtr(iPos, &pInstance))
		return Py_BuildException();
	
	return Py_BuildValue("i", pInstance->transmutation);
}
#endif


// 1) Search:
		{NULL, NULL, NULL},
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		{"GetItemTransmutation", safeboxGetItemTransmutation, METH_VARARGS},
		{"GetMallItemTransmutation", safeboxGetMallItemTransmutation, METH_VARARGS},
#endif