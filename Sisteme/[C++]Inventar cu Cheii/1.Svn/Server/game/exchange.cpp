//Find
		bool CExchange::CheckSpace()

//Find in
		 for (i = 0; i < EXCHANGE_ITEM_MAX_NUM; ++i)
		{
			if (!(item = m_apItems[i]))
				continue;
///Add
		#ifdef NEW_ADD_INVENTORY
		int envanterblack;
		if (item->IsDragonSoul())
			envanterblack = victim->GetEmptyDragonSoulInventory(item);
		else
			envanterblack = victim->GetEmptyInventory(item->GetSize());

		if (envanterblack < 0)
		{
			return false;
		}
		#endif