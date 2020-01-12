//1.0 suchen:
	kNetActorData.m_sAlignment=0;/*chrAddPacket.sAlignment*/;
//1.0 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
	kNetActorData.m_sVip=0;/*chrAddPacket.sVip*/;	
#endif	

//1.1 suchen:
		kNetActorData.m_sAlignment=chrInfoPacket.sAlignment;
//1.1 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
		kNetActorData.m_sVip=chrInfoPacket.sVip;
#endif

//1.2 suchen:
	kNetActorData.m_sAlignment=chrAddPacket.sAlignment;
//1.2 dahinter:
#ifdef ENABLE_VIP_SYSTEM
	kNetActorData.m_sVip=chrAddPacket.sVip;
#endif	

//1.3 suchen:
	kNetUpdateActorData.m_sAlignment=chrUpdatePacket.sAlignment;
//1.3 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
	kNetUpdateActorData.m_sVip=chrUpdatePacket.sVip;
#endif

//1.4 suchen:
	kNetUpdateActorData.m_sAlignment=chrUpdatePacket.sAlignment;
//1.4 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
	kNetUpdateActorData.m_sVip=chrUpdatePacket.sVip;
#endif
