// 1) Search: if (IsCubeOpen() || DragonSoul_RefineWindow_GetOpener() != NULL)
// 2) Delete this line and paste:
	if (IsAcceOpen() || IsCubeOpen() || DragonSoul_RefineWindow_GetOpener() != NULL)
		return false;

// 1) Search: BDRAGON_SCROLL = 6,
// 2) After make a new line and paste:
	ACCE_CLEAN_ATTR = 7,

// 1) Search: bool CHARACTER::RefineItem(LPITEM pkItem, LPITEM pkTarget)
// 2) After their function paste:
bool CHARACTER::CleanAcceAttr(LPITEM pkItem, LPITEM pkTarget)
{
	if (!CanHandleItem())
		return false;
	
	if (pkTarget->GetType() != ITEM_COSTUME && pkTarget->GetSubType() != COSTUME_ACCE)
		return false;
	
	if (pkTarget->GetAcceAttributeCount() < 1)
		return false;
	
	if (pkItem->GetValue(0) == ACCE_CLEAN_ATTR)
	{
		LogManager::instance().ItemLog(this, pkTarget, "USE_DETACHMENT", pkTarget->GetName());
		pkTarget->SetForceAttribute(0, 0, 0);
		pkTarget->SetForceAttribute(1, 0, 0);
		pkTarget->SetForceAttribute(2, 0, 0);
		pkTarget->SetForceAttribute(3, 0, 0);
		pkTarget->SetForceAttribute(4, 0, 0);
		pkTarget->SetForceAttribute(5, 0, 0);
		pkTarget->SetForceAttribute(6, 0, 0);
		pkTarget->SetForceAttribute(7, 0, 0);
		pkTarget->SetForceAttribute(8, 0, 0);
		pkTarget->SetForceAttribute(9, 0, 0);
		pkTarget->SetForceAttribute(10, 0, 0);
		pkTarget->SetForceAttribute(11, 0, 0);
		pkTarget->SetForceAttribute(12, 0, 0);
		pkTarget->SetForceAttribute(13, 0, 0);
		pkTarget->SetForceAttribute(14, 0, 0);
		pkItem->SetCount(pkItem->GetCount() - 1);
		return true;
	}
	
	return false;
}

// 1) Search: if (item2->GetVnum() >= 28330 && item2->GetVnum() <= 28343)
// 2) After their function paste:
							if (item->GetValue(0) == ACCE_CLEAN_ATTR)
							{
								CleanAcceAttr(item, item2);
							}

!!!!!!// 1) Search: if (IsCubeOpen() || DragonSoul_RefineWindow_GetOpener() != NULL)
// 2) Delete this line and paste:
	if (IsAcceOpen() || IsCubeOpen() || DragonSoul_RefineWindow_GetOpener() != NULL)

// 1) Search: if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
// 2) Delete this line and paste:
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen() || IsAcceOpen())

// 1) Search: if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
// 2) Delete this line and paste:
		if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen() || IsAcceOpen())

// 1) Search: else if (ITEM_UNIQUE == item->GetType() && 0 != item->GetSIGVnum())
// 2) After their function paste:
		else if (true == CItemVnumHelper::IsAcce_Grade1(dwVnum))
		{
			this->EffectPacket(SE_EQUIP_ACCE_1);
		}
		else if (true == CItemVnumHelper::IsAcce_Grade2(dwVnum))
		{
			this->EffectPacket(SE_EQUIP_ACCE_2);
		}
		else if (true == CItemVnumHelper::IsAcce_Grade3(dwVnum))
		{
			this->EffectPacket(SE_EQUIP_ACCE_3);
		}
		else if (true == CItemVnumHelper::IsAcce_Grade4(dwVnum))
		{
			this->EffectPacket(SE_EQUIP_ACCE_4);
		}

// 1) Search: LPITEM CHARACTER::AutoGiveItem(DWORD dwItemVnum, BYTE bCount, int iRarePct, bool bMsg)
// 2) After their function paste:
LPITEM CHARACTER::AutoGiveAcce(DWORD dwItemVnum, BYTE bCount, int iSocketTwo, int iRarePct, bool bMsg)
{
	TItemTable * p = ITEM_MANAGER::instance().GetTable(dwItemVnum);
	if (!p)
		return NULL;
	
	DBManager::instance().SendMoneyLog(MONEY_LOG_DROP, dwItemVnum, bCount);
	
	if (p->dwFlags & ITEM_FLAG_STACKABLE && p->bType != ITEM_BLEND) 
	{
		for (int i = 0; i < INVENTORY_MAX_NUM; ++i)
		{
			LPITEM item = GetInventoryItem(i);
			if (!item)
				continue;
			
			if (item->GetVnum() == dwItemVnum && FN_check_item_socket(item))
			{
				if (IS_SET(p->dwFlags, ITEM_FLAG_MAKECOUNT))
				{
					if (bCount < p->alValues[1])
						bCount = p->alValues[1];
				}
				
				BYTE bCount2 = MIN(200 - item->GetCount(), bCount);
				bCount -= bCount2;
				
				item->SetCount(item->GetCount() + bCount2);
				if (bCount == 0)
				{
					if (bMsg)
						ChatPacket(CHAT_TYPE_INFO, LC_TEXT("¾ÆÀÌÅÛ È¹µæ: %s"), item->GetName());
					
					return item;
				}
			}
		}
	}
	
	LPITEM item = ITEM_MANAGER::instance().CreateItem(dwItemVnum, bCount, 0, true);
	if (!item)
	{
		sys_err("Cannot create item by vnum %u (name: %s).", dwItemVnum, GetName());
		return NULL;
	}
	
	int iEmptyCell;
	if (item->IsDragonSoul())
	{
		iEmptyCell = GetEmptyDragonSoulInventory(item);
	}
	else
		iEmptyCell = GetEmptyInventory(item->GetSize());
	
	if (iEmptyCell != -1)
	{
		if (bMsg)
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("¾ÆÀÌÅÛ È¹µæ: %s"), item->GetName());
		
		if (item->IsDragonSoul())
			item->AddToCharacter(this, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyCell));
		else
			item->AddToCharacter(this, TItemPos(INVENTORY, iEmptyCell));
		
		item->SetSocket(1, iSocketTwo);
		LogManager::instance().ItemLog(this, item, "SYSTEM", item->GetName());
	}
	else
	{
		item->AddToGround(GetMapIndex(), GetXYZ());
		item->SetSocket(1, iSocketTwo);
		item->StartDestroyEvent();
		if (IS_SET(item->GetAntiFlag(), ITEM_ANTIFLAG_DROP))
			item->SetOwnership(this, 300);
		else
			item->SetOwnership(this, 60);
		
		LogManager::instance().ItemLog(this, item, "SYSTEM_DROP", item->GetName());
	}
	
	sys_log(0, "Acce received: %d %d", dwItemVnum, bCount);
	return item;
}

// 1) Search: bool CHARACTER::ItemProcess_Polymorph(LPITEM item)
// 2) After their function paste:
bool CHARACTER::CanDoAcce() const
{
	if (m_bIsObserver)
		return false;
	
	if (GetShop())
		return false;
	
	if (GetMyShop())
		return false;
	
	if (m_bUnderRefine)
		return false;
	
	if (IsWarping())
		return false;
	
	return true;
}