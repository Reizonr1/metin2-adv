//Find
void CPythonNetworkStream::__PlayInventoryItemUseSound(TItemPos uSlotPos)
{
	IAbstractPlayer& rkPlayer=IAbstractPlayer::GetSingleton();
	DWORD dwItemID=rkPlayer.GetItemIndex(uSlotPos);

	CPythonItem& rkItem=CPythonItem::Instance();
	rkItem.PlayUseSound(dwItemID);
}

///Add
#ifdef NEW_ADD_INVENTORY
bool CPythonNetworkStream::Envanter_paketi(/*TItemPos pos*/)
{
	if (!__CanActMainInstance())
		return true;

	TPacketCGEnvanter envanterpaketi;
	envanterpaketi.header = ENVANTER_BLACK;
	// envanterpaketi.pos = pos;

	if (!Send(sizeof(envanterpaketi), &envanterpaketi))
	{
		Tracen("Envanter genisletme bozuk.");
		return false;
	}

	return SendSequence();
}
#endif