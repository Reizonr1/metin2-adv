//Search in this file:
//In struct SNetworkUpdateActorData
	DWORD m_dwAtkSpd;
	short m_sAlignment;

//Add after:
#ifdef NEW_PET_SYSTEM
	DWORD	m_dwLevel;
#endif