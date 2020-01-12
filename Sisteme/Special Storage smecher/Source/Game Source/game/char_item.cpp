Cauta ------------------

LPITEM CHARACTER::GetInventoryItem(WORD wCell) const

Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
LPITEM CHARACTER::GetSkillBookInventoryItem(WORD wCell) const
{
	return GetItem(TItemPos(INVENTORY, wCell));
}
LPITEM CHARACTER::GetUpgradeItemsInventoryItem(WORD wCell) const
{
	return GetItem(TItemPos(INVENTORY, wCell));
}
LPITEM CHARACTER::GetStoneInventoryItem(WORD wCell) const
{
	return GetItem(TItemPos(INVENTORY, wCell));
}
LPITEM CHARACTER::GetSandikInventoryItem(WORD wCell) const
{
	return GetItem(TItemPos(INVENTORY, wCell));
}
#endif

Cauta ------------------

	case INVENTORY:
		{
			BYTE bCell = Cell.cell;

			// bItemCell? 0? false?? ???? ?? + 1 ?? ????.
			// ??? iExceptionCell? 1? ?? ????.
			++iExceptionCell;

			if (Cell.IsBeltInventoryPosition())
			{
				LPITEM beltItem = GetWear(WEAR_BELT);

				if (NULL == beltItem)
					return false;

				if (false == CBeltInventoryHelper::IsAvailableCell(bCell - BELT_INVENTORY_SLOT_START, beltItem->GetValue(0)))
					return false;

				if (m_pointsInstant.bItemGrid[bCell])
				{
					if (m_pointsInstant.bItemGrid[bCell] == iExceptionCell)
						return true;

					return false;
				}

				if (bSize == 1)
					return true;

			}

Adauga sub ----------------

sonraki } sonuna eklenir ;

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
			else if (Cell.IsSkillBookInventoryPosition())
			{
				if (bCell < SKILL_BOOK_INVENTORY_SLOT_START)
					return false;
				
				if (bCell > SKILL_BOOK_INVENTORY_SLOT_END)
					return false;
				
				if (m_pointsInstant.bItemGrid[bCell] == (UINT)iExceptionCell)
				{
					if (bSize == 1)
						return true;

					int j = 1;
					BYTE bPage = bCell / (SKILL_BOOK_INVENTORY_MAX_NUM / 3);

					do
					{
						UINT p = bCell + (5 * j);

						if (p >= SKILL_BOOK_INVENTORY_MAX_NUM)
							return false;

						if (p / (SKILL_BOOK_INVENTORY_MAX_NUM / 3) != bPage)
							return false;

						if (m_pointsInstant.bItemGrid[p])
							if (m_pointsInstant.bItemGrid[p] != iExceptionCell)
								return false;
					}
					while (++j < bSize);

					return true;
				}
			}
			else if (Cell.IsUpgradeItemsInventoryPosition())
			{
				if (bCell < UPGRADE_ITEMS_INVENTORY_SLOT_START)
					return false;
				
				if (bCell > UPGRADE_ITEMS_INVENTORY_SLOT_END)
					return false;
				
				if (m_pointsInstant.bItemGrid[bCell] == (UINT)iExceptionCell)
				{
					if (bSize == 1)
						return true;

					int j = 1;
					BYTE bPage = bCell / (UPGRADE_ITEMS_INVENTORY_MAX_NUM / 3);

					do
					{
						UINT p = bCell + (5 * j);

						if (p >= UPGRADE_ITEMS_INVENTORY_MAX_NUM)
							return false;

						if (p / (UPGRADE_ITEMS_INVENTORY_MAX_NUM / 3) != bPage)
							return false;

						if (m_pointsInstant.bItemGrid[p])
							if (m_pointsInstant.bItemGrid[p] != iExceptionCell)
								return false;
					}
					while (++j < bSize);

					return true;
				}
			}
			else if (Cell.IsStoneInventoryPosition())
			{
				if (bCell < STONE_INVENTORY_SLOT_START)
					return false;
				
				if (bCell > STONE_INVENTORY_SLOT_END)
					return false;
				
				if (m_pointsInstant.bItemGrid[bCell] == (UINT)iExceptionCell)
				{
					if (bSize == 1)
						return true;

					int j = 1;
					BYTE bPage = bCell / (STONE_INVENTORY_MAX_NUM / 3);

					do
					{
						UINT p = bCell + (5 * j);

						if (p >= STONE_INVENTORY_MAX_NUM)
							return false;

						if (p / (STONE_INVENTORY_MAX_NUM / 3) != bPage)
							return false;

						if (m_pointsInstant.bItemGrid[p])
							if (m_pointsInstant.bItemGrid[p] != iExceptionCell)
								return false;
					}
					while (++j < bSize);

					return true;
				}
			}
			else if (Cell.IsSandikInventoryPosition())
			{
				if (bCell < SANDIK_INVENTORY_SLOT_START)
					return false;
				
				if (bCell > SANDIK_INVENTORY_SLOT_END)
					return false;
				
				if (m_pointsInstant.bItemGrid[bCell] == (UINT)iExceptionCell)
				{
					if (bSize == 1)
						return true;

					int j = 1;
					BYTE bPage = bCell / (SANDIK_INVENTORY_MAX_NUM / 3);

					do
					{
						UINT p = bCell + (5 * j);

						if (p >= SANDIK_INVENTORY_MAX_NUM)
							return false;

						if (p / (SANDIK_INVENTORY_MAX_NUM / 3) != bPage)
							return false;

						if (m_pointsInstant.bItemGrid[p])
							if (m_pointsInstant.bItemGrid[p] != iExceptionCell)
								return false;
					}
					while (++j < bSize);

					return true;
				}
			}
