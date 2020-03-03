// 1) Search:
		DWORD	GetCount();
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
		DWORD	GetTransmutation() const	{return m_dwTransmutation;}
		void	SetTransmutation(DWORD dwVnum, bool bLog = false);
#endif


// 1) Search:
		DWORD		m_dwCount;
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
		DWORD	m_dwTransmutation;
#endif