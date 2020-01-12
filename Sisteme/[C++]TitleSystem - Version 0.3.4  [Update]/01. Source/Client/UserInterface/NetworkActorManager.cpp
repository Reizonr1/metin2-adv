// 1) Search: 	m_sAlignment = src.m_sAlignment;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	m_sPrestige = src.m_sPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	m_sAlignment=0;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	m_sPrestige=0;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	kCreateData.m_sAlignment=rkNetActorData.m_sAlignment;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	kCreateData.m_sPrestige=rkNetActorData.m_sPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	pkInstFind->SetAlignment(c_rkNetUpdateActorData.m_sAlignment);
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		pkInstFind->SetPrestige(c_rkNetUpdateActorData.m_sPrestige);
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:	rkNetActorData.m_sAlignment=c_rkNetUpdateActorData.m_sAlignment;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	rkNetActorData.m_sPrestige=c_rkNetUpdateActorData.m_sPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""