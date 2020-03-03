// Check this:
ACMD(do_in_game_mall)

// Add above:

ACMD(do_support_system)
{
	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));
	if (!*arg1)
		return;
	
	DWORD items = 0;
	str_to_number(items, arg1);
	if (ch->GetSupportSystem()->IsActiveSupport())
	{
		CSupportSystem* supportSystem = ch->GetSupportSystem();
		for (int i = 0; i < INVENTORY_MAX_NUM; i++)
		{
			LPITEM item = ch->GetInventoryItem(i);
			LPITEM pSummonItem = ITEM_MANAGER::instance().FindByVID(ch->GetSupportSystem()->GetActiveSupport()->GetSummonItemVID());
			if (item != NULL)
				if (item->GetVnum() == items)
				{
					if (item->GetType() == ITEM_COSTUME)
					{
						if (item->IsExchanging())
						{
							ch->ChatPacket(CHAT_TYPE_INFO, "<Support System> You can not do this when you are exchanging!");
							return;
						}
						if(item->GetSubType() == COSTUME_BODY)
						{
							item->ClearAttribute();
							pSummonItem->SetSocket(1,item->GetVnum());
							item->RemoveFromCharacter();
							break;
						}
						else
						{
							ch->ChatPacket(CHAT_TYPE_INFO, "<Support System> You can not put this item!");
							return;
						}	
					}
					
				}
		}
		ch->GetSupportSystem()->GetActiveSupport()->RefreshCostume();
	}
	else
		ch->ChatPacket(CHAT_TYPE_INFO, "<Support System> You have to call your support for use this function.");
}
ACMD(do_support_system_d)
{
	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));
	if (!*arg1)
		return;
	
	DWORD items = 0;
	str_to_number(items, arg1);
	if (ch->GetSupportSystem()->IsActiveSupport())
	{
		CSupportSystem* supportSystem = ch->GetSupportSystem();
		for (int i = 0; i < INVENTORY_MAX_NUM; i++)
		{
			LPITEM item = ch->GetInventoryItem(i);
			LPITEM pSummonItem = ITEM_MANAGER::instance().FindByVID(ch->GetSupportSystem()->GetActiveSupport()->GetSummonItemVID());
			if (item != NULL)
				if (item->GetVnum() == items)
				{
					if (item->GetType() == ITEM_COSTUME)
					{
						if (item->IsExchanging())
						{
							ch->ChatPacket(CHAT_TYPE_INFO, "<Support System> You can not do this when you are exchanging!");
							return;
						}
						if (item->GetSubType() == COSTUME_HAIR)
						{
							item->ClearAttribute();
							pSummonItem->SetSocket(2,item->GetValue(3));
							item->RemoveFromCharacter();
							break;
						}
						else
						{
							ch->ChatPacket(CHAT_TYPE_INFO, "<Support System> You can not put this item!");
							return;
						}
					}
					
				}
		}
		ch->GetSupportSystem()->GetActiveSupport()->RefreshCostume();
	}
	else
		ch->ChatPacket(CHAT_TYPE_INFO, "<Support System> You have to call your support for use this function.");
}