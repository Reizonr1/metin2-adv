// 1) Search: bool	m_isMain;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
			int		m_iTitleID;
#endif


// 1) Search: static const D3DXCOLOR& GetIndexedNameColor(UINT eNameColor);
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		static void RegistersTitleName(int iIndex, const char * c_szTitleName);
		static bool RegistersTitleColor(int iIndex, UINT r, UINT g, UINT b);
#endif


// 1) Search: void	BlockMovement();
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		void	SetsTitle(int iTitle);
		int		GetTitleID();
#endif


// 1) Search: struct SMoveAfterFunc
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		int		m_iTitleID;
#endif


// 1) Search: const D3DXCOLOR& GetTitleColor();
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		const D3DXCOLOR& GetsTitleColor(int iTitle);
#endif