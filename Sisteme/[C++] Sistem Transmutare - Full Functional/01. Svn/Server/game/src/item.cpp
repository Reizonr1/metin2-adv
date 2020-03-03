// 1) Search: m_dwCount(0),
// 2) After make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
		m_dwTransmutation(0), 
#endif
// 3) Example of result:
CItem::CItem(DWORD dwVnum): 
		m_dwVnum(dwVnum), 
		m_bWindow(0), 
		m_dwID(0), 
		m_bEquipped(false), 
		m_dwVID(0), 
		m_wCell(0), 
		m_dwCount(0), 
#ifdef __CHANGELOOK_SYSTEM__
		m_dwTransmutation(0), 
#endif
		m_lFlag(0), 
		m_dwLastOwnerPID(0),
		m_bExchanging(false), 
		m_pkDestroyEvent(NULL), 
		m_pkExpireEvent(NULL), 
		m_pkUniqueExpireEvent(NULL),
		m_pkTimerBasedOnWearExpireEvent(NULL), 
		m_pkRealTimeExpireEvent(NULL),
		m_pkAccessorySocketExpireEvent(NULL), 
		m_pkOwnershipEvent(NULL), 
		m_dwOwnershipPID(0), 
		m_bSkipSave(false), m_isLocked(false),
		m_dwMaskVnum(0), 
		m_dwSIGVnum (0)
{
	memset( &m_alSockets, 0, sizeof(m_alSockets) );
	memset( &m_aAttr, 0, sizeof(m_aAttr) );
}


// 1) Search:
	m_dwVID = m_wCell = m_dwCount = m_lFlag = 0;
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	m_dwTransmutation = 0;
#endif


// 1) Search:
	pack.count = m_dwCount;
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	pack.transmutation = m_dwTransmutation;
#endif


// 1) Search:
LPITEM CItem::RemoveFromCharacter()
// 2) Before this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
void CItem::SetTransmutation(DWORD dwVnum, bool bLog)
{
	m_dwTransmutation = dwVnum;
	UpdatePacket();
	Save();
}
#endif


// 1) Search:
				if (bAdd)
				{
					m_pOwner->SetPart(PART_WEAPON, GetVnum());
// 2) Replace with:
				if (bAdd)
				{
#ifdef __CHANGELOOK_SYSTEM__
					DWORD dwRes = GetTransmutation() != 0 ? GetTransmutation() : GetVnum();
					m_pOwner->SetPart(PART_WEAPON, dwRes);
#else
					m_pOwner->SetPart(PART_WEAPON, GetVnum());
#endif


// 1) Search:
					if (bAdd)
					{
						if (GetProto()->bSubType == ARMOR_BODY)
							m_pOwner->SetPart(PART_MAIN, GetVnum());
// 2) Replace with:
					if (bAdd)
					{
						if (GetProto()->bSubType == ARMOR_BODY)
#ifdef __CHANGELOOK_SYSTEM__
						{
							DWORD dwRes = GetTransmutation() != 0 ? GetTransmutation() : GetVnum();
							m_pOwner->SetPart(PART_MAIN, dwRes);
						}
#else
							m_pOwner->SetPart(PART_MAIN, GetVnum());
#endif


// 1) Search:
				if (GetSubType() == COSTUME_BODY)
				{
					toSetPart = PART_MAIN;
					if (false == bAdd)
					{
						const CItem* pArmor = m_pOwner->GetWear(WEAR_BODY);
						toSetValue = (NULL != pArmor) ? pArmor->GetVnum() : m_pOwner->GetOriginalPart(PART_MAIN);
					}
				}
// 2) Replace with:
				if (GetSubType() == COSTUME_BODY)
				{
					toSetPart = PART_MAIN;
					if (false == bAdd)
					{
						const CItem* pArmor = m_pOwner->GetWear(WEAR_BODY);
						toSetValue = (NULL != pArmor) ? pArmor->GetVnum() : m_pOwner->GetOriginalPart(PART_MAIN);
#ifdef __CHANGELOOK_SYSTEM__
						if (pArmor)
							toSetValue = pArmor->GetTransmutation() != 0 ? pArmor->GetTransmutation() : pArmor->GetVnum();
#endif
					}
#ifdef __CHANGELOOK_SYSTEM__
					else
						toSetValue = GetTransmutation() != 0 ? GetTransmutation() : GetVnum();
#endif
				}


// 1) Search:
				else if (GetSubType() == COSTUME_HAIR)
				{
					toSetPart = PART_HAIR;
					toSetValue = (true == bAdd) ? this->GetValue(3) : 0;
				}
// 2) Replace with:
				else if (GetSubType() == COSTUME_HAIR)
				{
					toSetPart = PART_HAIR;
					if (!bAdd)
						toSetValue = 0;
					else
					{
#ifdef __CHANGELOOK_SYSTEM__
						DWORD dwTransmutation = GetTransmutation();
						if (dwTransmutation != 0)
						{
							TItemTable* pItemTable = ITEM_MANAGER::instance().GetTable(dwTransmutation);
							toSetValue = (pItemTable != NULL) ? pItemTable->alValues[3] : GetValue(3);
						}
						else
							toSetValue = GetValue(3);
#else
						toSetValue = GetValue(3);
#endif
					}
				}