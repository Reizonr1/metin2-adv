// 1) Search: bool CPythonNetworkStream::SendSafeBoxMoneyPacket(BYTE byState, DWORD dwMoney)
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
bool CPythonNetworkStream::SendChangeTitle(int iTitle)
{
	if (!__CanActMainInstance())
		return true;
	
	TPacketGGTitleInfo p;
	p.bHeader = HEADER_CG_TITLE_CHOOSE;
	p.iTitle = iTitle;
	p.bAnswer = 0;
	if (!Send(sizeof(TPacketGGTitleInfo), &p))
	{
		Tracen(">> SendChangeTitle: error.");
		return false;
	}
	
	return SendSequence();
}
#endif