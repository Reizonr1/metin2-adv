// 1) Search:
			default:
				ret = RecvDefaultPacket(header);
				break;
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
			case HEADER_GC_CL:
				ret = RecvChangeLookPacket();
				break;
#endif


// 1) Search:
				for (int j = 0; j < ITEM_ATTRIBUTE_SLOT_MAX_NUM; ++j)
					CPythonExchange::Instance().SetItemAttributeToSelf(iSlotIndex, j, exchange_packet.aAttr[j].bType, exchange_packet.aAttr[j].sValue);
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
				CPythonExchange::Instance().SetItemTransmutation(iSlotIndex, exchange_packet.dwTransmutation, true);
#endif


// 1) Search:
				for (int j = 0; j < ITEM_ATTRIBUTE_SLOT_MAX_NUM; ++j)
					CPythonExchange::Instance().SetItemAttributeToTarget(iSlotIndex, j, exchange_packet.aAttr[j].bType, exchange_packet.aAttr[j].sValue);
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
				CPythonExchange::Instance().SetItemTransmutation(iSlotIndex, exchange_packet.dwTransmutation, false);
#endif


// 1) Go at the end of file, make a new line and paste (LEAVE A EMPTY NEW LINE AT THE END OF FILE TO DON'T GET WARNING):
#ifdef ENABLE_CHANGELOOK_SYSTEM
bool CPythonNetworkStream::RecvChangeLookPacket()
{
	TPacketChangeLook sPacket;
	if (!Recv(sizeof(sPacket), &sPacket))
		return false;
	
	switch (sPacket.subheader)
	{
		case CL_SUBHEADER_OPEN:
			{
				CPythonChangeLook::Instance().Clear();
				CPythonChangeLook::Instance().SetCost(sPacket.dwCost);
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "ActChangeLook", Py_BuildValue("(i)", 1));
			}
			break;
		case CL_SUBHEADER_CLOSE:
			{
				CPythonChangeLook::Instance().Clear();
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "ActChangeLook", Py_BuildValue("(i)", 2));
			}
			break;
		case CL_SUBHEADER_ADD:
			{
				CPythonChangeLook::Instance().AddMaterial(sPacket.bPos, sPacket.tPos);
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "ActChangeLook", Py_BuildValue("(i)", 3));
				if (sPacket.bPos == 1)
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "AlertChangeLook", Py_BuildValue("()"));
			}
			break;
		case CL_SUBHEADER_REMOVE:
			{
				if (sPacket.bPos == 1)
					CPythonChangeLook::Instance().RemoveMaterial(sPacket.bPos);
				else
					CPythonChangeLook::Instance().RemoveAllMaterials();
				
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "ActChangeLook", Py_BuildValue("(i)", 4));
			}
			break;
		case CL_SUBHEADER_REFINE:
			{
				CPythonChangeLook::Instance().RemoveAllMaterials();
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "ActChangeLook", Py_BuildValue("(i)", 4));
			}
			break;
		default:
			TraceError("CPythonNetworkStream::RecvChangeLookPacket: unknown subheader %d\n.", sPacket.subheader);
			break;
	}
	
	return true;
}

bool CPythonNetworkStream::SendClClosePacket()
{
	if (!__CanActMainInstance())
		return true;
	
	TItemPos tPos;
	tPos.window_type = INVENTORY;
	tPos.cell = 0;
	
	TPacketChangeLook sPacket;
	sPacket.header = HEADER_CG_CL;
	sPacket.subheader = CL_SUBHEADER_CLOSE;
	sPacket.dwCost = 0;
	sPacket.bPos = 0;
	sPacket.tPos = tPos;
	if (!Send(sizeof(sPacket), &sPacket))
		return false;
	
	return SendSequence();
}

bool CPythonNetworkStream::SendClAddPacket(TItemPos tPos, BYTE bPos)
{
	if (!__CanActMainInstance())
		return true;
	
	TPacketChangeLook sPacket;
	sPacket.header = HEADER_CG_CL;
	sPacket.subheader = CL_SUBHEADER_ADD;
	sPacket.dwCost = 0;
	sPacket.bPos = bPos;
	sPacket.tPos = tPos;
	if (!Send(sizeof(sPacket), &sPacket))
		return false;
	
	return SendSequence();
}

bool CPythonNetworkStream::SendClRemovePacket(BYTE bPos)
{
	if (!__CanActMainInstance())
		return true;
	
	TItemPos tPos;
	tPos.window_type = INVENTORY;
	tPos.cell = 0;
	
	TPacketChangeLook sPacket;
	sPacket.header = HEADER_CG_CL;
	sPacket.subheader = CL_SUBHEADER_REMOVE;
	sPacket.dwCost = 0;
	sPacket.bPos = bPos;
	sPacket.tPos = tPos;
	if (!Send(sizeof(sPacket), &sPacket))
		return false;
	
	return SendSequence();
}

bool CPythonNetworkStream::SendClRefinePacket()
{
	if (!__CanActMainInstance())
		return true;
	
	TItemPos tPos;
	tPos.window_type = INVENTORY;
	tPos.cell = 0;
	
	TPacketChangeLook sPacket;
	sPacket.header = HEADER_CG_CL;
	sPacket.subheader = CL_SUBHEADER_REFINE;
	sPacket.dwCost = 0;
	sPacket.bPos = 0;
	sPacket.tPos = tPos;
	if (!Send(sizeof(sPacket), &sPacket))
		return false;
	
	return SendSequence();
}
#endif