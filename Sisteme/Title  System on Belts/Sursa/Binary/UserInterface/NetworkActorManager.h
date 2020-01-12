// 1) Search: BYTE	m_byPKMode;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	int		m_iTitleID;
#endif


// 1) Search: short m_sAlignment;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	int   m_iTitleID;
#endif


// 1) Search: m_byPKMode=0;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		m_iTitleID = 0;
#endif