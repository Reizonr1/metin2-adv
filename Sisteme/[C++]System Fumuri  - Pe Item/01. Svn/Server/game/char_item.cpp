// 1) Search: bool CHARACTER::CanEquipNow(const LPITEM item, const TItemPos& srcCell, const TItemPos& destCell)
// 2) Before the end of function where is last:
	return true;
}
// 3) Make a new line and paste:
#ifdef __EFFECT_SYSTEM__
#ifdef __NEW_ARROW_SYSTEM__
	if (item->GetType() == ITEM_WEAPON && item->GetSubType() != WEAPON_ARROW && item->GetSubType() != WEAPON_UNLIMITED_ARROW)
#else
	if (item->GetType() == ITEM_WEAPON && item->GetSubType() != WEAPON_ARROW)
#endif
	{
		LPITEM pkItem = GetWear(WEAR_EFFECT_WEAPON);
		if (pkItem)
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You must unwear the weapon effect before."));
			return false;
		}
	}
	else if (item->GetType() == ITEM_ARMOR && item->GetSubType() == ARMOR_BODY)
	{
		LPITEM pkItem = GetWear(WEAR_EFFECT_ARMOR);
		if (pkItem)
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You must unwear the armor effect before."));
			return false;
		}
	}
	else if (item->GetType() == ITEM_COSTUME && item->GetSubType() == USE_EFFECT)
	{
		if (item->GetWearFlag() & WEARABLE_EFFECT_ARMOR)
		{
			LPITEM pkItem = GetWear(WEAR_BODY);
			if (!pkItem)
			{
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT("To can wear a armor effect you must have a armor weared."));
				return false;
			}
		}
		else
		{
			LPITEM pkItem = GetWear(WEAR_WEAPON);
			if (!pkItem)
			{
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT("To can wear a weapon effect you must have a weapon weared."));
				return false;
			}
		}
	}
#endif


// 1) Search: bool CHARACTER::CanUnequipNow(const LPITEM item, const TItemPos& srcCell, const TItemPos& destCell)
// 2) Before the end of function where is last:
	return true;
}
// 3) Make a new line and paste:
#ifdef __EFFECT_SYSTEM__
#ifdef __NEW_ARROW_SYSTEM__
	if (item->GetType() == ITEM_WEAPON && item->GetSubType() != WEAPON_ARROW && item->GetSubType() != WEAPON_UNLIMITED_ARROW)
#else
	if (item->GetType() == ITEM_WEAPON && item->GetSubType() != WEAPON_ARROW)
#endif
	{
		LPITEM pkItem = GetWear(WEAR_EFFECT_WEAPON);
		if (pkItem)
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You must unwear the weapon effect before."));
			return false;
		}
	}
	else if (item->GetType() == ITEM_ARMOR && item->GetSubType() == ARMOR_BODY)
	{
		LPITEM pkItem = GetWear(WEAR_EFFECT_ARMOR);
		if (pkItem)
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You must unwear the armor effect before."));
			return false;
		}
	}
#endif