// 1) Search:			void DetachLevel(DWORD dwVID);
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		void AttachPrestige_(DWORD dwVID, const char* c_szName, const D3DXCOLOR& c_rColor);
		void DetachPrestige_(DWORD dwVID);
#endif		

// 1) Search:			CGraphicTextInstance*			pLevelTextInstance;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
			CGraphicTextInstance*			pVegaS_TitleText_tInstance;
#endif	




