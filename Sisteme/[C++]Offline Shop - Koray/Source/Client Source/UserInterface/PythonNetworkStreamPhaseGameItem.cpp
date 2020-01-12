Search:
bool CPythonNetworkStream::SendSafeBoxMoneyPacket(BYTE byState, DWORD dwMoney)
{
	assert(!"CPythonNetworkStream::SendSafeBoxMoneyPacket - Don't use this function");
	return false;

//	TPacketCGSafeboxMoney kSafeboxMoney;
//	kSafeboxMoney.bHeader = HEADER_CG_SAFEBOX_MONEY;
//	kSafeboxMoney.bState = byState;
//	kSafeboxMoney.dwMoney = dwMoney;
//	if (!Send(sizeof(kSafeboxMoney), &kSafeboxMoney))
//		return false;
//
//	return SendSequence();
}

Change:
#ifdef __OFFLINE_SHOP__
bool CPythonNetworkStream::SendSafeBoxMoneyPacket(BYTE byState, uint64_t dwMoney)
#else
bool CPythonNetworkStream::SendSafeBoxMoneyPacket(BYTE byState, long dwMoney)
#endif
{
#ifndef __OFFLINE_SHOP__
	assert(!"CPythonNetworkStream::SendSafeBoxMoneyPacket - disabled");
	return false;
#else
	TPacketCGSafeboxMoney kSafeboxMoney;
	kSafeboxMoney.bHeader = HEADER_CG_SAFEBOX_MONEY;
	kSafeboxMoney.bState = byState;
	kSafeboxMoney.lMoney = dwMoney;
	if (!Send(sizeof(kSafeboxMoney), &kSafeboxMoney))
		return false;

	return SendSequence();
#endif
}

https://puu.sh/sgM7X/8f1c1521ea.png