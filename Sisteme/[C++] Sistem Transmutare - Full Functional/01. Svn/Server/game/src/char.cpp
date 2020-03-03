// 1) Search:
	m_iSyncHackCount = 0;
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	m_bChangeLook = false;
#endif


// 1) Search:
			if (!m_pkSafebox->Add(pItems->pos, item))
// 2) Before this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
			item->SetTransmutation(pItems->transmutation);
#endif


// 1) Search:
			item->SetAttributes(pItems->aAttr);
// 2) Before this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
			item->SetTransmutation(pItems->transmutation);
#endif


// 1) Go at the end of file, make a new line and paste (LEAVE A EMPTY NEW LINE AT THE END OF FILE TO DON'T GET WARNING):
#ifdef __CHANGELOOK_SYSTEM__
void CHARACTER::ChangeLookWindow(bool bOpen, bool bRequest)
{
	if ((bOpen) && (isChangeLookOpened()))
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Transmutation] The window is already opened."));
		return;
	}
	
	if ((!bOpen) && (!isChangeLookOpened()))
	{
		if (!bRequest)
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Transmutation] The window is not opened."));
		
		return;
	}
	
	TItemPos tPos;
	tPos.window_type = INVENTORY;
	tPos.cell = 0;
	
	TPacketChangeLook sPacket;
	sPacket.header = HEADER_GC_CL;
	sPacket.subheader = CL_SUBHEADER_OPEN;
	sPacket.subheader = bOpen == true ? CL_SUBHEADER_OPEN : CL_SUBHEADER_CLOSE;
	sPacket.dwCost = bOpen == true ? CL_TRANSMUTATION_PRICE : 0;
	sPacket.bPos = 0;
	sPacket.tPos = tPos;
	GetDesc()->Packet(&sPacket, sizeof(TPacketChangeLook));
	
	m_bChangeLook = bOpen;
	ClearClWindowMaterials();
}

void CHARACTER::ClearClWindowMaterials()
{
	LPITEM * pkItemMaterial;
	pkItemMaterial = GetClWindowMaterials();
	for (int i = 0; i < CL_WINDOW_MAX_MATERIALS; ++i)
	{
		if (!pkItemMaterial[i])
			continue;
		
		pkItemMaterial[i]->Lock(false);
		pkItemMaterial[i] = NULL;
	}
}

BYTE CHARACTER::CheckClEmptyMaterialSlot()
{
	LPITEM * pkItemMaterial;
	pkItemMaterial = GetClWindowMaterials();
	for (int i = 0; i < CL_WINDOW_MAX_MATERIALS; ++i)
	{
		if (!pkItemMaterial[i])
			return i;
	}
	
	return 255;
}

void CHARACTER::AddClMaterial(TItemPos tPos, BYTE bPos)
{
	if (!isChangeLookOpened())
		return;
	else if (bPos >= CL_WINDOW_MAX_MATERIALS)
	{
		if (bPos != 255)
			return;
		
		bPos = CheckClEmptyMaterialSlot();
		if (bPos >= CL_WINDOW_MAX_MATERIALS)
			return;
	}
	
	LPITEM pkItem = GetItem(tPos);
	if (!pkItem)
		return;
	else if ((pkItem->GetCell() >= INVENTORY_MAX_NUM) || (tPos.IsBeltInventoryPosition()))
		return;
	else if (pkItem->IsEquipped())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Transmutation] You cannot transmute an item while it is equipped."));
		return;
	}
	else if ((pkItem->GetType() != ITEM_WEAPON) && (pkItem->GetType() != ITEM_ARMOR) && (pkItem->GetType() != ITEM_COSTUME))
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Transmutation] This item cannot be transmuted."));
		return;
	}
#ifdef __NEW_ARROW_SYSTEM__
	else if ((pkItem->GetType() == ITEM_WEAPON) && ((pkItem->GetSubType() == WEAPON_ARROW) || (pkItem->GetSubType() == WEAPON_MOUNT_SPEAR) || (pkItem->GetSubType() == WEAPON_UNLIMITED_ARROW)))
