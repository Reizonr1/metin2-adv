Search:
void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice)
{
	DelPrivateShopItemStock(ItemPos);

	TShopItemTable SellingItem;
	SellingItem.vnum = 0;
	SellingItem.count = 0;
	SellingItem.pos = ItemPos;
	SellingItem.price = dwPrice;
	SellingItem.display_pos = dwDisplayPos;
	m_PrivateShopItemStock.insert(make_pair(ItemPos, SellingItem));
}

Change:
#ifdef __OFFLINE_SHOP__
void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwPrice2, DWORD dwPrice3, DWORD dwPrice4)
#else
void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice)
#endif
{
	DelPrivateShopItemStock(ItemPos);

	TShopItemTable SellingItem;
	SellingItem.vnum = 0;
	SellingItem.count = 0;
	SellingItem.pos = ItemPos;
	SellingItem.price = dwPrice;
#ifdef __OFFLINE_SHOP__
	SellingItem.price2 = dwPrice2;
	SellingItem.price3 = dwPrice3;
	SellingItem.price4 = dwPrice4;
#endif
	SellingItem.display_pos = dwDisplayPos;
	m_PrivateShopItemStock.insert(make_pair(ItemPos, SellingItem));
}

https://puu.sh/sgMwn/062aaed534.png

---

Search:
int CPythonShop::GetPrivateShopItemPrice(TItemPos ItemPos)
{
	...
}

Add it under:
#ifdef __OFFLINE_SHOP__
int CPythonShop::GetPrivateShopItemPrice2(TItemPos ItemPos)
{
	TPrivateShopItemStock::iterator itor = m_PrivateShopItemStock.find(ItemPos);

	if (m_PrivateShopItemStock.end() == itor)
		return 0;

	TShopItemTable & rShopItemTable = itor->second;
	return rShopItemTable.price2;
}
int CPythonShop::GetPrivateShopItemPrice3(TItemPos ItemPos)
{
	TPrivateShopItemStock::iterator itor = m_PrivateShopItemStock.find(ItemPos);

	if (m_PrivateShopItemStock.end() == itor)
		return 0;

	TShopItemTable & rShopItemTable = itor->second;
	return rShopItemTable.price3;
}
int CPythonShop::GetPrivateShopItemPrice4(TItemPos ItemPos)
{
	TPrivateShopItemStock::iterator itor = m_PrivateShopItemStock.find(ItemPos);

	if (m_PrivateShopItemStock.end() == itor)
		return 0;

	TShopItemTable & rShopItemTable = itor->second;
	return rShopItemTable.price4;
}
#endif

https://puu.sh/sgMy3/c88f6f7f9f.png

---

Search:
void CPythonShop::BuildPrivateShop(const char * c_szName)
{
	std::vector<TShopItemTable> ItemStock;
	ItemStock.reserve(m_PrivateShopItemStock.size());

	TPrivateShopItemStock::iterator itor = m_PrivateShopItemStock.begin();
	for (; itor != m_PrivateShopItemStock.end(); ++itor)
	{
		ItemStock.push_back(itor->second);
	}

	std::sort(ItemStock.begin(), ItemStock.end(), ItemStockSortFunc());

	CPythonNetworkStream::Instance().SendBuildPrivateShopPacket(c_szName, ItemStock);
}

Change:
#ifdef __OFFLINE_SHOP__
void CPythonShop::BuildPrivateShop(const char * c_szName, BYTE bType, BYTE bSize, BYTE bColor)
#else
void CPythonShop::BuildPrivateShop(const char * c_szName)
#endif
{
	std::vector<TShopItemTable> ItemStock;
	ItemStock.reserve(m_PrivateShopItemStock.size());

	TPrivateShopItemStock::iterator itor = m_PrivateShopItemStock.begin();
	for (; itor != m_PrivateShopItemStock.end(); ++itor)
	{
		ItemStock.push_back(itor->second);
	}

	std::sort(ItemStock.begin(), ItemStock.end(), ItemStockSortFunc());

#ifdef __OFFLINE_SHOP__
	CPythonNetworkStream::Instance().SendBuildPrivateShopPacket(c_szName, bType, bSize, bColor, ItemStock);
#else
	CPythonNetworkStream::Instance().SendBuildPrivateShopPacket(c_szName, ItemStock);
#endif
}

