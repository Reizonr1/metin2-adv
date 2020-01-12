Search:
PyObject * chrMoveToDestPosition(PyObject* poSelf, PyObject* poArgs)
{
	...
}

Add it under:
#ifdef __OFFLINE_SHOP__
PyObject * chrIsInvisible(PyObject* poSelf, PyObject* poArgs)
{
	int iVID;
	if (!PyTuple_GetInteger(poArgs, 0, &iVID))
		return Py_BadArgument();

	CInstanceBase * pCharacterInstance = CPythonCharacterManager::Instance().GetInstancePtr(iVID);
	if (!pCharacterInstance)
		return Py_BuildNone();

	return Py_BuildValue("i", (int)pCharacterInstance->IsInvisibility());
}
#endif

https://puu.sh/sgLby/07740d5f29.png

---

Search:
		{ "PickAll",					chrPickAll,							METH_VARARGS },

Add it under:
#ifdef __OFFLINE_SHOP__
		{ "IsInvisible",				chrIsInvisible,						METH_VARARGS },
#endif

https://puu.sh/sgLd5/0e8df2fd5a.png
