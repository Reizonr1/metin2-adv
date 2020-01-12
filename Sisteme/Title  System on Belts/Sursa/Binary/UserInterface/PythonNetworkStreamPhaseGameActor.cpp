// 1) Search: kNetActorData.m_byPKMode=0;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	kNetActorData.m_iTitleID = 0;
#endif


// 1) Search: kNetActorData.m_byPKMode=chrInfoPacket.bPKMode;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		kNetActorData.m_iTitleID = chrInfoPacket.iTitleID;
#endif


// 1) Search: kNetActorData.m_byPKMode=chrAddPacket.bPKMode;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	kNetActorData.m_iTitleID=chrAddPacket.iTitleID;
#endif


// 1) Search: kNetUpdateActorData.m_byPKMode=chrUpdatePacket.bPKMode;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	kNetUpdateActorData.m_iTitleID=chrUpdatePacket.iTitleID;
#endif


// 1) Search: kNetUpdateActorData.m_byPKMode=chrUpdatePacket.bPKMode;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	kNetUpdateActorData.m_iTitleID=chrUpdatePacket.iTitleID;
#endif