#endif

Cauta ------------------

int CHARACTER::GetEmptyDragonSoulInventory(LPITEM pItem) const

Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
int CHARACTER::GetEmptySkillBookInventory(BYTE size) const
{
	for (int i = SKILL_BOOK_INVENTORY_SLOT_START; i < SKILL_BOOK_INVENTORY_SLOT_END; ++i)
		if (IsEmptyItemGrid(TItemPos(INVENTORY, i), size))
			return i;
		
	return -1;
}

int CHARACTER::GetEmptyUpgradeItemsInventory(BYTE size) const
{
	for (int i = UPGRADE_ITEMS_INVENTORY_SLOT_START; i < UPGRADE_ITEMS_INVENTORY_SLOT_END; ++i)
		if (IsEmptyItemGrid(TItemPos(INVENTORY, i), size))
			return i;
		
	return -1;	
}

int CHARACTER::GetEmptyStoneInventory(BYTE size) const
{
	for (int i = STONE_INVENTORY_SLOT_START; i < STONE_INVENTORY_SLOT_END; ++i)
		if (IsEmptyItemGrid(TItemPos(INVENTORY, i), size))
			return i;
		
	return -1;	
}

int CHARACTER::GetEmptySandikInventory(BYTE size) const
{
	for (int i = SANDIK_INVENTORY_SLOT_START; i < SANDIK_INVENTORY_SLOT_END; ++i)
		if (IsEmptyItemGrid(TItemPos(INVENTORY, i), size))
			return i;
		
	return -1;	
}
#endif


Cauta ------------------

