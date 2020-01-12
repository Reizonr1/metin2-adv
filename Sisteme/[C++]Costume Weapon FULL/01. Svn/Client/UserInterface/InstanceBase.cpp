// 1) Search: DWORD CInstanceBase::GetWeaponType()
// 2) Delete their function and paste:
DWORD CInstanceBase::GetWeaponType()
{
	DWORD dwWeapon = GetPart(CRaceData::PART_WEAPON);
	CItemData * pItemData;
	if (!CItemManager::Instance().GetItemDataPointer(dwWeapon, &pItemData))
		return CItemData::WEAPON_NONE;
	
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
	if (pItemData->GetType() == CItemData::ITEM_TYPE_COSTUME)
		return pItemData->GetValue(3);
#endif
	return pItemData->GetWeaponType();
}

// 1) Search: else if (m_kHorse.IsMounting())
// 2) Be sure it is a member of RefreshState.
// 3) Before this make a new line and paste:
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
	else if (byItemType == CItemData::ITEM_TYPE_COSTUME)
	{
		switch (pItemData->GetValue(3))
		{
			case CItemData::WEAPON_SWORD:
				if (m_kHorse.IsMounting())
					SetMotionMode(CRaceMotionData::MODE_HORSE_ONEHAND_SWORD);
				else
					SetMotionMode(CRaceMotionData::MODE_ONEHAND_SWORD);
				break;
			case CItemData::WEAPON_DAGGER:
				if (m_kHorse.IsMounting())
					SetMotionMode(CRaceMotionData::MODE_HORSE_DUALHAND_SWORD);
				else
					SetMotionMode(CRaceMotionData::MODE_DUALHAND_SWORD);
				break;
			case CItemData::WEAPON_BOW:
				if (m_kHorse.IsMounting())
					SetMotionMode(CRaceMotionData::MODE_HORSE_BOW);
				else
#ifdef ENABLE_NEW_ARROW_SYSTEM
				{
					if (m_awPart[CRaceData::PART_ARROW_TYPE] == CItemData::WEAPON_UNLIMITED_ARROW)
						SetMotionMode(CRaceMotionData::MODE_BOW_SPECIAL);
					else
						SetMotionMode(CRaceMotionData::MODE_BOW);
				}
#else
					SetMotionMode(CRaceMotionData::MODE_BOW);
#endif
				break;
			case CItemData::WEAPON_TWO_HANDED:
				if (m_kHorse.IsMounting())
					SetMotionMode(CRaceMotionData::MODE_HORSE_TWOHAND_SWORD);
				else
					SetMotionMode(CRaceMotionData::MODE_TWOHAND_SWORD);
				break;
			case CItemData::WEAPON_BELL:
				if (m_kHorse.IsMounting())
					SetMotionMode(CRaceMotionData::MODE_HORSE_BELL);
				else
					SetMotionMode(CRaceMotionData::MODE_BELL);
				break;
			case CItemData::WEAPON_FAN:
				if (m_kHorse.IsMounting())
					SetMotionMode(CRaceMotionData::MODE_HORSE_FAN);
				else
					SetMotionMode(CRaceMotionData::MODE_FAN);
				break;
			case CItemData::WEAPON_CLAW:
				if (m_kHorse.IsMounting())
					SetMotionMode(CRaceMotionData::MODE_HORSE_CLAW);
				else
					SetMotionMode(CRaceMotionData::MODE_CLAW);
				break;
			default:
					if (m_kHorse.IsMounting())
						SetMotionMode(CRaceMotionData::MODE_HORSE);
					else
						SetMotionMode(CRaceMotionData::MODE_GENERAL);
				break;
		}
	}
#endif


// 1) Search:
	if (CItemManager::Instance().GetItemDataPointer(eWeapon, &pItemData))
		__GetRefinedEffect(pItemData);
// 2) Be sure it is inbool CInstanceBase::SetWeapon function.
// 3) Replace with:
	if (CItemManager::Instance().GetItemDataPointer(eWeapon, &pItemData))
	{
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
		if (pItemData->GetType() == CItemData::ITEM_TYPE_COSTUME)
			__ClearWeaponRefineEffect();
#endif
		
		__GetRefinedEffect(pItemData);
	}