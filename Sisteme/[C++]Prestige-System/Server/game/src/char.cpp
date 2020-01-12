// Suche :
	m_iSyncHackCount = 0;
// Füge darunter das ein :
#ifdef __PRESTIGE_SYSTEM__
	SetPrestigeLevel(0);
#endif
// Suche :
			addPacket.dwLevel = GetLevel();
// Füge darunter das ein :
#ifdef __PRESTIGE_SYSTEM__
			addPacket.bPrestige = GetPrestigeLevel();
#endif
// Suche :
			addPacket.dwLevel = 0;
// Füge darunter das ein :
#ifdef __PRESTIGE_SYSTEM__
			addPacket.bPrestige = 0;
#endif

// Suche :
	pack.bPKMode	= m_bPKMode;
// Füge darunter das ein :
#ifdef __PRESTIGE_SYSTEM__
			pack.bPrestige = GetPrestigeLevel();
#endif
// Suche :
	tab.level_step	= GetPoint(POINT_LEVEL_STEP);	
// Füge darunter das ein :
#ifdef __PRESTIGE_SYSTEM__
	tab.prestige = GetPrestigeLevel();
#endif
	
// Suche :
	SetLevel(t->level);
// Füge darunter das ein :
#ifdef __PRESTIGE_SYSTEM__
	SetPrestigeLevel(t->prestige);
#endif