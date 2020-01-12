// 1) Search: DWORD	m_dwHair;
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
			DWORD	m_dwBodyEffect;
			DWORD	m_dwWeaponEffectRight;
			DWORD	m_dwWeaponEffectLeft;
#endif


// 1) Search: void	ChangeHair(DWORD eHair);
// 2) Before this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
		void	SetSpecialEffect(DWORD dwArmorEffect = 0, DWORD dwWeaponEffectRight = 0, DWORD dwWeaponEffectLeft = 0);
		void	ClearSpecialEffect(bool isWeapon = false);
		void	SpecialEffectCheck(bool isWeapon = false);
#endif


// 1) Search: struct SMoveAfterFunc
// 2) Before this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
		DWORD	m_costumeWeaponEffectRight;
		DWORD	m_costumeWeaponEffectLeft;
		DWORD	m_costumeBodyEffect;
#endif