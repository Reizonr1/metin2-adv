// 1) Search:
void CPythonExchange::GetItemAttributeFromSelf(BYTE pos, int iAttrPos, BYTE * pbyType, short * psValue)
{
	if (pos >= EXCHANGE_ITEM_MAX_NUM)
		return;

	*pbyType = m_self.item_attr[pos][iAttrPos].bType;
	*psValue = m_self.item_attr[pos][iAttrPos].sValue;
}
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
void CPythonExchange::SetItemTransmutation(int iPos, DWORD dwTransmutation, bool bSelf)
{
	if (iPos >= EXCHANGE_ITEM_MAX_NUM)
		return;
	
	if (bSelf)
		m_self.transmutation[iPos] = dwTransmutation;
	else
		m_victim.transmutation[iPos] = dwTransmutation;
}

DWORD CPythonExchange::GetItemTransmutation(int iPos, bool bSelf)
{
	if (iPos >= EXCHANGE_ITEM_MAX_NUM)
		return 0;
	
	DWORD dwTransmutation = bSelf == true ? m_self.transmutation[iPos] : m_victim.transmutation[iPos];
	return dwTransmutation;
}
#endif