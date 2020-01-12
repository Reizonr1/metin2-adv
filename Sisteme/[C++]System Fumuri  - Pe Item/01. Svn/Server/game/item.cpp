// 1) Search: return WEAR_COSTUME_HAIR;
// 2) After make new line and paste:
#ifdef __EFFECT_SYSTEM__
		else if (GetSubType() == USE_EFFECT)
		{
			if (GetWearFlag() & WEARABLE_EFFECT_ARMOR)
				return WEAR_EFFECT_ARMOR;
			else
				return WEAR_EFFECT_WEAPON;
		}
#endif


// 1) Search: case ITEM_COSTUME:
// 2) Be sure is part of: void CItem::ModifyPoints(bool bAdd)
// 3) Now search:
				if (PART_MAX_NUM != toSetPart)
				{
					m_pOwner->SetPart((BYTE)toSetPart, toSetValue);
					m_pOwner->UpdatePacket();
				}
// 4) After this make a new line and paste:
#ifdef __EFFECT_SYSTEM__
				if (GetSubType() == USE_EFFECT)
				{
					if (GetWearFlag() & WEARABLE_EFFECT_ARMOR)
					{
						if (!bAdd)
							m_pOwner->SetPart((BYTE)BODY_EFFECT, 0);
						else
							m_pOwner->SetPart((BYTE)BODY_EFFECT, GetValue(0));
					}
					else
					{
						if (!bAdd)
						{
							m_pOwner->SetPart((BYTE)WEAPON_RIGHT_EFFECT, 0);
							m_pOwner->SetPart((BYTE)WEAPON_LEFT_EFFECT, 0);
						}
						else
						{
							const CItem* pWeaponEffectCheck = m_pOwner->GetWear(WEAR_WEAPON);
							if (pWeaponEffectCheck != NULL)
							{
								DWORD dwEffectRight = 0;
								DWORD dwEffectLeft = 0;
								if (pWeaponEffectCheck->GetSubType() == WEAPON_DAGGER)
								{
									dwEffectRight = GetValue(1);
									dwEffectLeft = GetValue(2);
								}
								else if (pWeaponEffectCheck->GetSubType() == WEAPON_BOW)
								{
									dwEffectRight = GetValue(3);
								}
								else if (pWeaponEffectCheck->GetSubType() == WEAPON_BELL)
								{
									dwEffectRight = GetValue(1);
								}
								else if (pWeaponEffectCheck->GetSubType() == WEAPON_FAN)
								{
									dwEffectRight = GetValue(4);
								}
#ifdef __WOLFMAN_CHARACTER__
								else if (pWeaponEffectCheck->GetSubType() == WEAPON_CLAW)
								{
									dwEffectRight = GetValue(1);
									dwEffectLeft = GetValue(2);
								}
#endif
								else
								{
									dwEffectRight = GetValue(0);
								}
								
								m_pOwner->SetPart((BYTE)WEAPON_RIGHT_EFFECT, dwEffectRight);
								m_pOwner->SetPart((BYTE)WEAPON_LEFT_EFFECT, dwEffectLeft);
							}
						}
					}
					
					m_pOwner->UpdatePacket();
				}
#endif