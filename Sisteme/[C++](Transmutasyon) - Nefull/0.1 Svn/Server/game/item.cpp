// Search for:
CItem::CItem(DWORD dwVnum)

// Replace their whole function with:
CItem::CItem(DWORD dwVnum)
	: m_dwVnum(dwVnum), m_bWindow(0), m_dwID(0), m_bEquipped(false), m_dwVID(0), m_wCell(0), m_dwCount(0), m_lFlag(0), m_dwLastOwnerPID(0),
	m_bExchanging(false), m_pkDestroyEvent(NULL), m_pkExpireEvent(NULL), m_pkUniqueExpireEvent(NULL),
	m_pkTimerBasedOnWearExpireEvent(NULL), m_pkRealTimeExpireEvent(NULL),
   	m_pkAccessorySocketExpireEvent(NULL), m_pkOwnershipEvent(NULL), m_dwOwnershipPID(0), m_bSkipSave(false), m_isLocked(false),
	m_dwMaskVnum(0), m_dwSIGVnum (0)
#ifdef __CHANGE_LOOK_SYSTEM__
	, m_dwLook(0)
#endif
{
	memset( &m_alSockets, 0, sizeof(m_alSockets) );
	memset( &m_aAttr, 0, sizeof(m_aAttr) );
}

// Search for:
	m_dwLastOwnerPID = 0;

// Add Under:
#ifdef __CHANGE_LOOK_SYSTEM__
	m_dwLook = 0;
#endif

// Search for:
	pack.Cell = TItemPos(GetWindow(), m_wCell);

// Add Under:
#ifdef __CHANGE_LOOK_SYSTEM__
	pack.dwVnum = m_dwLook;
#endif

// Search for On case ITEM_WEAPON:
					if (m_wCell == INVENTORY_MAX_NUM + WEAR_WEAPON)
						m_pOwner->SetPart(PART_WEAPON, GetVnum());

// Replace their function with:
#ifdef __CHANGE_LOOK_SYSTEM__
					if (m_wCell == INVENTORY_MAX_NUM + WEAR_WEAPON)
						m_pOwner->SetPart(PART_WEAPON, GetItemLook() > 0 ? GetItemLook() : GetVnum());
#else
					if (m_wCell == INVENTORY_MAX_NUM + WEAR_WEAPON)
						m_pOwner->SetPart(PART_WEAPON, GetVnum());
#endif

// Search for On case ITEM_ARMOR:
						if (GetProto()->bSubType == ARMOR_BODY)
							m_pOwner->SetPart(PART_MAIN, GetVnum());

// Replace their function with:
#ifdef __CHANGE_LOOK_SYSTEM__
						if (GetProto()->bSubType == ARMOR_BODY)
							m_pOwner->SetPart(PART_MAIN, GetItemLook() > 0 ? GetItemLook() : GetVnum());
#else
						if (GetProto()->bSubType == ARMOR_BODY)
							m_pOwner->SetPart(PART_MAIN, GetVnum());
#endif

// Search for On case ITEM_COSTUME:
						const CItem* pArmor = m_pOwner->GetWear(WEAR_BODY);

// Replace their function with:
#ifdef __CHANGE_LOOK_SYSTEM__
						CItem* pArmor = m_pOwner->GetWear(WEAR_BODY);
#else
						const CItem* pArmor = m_pOwner->GetWear(WEAR_BODY);
#endif

// Search for On case ITEM_COSTUME:
						toSetValue = (NULL != pArmor) ? pArmor->GetVnum() : m_pOwner->GetOriginalPart(PART_MAIN);

// Replace their function with:
#ifdef __CHANGE_LOOK_SYSTEM__
						toSetValue = (NULL != pArmor) ? pArmor->GetItemLook() > 0 ? pArmor->GetItemLook() : pArmor->GetVnum() : m_pOwner->GetOriginalPart(PART_MAIN);
#else
						toSetValue = (NULL != pArmor) ? pArmor->GetVnum() : m_pOwner->GetOriginalPart(PART_MAIN);
#endif

// If you have COSTUME_WEAPON on case ITEM_COSTUME:
						toSetValue = (NULL != pWeapon) ? pWeapon->GetVnum() : m_pOwner->GetPart(PART_WEAPON);

// Replace their function with: 
#ifdef __CHANGE_LOOK_SYSTEM__
						toSetValue = (NULL != pWeapon) ? pWeapon->GetItemLook() > 0 ? pWeapon->GetItemLook() : pWeapon->GetVnum() : m_pOwner->GetPart(PART_WEAPON);
#else
						toSetValue = (NULL != pWeapon) ? pWeapon->GetVnum() : m_pOwner->GetPart(PART_WEAPON);
#endif

// Go to the end of the file and paste this:
#ifdef __CHANGE_LOOK_SYSTEM__
void CItem::SetItemLook(DWORD look)
{
	m_dwLook = look;
	UpdatePacket();
	ITEM_MANAGER::instance().SaveSingleItem(this);
	Save();
}
#endif