#else
	else if ((pkItem->GetType() == ITEM_WEAPON) && ((pkItem->GetSubType() == WEAPON_ARROW) || (pkItem->GetSubType() == WEAPON_MOUNT_SPEAR)))
#endif
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Transmutation] This item cannot be transmuted."));
		return;
	}
	else if ((pkItem->GetType() == ITEM_ARMOR) && (pkItem->GetSubType() != ARMOR_BODY))
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Transmutation] This item cannot be transmuted."));
		return;
	}
#ifdef __WEAPON_COSTUME_SYSTEM__
	else if ((pkItem->GetType() == ITEM_COSTUME) && (pkItem->GetSubType() != COSTUME_BODY) && (pkItem->GetSubType() != COSTUME_HAIR) && (pkItem->GetSubType() != COSTUME_WEAPON))
#else
	else if ((pkItem->GetType() == ITEM_COSTUME) && (pkItem->GetSubType() != COSTUME_BODY) && (pkItem->GetSubType() != COSTUME_HAIR))
#endif
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Transmutation] This item cannot be transmuted."));
		return;
	}
#ifdef __SOULBINDING_SYSTEM__
	else if ((pkItem->IsBind()) || (pkItem->IsUntilBind()))
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Transmutation] You can't add binded items."));
		return;
	}
#endif
	else if (pkItem->isLocked())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Transmutation] You can't add locked items."));
		return;
	}
	else if (pkItem->GetTransmutation() != 0)
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Transmutation] You can't add items which are transmuted yet."));
		return;
	}
	
	LPITEM * pkItemMaterial;
	pkItemMaterial = GetClWindowMaterials();
	if ((bPos == 1) && (!pkItemMaterial[0]))
		return;
	
	if (pkItemMaterial[bPos])
		return;
	
	if (bPos == 1)
	{
		bool bStop = false;
		if (pkItemMaterial[0]->GetType() != pkItem->GetType())
			bStop = true;
		else if (pkItemMaterial[0]->GetSubType() != pkItem->GetSubType())
			bStop = true;
		else if (pkItemMaterial[0]->GetOriginalVnum() == pkItem->GetOriginalVnum())
			bStop = true;
		else if (((IS_SET(pkItemMaterial[0]->GetAntiFlag(), ITEM_ANTIFLAG_FEMALE)) && (!IS_SET(pkItem->GetAntiFlag(), ITEM_ANTIFLAG_FEMALE))) || ((IS_SET(pkItemMaterial[0]->GetAntiFlag(), ITEM_ANTIFLAG_MALE)) && (!IS_SET(pkItem->GetAntiFlag(), ITEM_ANTIFLAG_MALE))))
			bStop = true;
		else if ((pkItem->GetAntiFlag() & ITEM_ANTIFLAG_WARRIOR) && (!IS_SET(pkItemMaterial[0]->GetAntiFlag(), ITEM_ANTIFLAG_WARRIOR)))
			bStop = true;
		else if ((pkItem->GetAntiFlag() & ITEM_ANTIFLAG_ASSASSIN) && (!IS_SET(pkItemMaterial[0]->GetAntiFlag(), ITEM_ANTIFLAG_ASSASSIN)))
			bStop = true;
		else if ((pkItem->GetAntiFlag() & ITEM_ANTIFLAG_SHAMAN) && (!IS_SET(pkItemMaterial[0]->GetAntiFlag(), ITEM_ANTIFLAG_SHAMAN)))
			bStop = true;
		else if ((pkItem->GetAntiFlag() & ITEM_ANTIFLAG_SURA) && (!IS_SET(pkItemMaterial[0]->GetAntiFlag(), ITEM_ANTIFLAG_SURA)))
			bStop = true;
#ifdef __WOLFMAN_CHARACTER__
		else if ((pkItem->GetAntiFlag() & ITEM_ANTIFLAG_WOLFMAN) && (!IS_SET(pkItemMaterial[0]->GetAntiFlag(), ITEM_ANTIFLAG_WOLFMAN)))
			bStop = true;
#endif
		
		if (bStop)
		{
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Transmutation] You cannot submit this item."));
			return;
		}
	}
	
	pkItemMaterial[bPos] = pkItem;
	pkItemMaterial[bPos]->Lock(true);
	
	TPacketChangeLook sPacket;
	sPacket.header = HEADER_GC_CL;
	sPacket.subheader = CL_SUBHEADER_ADD;
	sPacket.dwCost = 0;
	sPacket.bPos = bPos;
	sPacket.tPos = tPos;
	GetDesc()->Packet(&sPacket, sizeof(TPacketChangeLook));
}

