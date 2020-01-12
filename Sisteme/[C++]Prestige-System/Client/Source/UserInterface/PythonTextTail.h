// Suche : 
void RegisterCharacterTextTail(DWORD dwGuildID, DWORD dwVirtualID, const D3DXCOLOR & c_rColor, float fAddHeight);
// Ersetze das mit :
#if ENABLE_NEW_PRESTIGE_SYSTEM == 1
		void RegisterCharacterTextTail(DWORD dwGuildID, DWORD dwVirtualID, const D3DXCOLOR & c_rColor, float fAddHeight = 10.0f, BYTE bPrestige = 0);
#else
		void RegisterCharacterTextTail(DWORD dwGuildID, DWORD dwVirtualID, const D3DXCOLOR & c_rColor, float fAddHeight = 10.0f);
#endif

// Suche :
void AttachTitle(DWORD dwVID, const char * c_szName, const D3DXCOLOR& c_rColor);
// Ersetze mit :
#if ENABLE_NEW_PRESTIGE_SYSTEM == 3
		void AttachTitle(DWORD dwVID, const char * c_szName, const D3DXCOLOR & c_rColor, BYTE bPrestige = 0);
#else
		void AttachTitle(DWORD dwVID, const char * c_szName, const D3DXCOLOR& c_rColor);
#endif