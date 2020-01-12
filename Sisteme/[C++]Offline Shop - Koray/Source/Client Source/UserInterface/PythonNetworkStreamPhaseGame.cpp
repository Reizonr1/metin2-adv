Search:
		case SHOP_SUBHEADER_GC_START:
			{
				CPythonShop::Instance().Clear();

				DWORD dwVID = *(DWORD *)&vecBuffer[0];

				TPacketGCShopStart * pShopStartPacket = (TPacketGCShopStart *)&vecBuffer[4];
				for (BYTE iItemIndex = 0; iItemIndex < SHOP_HOST_ITEM_MAX_NUM; ++iItemIndex)
				{
					CPythonShop::Instance().SetItemData(iItemIndex, pShopStartPacket->items[iItemIndex]);
				}

				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "StartShop", Py_BuildValue("(i)", dwVID));
			}
			break;

Change:
		case SHOP_SUBHEADER_GC_START:
			{
				CPythonShop::Instance().Clear();

				TPacketGCShopStart* p = (TPacketGCShopStart*)vecBuffer.data();
				for (BYTE iItemIndex = 0; iItemIndex < SHOP_HOST_ITEM_MAX_NUM; ++iItemIndex)
					CPythonShop::Instance().SetItemData(iItemIndex, p->items[iItemIndex]);

#ifdef __OFFLINE_SHOP__
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "StartShop", Py_BuildValue("(iii)", p->vid, p->owner_vid, p->grid_type));
#else
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "StartShop", Py_BuildValue("(i)", p->owner_vid));
#endif
			}
			break;

https://puu.sh/sgLK7/bb5027d1a4.png


---

Search:
		case SHOP_SUBHEADER_GC_START_EX:
			{
				CPythonShop::Instance().Clear();

				TPacketGCShopStartEx * pShopStartPacket = (TPacketGCShopStartEx *)&vecBuffer[0];
				size_t read_point = sizeof(TPacketGCShopStartEx);

				DWORD dwVID = pShopStartPacket->owner_vid;

Change:
		case SHOP_SUBHEADER_GC_START_EX:
			{
				CPythonShop::Instance().Clear();

				TPacketGCShopStartEx * pShopStartPacket = (TPacketGCShopStartEx *)&vecBuffer[0];
				size_t read_point = sizeof(TPacketGCShopStartEx);
#ifndef __OFFLINE_SHOP__
				DWORD dwVID = pShopStartPacket->owner_vid;
#endif

https://puu.sh/sgLNf/562539e387.png

---

Search:
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "StartShop", Py_BuildValue("(i)", dwVID));

Change:
#ifdef __OFFLINE_SHOP__
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "StartShop", Py_BuildValue("(ii)", pShopStartPacket->vid, pShopStartPacket->owner_vid));
#else
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "StartShop", Py_BuildValue("(i)", dwVID));
#endif


https://puu.sh/sgLOf/2386ea27e7.png

---

Search:
		case SHOP_SUBHEADER_GC_UPDATE_ITEM:
			{
				TPacketGCShopUpdateItem * pShopUpdateItemPacket = (TPacketGCShopUpdateItem *)&vecBuffer[0];
				CPythonShop::Instance().SetItemData(pShopUpdateItemPacket->pos, pShopUpdateItemPacket->item);
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshShop", Py_BuildValue("()"));
			}
			break;

Add it under:
#ifdef __OFFLINE_SHOP__
		case SHOP_SUBHEADER_GC_UPDATE_MONEY:
		{
			CPythonShop::Instance().SetMoney(*(INT*)vecBuffer.data());
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshShopMoney", Py_BuildValue("()"));
		}
		break;
#endif

https://puu.sh/sgLPX/792e3e8723.png

---

Search:
		case SHOP_SUBHEADER_GC_SOLDOUT:
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "SOLDOUT"));
			break;

Change:
#ifdef __OFFLINE_SHOP__	
		case SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_COIN:
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "NOT_ENOUGH_MONEY_COIN"));
			break;

		case SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_GOLDBAR:
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "NOT_ENOUGH_MONEY_GOLDBAR"));
			break;

		case SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_WON:
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "NOT_ENOUGH_MONEY_WON"));
			break;
#endif

		case SHOP_SUBHEADER_GC_SOLDOUT:
#ifdef __OFFLINE_SHOP__	
		case SHOP_SUBHEADER_GC_SOLD_OUT:
#endif
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "SOLDOUT"));
			break;

https://puu.sh/sgLSV/d0381fd680.png

---

