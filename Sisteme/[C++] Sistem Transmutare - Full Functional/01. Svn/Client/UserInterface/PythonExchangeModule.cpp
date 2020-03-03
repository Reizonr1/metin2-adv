// 1) Search:
void initTrade()
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
PyObject * exchangeGetItemTransmutation(PyObject * poTarget, PyObject * poArgs)
{
	int iPos;
	if (!PyTuple_GetInteger(poArgs, 0, &iPos))
		return Py_BuildException();
	
	bool bSelf;
	if (!PyTuple_GetBoolean(poArgs, 1, &bSelf))
		return Py_BadArgument();
	
	return Py_BuildValue("i", CPythonExchange::Instance().GetItemTransmutation(iPos, bSelf));
}
#endif


// 1) Search:
		{NULL, NULL, NULL},
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		{"GetItemTransmutation", exchangeGetItemTransmutation, METH_VARARGS},
#endif