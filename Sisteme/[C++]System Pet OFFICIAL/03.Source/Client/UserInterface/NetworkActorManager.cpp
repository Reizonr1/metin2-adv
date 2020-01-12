//Search in this file:
	m_sAlignment=0;
	m_byPKMode=0;
	m_dwMountVnum=0;

//Add after:
#ifdef NEW_PET_SYSTEM
	m_dwLevel=0;
#endif

//Search in this file:
		pkInstFind->SetAttackSpeed(c_rkNetUpdateActorData.m_dwAtkSpd);
		pkInstFind->SetAlignment(c_rkNetUpdateActorData.m_sAlignment);

//Add after:

#ifdef NEW_PET_SYSTEM
		pkInstFind->SetLevelText(c_rkNetUpdateActorData.m_dwLevel);
#endif

//Search in this file:

	rkNetActorData.m_kAffectFlags=c_rkNetUpdateActorData.m_kAffectFlags;
	rkNetActorData.m_dwGuildID=c_rkNetUpdateActorData.m_dwGuildID;

//Add after:

#ifdef NEW_PET_SYSTEM
	rkNetActorData.m_dwLevel=c_rkNetUpdateActorData.m_dwLevel;
#endif
