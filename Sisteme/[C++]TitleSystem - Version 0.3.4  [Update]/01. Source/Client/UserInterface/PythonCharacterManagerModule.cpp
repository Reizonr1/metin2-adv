// 1) Search:	PyObject * chrmgrRegisterTitleName(PyObject* poSelf, PyObject* poArgs)
// 2) After their function make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
PyObject * chrmgrRegisterTitlePrestigeName(PyObject* poSelf, PyObject* poArgs)
{
	int	iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BadArgument();
	char * szTitlePrestigeName;
	if (!PyTuple_GetString(poArgs, 1, &szTitlePrestigeName))
		return Py_BadArgument();

	CInstanceBase::RegisterTitlePrestigeName(iIndex, szTitlePrestigeName);
	return Py_BuildNone();
}
#endif 
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	PyObject * chrmgrRegisterTitleColor(PyObject* poSelf, PyObject* poArgs)
// 2) After their function make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
PyObject * chrmgrRegisterTitlePrestigeColor(PyObject* poSelf, PyObject* poArgs)
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

	CInstanceBase::RegisterTitlePrestigeColor(iIndex, ir, ig, ib);
	return Py_BuildNone();
}
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:			{ "RegisterTitleName",			chrmgrRegisterTitleName,				METH_VARARGS },
// 2) After their function make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		{ "RegisterTitlePrestigeName",			chrmgrRegisterTitlePrestigeName,				METH_VARARGS },
#endif 
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:			{ "RegisterTitleColor",			chrmgrRegisterTitleColor,				METH_VARARGS },
// 2) After their function make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		{ "RegisterTitlePrestigeColor",			chrmgrRegisterTitlePrestigeColor,				METH_VARARGS },
#endif
"""""""""""""""""""""""""""""""""""""""""