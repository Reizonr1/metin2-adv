// 1) Search: SetWeapon(c_rkCreateData.m_dwWeapon
// 2) After this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
		SetSpecialEffect(c_rkCreateData.m_dwBodyEffect, c_rkCreateData.m_dwWeaponEffectRight, c_rkCreateData.m_dwWeaponEffectLeft);
#endif


// 1) Search: void CInstanceBase::SetHair(DWORD eHair)
// 2) Before this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
void CInstanceBase::SetSpecialEffect(DWORD dwArmorEffect, DWORD dwWeaponEffectRight, DWORD dwWeaponEffectLeft)
{
	if (!IsPC())
		return;
	
	m_awPart[CRaceData::BODY_EFFECT] = dwArmorEffect;
	SpecialEffectCheck();
	
	m_awPart[CRaceData::WEAPON_RIGHT_EFFECT] = dwWeaponEffectRight;
	m_awPart[CRaceData::WEAPON_LEFT_EFFECT] = dwWeaponEffectLeft;
	SpecialEffectCheck(true);
}

void CInstanceBase::ClearSpecialEffect(bool isWeapon)
{
	if (!IsPC())
		return;
	
	if (isWeapon)
	{
		if (m_costumeWeaponEffectRight)
		{
			__EffectContainer_DetachEffect(m_costumeWeaponEffectRight);
			m_costumeWeaponEffectRight = 0;
		}
		
		if (m_costumeWeaponEffectLeft)
		{
			__EffectContainer_DetachEffect(m_costumeWeaponEffectLeft);
			m_costumeWeaponEffectLeft = 0;
		}
	}
	else
	{
		if (m_costumeBodyEffect)
		{
			__EffectContainer_DetachEffect(m_costumeBodyEffect);
			m_costumeBodyEffect = 0;
		}
	}
}

void CInstanceBase::SpecialEffectCheck(bool isWeapon)
{
	if (!IsPC())
		return;
	
	if (isWeapon)
	{
		ClearSpecialEffect(true);
		m_costumeWeaponEffectRight = m_awPart[CRaceData::WEAPON_RIGHT_EFFECT];
		m_costumeWeaponEffectLeft = m_awPart[CRaceData::WEAPON_LEFT_EFFECT];
		if (m_costumeWeaponEffectRight)
			__EffectContainer_AttachEffect(m_costumeWeaponEffectRight);
		
		if (m_costumeWeaponEffectLeft)
			__EffectContainer_AttachEffect(m_costumeWeaponEffectLeft);
	}
	else
	{
		ClearSpecialEffect();
		m_costumeBodyEffect = m_awPart[CRaceData::BODY_EFFECT];
		if (m_costumeBodyEffect)
			__EffectContainer_AttachEffect(m_costumeBodyEffect);
	}
}
#endif


// 1) Search: m_sAlignment = 0;
// 2) Before this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
	m_costumeWeaponEffectRight = 0;
	m_costumeWeaponEffectLeft = 0;
	m_costumeBodyEffect = 0;
#endif