if (DestCell.IsBeltInventoryPosition() && false == CBeltInventoryHelper::CanMoveIntoBeltInventory(item))

Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	//envanterden bk envanterine item alamaz.
	if (Cell.IsSkillBookInventoryPosition() && !DestCell.IsSkillBookInventoryPosition())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("DEPOLAMA_ENVANTER_1"));
		return false;
	}
	//envanterden yukseltme envanterine item alamaz.
	if (Cell.IsUpgradeItemsInventoryPosition() && !DestCell.IsUpgradeItemsInventoryPosition())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("DEPOLAMA_ENVANTER_1"));
		return false;
	}
	//envanterden ta? envanterine item alamaz.
	if (Cell.IsStoneInventoryPosition() && !DestCell.IsStoneInventoryPosition())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("DEPOLAMA_ENVANTER_1"));
		return false;
	}
	//
	if (Cell.IsDefaultInventoryPosition() && DestCell.IsSkillBookInventoryPosition())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("DEPOLAMA_ENVANTER_2"));
		return false;
	}
	
	if (Cell.IsDefaultInventoryPosition() && DestCell.IsUpgradeItemsInventoryPosition())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("DEPOLAMA_ENVANTER_3"));
		return false;
	}
	
	if (Cell.IsDefaultInventoryPosition() && DestCell.IsStoneInventoryPosition())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("DEPOLAMA_ENVANTER_4"));
		return false;
	}
	//BUG F?X. TAKILI OLAN ?TEM? BK ENVANTER?NE ALMA
	if (Cell.IsEquipPosition() && DestCell.IsSkillBookInventoryPosition())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("DEPOLAMA_ENVANTER_7"));
		return false;
	}
	//BUG F?X. TAKILI OLAN ?TEM? YUKSELTME ENVANTER?NE ALMA
	if (Cell.IsEquipPosition() && DestCell.IsUpgradeItemsInventoryPosition())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("DEPOLAMA_ENVANTER_8"));
		return false;
	}
	//BUG F?X. TAKILI OLAN ?TEM? TA? ENVANTER?NE ALMA
	if (Cell.IsEquipPosition() && DestCell.IsStoneInventoryPosition())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("DEPOLAMA_ENVANTER_9"));
		return false;
	}
	//SANDIK S?STEM?
	if (Cell.IsSandikInventoryPosition() && !DestCell.IsSandikInventoryPosition())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("DEPOLAMA_ENVANTER_1"));
		return false;
	}
	if (Cell.IsDefaultInventoryPosition() && DestCell.IsSandikInventoryPosition())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("DEPOLAMA_ENVANTER_10"));
		return false;
	}
	if (Cell.IsEquipPosition() && DestCell.IsSandikInventoryPosition())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("DEPOLAMA_ENVANTER_11"));
		return false;
	}
#endif

Cauta ------------------
				int iEmptyCell;
				if (item->IsDragonSoul())
				{
					if ((iEmptyCell = GetEmptyDragonSoulInventory(item)) == -1)
					{
						sys_log(0, "No empty ds inventory pid %u size %ud itemid %u", GetPlayerID(), item->GetSize(), item->GetID());
						ChatPacket(CHAT_TYPE_INFO, LC_TEXT("???? ?? ???? ?? ????."));
						return false;
					}
				}

Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
				else if (item->IsSkillBook())
				{
					if ((iEmptyCell = GetEmptySkillBookInventory(item->GetSize())) == -1)
					{
						sys_log(0, "No empty ds inventory pid %u size %ud itemid %u", GetPlayerID(), item->GetSize(), item->GetID());
						ChatPacket(CHAT_TYPE_INFO, LC_TEXT("???? ?? ???? ?? ????."));
						return false;
					}
				}
				else if (item->IsUpgradeItem())
				{
					if ((iEmptyCell = GetEmptyUpgradeItemsInventory(item->GetSize())) == -1)
					{
						sys_log(0, "No empty ds inventory pid %u size %ud itemid %u", GetPlayerID(), item->GetSize(), item->GetID());
						ChatPacket(CHAT_TYPE_INFO, LC_TEXT("???? ?? ???? ?? ????."));
						return false;
					}					
				}
				else if (item->IsStone())
				{
					if ((iEmptyCell = GetEmptyStoneInventory(item->GetSize())) == -1)
					{
						sys_log(0, "No empty ds inventory pid %u size %ud itemid %u", GetPlayerID(), item->GetSize(), item->GetID());
						ChatPacket(CHAT_TYPE_INFO, LC_TEXT("???? ?? ???? ?? ????."));
						return false;
					}					
				}
				else if (item->IsSandik())
				{
					if ((iEmptyCell = GetEmptySandikInventory(item->GetSize())) == -1)
					{
						sys_log(0, "No empty ds inventory pid %u size %ud itemid %u", GetPlayerID(), item->GetSize(), item->GetID());
						ChatPacket(CHAT_TYPE_INFO, LC_TEXT("???? ?? ???? ?? ????."));
						return false;
					}					
				}
