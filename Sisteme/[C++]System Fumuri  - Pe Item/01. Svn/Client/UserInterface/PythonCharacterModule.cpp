// 1) Search: kCreateData.m_dwHair=0;
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
		kCreateData.m_dwBodyEffect=0;
		kCreateData.m_dwWeaponEffectRight=0;
		kCreateData.m_dwWeaponEffectLeft=0;
#endif