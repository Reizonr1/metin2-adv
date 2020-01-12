/* 
Burhanbey 
26.07.2018
WJ_SPLIT_INVENTORY
*/

charitem.cpp deschide și adauga

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
		else if (Cell.IsSkillBookInventoryPosition())
			{
				if (bCell < SKILL_BOOK_INVENTORY_SLOT_START)
					return false;
				
				if (bCell > SKILL_BOOK_INVENTORY_SLOT_END)
					return false;
			[....]
			

schimba complet.


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


charitem.cpp ve char.h dosyalarında olan bütün bCell ve bDestCell fonksiyonlarını böyle yap

BYTE bCell
BYTE bDestCell 

fonksiyonlarını 

UINT bCell
UINT bDestCell

Yap çok önemli.


----------------------------------------------------------------------------------------

charitem.cpp aç ve bul

int CHARACTER::CountSpecifyItem(DWORD vnum) const


içinde bunu ara.

				count += item->GetCount();
			}
		}
	}
	
burdan sonra yapıştır.

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	for (int i = SKILL_BOOK_INVENTORY_SLOT_START; i < SKILL_BOOK_INVENTORY_SLOT_END; ++i)
	{
		item = GetSkillBookInventoryItem(i);
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
		item = GetUpgradeItemsInventoryItem(i);
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
		item = GetStoneInventoryItem(i);
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
		item = GetSandikInventoryItem(i);
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


------------------------------------------------------------------------------------------

charitem.cpp aç ve ara

void CHARACTER::RemoveSpecifyItem(DWORD vnum, DWORD count)

içinde bunu bul.

		else
		{
			GetInventoryItem(i)->SetCount(GetInventoryItem(i)->GetCount() - count);
			return;
		}
	}

pune dedesupt

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	for (UINT i = SKILL_BOOK_INVENTORY_SLOT_START; i < SANDIK_INVENTORY_SLOT_END; ++i)
	{
		if (NULL == GetInventoryItem(i))
			continue;

		if (GetInventoryItem(i)->GetVnum() != vnum)
			continue;

		//개인 상점에 등록된 물건이면 넘어간다. (개인 상점에서 판매될때 이 부분으로 들어올 경우 문제!)
		if(m_pkMyShop)
		{
			bool isItemSelling = m_pkMyShop->IsSellingItem(GetInventoryItem(i)->GetID());
			if (isItemSelling)
				continue;
		}

		if (vnum >= 80003 && vnum <= 80007)
			LogManager::instance().GoldBarLog(GetPlayerID(), GetInventoryItem(i)->GetID(), QUEST, "RemoveSpecifyItem");

		if (count >= GetInventoryItem(i)->GetCount())
		{
			count -= GetInventoryItem(i)->GetCount();
			GetInventoryItem(i)->SetCount(0);

			if (0 == count)
				return;
		}
		else
		{
			GetInventoryItem(i)->SetCount(GetInventoryItem(i)->GetCount() - count);
			return;
		}
	}
#endif

-----------------------------------------------------------------------------------------------------


charitem.cpp aç ve bul

int CHARACTER::CountSpecifyTypeItem(BYTE type) const

altında bunu ara

			count += pItem->GetCount();
		}
	}

pune dedesupt.

	for (int i = SKILL_BOOK_INVENTORY_SLOT_START; i < SANDIK_INVENTORY_SLOT_END; ++i)
	{
		LPITEM pItem = GetInventoryItem(i);
		if (pItem != NULL && pItem->GetType() == type)
		{
			count += pItem->GetCount();
		}
	}

--------------------------------------------------------------------------------------------


charitem.cpp aç ve cauta

void CHARACTER::RemoveSpecifyTypeItem(BYTE type, DWORD count)

gaseste sub

		else
		{
			GetInventoryItem(i)->SetCount(GetInventoryItem(i)->GetCount() - count);
			return;
		}
	}

