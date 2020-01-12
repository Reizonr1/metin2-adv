Cauta --------

int iEmptyPos;
	if (item->IsDragonSoul())
	{
		iEmptyPos = ch->GetEmptyDragonSoulInventory(item);
	}

Adauga sub ---------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	else if (item->IsSkillBook())
	{
		iEmptyPos = ch->GetEmptySkillBookInventory(item->GetSize());
	}
	else if (item->IsUpgradeItem())
	{
		iEmptyPos = ch->GetEmptyUpgradeItemsInventory(item->GetSize());
	}
	else if (item->IsStone())
	{
		iEmptyPos = ch->GetEmptyStoneInventory(item->GetSize());
	}
	else if (item->IsSandik())
	{
		iEmptyPos = ch->GetEmptySandikInventory(item->GetSize());
	}
#endif

Cauta --------

if (item->IsDragonSoul())
		item->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));

Adauga sub ---------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	else if (item->IsSkillBook())
		item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
	else if (item->IsUpgradeItem())
		item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
	else if (item->IsStone())
		item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
	else if (item->IsSandik())
		item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
#endif