void CHARACTER::RemoveClMaterial(BYTE bPos)
{
	if (bPos >= CL_WINDOW_MAX_MATERIALS)
		return;
	
	LPITEM * pkItemMaterial;
	pkItemMaterial = GetClWindowMaterials();
	
	if (!pkItemMaterial[bPos])
		return;
	
	if (bPos == 1)
	{
		pkItemMaterial[bPos]->Lock(false);
		pkItemMaterial[bPos] = NULL;
	}
	else
		ClearClWindowMaterials();
	
	TItemPos tPos;
	tPos.window_type = INVENTORY;
	tPos.cell = 0;
	
	TPacketChangeLook sPacket;
	sPacket.header = HEADER_GC_CL;
	sPacket.subheader = CL_SUBHEADER_REMOVE;
	sPacket.dwCost = 0;
	sPacket.bPos = bPos;
	sPacket.tPos = tPos;
	GetDesc()->Packet(&sPacket, sizeof(TPacketChangeLook));
}

void CHARACTER::RefineClMaterials()
{
	LPITEM * pkItemMaterial;
	pkItemMaterial = GetClWindowMaterials();
	if (!pkItemMaterial[0])
		return;
	else if (!pkItemMaterial[1])
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Transmutation] Please submit the item you want to transmute."));
		return;
	}
	
	DWORD dwPrice = CL_TRANSMUTATION_PRICE;
	if (GetGold() < dwPrice)
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Transmutation] You don't have enough Yang."));
		return;
	}
	
	DWORD dwVnum = pkItemMaterial[1]->GetVnum();
	PointChange(POINT_GOLD, -dwPrice);
	DBManager::instance().SendMoneyLog(MONEY_LOG_REFINE, pkItemMaterial[0]->GetVnum(), -dwPrice);
	ITEM_MANAGER::instance().RemoveItem(pkItemMaterial[1], "TRANSMUTED (SUCCESSFULLY)");
	
	pkItemMaterial[0]->SetTransmutation(dwVnum, true);
	ClearClWindowMaterials();
	
	TItemPos tPos;
	tPos.window_type = INVENTORY;
	tPos.cell = 0;
	
	TPacketChangeLook sPacket;
	sPacket.header = HEADER_GC_CL;
	sPacket.subheader = CL_SUBHEADER_REFINE;
	sPacket.dwCost = 0;
	sPacket.bPos = 0;
	sPacket.tPos = tPos;
	GetDesc()->Packet(&sPacket, sizeof(TPacketChangeLook));
}

bool CHARACTER::CleanTransmutation(LPITEM pkItem, LPITEM pkTarget)
{
	if (!CanHandleItem())
		return false;
	else if ((!pkItem) || (!pkTarget))
		return false;
	else if ((pkTarget->GetType() != ITEM_WEAPON) && (pkTarget->GetType() != ITEM_ARMOR) && (pkTarget->GetType() != ITEM_COSTUME))
		return false;
#ifdef __SOULBINDING_SYSTEM__
	else if ((pkTarget->IsBind()) || (pkTarget->IsUntilBind()))
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You can't remove the transmute because item is binded."));
		return false;
	}
#endif
	else if (pkTarget->isLocked())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You can't remove the transmute because item is locked."));
		return false;
	}
	
	if (pkTarget->GetTransmutation() == 0)
		return false;
	
	pkTarget->SetTransmutation(0);
	pkItem->SetCount(pkItem->GetCount() - 1);
	LogManager::instance().ItemLog(this, pkTarget, "USE_DETACHMENT (CLEAN TRANSMUTED)", pkTarget->GetName());
	return true;
}
#endif