pune dedesupt

	for (UINT i = SKILL_BOOK_INVENTORY_SLOT_START; i < SANDIK_INVENTORY_SLOT_END; ++i)
	{
		if (NULL == GetInventoryItem(i))
			continue;

		if (GetInventoryItem(i)->GetType() != type)
			continue;

		//개인 상점에 등록된 물건이면 넘어간다. (개인 상점에서 판매될때 이 부분으로 들어올 경우 문제!)
		if(m_pkMyShop)
		{
			bool isItemSelling = m_pkMyShop->IsSellingItem(GetInventoryItem(i)->GetID());
			if (isItemSelling)
				continue;
		}

		if (count >= GetInventoryItem(i)->GetCount())
		{
			count -= GetInventoryItem(i)->GetCount();
			GetInventoryItem(i)->SetCount(0);

			if (0 == count)
				return;
		}
		else
		{
			GetInventoryItem(i)->SetCount(GetInventoryItem(i)->GetCount() - count);
			return;
		}
	}
	
-----------------------------------------------------------------------------------------------


offlineshopmanager.cpp cauta

void COfflineShopManager::Giveback(LPCHARACTER ch)

gaseste sub

			if (pItem->IsDragonSoul())
				iEmptyPos = ch->GetEmptyDragonSoulInventory(pItem);

pune dedesupt

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
			else if (pItem->IsSkillBook())
				iEmptyPos = ch->GetEmptySkillBookInventory(pItem->GetSize());
			else if (pItem->IsUpgradeItem())
				iEmptyPos = ch->GetEmptyUpgradeItemsInventory(pItem->GetSize());
			else if (pItem->IsStone())
				iEmptyPos = ch->GetEmptyStoneInventory(pItem->GetSize());
			else if (pItem->IsSandik())
				iEmptyPos = ch->GetEmptySandikInventory(pItem->GetSize());
#endif

-------------------------------


cauta bunu

			if (pItem->IsDragonSoul())
				pItem->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
			
pune dedesupt

			else if (pItem->IsSkillBook())
				pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			else if (pItem->IsUpgradeItem())
				pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			else if (pItem->IsStone())
				pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			else if (pItem->IsSandik())
				pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			
------------------------------


cauta functia asta

void COfflineShopManager::Giveback3(LPCHARACTER ch)

sub el cauta
			if (pItem->IsDragonSoul())
				iEmptyPos = ch->GetEmptyDragonSoulInventory(pItem);

pune dedesupt

			else if (pItem->IsSkillBook())
				iEmptyPos = ch->GetEmptySkillBookInventory(pItem->GetSize());
			else if (pItem->IsUpgradeItem())
				iEmptyPos = ch->GetEmptyUpgradeItemsInventory(pItem->GetSize());
			else if (pItem->IsStone())
				iEmptyPos = ch->GetEmptyStoneInventory(pItem->GetSize());
			else if (pItem->IsSandik())
				iEmptyPos = ch->GetEmptySandikInventory(pItem->GetSize());

----------------------------------

gaseste sub

			if (pItem->IsDragonSoul())
				pItem->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));

pune dedesupt

			else if (pItem->IsSkillBook())
				pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			else if (pItem->IsUpgradeItem())
				pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			else if (pItem->IsStone())
				pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			else if (pItem->IsSandik())
				pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
---------------------------------


gaseste functia asta

void COfflineShopManager::Giveback2(LPCHARACTER ch)

gaseste sub 

			if (pItem->IsDragonSoul())
				iEmptyPos = ch->GetEmptyDragonSoulInventory(pItem);

pune dedesupt

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
			else if (pItem->IsSkillBook())
				iEmptyPos = ch->GetEmptySkillBookInventory(pItem->GetSize());
			else if (pItem->IsUpgradeItem())
				iEmptyPos = ch->GetEmptyUpgradeItemsInventory(pItem->GetSize());
			else if (pItem->IsStone())
				iEmptyPos = ch->GetEmptyStoneInventory(pItem->GetSize());
			else if (pItem->IsSandik())
				iEmptyPos = ch->GetEmptySandikInventory(pItem->GetSize());
#endif

