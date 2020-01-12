// 1) Search: else if (GetSubType() == COSTUME_HAIR)
// 2) After make a new line and paste:
		else if (GetSubType() == COSTUME_ACCE)
			return WEAR_COSTUME_ACCE;

// 1) Search: case ITEM_COSTUME:
// 2) Delete their function and paste:
		case ITEM_COSTUME:
			{
				DWORD toSetValue = this->GetVnum();
				EParts toSetPart = PART_MAX_NUM;
				if (GetSubType() == COSTUME_BODY)
				{
					toSetPart = PART_MAIN;
					if (false == bAdd)
					{
						const CItem* pArmor = m_pOwner->GetWear(WEAR_BODY);
						toSetValue = (NULL != pArmor) ? pArmor->GetVnum() : m_pOwner->GetOriginalPart(PART_MAIN);						
					}
				}
				else if (GetSubType() == COSTUME_HAIR)
				{
					toSetPart = PART_HAIR;
					toSetValue = (true == bAdd) ? this->GetValue(3) : 0;
				}
				else if (GetSubType() == COSTUME_ACCE)
				{
					if (GetSocket(1) >= 19)
					{
						toSetValue = (true == bAdd) ? this->GetValue(3) + 100 : 0;
					}
					else
					{
						toSetValue = (true == bAdd) ? this->GetValue(3) : 0;
					}
					
					toSetPart = PART_ACCE;
				}
				
				if (PART_MAX_NUM != toSetPart)
				{
					m_pOwner->SetPart((BYTE)toSetPart, toSetValue);
					m_pOwner->UpdatePacket();
				}
			}
			break;