#endif

Cauta ------------------

				if (item->IsDragonSoul())
					item->AddToCharacter(this, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyCell));

Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
				else if (item->IsSkillBook())
					item->AddToCharacter(this, TItemPos(INVENTORY, iEmptyCell));
				else if (item->IsUpgradeItem())
					item->AddToCharacter(this, TItemPos(INVENTORY, iEmptyCell));
				else if (item->IsStone())
					item->AddToCharacter(this, TItemPos(INVENTORY, iEmptyCell));
				else if (item->IsSandik())
					item->AddToCharacter(this, TItemPos(INVENTORY, iEmptyCell));
#endif

Cauta ------------------

if (item->IsDragonSoul())
			{
				if (!(owner && (iEmptyCell = owner->GetEmptyDragonSoulInventory(item)) != -1))
				{
					owner = this;

					if ((iEmptyCell = GetEmptyDragonSoulInventory(item)) == -1)
					{
						owner->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("???? ?? ???? ?? ????."));
						return false;
					}
				}
			}

Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
			else if (item->IsSkillBook())
			{
				if (!(owner && (iEmptyCell = owner->GetEmptySkillBookInventory(item->GetSize())) != -1))
				{
					owner = this;

					if ((iEmptyCell = GetEmptySkillBookInventory(item->GetSize())) == -1)
					{
						owner->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("???? ?? ???? ?? ????."));
						return false;
					}
				}				
			}
			else if (item->IsUpgradeItem())
			{
				if (!(owner && (iEmptyCell = owner->GetEmptyUpgradeItemsInventory(item->GetSize())) != -1))
				{
					owner = this;

					if ((iEmptyCell = GetEmptyUpgradeItemsInventory(item->GetSize())) == -1)
					{
						owner->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("???? ?? ???? ?? ????."));
						return false;
					}
				}					
			}
			else if (item->IsStone())
			{
				if (!(owner && (iEmptyCell = owner->GetEmptyStoneInventory(item->GetSize())) != -1))
				{
					owner = this;

					if ((iEmptyCell = GetEmptyStoneInventory(item->GetSize())) == -1)
					{
						owner->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("???? ?? ???? ?? ????."));
						return false;
					}
				}					
			}
			else if (item->IsSandik())
			{
				if (!(owner && (iEmptyCell = owner->GetEmptySandikInventory(item->GetSize())) != -1))
				{
					owner = this;

					if ((iEmptyCell = GetEmptySandikInventory(item->GetSize())) == -1)
					{
						owner->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("???? ?? ???? ?? ????."));
						return false;
					}
				}					
			}
#endif

Cauta ------------------

if (item->IsDragonSoul())
				item->AddToCharacter(owner, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyCell));

Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
			else if (item->IsSkillBook())
				item->AddToCharacter(owner, TItemPos(INVENTORY, iEmptyCell));
			else if (item->IsUpgradeItem())
				item->AddToCharacter(owner, TItemPos(INVENTORY, iEmptyCell));
			else if (item->IsStone())
				item->AddToCharacter(owner, TItemPos(INVENTORY, iEmptyCell));
			else if (item->IsSandik())
				item->AddToCharacter(owner, TItemPos(INVENTORY, iEmptyCell));
#endif

Cauta ------------------

bool CHARACTER::UnequipItem(LPITEM item)

DEÐÝÞTÝR ----------------

