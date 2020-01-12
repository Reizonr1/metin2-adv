// Search for:
bool ITEM_MANAGER::GetDropPct(LPCHARACTER pkChr, LPCHARACTER pkKiller, OUT int& iDeltaPercent, OUT int& iRandRange)

// Add (Under & Whole function):
#ifdef __SEND_TARGET_INFO__
bool ITEM_MANAGER::CreateDropItemVector(LPCHARACTER pkChr, LPCHARACTER pkKiller, std::vector<LPITEM> & vec_item)
{
	if (pkChr->IsPolymorphed() || pkChr->IsPC())
	{
		return false;
	}

	int iLevel = pkKiller->GetLevel();

	BYTE bRank = pkChr->GetMobRank();
	LPITEM item = NULL;

	std::vector<CItemDropInfo>::iterator it = g_vec_pkCommonDropItem[bRank].begin();

	while (it != g_vec_pkCommonDropItem[bRank].end())
	{
		const CItemDropInfo & c_rInfo = *(it++);

		if (iLevel < c_rInfo.m_iLevelStart || iLevel > c_rInfo.m_iLevelEnd)
			continue;

		TItemTable * table = GetTable(c_rInfo.m_dwVnum);

		if (!table)
			continue;

		item = NULL;

		if (table->bType == ITEM_POLYMORPH)
		{
			if (c_rInfo.m_dwVnum == pkChr->GetPolymorphItemVnum())
			{
				item = CreateItem(c_rInfo.m_dwVnum, 1, 0, true);

				if (item)
					item->SetSocket(0, pkChr->GetRaceNum());
			}
		}
		else
			item = CreateItem(c_rInfo.m_dwVnum, 1, 0, true);

		if (item) vec_item.push_back(item);
	}

	// Drop Item Group
	{
		itertype(m_map_pkDropItemGroup) it;
		it = m_map_pkDropItemGroup.find(pkChr->GetRaceNum());

		if (it != m_map_pkDropItemGroup.end())
		{
			typeof(it->second->GetVector()) v = it->second->GetVector();

			for (DWORD i = 0; i < v.size(); ++i)
			{
				item = CreateItem(v[i].dwVnum, v[i].iCount, 0, true);

				if (item)
				{
					if (item->GetType() == ITEM_POLYMORPH)
					{
						if (item->GetVnum() == pkChr->GetPolymorphItemVnum())
						{
							item->SetSocket(0, pkChr->GetRaceNum());
						}
					}

					vec_item.push_back(item);
				}
			}
		}
	}

	// MobDropItem Group
	{
		itertype(m_map_pkMobItemGroup) it;
		it = m_map_pkMobItemGroup.find(pkChr->GetRaceNum());

		if ( it != m_map_pkMobItemGroup.end() )
		{
			CMobItemGroup* pGroup = it->second;

			// MOB_DROP_ITEM_BUG_FIX
			// 20050805.myevan.MobDropItem ? ???? ?? ?? CMobItemGroup::GetOne() ??? ?? ?? ??
			if (pGroup && !pGroup->IsEmpty())
			{
				const CMobItemGroup::SMobItemGroupInfo& info = pGroup->GetOne();
				item = CreateItem(info.dwItemVnum, info.iCount, 0, true, info.iRarePct);

				if (item) vec_item.push_back(item);
			}
			// END_OF_MOB_DROP_ITEM_BUG_FIX
		}
	}

	// Level Item Group
	{
		itertype(m_map_pkLevelItemGroup) it;
		it = m_map_pkLevelItemGroup.find(pkChr->GetRaceNum());

		if ( it != m_map_pkLevelItemGroup.end() )
		{
			if ( it->second->GetLevelLimit() <= (DWORD)iLevel )
			{
				typeof(it->second->GetVector()) v = it->second->GetVector();

				for ( DWORD i=0; i < v.size(); i++ )
				{
					DWORD dwVnum = v[i].dwVNum;
					item = CreateItem(dwVnum, v[i].iCount, 0, true);
					if ( item ) vec_item.push_back(item);
				}
			}
		}
	}

	// BuyerTheitGloves Item Group
	{
		// by mhh ?? ??? ??? ?? drop ? ???? ??
		if (pkKiller->GetPremiumRemainSeconds(PREMIUM_ITEM) > 0 ||
				pkKiller->IsEquipUniqueGroup(UNIQUE_GROUP_DOUBLE_ITEM))
		{
			itertype(m_map_pkGloveItemGroup) it;
			it = m_map_pkGloveItemGroup.find(pkChr->GetRaceNum());

			if (it != m_map_pkGloveItemGroup.end())
			{
				typeof(it->second->GetVector()) v = it->second->GetVector();

				for (DWORD i = 0; i < v.size(); ++i)
				{
					
					DWORD dwVnum = v[i].dwVnum;
					item = CreateItem(dwVnum, v[i].iCount, 0, true);
					if (item) vec_item.push_back(item);
				}
			}
		}
	}

	// ??
	if (pkChr->GetMobDropItemVnum())
	{
		itertype(m_map_dwEtcItemDropProb) it = m_map_dwEtcItemDropProb.find(pkChr->GetMobDropItemVnum());

		if (it != m_map_dwEtcItemDropProb.end())
		{		
			item = CreateItem(pkChr->GetMobDropItemVnum(), 1, 0, true);
			if (item) vec_item.push_back(item);
		}
	}

	if (pkChr->IsStone())
	{
		if (pkChr->GetDropMetinStoneVnum())
		{
			item = CreateItem(pkChr->GetDropMetinStoneVnum(), 1, 0, true);
			if (item) vec_item.push_back(item);
		}
	}

	return vec_item.size();
}
#endif
