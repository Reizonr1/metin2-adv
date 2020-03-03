//Search:
	short m_sAlignment;
	BYTE m_byPKMode;

//Add after:
#ifdef ENABLE_SUPPORT_SYSTEM
	DWORD m_dwLevel;
#endif

//Search:
		m_dwWeapon=0;
		m_dwHair=0;

//Add after:
#ifdef ENABLE_SUPPORT_SYSTEM
		m_dwLevel=0;
#endif