// 1) Search:
/*
			case HEADER_GC_DRAGON_SOUL_REFINE:
				ret = RecvDragonSoulRefine();
				break;
*/
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
			case HEADER_GG_TITLE_ANSWER:
				ret = RecvTitleInformationPacket();
				break;
#endif


// 1) Search: bool CPythonNetworkStream::RecvRefineInformationPacket()
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
bool CPythonNetworkStream::RecvTitleInformationPacket()
{
	TPacketGGTitleInfo kTitleInfoPacket;
	if (!Recv(sizeof(kTitleInfoPacket), &kTitleInfoPacket))
		return false;
	
	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RecvTitle", Py_BuildValue("(ii)", kTitleInfoPacket.iTitle, kTitleInfoPacket.bAnswer));
#ifdef _DEBUG
	Tracef(">> RecvLanguageInformationPacket: language = %d, answer=%d\n", kTitleInfoPacket.iTitle, kTitleInfoPacket.bAnswer);
#endif
	
	return true;
}
#endif