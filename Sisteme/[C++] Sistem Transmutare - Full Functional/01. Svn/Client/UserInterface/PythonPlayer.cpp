// 1) Search:
void CPythonPlayer::SetItemCount(TItemPos Cell, BYTE byCount)
{
	if (!Cell.IsValidCell())
		return;

	(const_cast <TItemData *>(GetItemData(Cell)))->count = byCount;
	PyCallClassMemberFunc(m_ppyGameWindow, "RefreshInventory", Py_BuildValue("()"));
}
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
void CPythonPlayer::SetItemTransmutation(TItemPos Cell, DWORD dwVnum)
{
	if (!Cell.IsValidCell())
		return;
	
	(const_cast <TItemData *>(GetItemData(Cell)))->transmutation = dwVnum;
	PyCallClassMemberFunc(m_ppyGameWindow, "RefreshInventory", Py_BuildValue("()"));
}

DWORD CPythonPlayer::GetItemTransmutation(TItemPos Cell)
{
	if (Cell.IsValidCell())
	{
		const TItemData * pkItem = GetItemData(Cell);
		if (pkItem)
			return pkItem->transmutation;
	}
	
	return 0;
}
#endif