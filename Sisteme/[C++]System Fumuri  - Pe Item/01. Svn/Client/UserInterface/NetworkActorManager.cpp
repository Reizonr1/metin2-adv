// 1) Search: m_dwHair = src.m_dwHair;
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
	m_dwBodyEffect = src.m_dwBodyEffect;
	m_dwWeaponEffectRight = src.m_dwWeaponEffectRight;
	m_dwWeaponEffectLeft = src.m_dwWeaponEffectLeft;
#endif


// 1) Search: m_dwHair=0;
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
	m_dwBodyEffect=0;
	m_dwWeaponEffectRight=0;
	m_dwWeaponEffectLeft=0;
#endif


// 1) Search: kCreateData.m_dwHair=rkNetActorData.m_dwHair;
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
	kCreateData.m_dwBodyEffect=rkNetActorData.m_dwBodyEffect;
	kCreateData.m_dwWeaponEffectRight=rkNetActorData.m_dwWeaponEffectRight;
	kCreateData.m_dwWeaponEffectLeft=rkNetActorData.m_dwWeaponEffectLeft;
#endif


// 1) Search: pkInstFind->ChangeHair(c_rkNetUpdateActorData.m_dwHair);
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
		pkInstFind->SetSpecialEffect(c_rkNetUpdateActorData.m_dwBodyEffect, c_rkNetUpdateActorData.m_dwWeaponEffectRight, c_rkNetUpdateActorData.m_dwWeaponEffectLeft);
#endif


// 1) Search: rkNetActorData.m_dwHair=c_rkNetUpdateActorData.m_dwHair;
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
	rkNetActorData.m_dwBodyEffect=rkNetActorData.m_dwBodyEffect;
	rkNetActorData.m_dwWeaponEffectRight=rkNetActorData.m_dwWeaponEffectRight;
	rkNetActorData.m_dwWeaponEffectLeft=rkNetActorData.m_dwWeaponEffectLeft;
#endif