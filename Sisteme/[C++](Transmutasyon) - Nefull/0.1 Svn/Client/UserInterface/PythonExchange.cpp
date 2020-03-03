// Search for:
DWORD CPythonExchange::GetElkFromSelf()
{
	return m_self.elk;
}

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
DWORD CPythonExchange::GetItemLookVnumFromTarget(BYTE pos)
{
	if (pos >= EXCHANGE_ITEM_MAX_NUM)
		return 0;

	return m_victim.item_look[pos];
}

DWORD CPythonExchange::GetItemLookVnumFromSelf(BYTE pos)
{
	if (pos >= EXCHANGE_ITEM_MAX_NUM)
		return 0;

	return m_self.item_look[pos];
}
#endif

// Search for:
void CPythonExchange::SetItemToTarget(DWORD pos, DWORD vnum, BYTE count)

// Replace their function with:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
void CPythonExchange::SetItemToTarget(DWORD pos, DWORD vnum, BYTE count, DWORD dwLookVnum)
#else
void CPythonExchange::SetItemToTarget(DWORD pos, DWORD vnum, BYTE count)
#endif

// Search for:
	m_victim.item_count[pos] = count;

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	m_victim.item_look[pos] = dwLookVnum;
#endif

// Search for:
void CPythonExchange::SetItemToSelf(DWORD pos, DWORD vnum, BYTE count)

// Replace their function with:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
void CPythonExchange::SetItemToSelf(DWORD pos, DWORD vnum, BYTE count, DWORD dwLookVnum)
#else
void CPythonExchange::SetItemToSelf(DWORD pos, DWORD vnum, BYTE count)
#endif

// Search for:
	m_self.item_count[pos] = count;

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	m_self.item_look[pos] = dwLookVnum;
#endif
