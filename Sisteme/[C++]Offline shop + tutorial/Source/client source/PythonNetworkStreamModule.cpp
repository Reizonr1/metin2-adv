Arat ;
PyObject* netSendShopSellPacketNew(PyObject* poSelf, PyObject* poArgs)
{
	int iSlotNumber;
	if (!PyTuple_GetInteger(poArgs, 0, &iSlotNumber))
		return Py_BuildException();
	int iCount;
	if (!PyTuple_GetInteger(poArgs, 1, &iCount))
		return Py_BuildException();
	CPythonNetworkStream& rkNetStream=CPythonNetworkStream::Instance();
	rkNetStream.SendShopSellPacketNew(iSlotNumber, iCount);
	return Py_BuildNone();
}

Altına Ekle ;

PyObject* netSendOfflineShopEndPacket(PyObject* poSelf, PyObject* poArgs)
{
	CPythonNetworkStream& rkNetStream = CPythonNetworkStream::Instance();
	rkNetStream.SendOfflineShopEndPacket();
	return Py_BuildNone();
}

PyObject* netSendOfflineShopBuyPacket(PyObject* poSelf, PyObject* poArgs)
{
	int iCount;
	if (!PyTuple_GetInteger(poArgs, 0, &iCount))
		return Py_BuildException();

	CPythonNetworkStream& rkNetStream = CPythonNetworkStream::Instance();
	rkNetStream.SendOfflineShopBuyPacket(iCount);
	return Py_BuildNone();
}

PyObject * netSendChangeOfflineShopTime(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bTime = 0;
	if (!PyTuple_GetByte(poArgs, 0, &bTime))
		return Py_BuildException();

	CPythonNetworkStream & rkNetStream = CPythonNetworkStream::instance();
	rkNetStream.SendChangeOfflineShopTime(bTime);
	return Py_BuildNone();
}

PyObject * netSendChangePriceOfflineShopItem(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bPos;
	int iPrice;

	if (!PyTuple_GetInteger(poArgs, 0, &bPos))
		return Py_BuildException();
	if (!PyTuple_GetInteger(poArgs, 1, &iPrice))
		return Py_BuildException();

	CPythonNetworkStream & rkNetStream = CPythonNetworkStream::instance();
	rkNetStream.SendChangePriceOfflineShopItem(bPos, iPrice);
	return Py_BuildNone();
}

PyObject * netSendRefreshOfflineShop(PyObject * poSelf, PyObject * poArgs)
{
	CPythonNetworkStream & rkNetStream = CPythonNetworkStream::instance();
	rkNetStream.SendRefreshOfflineShop();
	return Py_BuildNone();
}

PyObject * netSendAddOfflineShopItem(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bDisplayPos;
	BYTE bPos;
	int iPrice;

	if (!PyTuple_GetInteger(poArgs, 0, &bDisplayPos))
		return Py_BuildException();
	if (!PyTuple_GetInteger(poArgs, 1, &bPos))
		return Py_BuildException();
	if (!PyTuple_GetInteger(poArgs, 2, &iPrice))
		return Py_BuildException();

	CPythonNetworkStream & rkNetStream = CPythonNetworkStream::instance();
	rkNetStream.SendAddOfflineShopItem(bDisplayPos, bPos, iPrice);
	return Py_BuildNone();
}

PyObject * netSendRemoveOfflineShopItem(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bPos;
	if (!PyTuple_GetInteger(poArgs, 0, &bPos))
		return Py_BuildException();

	CPythonNetworkStream & rkNetStream = CPythonNetworkStream::instance();
	rkNetStream.SendRemoveOfflineShopItem(bPos);
	return Py_BuildNone();
}

PyObject * netSendDestroyOfflineShop(PyObject * poSelf, PyObject * poArgs)
{
	CPythonNetworkStream & rkNetStream = CPythonNetworkStream::instance();
	rkNetStream.SendDestroyOfflineShop();
	return Py_BuildNone();
}

PyObject * netSendRefreshOfflineShopMoney(PyObject * poSelf, PyObject * poArgs)
{
	CPythonNetworkStream & rkNetStream = CPythonNetworkStream::instance();
	rkNetStream.SendRefreshOfflineShopMoney();
	return Py_BuildNone();
}

PyObject * netOfflineShopWithdrawMoney(PyObject * poSelf, PyObject * poArgs)
{
	int iMoney;
	if (!PyTuple_GetInteger(poArgs, 0, &iMoney))
		return Py_BuildException();

	CPythonNetworkStream & rkNetStream = CPythonNetworkStream::instance();
	rkNetStream.SendOfflineShopWithdrawMoney(iMoney);
	return Py_BuildNone();
}





Arat ;
		{ "SendShopSellPacketNew",				netSendShopSellPacketNew,				METH_VARARGS },

Altına Ekle ;
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
		{ "SendOfflineShopEndPacket",			netSendOfflineShopEndPacket,			METH_VARARGS },
		{ "SendOfflineShopBuyPacket",			netSendOfflineShopBuyPacket,			METH_VARARGS },
		{ "SendChangeOfflineShopTime",			netSendChangeOfflineShopTime,			METH_VARARGS },
		{ "SendChangePriceOfflineShopItem",		netSendChangePriceOfflineShopItem,		METH_VARARGS },
		{ "SendAddOfflineShopItem",				netSendAddOfflineShopItem,				METH_VARARGS },
		{ "SendRemoveOfflineShopItem",			netSendRemoveOfflineShopItem,			METH_VARARGS },
		{ "SendDestroyOfflineShop",				netSendDestroyOfflineShop,				METH_VARARGS },
		{ "SendRefreshOfflineShop",				netSendRefreshOfflineShop,				METH_VARARGS },
		{ "SendRefreshOfflineShopMoney",		netSendRefreshOfflineShopMoney,			METH_VARARGS },
		{ "SendOfflineShopWithdrawMoney",		netOfflineShopWithdrawMoney,			METH_VARARGS },
#endif