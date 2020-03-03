// Go to the end of the file and paste this:
#ifdef __CHANGE_LOOK_SYSTEM__
ACMD(do_transmutate)
{
	char arg1[256];
	char arg2[256];
	two_arguments (argument, arg1, sizeof(arg1), arg2, sizeof(arg2));

	BYTE slot0 = atoi(arg1);
	BYTE slot1 = atoi(arg2);

	LPITEM item0 = ch->GetInventoryItem(slot0);
	LPITEM item1 = ch->GetInventoryItem(slot1);

	if (!item0 || !item1 || !ch->SameItem(item0, item1))
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("CHANGE_LOOK_NEED_ITEM."));
		return;
	}
	else
	{
		if ((item0->IsArmor() && item1->IsArmor()) || (item0->IsWeapon() && item1->IsWeapon()))
		{
			if (ch->GetGold() >= 50000000)
			{
				item0->SetItemLook(item1->GetVnum());
				ITEM_MANAGER::instance().RemoveItem(item1, "CHANGE_LOOK_SECOND_ITEM_DESTROY");
				ch->PointChange(POINT_GOLD, -50000000);
				ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("CHANGE_LOOK_ITEM_REMOVE"));
				ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("CHANGE_LOOK_GOLD_REMOVE"));
			}
			else
			{
				ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("CHANGE_LOOK_NOT_ENOUGH_MONEY"));
			}
		}
		else
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("CHANGE_LOOK_WRONG_TYPES"));
		}
	}
}
#endif
