// 1) Search: DWORD	m_dwHair;
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
	DWORD	m_dwBodyEffect;
	DWORD	m_dwWeaponEffectRight;
	DWORD	m_dwWeaponEffectLeft;
#endif


// 1) Search: DWORD m_dwHair;
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
	DWORD m_dwBodyEffect;
	DWORD m_dwWeaponEffectRight;
	DWORD m_dwWeaponEffectLeft;
#endif


// 1) Search: m_dwHair=0;
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
		m_dwBodyEffect=0;
		m_dwWeaponEffectRight=0;
		m_dwWeaponEffectLeft=0;
#endif