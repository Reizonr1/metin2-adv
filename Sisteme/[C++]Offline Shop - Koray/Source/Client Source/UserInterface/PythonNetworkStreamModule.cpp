Search:
PyObject* netSendSafeboxSaveMoneyPacket(PyObject* poSelf, PyObject* poArgs)
{
	int iMoney;
	if (!PyTuple_GetInteger(poArgs, 0, &iMoney))
		return Py_BuildException();

	CPythonNetworkStream& rns=CPythonNetworkStream::Instance();
	rns.SendSafeBoxMoneyPacket(SAFEBOX_MONEY_STATE_SAVE, iMoney);

	return Py_BuildNone();
}

PyObject* netSendSafeboxWithdrawMoneyPacket(PyObject* poSelf, PyObject* poArgs)
{
	int iMoney;
	if (!PyTuple_GetInteger(poArgs, 0, &iMoney))
		return Py_BuildException();

	CPythonNetworkStream& rns=CPythonNetworkStream::Instance();
	rns.SendSafeBoxMoneyPacket(SAFEBOX_MONEY_STATE_WITHDRAW, iMoney);

	return Py_BuildNone();
}

Change:
PyObject* netSendSafeboxSaveMoneyPacket(PyObject* poSelf, PyObject* poArgs)
{
#ifdef __OFFLINE_SHOP__
	uint64_t iMoney;
	if (!PyTuple_GetUnsignedLongLong(poArgs, 0, &iMoney))
		return Py_BuildException();
#else
	int iMoney;
	if (!PyTuple_GetInteger(poArgs, 0, &iMoney))
		return Py_BuildException();
#endif

	CPythonNetworkStream& rns=CPythonNetworkStream::Instance();
	rns.SendSafeBoxMoneyPacket(SAFEBOX_MONEY_STATE_SAVE, iMoney);

	return Py_BuildNone();
}

PyObject* netSendSafeboxWithdrawMoneyPacket(PyObject* poSelf, PyObject* poArgs)
{
#ifdef __OFFLINE_SHOP__
	uint64_t iMoney;
	if (!PyTuple_GetUnsignedLongLong(poArgs, 0, &iMoney))
		return Py_BuildException();
#else
	int iMoney;
	if (!PyTuple_GetInteger(poArgs, 0, &iMoney))
		return Py_BuildException();
#endif

	CPythonNetworkStream& rns=CPythonNetworkStream::Instance();
	rns.SendSafeBoxMoneyPacket(SAFEBOX_MONEY_STATE_WITHDRAW, iMoney);

	return Py_BuildNone();
}

https://puu.sh/sgLt0/3cbb17943b.png

---

Search:
PyObject* netRegisterErrorLog(PyObject* poSelf, PyObject* poArgs)
{
	char * szLog;
	if (!PyTuple_GetString(poArgs, 0, &szLog))
		return Py_BuildException();

	return Py_BuildNone();
}

Add it under:
#ifdef __OFFLINE_SHOP__
PyObject* netSetShopMoveMode(PyObject* poSelf, PyObject* poArgs)
{
	int iType;
	if (!PyTuple_GetInteger(poArgs, 0, &iType))
		return Py_BuildException();

	CPythonNetworkStream& rns = CPythonNetworkStream::Instance();
	rns.SetShopMoveMode(iType);

	return Py_BuildNone();
}
#endif

https://puu.sh/sgLvo/ff519c004c.png

---

Search:
		{ "SendMessengerRemovePacket",			netSendMessengerRemovePacket,			METH_VARARGS },

Add it under:
#ifdef __OFFLINE_SHOP__
		{ "SetShopMoveMode",					netSetShopMoveMode,						METH_VARARGS },
#endif

https://puu.sh/sgLwD/e935e3a6fc.png
