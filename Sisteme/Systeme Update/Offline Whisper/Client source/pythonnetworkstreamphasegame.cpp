Search:
bool CPythonNetworkStream::SendRefinePacket(BYTE byPos, BYTE byType)
{
	TPacketCGRefine kRefinePacket;
	kRefinePacket.header = HEADER_CG_REFINE;
	kRefinePacket.pos = byPos;
	kRefinePacket.type = byType;

	if (!Send(sizeof(kRefinePacket), &kRefinePacket))
		return false;

	return SendSequence();
}

Add it under:
#ifdef OFFLINE_MESSAGE
bool CPythonNetworkStream::SendOfflineMessagePacket(const char* szTargetName, const char* szText)
{
	TPacketCGOfflineMessage kOfflineMessage;
	kOfflineMessage.bHeader = HEADER_CG_OFFLINE_WHISPER;
	strncpy(kOfflineMessage.szTargetName, szTargetName, sizeof(kOfflineMessage.szTargetName) - 1);
	strncpy(kOfflineMessage.szText, szText, sizeof(kOfflineMessage.szText) - 1);

	if (!Send(sizeof(kOfflineMessage), &kOfflineMessage))
		return false;

	return SendSequence();
}
#endif