bool CHARACTER::UnequipItem(LPITEM item)
{
	int pos;

	if (false == CanUnequipNow(item))
		return false;

	if (item->IsDragonSoul())
		pos = GetEmptyDragonSoulInventory(item);
#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	else if (item->IsSkillBook())
		pos = GetEmptySkillBookInventory(item->GetSize());
	else if (item->IsUpgradeItem())
		pos = GetEmptyUpgradeItemsInventory(item->GetSize());
	else if (item->IsStone())
		pos = GetEmptyStoneInventory(item->GetSize());
	else if (item->IsSandik())
		pos = GetEmptySandikInventory(item->GetSize());
#endif
	else
		pos = GetEmptyInventory(item->GetSize());

	// HARD CODING
	if (item->GetVnum() == UNIQUE_ITEM_HIDE_ALIGNMENT_TITLE)
		ShowAlignment(true);

	item->RemoveFromCharacter();
	if (item->IsDragonSoul())
#ifdef __HIGHLIGHT_SYSTEM__
		item->AddToCharacter(this, TItemPos(DRAGON_SOUL_INVENTORY, pos), false);
#else
		item->AddToCharacter(this, TItemPos(DRAGON_SOUL_INVENTORY, pos));
#endif
#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	else if (item->IsSkillBook())
#ifdef __HIGHLIGHT_SYSTEM__
		item->AddToCharacter(this, TItemPos(INVENTORY, pos), false);
#else
		item->AddToCharacter(this, TItemPos(INVENTORY, pos));
#endif
	else if (item->IsUpgradeItem())
#ifdef __HIGHLIGHT_SYSTEM__
		item->AddToCharacter(this, TItemPos(INVENTORY, pos), false);
#else
		item->AddToCharacter(this, TItemPos(INVENTORY, pos));
#endif
	else if (item->IsStone())
#ifdef __HIGHLIGHT_SYSTEM__
		item->AddToCharacter(this, TItemPos(INVENTORY, pos), false);
#else
		item->AddToCharacter(this, TItemPos(INVENTORY, pos));
#endif
	else if (item->IsSandik())
#ifdef __HIGHLIGHT_SYSTEM__
		item->AddToCharacter(this, TItemPos(INVENTORY, pos), false);
#else
		item->AddToCharacter(this, TItemPos(INVENTORY, pos));
#endif
#endif
	else
#ifdef __HIGHLIGHT_SYSTEM__
		item->AddToCharacter(this, TItemPos(INVENTORY, pos), false);
#else
		item->AddToCharacter(this, TItemPos(INVENTORY, pos));
#endif

	CheckMaximumPoints();

	return true;
}


Cauta ------------------

int CHARACTER::CountSpecifyItem(DWORD vnum) const

ALTINDAKÝ  ----

count += item->GetCount();
			}
		}
	}
	
	SONUNA EKLENÝR -----

Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	for (int i = SKILL_BOOK_INVENTORY_SLOT_START; i < SKILL_BOOK_INVENTORY_SLOT_END; ++i)
	{
		item = GetInventoryItem(i);
		if (NULL != item && item->GetVnum() == vnum)
		{
			// ?? ??? ??? ???? ????.
			if (m_pkMyShop && m_pkMyShop->IsSellingItem(item->GetID()))
			{
				continue;
			}
			else
			{
				count += item->GetCount();
			}
		}		
	}
	
	for (int i = UPGRADE_ITEMS_INVENTORY_SLOT_START; i < UPGRADE_ITEMS_INVENTORY_SLOT_END; ++i)
	{
		item = GetInventoryItem(i);
		if (NULL != item && item->GetVnum() == vnum)
		{
			// ?? ??? ??? ???? ????.
			if (m_pkMyShop && m_pkMyShop->IsSellingItem(item->GetID()))
			{
				continue;
			}
			else
			{
				count += item->GetCount();
			}
		}			
	}
	
	for (int i = STONE_INVENTORY_SLOT_START; i < STONE_INVENTORY_SLOT_END; ++i)
	{
		item = GetInventoryItem(i);
		if (NULL != item && item->GetVnum() == vnum)
		{
			// ?? ??? ??? ???? ????.
			if (m_pkMyShop && m_pkMyShop->IsSellingItem(item->GetID()))
			{
				continue;
			}
			else
			{
				count += item->GetCount();
			}
		}			
	}
	
	for (int i = SANDIK_INVENTORY_SLOT_START; i < SANDIK_INVENTORY_SLOT_END; ++i)
	{
		item = GetInventoryItem(i);
		if (NULL != item && item->GetVnum() == vnum)
		{
			// ?? ??? ??? ???? ????.
			if (m_pkMyShop && m_pkMyShop->IsSellingItem(item->GetID()))
			{
				continue;
			}
			else
			{
				count += item->GetCount();
			}
		}			
	}
