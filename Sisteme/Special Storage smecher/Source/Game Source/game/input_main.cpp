Cauta --------

pkSafebox->Remove(p->bSafePos);
		pkItem->AddToCharacter(ch, DestPos);
		ITEM_MANAGER::instance().FlushDelayedSave(pkItem);
	}

Adauga sub -------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	else if (pkItem->IsSkillBook())
	{
		if (DRAGON_SOUL_INVENTORY == p->ItemPos.window_type)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("<??> ?? ? ?? ?????."));
			return;
		}
		
		if (p->ItemPos.IsSkillBookInventoryPosition() == false)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("CANNOT_MOVE_ITEM_THIS_WINDOW"));
			return;
		}
		
		pkSafebox->Remove(p->bSafePos);
		pkItem->AddToCharacter(ch, p->ItemPos);
		ITEM_MANAGER::instance().FlushDelayedSave(pkItem);
	}
	else if (pkItem->IsStone())
	{
		if (DRAGON_SOUL_INVENTORY == p->ItemPos.window_type)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("<??> ?? ? ?? ?????."));
			return;
		}
		
		if (p->ItemPos.IsStoneInventoryPosition() == false)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("CANNOT_MOVE_ITEM_THIS_WINDOW"));
			return;
		}
		
		pkSafebox->Remove(p->bSafePos);
		pkItem->AddToCharacter(ch, p->ItemPos);
		ITEM_MANAGER::instance().FlushDelayedSave(pkItem);		
	}
	else if (pkItem->IsSandik())
	{
		if (DRAGON_SOUL_INVENTORY == p->ItemPos.window_type)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("<??> ?? ? ?? ?????."));
			return;
		}
		
		if (p->ItemPos.IsSandikInventoryPosition() == false)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("CANNOT_MOVE_ITEM_THIS_WINDOW"));
			return;
		}
		
		pkSafebox->Remove(p->bSafePos);
		pkItem->AddToCharacter(ch, p->ItemPos);
		ITEM_MANAGER::instance().FlushDelayedSave(pkItem);		
	}
#endif