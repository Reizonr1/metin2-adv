// 1) Search:		int					GetAlignment() const;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		void				UpdateTitle(int iAmount);
		int					GetTitle() const;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:		void				ShowAlignment(bool bShow);
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		int					GetRealTitle() const;
		void				ShowTitle(bool bShow);
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:		int					m_iRealAlignment;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		int					m_iPrestige;	
		int					m_iRealPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""