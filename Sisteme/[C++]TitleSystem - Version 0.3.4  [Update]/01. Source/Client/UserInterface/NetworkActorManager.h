// 1) Search in function:	struct SNetworkUpdateActorData
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	short	m_sPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search in function:	struct SNetworkActorData
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
	short m_sPrestige;
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1) Search:		m_sAlignment=0;
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		m_sPrestige=0;
#endif
"""""""""""""""""""""""""""""""""""""""""