Search:
bool CPythonNetworkStream::SendBuildPrivateShopPacket(const char * c_szName, const std::vector<TShopItemTable> & c_rSellingItemStock)
{
	TPacketCGMyShop packet;
	packet.bHeader = HEADER_CG_MYSHOP;
	strncpy(packet.szSign, c_szName, SHOP_SIGN_MAX_LEN);
	packet.bCount = c_rSellingItemStock.size();
	if (!Send(sizeof(packet), &packet))
		return false;

	for (std::vector<TShopItemTable>::const_iterator itor = c_rSellingItemStock.begin(); itor < c_rSellingItemStock.end(); ++itor)
	{
		const TShopItemTable & c_rItem = *itor;
		if (!Send(sizeof(c_rItem), &c_rItem))
			return false;
	}

	return SendSequence();
}

Change:

#ifdef __OFFLINE_SHOP__
void CPythonNetworkStream::DisappearShopSign(DWORD dwVID)
{
	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_PrivateShop_Disappear", Py_BuildValue("(i)", dwVID));
}

void CPythonNetworkStream::AppearShopSign(DWORD dwVID, std::string stSign)
{
	if (stSign.empty())
		for (auto it = m_mapShopSign.begin(); it != m_mapShopSign.end(); ++it)
			if (dwVID == it->first)
				stSign = it->second;

	// LogBoxf("AppearShopSign: %u-%s", dwVID, stSign.c_str());
	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_PrivateShop_Appear", Py_BuildValue("(is)", dwVID, stSign.c_str()));
}

bool CPythonNetworkStream::SendBuildPrivateShopPacket(const char * c_szName, BYTE bType, BYTE bSize, BYTE bColor, const std::vector<TShopItemTable> & c_rSellingItemStock)
#else
bool CPythonNetworkStream::SendBuildPrivateShopPacket(const char * c_szName, const std::vector<TShopItemTable> & c_rSellingItemStock)
#endif
{
	TPacketCGMyShop packet;
	packet.bHeader = HEADER_CG_MYSHOP;
	strncpy(packet.szSign, c_szName, SHOP_SIGN_MAX_LEN);
	packet.bCount = c_rSellingItemStock.size();
#ifdef __OFFLINE_SHOP__
	packet.bType = bType;
	packet.bSize = bSize;
	packet.bColor = bColor;
#endif

	if (!Send(sizeof(packet), &packet))
		return false;

	for (std::vector<TShopItemTable>::const_iterator itor = c_rSellingItemStock.begin(); itor < c_rSellingItemStock.end(); ++itor)
	{
		const TShopItemTable & c_rItem = *itor;
		if (!Send(sizeof(c_rItem), &c_rItem))
			return false;
	}

	return SendSequence();
}

https://puu.sh/sgLVu/a746cdc5ff.png
https://puu.sh/sgLVH/c84451ea06.png

---

Search:
bool CPythonNetworkStream::RecvShopSignPacket()
{
	TPacketGCShopSign p;
	if (!Recv(sizeof(TPacketGCShopSign), &p))
		return false;

	CPythonPlayer& rkPlayer=CPythonPlayer::Instance();

	if (0 == strlen(p.szSign))
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME],
			"BINARY_PrivateShop_Disappear",
			Py_BuildValue("(i)", p.dwVID)
		);

		if (rkPlayer.IsMainCharacterIndex(p.dwVID))
			rkPlayer.ClosePrivateShop();
	}
	else
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME],
			"BINARY_PrivateShop_Appear",
			Py_BuildValue("(is)", p.dwVID, p.szSign)
		);

		if (rkPlayer.IsMainCharacterIndex(p.dwVID))
			rkPlayer.OpenPrivateShop();
	}

	return true;
}

Change:
bool CPythonNetworkStream::RecvShopSignPacket()
{
	TPacketGCShopSign p;
	if (!Recv(sizeof(TPacketGCShopSign), &p))
		return false;

	CPythonPlayer& rkPlayer=CPythonPlayer::Instance();

	if (0 == strlen(p.szSign))
	{
#ifdef __OFFLINE_SHOP__
		DisappearShopSign(p.dwVID);
#else
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_PrivateShop_Disappear", Py_BuildValue("(i)", p.dwVID));
#endif

		if (rkPlayer.IsMainCharacterIndex(p.dwVID))
			rkPlayer.ClosePrivateShop();
	}
	else
	{
#ifdef __OFFLINE_SHOP__		
		if (!m_mapShopSign.empty() && m_mapShopSign.find(p.dwVID) != m_mapShopSign.end())
			m_mapShopSign.erase(p.dwVID);
		m_mapShopSign[p.dwVID] = p.szSign;
		AppearShopSign(p.dwVID, p.szSign);
#else
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME],
			"BINARY_PrivateShop_Appear",
			Py_BuildValue("(is)", p.dwVID, p.szSign)
		);
#endif

		if (rkPlayer.IsMainCharacterIndex(p.dwVID))
			rkPlayer.OpenPrivateShop();
	}

	return true;
}

https://puu.sh/sgM26/98fd305cfd.png
https://puu.sh/sgM2r/353817ad69.png








