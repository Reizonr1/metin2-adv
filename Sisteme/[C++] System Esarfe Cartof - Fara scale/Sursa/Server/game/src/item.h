// 1) Search: long		GetLimitValue(DWORD idx) const { return m_pProto ? m_pProto->aLimits[idx].lValue : 0;	}
// 2) After make a new line and paste:
		BYTE		GetNewAttributeType(int i)	{return m_pProto ? m_pProto->aApplies[i].bType : 0;}
		short		GetNewAttributeValue(int i)	{return m_pProto ? m_pProto->aApplies[i].lValue : 0;}

// 1) Search: int		GetAttributeCount();
// 2) After make a new line and paste:
		int		GetAcceAttributeCount();