// 1) Search: rkPlayer.SetWeaponPower(minPower, maxPower, minMagicPower, maxMagicPower, addPower);
// 2) Before this line paste:
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
	CItemData * pItemData;
	if (CItemManager::Instance().GetItemDataPointer(CPythonPlayer::Instance().GetItemIndex(TItemPos(INVENTORY, c_Equipment_Weapon)), &pItemData))
	{
		minPower=pItemData->GetValue(3);
		maxPower=pItemData->GetValue(4);
		minMagicPower=pItemData->GetValue(1);
		maxMagicPower=pItemData->GetValue(2);
		addPower=pItemData->GetValue(5);
	}
#endif