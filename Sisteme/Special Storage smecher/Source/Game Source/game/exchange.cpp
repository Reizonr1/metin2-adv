Cauta -----

static CGrid s_grid4(5, INVENTORY_MAX_NUM / 5 / 4);

Adauga sub-------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	static CGrid s_grid5(5, SKILL_BOOK_INVENTORY_MAX_NUM / 5 / 4);
	static CGrid s_grid6(5, UPGRADE_ITEMS_INVENTORY_MAX_NUM / 5 / 4);
	static CGrid s_grid7(5, STONE_INVENTORY_MAX_NUM / 5 / 4);
	static CGrid s_grid8(5, SANDIK_INVENTORY_MAX_NUM / 5 / 4);
#endif

Cauta -----

s_grid4.Clear();

Adauga sub-------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	s_grid5.Clear();
	s_grid6.Clear();
	s_grid7.Clear();
	s_grid8.Clear();
#endif

Cauta -----

s_grid4.Put(i - perPageSlotCount * 3, 1, itemSize);
    }

Adauga sub-------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	int x;
	int y;
	const int perPageSkillBookSlotCount = SKILL_BOOK_INVENTORY_MAX_NUM / 1;
	const int perPageUpgradeItemsSlotCount = UPGRADE_ITEMS_INVENTORY_MAX_NUM / 1;
	const int perPageStoneSlotCount = STONE_INVENTORY_MAX_NUM / 1;
	const int perPageSandikSlotCount = SANDIK_INVENTORY_MAX_NUM / 1;
	for (x = 0; x < SKILL_BOOK_INVENTORY_MAX_NUM; ++x) {
		if (!(item = victim->GetSkillBookInventoryItem(x)))
			continue;
		
		BYTE itemSize = item->GetSize();
		
		if (x < perPageSkillBookSlotCount)
			s_grid5.Put(x, 1, itemSize);
	}
	
	for (y = 0; y < UPGRADE_ITEMS_INVENTORY_MAX_NUM; ++y) {
		if (!(item = victim->GetUpgradeItemsInventoryItem(y)))
			continue;
		
		BYTE itemSize = item->GetSize();
		
		if (y < perPageUpgradeItemsSlotCount)
			s_grid6.Put(y, 1, itemSize);
	}
	
	for (y = 0; y < STONE_INVENTORY_MAX_NUM; ++y) {
		if (!(item = victim->GetStoneInventoryItem(y)))
			continue;
		
		BYTE itemSize = item->GetSize();
		
		if (y < perPageStoneSlotCount)
			s_grid7.Put(y, 1, itemSize);
	}
	
	for (y = 0; y < SANDIK_INVENTORY_MAX_NUM; ++y) {
		if (!(item = victim->GetSandikInventoryItem(y)))
			continue;
		
		BYTE itemSize = item->GetSize();
		
		if (y < perPageSandikSlotCount)
			s_grid8.Put(y, 1, itemSize);
	}
#endif

Cauta -----

if (!bExistEmptySpace)
                return false;
        }

Adauga sub-------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
		else if (item->IsSkillBook())
		{
			int iPos = s_grid5.FindBlank(1, itemSize);
			if (iPos >= 0) {
				s_grid5.Put(iPos, 1, itemSize);
				continue;
			}
			
			return false;
		}
		else if (item->IsUpgradeItem())
		{
			int iPos = s_grid6.FindBlank(1, itemSize);
			if (iPos >= 0) {
				s_grid6.Put(iPos, 1, itemSize);
				continue;
			}
			
			return false;
		}
		else if (item->IsStone())
		{
			int iPos = s_grid7.FindBlank(1, itemSize);
			if (iPos >= 0) {
				s_grid7.Put(iPos, 1, itemSize);
				continue;
			}
			
			return false;
		}
		else if (item->IsSandik())
		{
			int iPos = s_grid8.FindBlank(1, itemSize);
			if (iPos >= 0) {
				s_grid8.Put(iPos, 1, itemSize);
				continue;
			}
			
			return false;
		}
#endif	

Cauta -----

if (item->IsDragonSoul())
			empty_pos = victim->GetEmptyDragonSoulInventory(item);

Adauga sub-------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
		else if (item->IsSkillBook())
			empty_pos = victim->GetEmptySkillBookInventory(item->GetSize());
		else if (item->IsUpgradeItem())
			empty_pos = victim->GetEmptyUpgradeItemsInventory(item->GetSize());
		else if (item->IsStone())
			empty_pos = victim->GetEmptyStoneInventory(item->GetSize());
		else if (item->IsSandik())
			empty_pos = victim->GetEmptySandikInventory(item->GetSize());
#endif

Cauta -----

if (item->IsDragonSoul())
			item->AddToCharacter(victim, TItemPos(DRAGON_SOUL_INVENTORY, empty_pos));

Adauga sub-------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
		else if (item->IsSkillBook())
			item->AddToCharacter(victim, TItemPos(INVENTORY, empty_pos));
		else if (item->IsUpgradeItem())
			item->AddToCharacter(victim, TItemPos(INVENTORY, empty_pos));
		else if (item->IsStone())
			item->AddToCharacter(victim, TItemPos(INVENTORY, empty_pos));
		else if (item->IsSandik())
			item->AddToCharacter(victim, TItemPos(INVENTORY, empty_pos));
#endif
