// 1) Search: CGraphicTextInstance*			pOwnerTextInstance;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
			CGraphicTextInstance*			psTitleNameTextInstance;
#endif


// 1) Search: void AttachTitle(DWORD dwVID, const char * c_szName, const D3DXCOLOR& c_rColor);
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		void AttachsTitle(DWORD dwVID, const char * c_szName, const D3DXCOLOR& c_rColor);
		void DetachsTitle(DWORD dwVID);
#endif