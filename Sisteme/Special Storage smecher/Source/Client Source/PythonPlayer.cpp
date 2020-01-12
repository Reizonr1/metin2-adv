Cauta ----------

#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
bool CPythonPlayer::IsBeltInventorySlot(TItemPos Cell)
{
	return Cell.IsBeltInventoryCell();
}
#endif


Adauga sub -------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
bool CPythonPlayer::IsSkillBookInventorySlot(TItemPos Cell)
{
	return Cell.IsSkillBookInventoryCell();
}

bool CPythonPlayer::IsUpgradeItemsInventorySlot(TItemPos Cell)
{
	return Cell.IsUpgradeItemsInventoryCell();
}

bool CPythonPlayer::IsStoneInventorySlot(TItemPos Cell)
{
	return Cell.IsStoneInventoryCell();
}

bool CPythonPlayer::IsSandikInventorySlot(TItemPos Cell)
{
	return Cell.IsSandikInventoryCell();
}
#endif