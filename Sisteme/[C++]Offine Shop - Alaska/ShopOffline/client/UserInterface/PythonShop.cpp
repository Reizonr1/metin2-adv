[..]
//find function CPythonShop::BuildPrivateShop and replace with this
#ifdef ENABLE_OFFLINE_SHOP
void CPythonShop::BuildPrivateShop(const char * c_szName,DWORD days)
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
	#ifdef ENABLE_OFFLINE_SHOP
	CPythonNetworkStream::Instance().SendBuildPrivateShopPacket(c_szName, ItemStock,days);
	#else
	CPythonNetworkStream::Instance().SendBuildPrivateShopPacket(c_szName, ItemStock);
	#endif
}

//find function AddPrivateShopItemStock and replace
#ifdef ENABLE_FULL_YANG
void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice)
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
	SellingItem.display_pos = dwDisplayPos;
	m_PrivateShopItemStock.insert(make_pair(ItemPos, SellingItem));
}


//find function GetPrivateShopItemPrice and replace
#ifdef ENABLE_FULL_YANG
long long CPythonShop::GetPrivateShopItemPrice(TItemPos ItemPos)
#else
int CPythonShop::GetPrivateShopItemPrice(TItemPos ItemPos)
#endif
{
	TPrivateShopItemStock::iterator itor = m_PrivateShopItemStock.find(ItemPos);

	if (m_PrivateShopItemStock.end() == itor)
		return 0;

	TShopItemTable & rShopItemTable = itor->second;
	return rShopItemTable.price;
}
//find shopBuildPrivateShop and replace
PyObject * shopBuildPrivateShop(PyObject * poSelf, PyObject * poArgs)
{
	char * szName;
	if (!PyTuple_GetString(poArgs, 0, &szName))
		return Py_BuildException();
	#ifdef ENABLE_OFFLINE_SHOP
	int days;
	if (!PyTuple_GetInteger(poArgs, 1, &days))
		return Py_BuildException();
	CPythonShop::Instance().BuildPrivateShop(szName,days);
	#else
	CPythonShop::Instance().BuildPrivateShop(szName);
	#endif
	return Py_BuildNone();
}

PyObject * shopGetItemPrice(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();

	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
#ifdef ENABLE_FULL_YANG
		return Py_BuildValue("L", c_pItemData->price);
#else
		return Py_BuildValue("i", c_pItemData->price);
#endif

	return Py_BuildValue("i", 0);
}
PyObject * shopGetPrivateShopItemPrice(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();
#ifdef ENABLE_FULL_YANG
	return Py_BuildValue("L", CPythonShop::Instance().GetPrivateShopItemPrice(TItemPos(bItemWindowType, wItemSlotIndex)));
#else
	return Py_BuildValue("i", CPythonShop::Instance().GetPrivateShopItemPrice(TItemPos(bItemWindowType, wItemSlotIndex)));
#endif

	return Py_BuildValue("i", 0);
}
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

#ifdef ENABLE_FULL_YANG
	PyObject* val;
	if (!PyTuple_GetObject(poArgs, 3, &val))
		return Py_BuildException();
	long long iPrice = PyLong_AsLongLong(val);
#else
	int iPrice;
	if (!PyTuple_GetInteger(poArgs, 3, &iPrice))
		return Py_BuildException();
#endif

	CPythonShop::Instance().AddPrivateShopItemStock(TItemPos(bItemWindowType, wItemSlotIndex), iDisplaySlotIndex, iPrice);

	return Py_BuildNone();
}
[..]