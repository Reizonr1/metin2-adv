// 1) Search: if (item->GetWearFlag() & WEARABLE_UNIQUE)
// 2) After their definition make a new line and paste:
#ifdef __WEAPON_COSTUME_SYSTEM__
#ifdef __NEW_ARROW_SYSTEM__
	if (item->GetType() == ITEM_WEAPON && item->GetSubType() != WEAPON_ARROW && item->GetSubType() != WEAPON_UNLIMITED_ARROW)
#else
	if (item->GetType() == ITEM_WEAPON && item->GetSubType() != WEAPON_ARROW)
#endif
	{
		LPITEM pkItem = GetWear(WEAR_COSTUME_WEAPON);
		if (pkItem)
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("For can do this unwear the costume weapon."));
			return false;
		}
	}
	else if (item->GetType() == ITEM_COSTUME && item->GetSubType() == COSTUME_WEAPON)
	{
		LPITEM pkItem = GetWear(WEAR_WEAPON);
		if (!pkItem)
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You can't wear a costume weapon without have a weapon weared."));
			return false;
		}
		else if (item->GetValue(3) != pkItem->GetSubType())
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You can't wear a costume weapon who has different type of your weapon."));
			return false;
		}
	}
	
	if (item->GetType() == ITEM_ROD || item->GetType() == ITEM_PICK)
	{
		LPITEM pkItem = GetWear(WEAR_COSTUME_WEAPON);
		if (pkItem)
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("For can do this unwear the costume weapon."));
			return false;
		}
	}
#endif


// 1) Search: bool CHARACTER::CanUnequipNow(const LPITEM item, const TItemPos& srcCell, const TItemPos& destCell)
// 2) Replace their definition with:
bool CHARACTER::CanUnequipNow(const LPITEM item, const TItemPos& srcCell, const TItemPos& destCell)
{
	if (ITEM_BELT == item->GetType())
		VERIFY_MSG(CBeltInventoryHelper::IsExistItemInBeltInventory(this), "벨트 인벤토리에 아이템이 존재하면 해제할 수 없습니다.");
	
	// 영원히 해제할 수 없는 아이템
	if (IS_SET(item->GetFlag(), ITEM_FLAG_IRREMOVABLE))
		return false;
	
	// 아이템 unequip시 인벤토리로 옮길 때 빈 자리가 있는 지 확인
	{
		int pos = -1;
		if (item->IsDragonSoul())
			pos = GetEmptyDragonSoulInventory(item);
		else
			pos = GetEmptyInventory(item->GetSize());
		
		VERIFY_MSG( -1 == pos, "소지품에 빈 공간이 없습니다." );
	}
	
#ifdef __WEAPON_COSTUME_SYSTEM__
#ifdef __NEW_ARROW_SYSTEM__
	if (item->GetType() == ITEM_WEAPON && item->GetSubType() != WEAPON_ARROW && item->GetSubType() != WEAPON_UNLIMITED_ARROW)
#else
	if (item->GetType() == ITEM_WEAPON && item->GetSubType() != WEAPON_ARROW)
#endif
	{
		LPITEM pkItem = GetWear(WEAR_COSTUME_WEAPON);
		if (pkItem)
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("For can do this unwear the costume weapon."));
			return false;
		}
	}
#endif
	
	return true;
}


// 1) Search: static BYTE abSlot[] = {WEAR_COSTUME_BODY, WEAR_COSTUME_HAIR,};
// 2) Replace with:
					static BYTE abSlot[] = {WEAR_COSTUME_BODY, WEAR_COSTUME_HAIR,
#ifdef __WEAPON_COSTUME_SYSTEM__
WEAR_COSTUME_WEAPON,
#endif
					};