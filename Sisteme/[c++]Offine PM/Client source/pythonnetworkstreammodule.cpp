Search:
PyObject* netSendWhisperPacket(PyObject* poSelf, PyObject* poArgs)
{
	char* szName;
	char* szLine;

	if (!PyTuple_GetString(poArgs, 0, &szName))
		return Py_BuildException();

	if (!PyTuple_GetString(poArgs, 1, &szLine))
		return Py_BuildException();

	CPythonNetworkStream& rkNetStream=CPythonNetworkStream::Instance();
	rkNetStream.SendWhisperPacket(szName, szLine);
	return Py_BuildNone();
}


Add it under:
#ifdef OFFLINE_MESSAGE
PyObject* netSendOfflineMessagePacket(PyObject* poSelf, PyObject* poArgs)
{
	char* szName;
	char* szMsg;

	if (!PyTuple_GetString(poArgs, 0, &szName))
		return Py_BuildException();

	if (!PyTuple_GetString(poArgs, 1, &szMsg))
		return Py_BuildException();

	CPythonNetworkStream& rkNetStream = CPythonNetworkStream::Instance();
	rkNetStream.SendOfflineMessagePacket(szName, szMsg);
	return Py_BuildNone();
}
#endif

---

Search:
		{ "SendWhisperPacket",					netSendWhisperPacket,					METH_VARARGS },

Add it under:
#ifdef OFFLINE_MESSAGE
		{ "SendOfflineMessagePacket",			netSendOfflineMessagePacket,			METH_VARARGS },
#endif
