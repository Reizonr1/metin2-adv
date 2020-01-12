// 1) Search:	kNetActorData.m_sAlignment=0;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	kNetActorData.m_sPrestige=0;/*chrAddPacket.sPrestige*/;	
#endif

// 1) Search:		kNetActorData.m_sAlignment=chrInfoPacket.sAlignment;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		kNetActorData.m_sPrestige=chrInfoPacket.sPrestige;
#endif		

// 1) Search:	kNetActorData.m_sAlignment=chrAddPacket.sAlignment;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	kNetActorData.m_sPrestige=chrAddPacket.sPrestige;
#endif

// 1) Search in function:	bool CPythonNetworkStream::RecvCharacterUpdatePacket()
	kNetUpdateActorData.m_sAlignment=chrUpdatePacket.sAlignment;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	kNetUpdateActorData.m_sPrestige=chrUpdatePacket.sPrestige;
#endif

// 1) Search in function:	bool CPythonNetworkStream::RecvCharacterUpdatePacketNew()
	kNetUpdateActorData.m_sAlignment=chrUpdatePacket.sAlignment;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	kNetUpdateActorData.m_sPrestige=chrUpdatePacket.sPrestige;
#endif