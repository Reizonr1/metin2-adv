// 1) Search: DWORD	m_dwHair;
// 2) After make a new line and paste:
			DWORD	m_dwAcce;

// 1) Search: AFFECT_GERMANY,
// 2) After make a new line and paste:
			AFFECT_ACCE,

// 1) Search: EFFECT_TEMP,
// 2) After make a new line and paste:
			EFFECT_ACCE_SUCCEDED_1,
			EFFECT_EQUIP_ACCE_1,
			EFFECT_EQUIP_ACCE_2,
			EFFECT_EQUIP_ACCE_3,
			EFFECT_EQUIP_ACCE_4,

// 1) Search:void	SetHair(DWORD eHair);
// 2) After make a new line and paste:
		void	SetAcce(DWORD eAcce);
		void	ChangeAcce(DWORD eAcce);

// 1) Search: EFFECT_BODYARMOR_SPECIAL2,
// 2) After make a new line and paste:
			EFFECT_ACCE_SPECIAL,
			
// 1) Search: DWORD					m_armorRefineEffect;
// 2) After make a new line and paste:
		DWORD	m_acceEffect;

// 1) Search: void	__ClearArmorRefineEffect();
// 2) After make a new line and paste:
		void	__ClearAcceRefineEffect();