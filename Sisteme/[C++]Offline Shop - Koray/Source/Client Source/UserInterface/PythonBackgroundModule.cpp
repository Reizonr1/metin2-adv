Search:
PyObject * backgroundGetCurrentMapName(PyObject * poSelf, PyObject * poArgs)
{
	CPythonBackground& rkBG=CPythonBackground::Instance();
	return Py_BuildValue("s", rkBG.GetWarpMapName());
}

Add it under:
#ifdef __OFFLINE_SHOP__
PyObject * backgroundGetMapName(PyObject * poSelf, PyObject * poArgs)
{
	DWORD dwX;
	if (!PyTuple_GetUnsignedLong(poArgs, 0, &dwX))
		return Py_BadArgument();

	DWORD dwY;
	if (!PyTuple_GetUnsignedLong(poArgs, 1, &dwY))
		return Py_BadArgument();

	CPythonBackground& rkBG = CPythonBackground::Instance();
	std::string szMapName = rkBG.GetMapName(dwX, dwY);
	if (szMapName.empty() || szMapName == "")
		return Py_BuildNone();

	return Py_BuildValue("s", szMapName.c_str());
}
#endif

https://puu.sh/sgL10/a8b5e471a1.png

---

Search:
		{ "GetCurrentMapName",					backgroundGetCurrentMapName,				METH_VARARGS },

Add it under:
#ifdef __OFFLINE_SHOP__
		{ "GetMapName",							backgroundGetMapName,						METH_VARARGS },
#endif

https://puu.sh/sgL2a/72efbb7769.png