https://puu.sh/sgMzO/759e553fa7.png

---

Search:
	m_isMainPlayerPrivateShop = FALSE;
	ClearPrivateShopStock();
	m_bTabCount = 1;

Add it under:
#ifdef __OFFLINE_SHOP__
	m_llMoney = 0;
#endif


https://puu.sh/sgMBT/f867f50391.png

---

Search:
PyObject * shopIsMainPlayerPrivateShop(PyObject * poSelf, PyObject * poArgs)
{
	CPythonShop& rkShop=CPythonShop::Instance();
	return Py_BuildValue("i", rkShop.IsMainPlayerPrivateShop());
}

Add it under:
#ifdef __OFFLINE_SHOP__
PyObject * shopGetItemIsSold(PyObject * poSelf, PyObject * poArgs)
{
	int nPos;
	if (!PyTuple_GetInteger(poArgs, 0, &nPos))
		return Py_BuildException();

	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(nPos, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->isSold);

	return Py_BuildValue("i", 0);
}
#endif

https://puu.sh/sgMDt/3a57f9ec01.png

---

Search:
PyObject * shopGetItemPrice(PyObject * poSelf, PyObject * poArgs)
{
	...
}

Add it under:
#ifdef __OFFLINE_SHOP__
PyObject * shopGetItemPrice2(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();

	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->price2);

	return Py_BuildValue("i", 0);
}
PyObject * shopGetItemPrice3(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();

	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->price3);

	return Py_BuildValue("i", 0);
}
PyObject * shopGetItemPrice4(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();

	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->price4);

	return Py_BuildValue("i", 0);
}
#endif

https://puu.sh/sgMFP/c94bf8042b.png

---

Search:
PyObject * shopAddPrivateShopItemStock(PyObject * poSelf, PyObject * poArgs)
{
	...
}

Change:
PyObject * shopAddPrivateShopItemStock(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();
	int iDisplaySlotIndex;
	if (!PyTuple_GetInteger(poArgs, 2, &iDisplaySlotIndex))
		return Py_BuildException();
	int iPrice;
	if (!PyTuple_GetInteger(poArgs, 3, &iPrice))
		return Py_BuildException();
#ifdef __OFFLINE_SHOP__
	int iPrice2;
	if (!PyTuple_GetInteger(poArgs, 4, &iPrice2))
		iPrice2 = 0;
	int iPrice3;
	if (!PyTuple_GetInteger(poArgs, 5, &iPrice3))
		iPrice3 = 0;
	int iPrice4;
	if (!PyTuple_GetInteger(poArgs, 6, &iPrice4))
		iPrice4 = 0;
#endif

#ifdef __OFFLINE_SHOP__
	CPythonShop::Instance().AddPrivateShopItemStock(TItemPos(bItemWindowType, wItemSlotIndex), iDisplaySlotIndex, iPrice, iPrice2, iPrice3, iPrice4);
#else
	CPythonShop::Instance().AddPrivateShopItemStock(TItemPos(bItemWindowType, wItemSlotIndex), iDisplaySlotIndex, iPrice);
#endif
	return Py_BuildNone();
}

https://puu.sh/sgMIf/cb6e83a2f2.png

---

Search:
PyObject * shopGetPrivateShopItemPrice(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();

	int iValue = CPythonShop::Instance().GetPrivateShopItemPrice(TItemPos(bItemWindowType, wItemSlotIndex));
	return Py_BuildValue("i", iValue);
}

