// Suche :
	m_stName = src.m_stName;
// Füge darunter dass ein :
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
	m_byPrestige = src.m_byPrestige;
#endif
// Suche :
	kCreateData.m_dwLevel=rkNetActorData.m_dwLevel;
// Füge darunter dass ein :
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
	kCreateData.m_byPrestige=rkNetActorData.m_byPrestige;
#endif
// Suche :
		pkInstFind->SetStateFlags(c_rkNetUpdateActorData.m_dwStateFlags);
// Füge darunter dass ein : 
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
		pkInstFind->SetPrestigeLevel(c_rkNetUpdateActorData.m_byPrestige);
#endif
#if ENABLE_NEW_PRESTIGE_SYSTEM >= 1
		if (c_rkNetUpdateActorData.m_byPrestige >= 0)
			pkInstFind->RefreshPrestigeTextTail();
#endif