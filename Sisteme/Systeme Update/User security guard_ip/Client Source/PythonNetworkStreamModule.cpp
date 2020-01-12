Search:
PyObject* netSetLoginInfo(PyObject* poSelf, PyObject* poArgs)
{
	char* szName;
	if (!PyTuple_GetString(poArgs, 0, &szName))
		return Py_BuildException();

	char* szPwd;
	if (!PyTuple_GetString(poArgs, 1, &szPwd))
		return Py_BuildException();

	CPythonNetworkStream& rkNetStream=CPythonNetworkStream::Instance();
	CAccountConnector & rkAccountConnector = CAccountConnector::Instance();

	rkNetStream.SetLoginInfo(szName, szPwd);
	rkAccountConnector.SetLoginInfo(szName, szPwd);

	return Py_BuildNone();
}

Change:
PyObject* netSetLoginInfo(PyObject* poSelf, PyObject* poArgs)
{
	char* szName;
	if (!PyTuple_GetString(poArgs, 0, &szName))
		return Py_BuildException();

	char* szPwd;
	if (!PyTuple_GetString(poArgs, 1, &szPwd))
		return Py_BuildException();

#ifdef USER_SECURITY_GUARD
	char* szGuard;
	if (!PyTuple_GetString(poArgs, 2, &szGuard))
		return Py_BuildException();
#endif

	CPythonNetworkStream& rkNetStream=CPythonNetworkStream::Instance();
	CAccountConnector & rkAccountConnector = CAccountConnector::Instance();

#ifdef USER_SECURITY_GUARD
	rkNetStream.SetLoginInfo(szName, szPwd, szGuard);
	rkAccountConnector.SetLoginInfo(szName, szPwd, szGuard);
#else
	rkNetStream.SetLoginInfo(szName, szPwd);
	rkAccountConnector.SetLoginInfo(szName, szPwd);
#endif

	return Py_BuildNone();
}
