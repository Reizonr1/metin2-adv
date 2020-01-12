Cauta ------------------

LPITEM			GetInventoryItem(WORD wCell) const;


Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
		LPITEM			GetSkillBookInventoryItem(WORD wCell) const;
		LPITEM			GetUpgradeItemsInventoryItem(WORD wCell) const;
		LPITEM			GetStoneInventoryItem(WORD wCell) const;
		LPITEM			GetSandikInventoryItem(WORD wCell) const;
#endif


Cauta ------------------

int				GetEmptyDragonSoulInventory(LPITEM pItem) const;



Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
		int				GetEmptySkillBookInventory(BYTE size) const;
		int				GetEmptyUpgradeItemsInventory(BYTE size) const;
		int				GetEmptyStoneInventory(BYTE size) const;
		int				GetEmptySandikInventory(BYTE size) const;
#endif
