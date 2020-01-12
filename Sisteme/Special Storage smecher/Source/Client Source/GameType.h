Cauta --------

const DWORD c_Belt_Inventory_Slot_End = c_Belt_Inventory_Slot_Start + c_Belt_Inventory_Slot_Count;
#endif

Adauga sub ------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	const DWORD c_Skill_Book_Inventory_Slot_Start = c_Belt_Inventory_Slot_End;
	const DWORD c_Skill_Book_Inventory_Slot_Count = 135;
	const DWORD c_Skill_Book_Inventory_Slot_End = c_Skill_Book_Inventory_Slot_Start + c_Skill_Book_Inventory_Slot_Count;
	
	const DWORD c_Upgrade_Items_Inventory_Slot_Start = c_Skill_Book_Inventory_Slot_End;
	const DWORD c_Upgrade_Items_Inventory_Slot_Count = 135;
	const DWORD c_Upgrade_Items_Inventory_Slot_End = c_Upgrade_Items_Inventory_Slot_Start + c_Upgrade_Items_Inventory_Slot_Count;
	
	const DWORD c_Stone_Inventory_Slot_Start = c_Upgrade_Items_Inventory_Slot_End;
	const DWORD c_Stone_Inventory_Slot_Count = 135;
	const DWORD c_Stone_Inventory_Slot_End = c_Stone_Inventory_Slot_Start + c_Stone_Inventory_Slot_Count;
	
	const DWORD c_Sandik_Inventory_Slot_Start = c_Stone_Inventory_Slot_End;
	const DWORD c_Sandik_Inventory_Slot_Count = 135;
	const DWORD c_Sandik_Inventory_Slot_End = c_Sandik_Inventory_Slot_Start + c_Sandik_Inventory_Slot_Count;
	
	const DWORD c_Inventory_Count	= c_Sandik_Inventory_Slot_End;
#else


Cauta --------

SLOT_TYPE_DRAGON_SOUL_INVENTORY,

Adauga sub -------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	SLOT_TYPE_SKILL_BOOK_INVENTORY,
	SLOT_TYPE_UPGRADE_ITEMS_INVENTORY,
	SLOT_TYPE_STONE_INVENTORY,
	SLOT_TYPE_SANDIK_INVENTORY,
#endif

Cauta --------

BELT_INVENTORY,

Adauga sub -------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	SKILL_BOOK_INVENTORY,
	UPGRADE_ITEMS_INVENTORY,
	STONE_INVENTORY,
	SANDIK_INVENTORY,
#endif

Cauta --------

bool operator==(const struct SItemPos& rhs) const

üstüne EKLENÝR -------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	bool IsSkillBookInventoryCell()
	{
		bool bResult = c_Skill_Book_Inventory_Slot_Start <= cell && c_Skill_Book_Inventory_Slot_End > cell;
		return bResult;
	}
	
	bool IsUpgradeItemsInventoryCell()
	{
		bool bResult = c_Upgrade_Items_Inventory_Slot_Start <= cell && c_Upgrade_Items_Inventory_Slot_End > cell;
		return bResult;
	}
	
	bool IsStoneInventoryCell()
	{
		bool bResult = c_Stone_Inventory_Slot_Start <= cell && c_Stone_Inventory_Slot_End > cell;
		return bResult;
	}
	
	bool IsSandikInventoryCell()
	{
		bool bResult = c_Sandik_Inventory_Slot_Start <= cell && c_Sandik_Inventory_Slot_End > cell;
		return bResult;
	}
#endif
