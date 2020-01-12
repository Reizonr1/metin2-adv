// Suche : 
	kNetActorData.m_dwLevel = 0;
// Füge darunter das ein :
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
	kNetActorData.m_byPrestige = 0;
#endif
// Suche :
		kNetActorData.m_dwLevel = chrInfoPacket.dwLevel;
// Füge daruner das ein :
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
		kNetActorData.m_byPrestige = chrInfoPacket.bPrestige;
#endif
// Suche :
	kNetActorData.m_dwLevel=0;
// Füge daruner das ein :
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
	kNetActorData.m_byPrestige=0;
#endif
// Suche :
	kNetUpdateActorData.m_dwMountVnum=chrUpdatePacket.dwMountVnum;
// Füge daruner das ein :
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
	kNetUpdateActorData.m_byPrestige=chrUpdatePacket.bPrestige;
#endif