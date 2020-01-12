//Search:
		pkInstFind->SetPKMode(c_rkNetUpdateActorData.m_byPKMode);
		pkInstFind->SetStateFlags(c_rkNetUpdateActorData.m_dwStateFlags);

//Add after:
#ifdef ENABLE_SUPPORT_SYSTEM
		pkInstFind->SetLevelText(c_rkNetUpdateActorData.m_dwLevel);
#endif

//Search:
	rkNetActorData.m_dwAtkSpd=c_rkNetUpdateActorData.m_dwAtkSpd;
	rkNetActorData.m_dwArmor=c_rkNetUpdateActorData.m_dwArmor;

//Add after:
#ifdef ENABLE_SUPPORT_SYSTEM
	rkNetActorData.m_dwLevel=c_rkNetUpdateActorData.m_dwLevel;
#endif