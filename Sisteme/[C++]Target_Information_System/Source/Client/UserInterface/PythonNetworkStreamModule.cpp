// Search for:
PyObject* netConnectToAccountServer(PyObject* poSelf, PyObject* poArgs)

// Add (Under & Whole function):
#ifdef ENABLE_SEND_TARGET_INFO
PyObject* netTargetInfoLoad(PyObject* poSelf, PyObject* poArgs)
{
	DWORD dwVID;

	if (!PyArg_ParseTuple(poArgs, "i", &dwVID))
	{
		return Py_BuildException();
	}
	if (dwVID < 0)
	{
		return Py_BuildNone();
	}

	CPythonNetworkStream& rns = CPythonNetworkStream::Instance();
	rns.SendTargetInfoLoadPacket(dwVID);

	return Py_BuildNone();
}
#endif

// Search for:
		{ "ConnectToAccountServer",				netConnectToAccountServer,				METH_VARARGS },

// Add (Under):
#ifdef ENABLE_SEND_TARGET_INFO
		{ "SendTargetInfoLoad",					netTargetInfoLoad,						METH_VARARGS },
#endif