-------------------------------------


gaseste sub

			if (pItem->IsDragonSoul())
				pItem->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));

pune dedesupt

			else if (pItem->IsSkillBook())
				pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			else if (pItem->IsUpgradeItem())
				pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			else if (pItem->IsStone())
				pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			else if (pItem->IsSandik())
				pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));

--------------------------------------

gaseste functia asta

void COfflineShopManager::RemoveItem(LPCHARACTER ch, BYTE bPos)

cauta mai jos

		if (pItem->IsDragonSoul())
			iEmptyPos = ch->GetEmptyDragonSoulInventory(pItem);

pune dedesupt

		else if (pItem->IsSkillBook())
			iEmptyPos = ch->GetEmptySkillBookInventory(pItem->GetSize());
		else if (pItem->IsUpgradeItem())
			iEmptyPos = ch->GetEmptyUpgradeItemsInventory(pItem->GetSize());
		else if (pItem->IsStone())
			iEmptyPos = ch->GetEmptyStoneInventory(pItem->GetSize());
		else if (pItem->IsSandik())
			iEmptyPos = ch->GetEmptySandikInventory(pItem->GetSize());
------------------------------------------

gaseste sub el

		if (pItem->IsDragonSoul())
			pItem->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));

pune dedesupt

		else if (pItem->IsSkillBook())
			pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
		else if (pItem->IsUpgradeItem())
			pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
		else if (pItem->IsStone())
			pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
		else if (pItem->IsSandik())
			pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));

--------------------------------------

cauta mai jos

		if (pItem->IsDragonSoul())
			iEmptyPos = ch->GetEmptyDragonSoulInventory(pItem);

pune dedesupt

		else if (pItem->IsSkillBook())
			iEmptyPos = ch->GetEmptySkillBookInventory(pItem->GetSize());
		else if (pItem->IsUpgradeItem())
			iEmptyPos = ch->GetEmptyUpgradeItemsInventory(pItem->GetSize());
		else if (pItem->IsStone())
			iEmptyPos = ch->GetEmptyStoneInventory(pItem->GetSize());
		else if (pItem->IsSandik())
			iEmptyPos = ch->GetEmptySandikInventory(pItem->GetSize());
------------------------------------------

gaseste sub el

		if (pItem->IsDragonSoul())
			pItem->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));

pune dedesupt

		else if (pItem->IsSkillBook())
			pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
		else if (pItem->IsUpgradeItem())
			pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
		else if (pItem->IsStone())
			pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
		else if (pItem->IsSandik())
			pItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));

offlineshopmanager.cpp bitti.
------------------------------------------------------------------------------

offlineshop.cpp aç ve cauta

int COfflineShop::Buy(LPCHARACTER ch, BYTE bPos)

altına bunu cauta

	if (pItem->IsDragonSoul())
		iEmptyPos = ch->GetEmptyDragonSoulInventory(pItem);

pune dedesupt


#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	else if (pItem->IsSkillBook())
		iEmptyPos = ch->GetEmptySkillBookInventory(pItem->GetSize());
	else if (pItem->IsUpgradeItem())
		iEmptyPos = ch->GetEmptyUpgradeItemsInventory(pItem->GetSize());
	else if (pItem->IsStone())
		iEmptyPos = ch->GetEmptyStoneInventory(pItem->GetSize());
	else if (pItem->IsSandik())
		iEmptyPos = ch->GetEmptySandikInventory(pItem->GetSize());
#endif

sonra gaseste sub

	if (pItem->IsDragonSoul())
		pItem->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));

pune dedesupt

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	else if (pItem->IsSkillBook())
		pItem->AddToCharacter(ch, TItemPos(INVENTORY,iEmptyPos));
	else if (pItem->IsUpgradeItem())
		pItem->AddToCharacter(ch, TItemPos(INVENTORY,iEmptyPos));
	else if (pItem->IsStone())
		pItem->AddToCharacter(ch, TItemPos(INVENTORY,iEmptyPos));
	else if (pItem->IsSandik())
		pItem->AddToCharacter(ch, TItemPos(INVENTORY,iEmptyPos));
