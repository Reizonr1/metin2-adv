Arat ;
PyObject * playerSetPlayTime(PyObject* poSelf, PyObject* poArgs)
{
	int iTime;
	if (!PyTuple_GetInteger(poArgs, 0, &iTime))
		return Py_BuildException();

	CPythonPlayer::Instance().SetPlayTime(iTime);
	return Py_BuildNone();
}

Altına Ekle ;
PyObject * playerGetCurrentOfflineShopMoney(PyObject * poSelf, PyObject * poArgs)
{
	return Py_BuildValue("i", CPythonPlayer::Instance().GetCurrentOfflineShopMoney());
}




Arat ;
		{ "SetPlayTime",				playerSetPlayTime,					METH_VARARGS },

Altına Ekle ;
		{ "GetCurrentOfflineShopMoney",	playerGetCurrentOfflineShopMoney,	METH_VARARGS },



Arat ;
PyModule_AddIntConstant(poModule, "ENERGY_END_TIME", POINT_ENERGY_END_TIME);

Altına Ekle ;
PyModule_AddIntConstant(poModule, "SLOT_TYPE_OFFLINE_SHOP", SLOT_TYPE_OFFLINE_SHOP);