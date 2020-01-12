Search:
PyObject * systemSetShowSalesTextFlag(PyObject * poSelf, PyObject * poArgs)
{
	int iFlag;
	if (!PyTuple_GetInteger(poArgs, 0, &iFlag))
		return Py_BuildException();

	CPythonSystem::Instance().SetShowSalesTextFlag(iFlag);

	return Py_BuildNone();
}

Add it under:
#ifdef __OFFLINE_SHOP__
PyObject * systemSetShowOfflineShop(PyObject * poSelf, PyObject * poArgs)
{
	int iFlag;
	if (!PyTuple_GetInteger(poArgs, 0, &iFlag))
		return Py_BuildException();

	CPythonSystem::Instance().SetShowOfflineShop(iFlag);

	return Py_BuildNone();
}
#endif

https://puu.sh/sgNfk/1d8600c56a.png

---

Search:
PyObject * systemIsShowSalesText(PyObject * poSelf, PyObject * poArgs)
{
	return Py_BuildValue("i", CPythonSystem::Instance().IsShowSalesText());
}

Add it under:
#ifdef __OFFLINE_SHOP__
PyObject * systemIsShowOfflineShop(PyObject * poSelf, PyObject * poArgs)
{
	return Py_BuildValue("i", CPythonSystem::Instance().GetShowOfflineShopFlag());
}
#endif

https://puu.sh/sgNgo/d60831054c.png

---

Search:
		{ "IsShowSalesText",			systemIsShowSalesText,			METH_VARARGS },

Add it under:
#ifdef __OFFLINE_SHOP__
		{ "SetShowOfflineShop",			systemSetShowOfflineShop,		METH_VARARGS },
		{ "IsShowOfflineShop",			systemIsShowOfflineShop,		METH_VARARGS },
#endif

https://puu.sh/sgNhM/d64669b374.png
