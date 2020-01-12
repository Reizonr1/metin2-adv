//Search in this file:
//In funtion named : CInstanceBase::Create
	if (!SetRace(c_rkCreateData.m_dwRace))
		return false;

//Replace With:
#ifdef NEW_PET_SYSTEM
	if (!SetRace(c_rkCreateData.m_dwRace))
		return false;

	if(c_rkCreateData.m_dwRace == 34041 || c_rkCreateData.m_dwRace == 34045 || c_rkCreateData.m_dwRace == 34049 || c_rkCreateData.m_dwRace == 34053)
	{
		if(c_rkCreateData.m_dwLevel >= 81)
			SetRace(c_rkCreateData.m_dwRace+1);
	}
#else
	if (!SetRace(c_rkCreateData.m_dwRace))
		return false;
#endif

//Search in this funtion again:
	SetVirtualNumber(c_rkCreateData.m_dwRace);
	SetRotation(c_rkCreateData.m_fRot);

	SetAlignment(c_rkCreateData.m_sAlignment);

//Add after:
#ifdef NEW_PET_SYSTEM
	SetLevelText(c_rkCreateData.m_dwLevel);
#endif

//Search again:
	SetPKMode(c_rkCreateData.m_byPKMode);

	SetMoveSpeed(c_rkCreateData.m_dwMovSpd);
	SetAttackSpeed(c_rkCreateData.m_dwAtkSpd);

//Add after this:

#ifdef NEW_PET_SYSTEM
	if(m_dwRace == 34041 ||m_dwRace == 34045 || m_dwRace == 34049 ||m_dwRace == 34053){
		float scale = c_rkCreateData.m_dwLevel * 0.005f + 0.75f;
		m_GraphicThingInstance.SetScaleNew(scale, scale, scale);
	}
	else
		m_GraphicThingInstance.SetScaleNew(1.0f,1.0f,1.0f);
#endif


//Search in this file:
void CInstanceBase::SetAlignment(short sAlignment)
{
	m_sAlignment = sAlignment;
	RefreshTextTailTitle();
}

//Add after:

#ifdef NEW_PET_SYSTEM
void CInstanceBase::SetLevelText(int sLevel)
{
	m_dwLevel = sLevel;
	UpdateTextTailLevel(sLevel);
}
#endif

//Search in this file:
BOOL CInstanceBase::IsNPC()
{
	return m_GraphicThingInstance.IsNPC();
}

//Add after:
#ifdef NEW_PET_SYSTEM
BOOL CInstanceBase::IsNewPet()
{
	return m_GraphicThingInstance.IsNewPet();
}
#endif
