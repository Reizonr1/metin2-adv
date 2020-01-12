// Suche :
			DWORD	m_dwLevel;
// Add :
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
			BYTE	m_byPrestige;
#endif
// Suche :
		DWORD					m_dwLevel;
// Add :
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
			BYTE					m_byPrestige;
#endif

// Unter :
		DWORD					m_dwGuildID;
// Add :
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
	public:
		void SetPrestigeLevel(BYTE Level) { m_byPrestige = Level;  };
		BYTE GetPrestigeLevel() { return m_byPrestige; };
		void RefreshPrestigeTextTail();
#endif

// Suche : 
		void					AttachTextTail();
// Ersetzen mit :
#if ENABLE_NEW_PRESTIGE_SYSTEM == 1
		void					AttachTextTail(BYTE bPrestige = 0);
#else
		void					AttachTextTail();
#endif