#endif

offlineshop.cpp bitti

-------------------------------------------------

over9refine.cpp aç ve cauta

bool COver9RefineManager::Change9ToOver9(LPCHARACTER pChar, LPITEM item)

bunu bul schimba complet


bool COver9RefineManager::Change9ToOver9(LPCHARACTER pChar, LPITEM item)
{
	OVER9ITEM_MAP::iterator iter = m_mapItem.find(item->GetVnum());

	if (iter == m_mapItem.end())
		return false;

	DWORD dwVnum = iter->second;

	LPITEM over9 = ITEM_MANAGER::instance().CreateItem(dwVnum, 1);

	if (over9 == NULL)
		return false;

	item->CopySocketTo(over9);
	item->CopyAttributeTo(over9);

	int iEmptyCell = pChar->GetEmptyInventory(over9->GetSize());
	int iEmptyCell1 = pChar->GetEmptySkillBookInventory(over9->GetSize());
	int iEmptyCell2 = pChar->GetEmptyUpgradeItemsInventory(over9->GetSize());
	int iEmptyCell3 = pChar->GetEmptyStoneInventory(over9->GetSize());
	int iEmptyCell4 = pChar->GetEmptySandikInventory(over9->GetSize());

	if (iEmptyCell == -1)
		return false;

	else if (iEmptyCell1 == -1)
		return false;

	else if (iEmptyCell2 == -1)
		return false;

	else if (iEmptyCell3 == -1)
		return false;

	else if (iEmptyCell4 == -1)
		return false;

	item->RemoveFromCharacter();

	over9->AddToCharacter(pChar, TItemPos(INVENTORY, iEmptyCell));
	over9->AddToCharacter(pChar, TItemPos(INVENTORY, iEmptyCell1));
	over9->AddToCharacter(pChar, TItemPos(INVENTORY, iEmptyCell2));
	over9->AddToCharacter(pChar, TItemPos(INVENTORY, iEmptyCell3));
	over9->AddToCharacter(pChar, TItemPos(INVENTORY, iEmptyCell4));

	char szBuf[256];
	snprintf(szBuf, sizeof(szBuf), "SUCCESS %u %s %u", over9->GetID(), over9->GetName(), over9->GetOriginalVnum());
	LogManager::instance().ItemLog(pChar, item, "REFINE OVER9", szBuf);
	return true;
}


sonra bunu bul schimba complet

bool COver9RefineManager::Over9Refine(LPCHARACTER pChar, LPITEM item)

bununla


bool COver9RefineManager::Over9Refine(LPCHARACTER pChar, LPITEM item)
{
	DWORD dwVnum = item->GetRefinedVnum();

	if (dwVnum == 0)
		return false;

	LPITEM over9 = ITEM_MANAGER::instance().CreateItem(dwVnum, 1);

	if (over9 == NULL)
		return false;

	item->CopySocketTo(over9);
	item->CopyAttributeTo(over9);

	int iEmptyCell = pChar->GetEmptyInventory(over9->GetSize());
	int iEmptyCell1 = pChar->GetEmptySkillBookInventory(over9->GetSize());
	int iEmptyCell2 = pChar->GetEmptyUpgradeItemsInventory(over9->GetSize());
	int iEmptyCell3 = pChar->GetEmptyStoneInventory(over9->GetSize());
	int iEmptyCell4 = pChar->GetEmptySandikInventory(over9->GetSize());

	if (iEmptyCell == -1)
		return false;

	else if (iEmptyCell1 == -1)
		return false;

	else if (iEmptyCell2 == -1)
		return false;

	else if (iEmptyCell3 == -1)
		return false;

	else if (iEmptyCell4 == -1)
		return false;

	item->RemoveFromCharacter();

	over9->AddToCharacter(pChar, TItemPos(INVENTORY, iEmptyCell));
	over9->AddToCharacter(pChar, TItemPos(INVENTORY, iEmptyCell1));
	over9->AddToCharacter(pChar, TItemPos(INVENTORY, iEmptyCell2));
	over9->AddToCharacter(pChar, TItemPos(INVENTORY, iEmptyCell3));
	over9->AddToCharacter(pChar, TItemPos(INVENTORY, iEmptyCell4));

	char szBuf[256];
	snprintf(szBuf, sizeof(szBuf), "SUCCESS %u %s %u", over9->GetID(), over9->GetName(), over9->GetOriginalVnum());
	LogManager::instance().ItemLog(pChar, item, "REFINE OVER9", szBuf);
	return true;
}