#endif

Cauta ------------------

int cell;
	if (item->IsDragonSoul())
	{
		cell = GetEmptyDragonSoulInventory(item);
	}

Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	else if (item->IsSkillBook())
	{
		cell = GetEmptySkillBookInventory(item->GetSize());
	}
	else if (item->IsUpgradeItem())
	{
		cell = GetEmptyUpgradeItemsInventory(item->GetSize());
	}
	else if (item->IsStone())
	{
		cell = GetEmptyStoneInventory(item->GetSize());
	}
	else if (item->IsSandik())
	{
		cell = GetEmptySandikInventory(item->GetSize());
	}
#endif

Cauta ------------------

if (cell != -1)
	{
		if (item->IsDragonSoul())
			item->AddToCharacter(this, TItemPos(DRAGON_SOUL_INVENTORY, cell));

Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
		else if (item->IsSkillBook())
			item->AddToCharacter(this, TItemPos(INVENTORY, cell));
		else if (item->IsUpgradeItem())
			item->AddToCharacter(this, TItemPos(INVENTORY, cell));
		else if (item->IsStone())
			item->AddToCharacter(this, TItemPos(INVENTORY, cell));
		else if (item->IsSandik())
			item->AddToCharacter(this, TItemPos(INVENTORY, cell));
#endif

Cauta ------------------

if (item->IsDragonSoul())
			item->AddToCharacter(this, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyCell));

Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
		else if (item->IsSkillBook())
			item->AddToCharacter(this, TItemPos(INVENTORY, iEmptyCell));
		else if (item->IsUpgradeItem())
			item->AddToCharacter(this, TItemPos(INVENTORY, iEmptyCell));
		else if (item->IsStone())
			item->AddToCharacter(this, TItemPos(INVENTORY, iEmptyCell));
		else if (item->IsSandik())
			item->AddToCharacter(this, TItemPos(INVENTORY, iEmptyCell));
#endif

Cauta ------------------

{
		int pos = -1;
		if (item->IsDragonSoul())
			pos = GetEmptyDragonSoulInventory(item);

Adauga sub ----------------

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
		else if (item->IsSkillBook())
			pos = GetEmptySkillBookInventory(item->GetSize());
		else if (item->IsUpgradeItem())
			pos = GetEmptyUpgradeItemsInventory(item->GetSize());
		else if (item->IsStone())
			pos = GetEmptyStoneInventory(item->GetSize());
		else if (item->IsSandik())
			pos = GetEmptySandikInventory(item->GetSize());
#endif

Cauta ------------------

if (pItem)
	
ALTINDAKÝ : case EQUIPMENT:  DEÐÝÞTÝR

DEÐÝÞTÝR ----------------

case EQUIPMENT:
			if ((wCell < INVENTORY_MAX_NUM) || (BELT_INVENTORY_SLOT_START <= wCell && BELT_INVENTORY_SLOT_END > wCell) || (SKILL_BOOK_INVENTORY_SLOT_START <= wCell && SKILL_BOOK_INVENTORY_SLOT_END > wCell) || (UPGRADE_ITEMS_INVENTORY_SLOT_START <= wCell && UPGRADE_ITEMS_INVENTORY_SLOT_END > wCell) || (STONE_INVENTORY_SLOT_START <= wCell && STONE_INVENTORY_SLOT_END > wCell) || (SANDIK_INVENTORY_SLOT_START <= wCell && SANDIK_INVENTORY_SLOT_END > wCell))
				pItem->SetWindow(INVENTORY);
			else
				pItem->SetWindow(EQUIPMENT);
			break;
