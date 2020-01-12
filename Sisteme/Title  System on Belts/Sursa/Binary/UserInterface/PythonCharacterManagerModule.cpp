// 1) Search: void initchrmgr()
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
PyObject * chrmgrRegistersTitleName(PyObject* poSelf, PyObject* poArgs)
{
	int	iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BadArgument();
	
	char * szTitleName;
	if (!PyTuple_GetString(poArgs, 1, &szTitleName))
		return Py_BadArgument();
	
	CInstanceBase::RegistersTitleName(iIndex, szTitleName);
	return Py_BuildNone();
}

PyObject * chrmgrRegistersTitleColor(PyObject* poSelf, PyObject* poArgs)
{
	int	iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BadArgument();
	
	int ir;
	if (!PyTuple_GetInteger(poArgs, 1, &ir))
		return Py_BadArgument();
	
	int ig;
	if (!PyTuple_GetInteger(poArgs, 2, &ig))
		return Py_BadArgument();
	
	int ib;
	if (!PyTuple_GetInteger(poArgs, 3, &ib))
		return Py_BadArgument();
	
	CInstanceBase::RegistersTitleColor(iIndex, ir, ig, ib);
	return Py_BuildNone();
}
#endif


// 1) Search: {NULL, NULL, NULL},
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		{"RegistersTitleName", chrmgrRegistersTitleName, METH_VARARGS},
		{"RegistersTitleColor", chrmgrRegistersTitleColor, METH_VARARGS},
#endif