// Search for:
const DWORD POINT_MAGIC_NUMBER = 0xe73ac1da;

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
void CPythonPlayer::SetItemLook(TItemPos Cell, DWORD dwVnum)
{
	if (!Cell.IsValidCell())
	{
		return;
	}

	(const_cast <TItemData *>(GetItemData(Cell)))->dwVnum = dwVnum;
	PyCallClassMemberFunc(m_ppyGameWindow, "RefreshInventory", Py_BuildValue("()"));
}

DWORD CPythonPlayer::GetItemLook(TItemPos Cell)
{
	if (!Cell.IsValidCell())
	{
		return 0;
	}

	const TItemData * pItem = GetItemData(Cell);

	if (pItem == NULL)
		return 0;
	else
	{
		return pItem->dwVnum;
	}
}
#endif

// Search for:
	m_inGuildAreaID = 0xffffffff;

	m_bMobileFlag = FALSE;

	__ClearAutoAttackTargetActorID();

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	m_ChangeLookRefineActivedSlot[0] = -1;
	m_ChangeLookRefineActivedSlot[1] = -1;
#endif

// Search for:
CPythonPlayer::CPythonPlayer(void)

// Before Paste:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
void CPythonPlayer::SetActivedChangeLookSlot(int ChangeLookSlot, int itemPos)
{
	m_ChangeLookRefineActivedSlot[ChangeLookSlot] = itemPos;
}

int CPythonPlayer::FindActivedChangeLookSlot(int ChangeLookSlot)
{
	
	return m_ChangeLookRefineActivedSlot[ChangeLookSlot];
}

int CPythonPlayer::FindUsingChangeLookSlot(int ChangeLookSlot)
{
	return m_ChangeLookRefineActivedSlot[ChangeLookSlot];
}
#endif

