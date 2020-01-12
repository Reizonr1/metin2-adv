Cauta ------------

ACMD(do_group_random)

ÜSTÜNE EKLENÝR ------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
		else if (item->IsSkillBook())
		{
			int iEmptyPos = ch->GetEmptySkillBookInventory(item->GetSize());
			
			if (iEmptyPos != -1)
			{
				item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
				LogManager::instance().ItemLog(ch, item, "GM", item->GetName());
			}
			else
			{
				M2_DESTROY_ITEM(item);
				ch->ChatPacket(CHAT_TYPE_INFO, "Not enough inventory space.");	
			}
		}
		else if (item->IsUpgradeItem())
		{
			int iEmptyPos = ch->GetEmptyUpgradeItemsInventory(item->GetSize());
			
			if (iEmptyPos != -1)
			{
				item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
				LogManager::instance().ItemLog(ch, item, "GM", item->GetName());
			}
			else
			{
				M2_DESTROY_ITEM(item);
				ch->ChatPacket(CHAT_TYPE_INFO, "Not enough inventory space.");	
			}			
		}
		else if (item->IsStone())
		{
			int iEmptyPos = ch->GetEmptyStoneInventory(item->GetSize());
			
			if (iEmptyPos != -1)
			{
				item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
				LogManager::instance().ItemLog(ch, item, "GM", item->GetName());
			}
			else
			{
				M2_DESTROY_ITEM(item);
				ch->ChatPacket(CHAT_TYPE_INFO, "Not enough inventory space.");	
			}			
		}
		else if (item->IsSandik())
		{
			int iEmptyPos = ch->GetEmptySandikInventory(item->GetSize());
			
			if (iEmptyPos != -1)
			{
				item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
				LogManager::instance().ItemLog(ch, item, "GM", item->GetName());
			}
			else
			{
				M2_DESTROY_ITEM(item);
				ch->ChatPacket(CHAT_TYPE_INFO, "Not enough inventory space.");	
			}			
		}
#endif
		else
		{
			int iEmptyPos = ch->GetEmptyInventory(item->GetSize());

			if (iEmptyPos != -1)
			{
				item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
				LogManager::instance().ItemLog(ch, item, "GM", item->GetName());
			}
			else
			{
				M2_DESTROY_ITEM(item);
				ch->ChatPacket(CHAT_TYPE_INFO, "Envanterde bo? alan yok l?fen bo?alt??.");
			}
		}
	}
	else
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "#%u item not exist by that vnum.", dwVnum);
	}
}
