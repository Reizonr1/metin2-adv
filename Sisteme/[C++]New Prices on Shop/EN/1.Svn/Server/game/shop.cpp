//Find
int CShop::Buy(LPCHARACTER ch, BYTE pos)
//Find
if (iEmptyPos < 0)
	{
		if (m_pkPC)
		{
			sys_log(1, "Shop::Buy at PC Shop : Inventory full : %s size %d", ch->GetName(), item->GetSize());
			return SHOP_SUBHEADER_GC_INVENTORY_FULL;
		}
		else
		{
			sys_log(1, "Shop::Buy : Inventory full : %s size %d", ch->GetName(), item->GetSize());
			M2_DESTROY_ITEM(item);
			return SHOP_SUBHEADER_GC_INVENTORY_FULL;
		}
	}

	ch->PointChange(POINT_GOLD, -dwPrice, false);
	
///Replace : ch->PointChange(POINT_GOLD, -dwPrice, false);

	if (item->GetAntiFlag() & ITEM_ANTIFLAG_SHOP_TRIPLE && !m_pkPC)
	{
		DWORD fiyat = r_item.price;
		// I'm using Coins
		long ep = ch->Ep_Miktar();
		if (ep < fiyat)
		{
			return YOK_2;
		}
		else
			ch->Set_Ep(ch->Ep_Miktar()-fiyat);
	}
	else if (item->GetAntiFlag() & ITEM_ANTIFLAG_SHOP_SECONDARY && !m_pkPC)
	{
		DWORD fiyat = r_item.price;

		if (ch->GetCheque() < fiyat)
		{
			return YOK_3;
		}
		else
			ch->PointChange(POINT_CHEQUE, -fiyat, false);
	}
	else
	{
		ch->PointChange(POINT_GOLD, -dwPrice, false);
		#ifdef ENABLE_CHEQUE_SYSTEM
			ch->PointChange(POINT_CHEQUE, -dwPriceCheque, false);
		#endif
	}
	
//Find
	if (ch->GetGold() < (int) dwPrice)
	{
		sys_log(1, "Shop::Buy : Not enough money : %s has %d, price %d", ch->GetName(), ch->GetGold(), dwPrice);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}
	
///Replace

	if (ch->GetGold() < (int) dwPrice && !(item->GetAntiFlag() & (ITEM_ANTIFLAG_SHOP_SECONDARY || ITEM_ANTIFLAG_SHOP_TRIPLE)))
	{
		sys_log(1, "Shop::Buy : Not enough money : %s has %d, price %d", ch->GetName(), ch->GetGold(), dwPrice);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}