Add it under:
#ifdef __OFFLINE_SHOP__
PyObject * shopGetPrivateShopItemPrice2(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();

	int iValue = CPythonShop::Instance().GetPrivateShopItemPrice2(TItemPos(bItemWindowType, wItemSlotIndex));
	return Py_BuildValue("i", iValue);
}
PyObject * shopGetPrivateShopItemPrice3(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();

	int iValue = CPythonShop::Instance().GetPrivateShopItemPrice3(TItemPos(bItemWindowType, wItemSlotIndex));
	return Py_BuildValue("i", iValue);
}
PyObject * shopGetPrivateShopItemPrice4(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();

	int iValue = CPythonShop::Instance().GetPrivateShopItemPrice4(TItemPos(bItemWindowType, wItemSlotIndex));
	return Py_BuildValue("i", iValue);
}
#endif

https://puu.sh/sgMK7/e81b865f7c.png

---

Search:
PyObject * shopBuildPrivateShop(PyObject * poSelf, PyObject * poArgs)
{
	char * szName;
	if (!PyTuple_GetString(poArgs, 0, &szName))
		return Py_BuildException();

	CPythonShop::Instance().BuildPrivateShop(szName);
	return Py_BuildNone();
}

Change:
PyObject * shopBuildPrivateShop(PyObject * poSelf, PyObject * poArgs)
{
	char * szName;
	if (!PyTuple_GetString(poArgs, 0, &szName))
		return Py_BuildException();

#ifdef __OFFLINE_SHOP__
	BYTE bType;
	if (!PyTuple_GetByte(poArgs, 1, &bType))
		return Py_BuildException();

	BYTE bSize;
	if (!PyTuple_GetByte(poArgs, 2, &bSize))
		return Py_BuildException();

	BYTE bColor;
	if (!PyTuple_GetByte(poArgs, 3, &bColor))
		return Py_BuildException();

	CPythonShop::Instance().BuildPrivateShop(szName, bType, bSize, bColor);
#else
	CPythonShop::Instance().BuildPrivateShop(szName);
#endif

	return Py_BuildNone();
}

https://puu.sh/sgMMF/ba2d2cbe74.png

---

Search:
PyObject * shopGetTabCoinType(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bTabIdx;
	if (!PyTuple_GetInteger(poArgs, 0, &bTabIdx))
		return Py_BuildException();

	return Py_BuildValue("i", CPythonShop::instance().GetTabCoinType(bTabIdx));
}

Add it under:
#ifdef __OFFLINE_SHOP__
PyObject * shopGetMoney(PyObject * poSelf, PyObject * poArgs)
{
	return PyLong_FromUnsignedLongLong(CPythonShop::instance().GetMoney());
}
#endif

https://puu.sh/sgMNZ/fe5a362ef8.png

---

Search:
		{ "IsMainPlayerPrivateShop",	shopIsMainPlayerPrivateShop,	METH_VARARGS },

Add it under:
#ifdef __OFFLINE_SHOP__
		{ "GetItemIsSold",				shopGetItemIsSold,				METH_VARARGS },
#endif

Search:
		{ "GetItemPrice",				shopGetItemPrice,				METH_VARARGS },

Add it under:
#ifdef __OFFLINE_SHOP__
		{ "GetItemPrice2",				shopGetItemPrice2,				METH_VARARGS },
		{ "GetItemPrice3",				shopGetItemPrice3,				METH_VARARGS },
		{ "GetItemPrice4",				shopGetItemPrice4,				METH_VARARGS },
#endif

https://puu.sh/sgMRU/8fcd65e617.png

---

Search:
		{ "GetPrivateShopItemPrice",	shopGetPrivateShopItemPrice,	METH_VARARGS },

Add it under:
#ifdef __OFFLINE_SHOP__
		{ "GetPrivateShopItemPrice2",	shopGetPrivateShopItemPrice2,	METH_VARARGS },
		{ "GetPrivateShopItemPrice3",	shopGetPrivateShopItemPrice3,	METH_VARARGS },
		{ "GetPrivateShopItemPrice4",	shopGetPrivateShopItemPrice4,	METH_VARARGS },
#endif

Search:
		{ "BuildPrivateShop",			shopBuildPrivateShop,			METH_VARARGS },

Add it under:
#ifdef __OFFLINE_SHOP__
		{ "GetMoney",					shopGetMoney,					METH_VARARGS },
#endif

https://puu.sh/sgMUX/2fedc6426a.png


