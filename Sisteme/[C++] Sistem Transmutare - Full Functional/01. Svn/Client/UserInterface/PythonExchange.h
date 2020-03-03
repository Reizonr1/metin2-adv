// 1) Search:
} TExchangeData;
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
			DWORD	transmutation[EXCHANGE_ITEM_MAX_NUM];
#endif


// 1) Search:
		void	GetItemAttributeFromSelf(BYTE pos, int iAttrPos, BYTE * pbyType, short * psValue);
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		void	SetItemTransmutation(int iPos, DWORD dwTransmutation, bool bSelf);
		DWORD	GetItemTransmutation(int iPos, bool bSelf);
#endif