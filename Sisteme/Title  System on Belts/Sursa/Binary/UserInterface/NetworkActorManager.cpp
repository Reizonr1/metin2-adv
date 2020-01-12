// 1) Search: m_byPKMode = src.m_byPKMode;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	m_iTitleID = src.m_iTitleID;
#endif


// 1) Search: m_byPKMode=0;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	m_iTitleID = 0;
#endif


// 1) Search: kCreateData.m_byPKMode=rkNetActorData.m_byPKMode;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	kCreateData.m_iTitleID = rkNetActorData.m_iTitleID;
#endif


// 1) Search: pkInstFind->SetPKMode(c_rkNetUpdateActorData.m_byPKMode);
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		pkInstFind->SetsTitle(c_rkNetUpdateActorData.m_iTitleID);
#endif


// 1) Search: rkNetActorData.m_byPKMode=c_rkNetUpdateActorData.m_byPKMode;
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	rkNetActorData.m_iTitleID=c_rkNetUpdateActorData.m_iTitleID;
#endif