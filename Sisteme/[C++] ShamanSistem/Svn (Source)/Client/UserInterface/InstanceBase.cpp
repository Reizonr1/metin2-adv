//Search:
	IAbstractApplication::GetSingleton().SkipRenderBuffering(300);

	SetInstanceType(c_rkCreateData.m_bType);
	if (!SetRace(c_rkCreateData.m_dwRace))
		return false;
	
//Add after:
#ifdef ENABLE_SUPPORT_SYSTEM
	int i=0;
	if(c_rkCreateData.m_dwRace == 34001)
	{
		SetInstanceType(CActorInstance::TYPE_PC);	
		SetRace(7);
		i=1;
	}
#endif

//Search:
	if (IsPC())
	{
		SetHair(c_rkCreateData.m_dwHair);
		SetWeapon(c_rkCreateData.m_dwWeapon);
	}
	
//Replace with:
	if (IsPC() || i == 1 )
	{
		SetHair(c_rkCreateData.m_dwHair);
		SetWeapon(c_rkCreateData.m_dwWeapon);
	}
	
//Search:
	SetVirtualNumber(c_rkCreateData.m_dwRace);
	SetRotation(c_rkCreateData.m_fRot);

//Add after:
#ifdef ENABLE_SUPPORT_SYSTEM
	SetLevelText(c_rkCreateData.m_dwLevel);
#endif

//Search:
void CInstanceBase::SetAlignment(short sAlignment)
{
	m_sAlignment = sAlignment;
	RefreshTextTailTitle();
}
//Add after:
void CInstanceBase::SetLevelText(int sLevel)
{
	m_dwLevel = sLevel;
	UpdateTextTailLevel(sLevel);
}