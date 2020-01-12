// 1) Search: SetHair(c_rkCreateData.m_dwHair);
// 2) After make a new line and paste:
		SetAcce(c_rkCreateData.m_dwAcce);

// 1) Search: void CInstanceBase::SetArmor(DWORD dwArmor)
// 2) After their function make a new line and paste:
void CInstanceBase::SetAcce(DWORD eAcce)
{
	if (IsPC() == false)
		return;
	
	__ClearAcceRefineEffect();
	float fSpecular = 0.0f;
	int iAcce = (eAcce > 100) ? (int)(eAcce - 100) : (int)(eAcce);
	if (eAcce > 100)
	{
		fSpecular = 100.0f;
		m_acceEffect = EFFECT_REFINED+EFFECT_ACCE_SPECIAL;
		__EffectContainer_AttachEffect(m_acceEffect);
	}
	
	m_awPart[CRaceData::PART_ACCE] = iAcce;
	m_GraphicThingInstance.SetAcce(iAcce, fSpecular);
}

void CInstanceBase::ChangeAcce(DWORD eAcce)
{
	if (IsPC() == false)
		return;
	
	SetAcce(eAcce);
}

// 1) Search: DWORD eHair = GetPart(CRaceData::PART_HAIR);
// 2) After make a new line and paste:
	DWORD eAcce = GetPart(CRaceData::PART_ACCE);

// 1) Search: SetHair(eHair);
// 2) After make a new line and paste:
	SetAcce(eAcce);

// 1) Search: m_armorRefineEffect = 0;
// 2) After make a new line and paste:
	m_acceEffect = 0;

// 1) Search: void CInstanceBase::__ClearWeaponRefineEffect()
// 2) After their function make a new line and paste:
void CInstanceBase::__ClearAcceRefineEffect()
{
	if (m_acceEffect)
	{
		__EffectContainer_DetachEffect(EFFECT_REFINED+EFFECT_ACCE_SPECIAL);
		m_acceEffect = 0;
	}
}