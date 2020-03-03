// 1) Search:
void __SetWeaponPower(IAbstractPlayer& rkPlayer, DWORD dwWeaponID)
// 2) Inside this func search:
	if (CItemManager::Instance().GetItemDataPointer(dwWeaponID, &pkWeapon))
// 3) Replace with:
#if defined(ENABLE_COSTUME_WEAPON_SYSTEM) || defined(ENABLE_CHANGELOOK_SYSTEM)
	if (CItemManager::Instance().GetItemDataPointer(CPythonPlayer::Instance().GetItemIndex(TItemPos(INVENTORY, c_Equipment_Weapon)), &pkWeapon))
#else
	if (CItemManager::Instance().GetItemDataPointer(dwWeaponID, &pkWeapon))
#endif