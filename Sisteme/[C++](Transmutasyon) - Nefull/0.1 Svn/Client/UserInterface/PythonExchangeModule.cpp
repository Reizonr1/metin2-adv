// Search for:
void initTrade()

// Add Before:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
PyObject * exchangeGetItemLookVnumFromSelf(PyObject * poTarget, PyObject * poArgs)
{
	int pos;

	if (!PyTuple_GetInteger(poArgs, 0, &pos))
		return Py_BuildException();

	return Py_BuildValue("i", CPythonExchange::Instance().GetItemLookVnumFromSelf((char) pos));
}

PyObject * exchangeGetItemLookVnumFromTarget(PyObject * poTarget, PyObject * poArgs)
{
	int pos;

	if (!PyTuple_GetInteger(poArgs, 0, &pos))
		return Py_BuildException();

	return Py_BuildValue("i", CPythonExchange::Instance().GetItemLookVnumFromTarget((char) pos));
}
#endif

// Search for:
		{"SetElkMode",					exchangeSetElkMode,					METH_VARARGS},

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
		{"GetItemLookVnumFromSelf",			exchangeGetItemLookVnumFromSelf,		METH_VARARGS},
		{"GetItemLookVnumFromTarget",		exchangeGetItemLookVnumFromTarget,		METH_VARARGS},
#endif
