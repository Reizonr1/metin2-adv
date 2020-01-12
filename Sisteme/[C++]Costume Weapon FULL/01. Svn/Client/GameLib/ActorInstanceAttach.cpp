// 1) Search: void CActorInstance::AttachWeapon(DWORD dwItemIndex, DWORD dwParentPartIndex, DWORD dwPartIndex)
// 2) Replace their function with:
void CActorInstance::AttachWeapon(DWORD dwItemIndex, DWORD dwParentPartIndex, DWORD dwPartIndex)
{
	if (dwPartIndex>=CRaceData::PART_MAX_NUM)
		return;
	
	m_adwPartItemID[dwPartIndex]=dwItemIndex;
	if (USE_VIETNAM_CONVERT_WEAPON_VNUM)
		dwItemIndex = Vietnam_ConvertWeaponVnum(dwItemIndex);
	
	CItemData * pItemData;
	if (!CItemManager::Instance().GetItemDataPointer(dwItemIndex, &pItemData))
	{
		RegisterModelThing(dwPartIndex, NULL);
		SetModelInstance(dwPartIndex, dwPartIndex, 0);

		RegisterModelThing(CRaceData::PART_WEAPON_LEFT, NULL);
		SetModelInstance(CRaceData::PART_WEAPON_LEFT, CRaceData::PART_WEAPON_LEFT, 0);

		RefreshActorInstance();
		return;
	}
	
	__DestroyWeaponTrace();
	if (pItemData->GetType() != CItemData::ITEM_TYPE_COSTUME)
	{
		if (__IsRightHandWeapon(pItemData->GetWeaponType()))
			AttachWeapon(dwParentPartIndex, CRaceData::PART_WEAPON, pItemData);
		
		if (__IsLeftHandWeapon(pItemData->GetWeaponType()))
			AttachWeapon(dwParentPartIndex, CRaceData::PART_WEAPON_LEFT, pItemData);
	}
	else
	{
		DWORD typeDec = pItemData->GetValue(3);
		if (__IsRightHandWeapon(typeDec))
			AttachWeapon(dwParentPartIndex, CRaceData::PART_WEAPON, pItemData);
		
		if (__IsLeftHandWeapon(typeDec))
			AttachWeapon(dwParentPartIndex, CRaceData::PART_WEAPON_LEFT, pItemData);
	}
}


// 1) Search: void CActorInstance::AttachWeapon(DWORD dwParentPartIndex, DWORD dwPartIndex, CItemData * pItemData)
// 2) Replace their function with:
void CActorInstance::AttachWeapon(DWORD dwParentPartIndex, DWORD dwPartIndex, CItemData * pItemData)
{
	if (!pItemData)
		return;
	
	const char * szBoneName;
	if (!GetAttachingBoneName(dwPartIndex, &szBoneName))
		return;
	
	if (CRaceData::PART_WEAPON_LEFT == dwPartIndex)
	{
		RegisterModelThing(dwPartIndex, pItemData->GetSubModelThing());
	}
	else
	{
		RegisterModelThing(dwPartIndex, pItemData->GetModelThing());
	}
	
	for (DWORD i = 0; i < pItemData->GetLODModelThingCount(); ++i)
	{
		CGraphicThing * pThing;
		if (!pItemData->GetLODModelThingPointer(i, &pThing))
			continue;
		
		RegisterLODThing(dwPartIndex, pThing);
	}
	
	SetModelInstance(dwPartIndex, dwPartIndex, 0);
	AttachModelInstance(dwParentPartIndex, szBoneName, dwPartIndex);
	if (USE_WEAPON_SPECULAR)
	{
		SMaterialData kMaterialData;
		kMaterialData.pImage = NULL;
		kMaterialData.isSpecularEnable = TRUE;
		kMaterialData.fSpecularPower = pItemData->GetSpecularPowerf();
		kMaterialData.bSphereMapIndex = 1;
		SetMaterialData(dwPartIndex, NULL, kMaterialData);
	}
	
	if (pItemData->GetType() != CItemData::ITEM_TYPE_COSTUME)
	{
		if (__IsWeaponTrace(pItemData->GetWeaponType()))
		{
			CWeaponTrace * pWeaponTrace = CWeaponTrace::New();
			pWeaponTrace->SetWeaponInstance(this, dwPartIndex, szBoneName);
			m_WeaponTraceVector.push_back(pWeaponTrace);
		}
	}
	else
	{
		DWORD typeDec = pItemData->GetValue(3);
		if (__IsWeaponTrace(typeDec))
		{
			CWeaponTrace * pWeaponTrace = CWeaponTrace::New();
			pWeaponTrace->SetWeaponInstance(this, dwPartIndex, szBoneName);
			m_WeaponTraceVector.push_back(pWeaponTrace);
		}
	}
}