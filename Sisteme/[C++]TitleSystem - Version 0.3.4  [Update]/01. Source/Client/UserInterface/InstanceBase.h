// 1) Search: 			short	m_sAlignment;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
			short	m_sPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:		const D3DXCOLOR& GetTitleColor();
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		const D3DXCOLOR& GetTitlePrestigeColor();
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:			short	m_sAlignment;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
			short	m_sPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:		DWORD					m_dwVirtualNumber;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		short					m_sPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:		int						GetAlignmentType();
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		int						GetPrestige();
		UINT					GetPrestigeGrade();
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:		void					SetAlignment(short sAlignment);
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		void					SetPrestige(short sPrestige);
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:		static void RegisterTitleName(int iIndex, const char * c_szTitleName);
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		static void RegisterTitlePrestigeName(int iIndex, const char * c_szTitlePrestigeName);
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	static bool RegisterTitleColor(UINT uIndex, UINT r, UINT g, UINT b);
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		static bool RegisterTitlePrestigeColor(UINT uIndex, UINT r, UINT g, UINT b);
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	EMOTICON_NUM			= 128,
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
			TITLE_NUM_PRESTIGE		= 20,
			TITLE_NONE_PRESTIGE		= 19,
#endif
"""""""""""""""""""""""""""""""""""""""""