//find CPythonNetworkStream::SendBuildPrivateShopPacket and replace
#ifdef ENABLE_OFFLINE_SHOP
bool CPythonNetworkStream::SendBuildPrivateShopPacket(const char * c_szName, const std::vector<TShopItemTable> & c_rSellingItemStock,DWORD days)
#else
bool CPythonNetworkStream::SendBuildPrivateShopPacket(const char * c_szName, const std::vector<TShopItemTable> & c_rSellingItemStock)
#endif
{
	TPacketCGMyShop packet;
	packet.bHeader = HEADER_CG_MYSHOP;
	strncpy_s(packet.szSign, c_szName, SHOP_SIGN_MAX_LEN);
	packet.bCount = c_rSellingItemStock.size();
	#ifdef ENABLE_OFFLINE_SHOP
	packet.days = days;
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


//find CPythonNetworkStream::RecvShopSignPacket() and replace
bool CPythonNetworkStream::RecvShopSignPacket()
{
	TPacketGCShopSign p;
	if (!Recv(sizeof(TPacketGCShopSign), &p)) return false;

	CPythonPlayer& rkPlayer=CPythonPlayer::Instance();
	
	if (strlen(p.szSign) == 0)
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_PrivateShop_Disappear", Py_BuildValue("(i)", p.dwVID));
		if (rkPlayer.IsMainCharacterIndex(p.dwVID))
			rkPlayer.ClosePrivateShop();
	}
	else
	{
		CInstanceBase * pInstance = CPythonCharacterManager::instance().GetInstancePtr(p.dwVID);
		if (pInstance && (pInstance->IsPC() || pInstance->GetRace() == 30000))
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_PrivateShop_Appear", Py_BuildValue("(is)", p.dwVID, p.szSign));
			if (rkPlayer.IsMainCharacterIndex(p.dwVID))
				rkPlayer.OpenPrivateShop();
		}else
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_PrivateShop_Disappear", Py_BuildValue("(i)", p.dwVID));
	}

	return true;
}
[..]