over9refine.cpp bitti

-----------------------------------------------------------------------------------

questlua_pc.cpp aç ve cauta


	int pc_enough_inventory(lua_State* L)

schimba complet

	int pc_enough_inventory(lua_State* L)
	{
		LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();
		if (!lua_isnumber(L, 1))
		{
			lua_pushboolean(L, 0);
			return 1;
		}

		DWORD item_vnum = (DWORD)lua_tonumber(L, 1);
		TItemTable * pTable = ITEM_MANAGER::instance().GetTable(item_vnum);
		if (!pTable)
		{
			lua_pushboolean(L, 0);
			return 1;
		}

		bool bEnoughInventoryForItem = ch->GetEmptyInventory(pTable->bSize) != -1;
		bool bEnoughInventoryForItem1 = ch->GetEmptySkillBookInventory(pTable->bSize) != -1;
		bool bEnoughInventoryForItem2 = ch->GetEmptyUpgradeItemsInventory(pTable->bSize) != -1;
		bool bEnoughInventoryForItem3 = ch->GetEmptyStoneInventory(pTable->bSize) != -1;
		bool bEnoughInventoryForItem4 = ch->GetEmptySandikInventory(pTable->bSize) != -1;
		lua_pushboolean(L, bEnoughInventoryForItem);
		lua_pushboolean(L, bEnoughInventoryForItem1);
		lua_pushboolean(L, bEnoughInventoryForItem2);
		lua_pushboolean(L, bEnoughInventoryForItem3);
		lua_pushboolean(L, bEnoughInventoryForItem4);
		return 1;
	}

bitti
-----------------------------------------------------------------------------------------------

shop.cpp aç ve cauta

int CShop::Buy(LPCHARACTER ch, BYTE pos)

gaseste sub

	if (item->IsDragonSoul())
	{
		iEmptyPos = ch->GetEmptyDragonSoulInventory(item);
	}
pune dedesupt

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	else if (item->IsSkillBook())
	{
		iEmptyPos = ch->GetEmptySkillBookInventory(item->GetSize());
	}
	else if (item->IsUpgradeItem())
	{
		iEmptyPos = ch->GetEmptyUpgradeItemsInventory(item->GetSize());
	}
	else if (item->IsStone())
	{
		iEmptyPos = ch->GetEmptyStoneInventory(item->GetSize());
	}
	else if (item->IsSandik())
	{
		iEmptyPos = ch->GetEmptySandikInventory(item->GetSize());
	}
#endif

bitti
----------------------------------------------------------

shopex.cpp aç ve cauta

int CShopEx::Buy(LPCHARACTER ch, BYTE pos)

gaseste sub

	if (item->IsDragonSoul())
	{
		iEmptyPos = ch->GetEmptyDragonSoulInventory(item);
	}

pune dedesupt

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	else if (item->IsSkillBook())
	{
		iEmptyPos = ch->GetEmptySkillBookInventory(item->GetSize());
	}
	else if (item->IsUpgradeItem())
	{
		iEmptyPos = ch->GetEmptyUpgradeItemsInventory(item->GetSize());
	}
	else if (item->IsStone())
	{
		iEmptyPos = ch->GetEmptyStoneInventory(item->GetSize());
	}
	else if (item->IsSandik())
	{
		iEmptyPos = ch->GetEmptySandikInventory(item->GetSize());
	}
#endif

bitti
---------------------------------------------------------------

































