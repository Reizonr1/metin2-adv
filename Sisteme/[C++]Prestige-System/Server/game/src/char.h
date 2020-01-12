// Füge dass zu Klasse hinzu;
#ifdef __PRESTIGE_SYSTEM__
	private:
		BYTE	m_byPrestigeLevel;
	public:
		BYTE	GetPrestigeLevel() { return m_byPrestigeLevel; };
		void	SetPrestigeLevel(BYTE level) { m_byPrestigeLevel = level; };
#endif