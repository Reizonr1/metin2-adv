// 1) Search: else if (GetSubType() == COSTUME_HAIR)
// 2) Be sure is a member of: int CItem::FindEquipCell(LPCHARACTER ch, int iCandidateCell)
// 3) After make a new line and paste:
#ifdef __WEAPON_COSTUME_SYSTEM__
		else if (GetSubType() == COSTUME_WEAPON)
			return WEAR_COSTUME_WEAPON;
#endif


// 1) Search:
		case ITEM_ROD:
			{
				if (bAdd)
				{
					if (m_wCell == INVENTORY_MAX_NUM + WEAR_WEAPON)
						m_pOwner->SetPart(PART_WEAPON, GetVnum());
				}
				else
				{
					if (m_wCell == INVENTORY_MAX_NUM + WEAR_WEAPON)
						m_pOwner->SetPart(PART_WEAPON, m_pOwner->GetOriginalPart(PART_WEAPON));
				}
			}
			break;
// 2) Replace with:
		case ITEM_ROD:
			{
				if (bAdd)
				{
					if (m_wCell == INVENTORY_MAX_NUM + WEAR_WEAPON)
						m_pOwner->SetPart(PART_WEAPON, GetVnum());
				}
				else
				{
					if (m_wCell == INVENTORY_MAX_NUM + WEAR_WEAPON)
#ifdef __WEAPON_COSTUME_SYSTEM__
						m_pOwner->SetPart(PART_WEAPON, 0);
#else
						m_pOwner->SetPart(PART_WEAPON, m_pOwner->GetOriginalPart(PART_WEAPON));
#endif
				}
			}
			break;


// 1) Search: case ITEM_WEAPON:
// 2) Be sure their definition contain: m_pOwner->SetPart(PART_WEAPON, m_pOwner->GetOriginalPart(PART_WEAPON));
// 3) Replace with:
		case ITEM_WEAPON:
			{
#ifdef __WEAPON_COSTUME_SYSTEM__
				if (m_pOwner->GetWear(WEAR_COSTUME_WEAPON) != 0)
					break;
#endif
				if (bAdd)
				{
					if (m_wCell == INVENTORY_MAX_NUM + WEAR_WEAPON)
						m_pOwner->SetPart(PART_WEAPON, GetVnum());
				}
				else
				{
					if (m_wCell == INVENTORY_MAX_NUM + WEAR_WEAPON)
						m_pOwner->SetPart(PART_WEAPON, m_pOwner->GetOriginalPart(PART_WEAPON));
				}
			}
			break;

// 1) Search: else if (GetSubType() == COSTUME_HAIR)
// 2) Be sure is a member of: case ITEM_COSTUME:
// 3) Before make a new line and paste:
#ifdef __WEAPON_COSTUME_SYSTEM__
				else if (GetSubType() == COSTUME_WEAPON)
				{
					toSetPart = PART_WEAPON;
					if (!bAdd)
					{
						const CItem* pWeapon = m_pOwner->GetWear(WEAR_WEAPON);
						toSetValue = (NULL != pWeapon) ? pWeapon->GetVnum() : m_pOwner->GetPart(PART_WEAPON);						
					}
				}
#endif


// 1) Search:
				else
				{
					if (m_wCell == INVENTORY_MAX_NUM + WEAR_WEAPON)
						m_pOwner->SetPart(PART_WEAPON, m_pOwner->GetOriginalPart(PART_WEAPON));
				}
			}
			break;
		case ITEM_ARMOR:
// 2) Replace with:
				else
				{
					if (m_wCell == INVENTORY_MAX_NUM + WEAR_WEAPON)
#ifdef __WEAPON_COSTUME_SYSTEM__
						m_pOwner->SetPart(PART_WEAPON, 0);
#else
						m_pOwner->SetPart(PART_WEAPON, m_pOwner->GetOriginalPart(PART_WEAPON));
#endif
				}
			}
			break;
		case ITEM_ARMOR: