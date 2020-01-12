// 1) Search: if (pItemData->GetType() == CItemData::ITEM_TYPE_WEAPON && (pItemData->GetWeaponType() == CItemData::WEAPON_SWORD || pItemData->GetWeaponType() == CItemData::WEAPON_ARROW || pItemData->GetWeaponType() == CItemData::WEAPON_UNLIMITED_ARROW))
// 2) After this make a new line and paste:
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
		if (pItemData->GetType() == CItemData::ITEM_TYPE_COSTUME && pItemData->GetSubType() == CItemData::COSTUME_WEAPON || pItemData->GetType() == CItemData::ITEM_TYPE_WEAPON && (pItemData->GetWeaponType() == CItemData::WEAPON_SWORD || pItemData->GetWeaponType() == CItemData::WEAPON_ARROW))
			bStabGround = true;
#endif