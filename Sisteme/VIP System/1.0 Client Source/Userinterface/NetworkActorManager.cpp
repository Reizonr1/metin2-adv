//1.0 suchen:
	m_sAlignment = src.m_sAlignment;
//1.0 dahinter:
#ifdef ENABLE_VIP_SYSTEM
	m_sVip = src.m_sVip;
#endif	

//1.1 suchen:
	m_sAlignment=0;
//1.1 dahinter:
#ifdef ENABLE_VIP_SYSTEM
	m_sVip=0;
#endif	

//1.2 suchen:
	kCreateData.m_sAlignment=rkNetActorData.m_sAlignment;
//1.2 dahinter:
#ifdef ENABLE_VIP_SYSTEM
	kCreateData.m_sVip=rkNetActorData.m_sVip;
#endif	

//1.3 suchen:
		pkInstFind->SetAlignment(c_rkNetUpdateActorData.m_sAlignment);
//1.3 dahinter:		
#ifdef ENABLE_VIP_SYSTEM
		pkInstFind->SetVip(c_rkNetUpdateActorData.m_sVip);
#endif	

//1.4 suchen:
	rkNetActorData.m_sAlignment=c_rkNetUpdateActorData.m_sAlignment;
//1.4 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
	rkNetActorData.m_sVip=c_rkNetUpdateActorData.m_sVip;
#endif	

