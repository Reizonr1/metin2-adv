Search:
	if (!InitializeShopTable())
	{
		sys_err("InitializeShopTable FAILED");
		return false;
	}

Add it under:
#ifdef __OFFLINE_SHOP__
	if (!InitializeOfflineShopTable())
	{
		sys_err("InitializeOfflineShopTable FAILED");
		return false;
	}
#endif

http://i.imgur.com/Rledknn.png
---

Search:
bool CClientManager::InitializeShopTable()
{
	...
}

Add it under:

#ifdef __OFFLINE_SHOP__
bool CClientManager::InitializeOfflineShopTable()
{
	DWORD dwItems[SHOP_HOST_ITEM_MAX_NUM];

	char szQuery[QUERY_MAX_LEN];
	snprintf(szQuery, sizeof(szQuery),
			 "SELECT player.account_id,shop.pid,shop.x,shop.y,shop.map_index,shop.channel,shop.duration,shop.installtime,shop.size,shop.gold,shop.item,shop.price,shop.price2,shop.price3,shop.price4,player.name,shop.sign,shop.color "
			 "FROM offline_shop%s AS shop LEFT JOIN player%s AS player "
			 "ON shop.pid=player.id WHERE player.name IS NOT NULL",
			 GetTablePostfix(), GetTablePostfix());

	std::auto_ptr<SQLMsg> pMsg(CDBManager::instance().DirectQuery(szQuery));
	SQLResult* pRes = pMsg->Get();

	m_pOfflineShopTable = new TOfflineShopTable[pRes->uiNumRows];
	memset(m_pOfflineShopTable, 0, sizeof(TOfflineShopTable) * pRes->uiNumRows);

	while (MYSQL_ROW row = mysql_fetch_row(pRes->pSQLResult))
	{
		int idx = 0;

		TOfflineShopTable& shop_table = m_pOfflineShopTable[m_iOfflineShopTableSize++];
		str_to_number(shop_table.dwAID, row[idx++]);
		str_to_number(shop_table.dwPID, row[idx++]);
		str_to_number(shop_table.dwX, row[idx++]);
		str_to_number(shop_table.dwY, row[idx++]);
		str_to_number(shop_table.dwMapIndex, row[idx++]);
		str_to_number(shop_table.dwChannel, row[idx++]);
		str_to_number(shop_table.dwDuration, row[idx++]);
		str_to_number(shop_table.dwInstallTime, row[idx++]);
		str_to_number(shop_table.dwSize, row[idx++]);
		str_to_number(shop_table.ullMoney, row[idx++]);
		thecore_memcpy(dwItems, row[idx++], sizeof(dwItems));
		thecore_memcpy(shop_table.price, row[idx++], sizeof(shop_table.price));
		thecore_memcpy(shop_table.price2, row[idx++], sizeof(shop_table.price2));
		thecore_memcpy(shop_table.price3, row[idx++], sizeof(shop_table.price3));
		thecore_memcpy(shop_table.price4, row[idx++], sizeof(shop_table.price4));
		strlcpy(shop_table.szName, row[idx++], sizeof(shop_table.szName));
		strlcpy(shop_table.szSign, row[idx++], sizeof(shop_table.szSign));
		str_to_number(shop_table.dwColor, row[idx++]);

		CreateItemCacheSet(shop_table.dwPID);


		char szSockets[QUERY_MAX_LEN / 2] = { '\0' }, szAttrs[QUERY_MAX_LEN / 2] = { '\0' };
		char *pTmpSockets = szSockets, *pTmpAttrs = szAttrs;

		int i = 0;
		for (i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; i++)
		{
			pTmpAttrs += (i < 7) ? sprintf(pTmpAttrs, "attrtype%d,attrvalue%d", i, i) : sprintf(pTmpAttrs, "applytype%d,applyvalue%d", i - 7, i - 7);
			if (i < ITEM_ATTRIBUTE_MAX_NUM - 1)
				pTmpAttrs += sprintf(pTmpAttrs, ",");
		}
		for (i = 0; i < ITEM_SOCKET_MAX_NUM; i++)
		{
			pTmpSockets += sprintf(pTmpSockets, "socket%d", i);
			if (i < ITEM_SOCKET_MAX_NUM - 1)
				pTmpSockets += sprintf(pTmpSockets, ",");
		}

		snprintf(szQuery, sizeof(szQuery),
			"SELECT id,pos,count,"
			"vnum,%s,%s "
			"FROM item%s WHERE owner_id=%d AND window=%d", 
			szSockets, szAttrs, GetTablePostfix(), shop_table.dwPID, OFFLINE_SHOP);

		std::auto_ptr<SQLMsg> pMsg2(CDBManager::instance().DirectQuery(szQuery));
		SQLResult* pRes2 = pMsg2->Get();

		DWORD dwItemID, dwItemPos;
		while (MYSQL_ROW row2 = mysql_fetch_row(pRes2->pSQLResult))
		{
			int idx2 = 0;
			str_to_number(dwItemID, row2[idx2++]);
			str_to_number(dwItemPos, row2[idx2++]);

			if (dwItemID != dwItems[dwItemPos])
				continue;

			TPlayerItem& pItem = shop_table.items[dwItemPos];
			pItem.id = dwItemID;
			pItem.pos = dwItemPos;
			str_to_number(pItem.count, row2[idx2++]);
			str_to_number(pItem.vnum, row2[idx2++]);

			int i = 0;
			for (i = 0; i < ITEM_SOCKET_MAX_NUM; i++)
				str_to_number(pItem.alSockets[i], row2[idx2++]);

			for (i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; i++)
			{
				str_to_number(pItem.aAttr[i].bType, row2[idx2++]);
				str_to_number(pItem.aAttr[i].sValue, row2[idx2++]);
			}

			pItem.window = OFFLINE_SHOP;
			pItem.owner = shop_table.dwPID;

			PutItemCache(&pItem, true);
		}
	}

	return true;
}
#endif

http://i.imgur.com/Txi9S92.png