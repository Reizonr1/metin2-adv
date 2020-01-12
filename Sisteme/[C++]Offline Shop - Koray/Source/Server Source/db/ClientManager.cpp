Search:
	m_iShopTableSize(0),
	m_pShopTable(NULL),

Add it under:
#ifdef __OFFLINE_SHOP__
	m_iOfflineShopTableSize(0),
	m_pOfflineShopTable(NULL),
#endif

http://i.imgur.com/jegz65M.png
---

Search:
		sizeof(WORD) + sizeof(WORD) + sizeof(TShopTable) * m_iShopTableSize +

Add it under:
#ifdef __OFFLINE_SHOP__
		sizeof(WORD) + sizeof(WORD) + sizeof(TOfflineShopTable) * m_iOfflineShopTableSize +
#endif

http://i.imgur.com/NepsbY8.png
---

Search:
	sys_log(0, "sizeof(TShopTable) = %d", sizeof(TShopTable));

Add it under:
#ifdef __OFFLINE_SHOP__
	sys_log(0, "sizeof(TOfflineShopTable) = %d", sizeof(TOfflineShopTable));
#endif

http://i.imgur.com/idXLpbI.png
---

Search:
	peer->EncodeWORD(sizeof(TShopTable));
	peer->EncodeWORD(m_iShopTableSize);
	peer->Encode(m_pShopTable, sizeof(TShopTable) * m_iShopTableSize);

Add it under:
#ifdef __OFFLINE_SHOP__
	peer->EncodeWORD(sizeof(TOfflineShopTable));
	peer->EncodeWORD(m_iOfflineShopTableSize);
	peer->Encode(m_pOfflineShopTable, sizeof(TOfflineShopTable)* m_iOfflineShopTableSize);
#endif

http://i.imgur.com/v1ijQX4.png
---

Search:
	char szQuery[QUERY_MAX_LEN];
	snprintf(szQuery, sizeof(szQuery),
			"SELECT account_id, size, password FROM safebox%s WHERE account_id=%u",

Change:
	char szQuery[QUERY_MAX_LEN];
	snprintf(szQuery, sizeof(szQuery),
#ifdef __OFFLINE_SHOP__
			"SELECT account_id, size, password, gold FROM safebox%s WHERE account_id=%u",
#else
			"SELECT account_id, size, password FROM safebox%s WHERE account_id=%u",
#endif
	
http://i.imgur.com/GOwmn8s.png
---

Search:
			/*
			   if (!row[3])
			   pSafebox->dwGold = 0;
			   else
			   pSafebox->dwGold = atoi(row[3]);
			   */

Change:

#ifdef __OFFLINE_SHOP__
			if (!row[3])
			   pSafebox->dwGold = 0;
			else
			   pSafebox->dwGold = atoi(row[3]);
#endif

http://i.imgur.com/7gAPKF9.png
---

Search:
void CClientManager::QUERY_SAFEBOX_CHANGE_SIZE(CPeer * pkPeer, DWORD dwHandle, TSafeboxChangeSizePacket * p)
{
	ClientHandleInfo * pi = new ClientHandleInfo(dwHandle);
	pi->account_index = p->bSize;	// account_index¸¦ »çÀÌÁî·Î ÀÓ½Ã·Î »ç¿ë

	char szQuery[QUERY_MAX_LEN];

	if (p->bSize == 1)
		snprintf(szQuery, sizeof(szQuery), "INSERT INTO safebox%s (account_id, size) VALUES(%u, %u)", GetTablePostfix(), p->dwID, p->bSize);
	else
		snprintf(szQuery, sizeof(szQuery), "UPDATE safebox%s SET size=%u WHERE account_id=%u", GetTablePostfix(), p->bSize, p->dwID);

	CDBManager::instance().ReturnQuery(szQuery, QID_SAFEBOX_CHANGE_SIZE, pkPeer->GetHandle(), pi);
}

Change:
void CClientManager::QUERY_SAFEBOX_CHANGE_SIZE(CPeer * pkPeer, DWORD dwHandle, TSafeboxChangeSizePacket * p)
{
	ClientHandleInfo * pi = new ClientHandleInfo(dwHandle);
	pi->account_index = p->bSize;	// account_index¸¦ »çÀÌÁî·Î ÀÓ½Ã·Î »ç¿ë

	char szQuery[QUERY_MAX_LEN];

	if (p->bSize == 1)
	{
		snprintf(szQuery, sizeof(szQuery), "UPDATE safebox%s SET size=1 WHERE account_id=%u", GetTablePostfix(), p->dwID);

		std::auto_ptr<SQLMsg> pMsg(CDBManager::instance().DirectQuery(szQuery, SQL_PLAYER));

		if (pMsg->Get()->uiAffectedRows == 0)
			snprintf(szQuery, sizeof(szQuery), "INSERT INTO safebox%s (account_id, size) VALUES(%u, 1)", GetTablePostfix(), p->dwID);
	}
	else {
		snprintf(szQuery, sizeof(szQuery), "UPDATE safebox%s SET size=%u WHERE account_id=%u", GetTablePostfix(), p->bSize, p->dwID);
	}
	CDBManager::instance().ReturnQuery(szQuery, QID_SAFEBOX_CHANGE_SIZE, pkPeer->GetHandle(), pi);
}

http://i.imgur.com/ldYLRlA.png
---

Search:
void CClientManager::RESULT_SAFEBOX_CHANGE_PASSWORD_SECOND(CPeer * pkPeer, SQLMsg * msg)
{
	CQueryInfo * qi = (CQueryInfo *) msg->pvUserData;
	ClientHandleInfo * p = (ClientHandleInfo *) qi->pvData;
	DWORD dwHandle = p->dwHandle;
	delete p;

	pkPeer->EncodeHeader(HEADER_DG_SAFEBOX_CHANGE_PASSWORD_ANSWER, dwHandle, sizeof(BYTE));
	pkPeer->EncodeBYTE(1);
}

Add it under:

#ifdef __OFFLINE_SHOP__
void CClientManager::QUERY_COLLECT_OFFLINE_SHOP_ITEM(CPeer * pkPeer, DWORD dwHandle, DWORD dwPID)
{
	int item_idx = 0;

	static TPlayerItem items[10];
	memset(&items, 0, sizeof(items));

	if (TItemCacheSet* pSet = GetItemCacheSet(dwPID))
	{
		TItemCacheSet::iterator it = pSet->begin();
		while (it != pSet->end())
		{
			TPlayerItem * pItem = (*it++)->Get();
			if (pItem->vnum && pItem->window == SAFEBOX_OFFLINE_SHOP)
			{
				TPlayerItem& item = items[item_idx];
				memcpy(&item, pItem, sizeof(TPlayerItem));

				sys_log(1, "COLLECT_OFFLINE_SHOP_ITEM_SAVE : item id %u", item.id);

				item_idx++;
				if (item_idx == 10)
					break;
			}
		}
	}

	if (item_idx < 10)
	{

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

		char szQuery[512];
		snprintf(szQuery, sizeof(szQuery),
				 "SELECT id,count,vnum,%s,%s "
				 "FROM item%s WHERE owner_id=%u AND window=%d",
				 GetTablePostfix(), szSockets, szAttrs, dwPID, SAFEBOX_OFFLINE_SHOP);

		std::auto_ptr<SQLMsg> pMsg(CDBManager::instance().DirectQuery(szQuery));
		SQLResult* pRes = pMsg->Get();

		while (MYSQL_ROW row = mysql_fetch_row(pRes->pSQLResult))
		{
			int i = 0;
			int idx = 0;

			TPlayerItem& item = items[item_idx];

			str_to_number(item.id, row[idx++]);
			if (GetItemCache(item.id))
				continue;

			str_to_number(item.count, row[idx++]);
			str_to_number(item.vnum, row[idx++]);

			for (i = 0; i < ITEM_SOCKET_MAX_NUM; i++)
				str_to_number(item.alSockets[i], row[idx++]);

			for (i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; i++)
			{
				str_to_number(item.aAttr[i].bType, row[idx++]);
				str_to_number(item.aAttr[i].sValue, row[idx++]);
			}

			item.window = SAFEBOX_OFFLINE_SHOP;
			item.owner = dwPID;
			PutItemCache(&item, true);

			sys_log(1, "COLLECT_OFFLINE_SHOP_ITEM_APPLY : item id %u", item.id);

			item_idx++;
			if (item_idx == 10)
				break;
		}
	}

	pkPeer->EncodeHeader(HEADER_DG_COLLECT_OFFLINE_SHOP_ITEM, dwHandle, sizeof(BYTE) + sizeof(TPlayerItem) * item_idx);
	pkPeer->EncodeBYTE(item_idx);
	pkPeer->Encode(&items, sizeof(TPlayerItem) * item_idx);
}
#endif

http://i.imgur.com/6l9Q3px.png
---

Search:
void CClientManager::QUERY_SAFEBOX_SAVE(CPeer * pkPeer, TSafeboxTable * pTable)
{
	char szQuery[QUERY_MAX_LEN];

	snprintf(szQuery, sizeof(szQuery),
			"UPDATE safebox%s SET gold='%u' WHERE account_id=%u",
			GetTablePostfix(), pTable->dwGold, pTable->dwID);

	CDBManager::instance().ReturnQuery(szQuery, QID_SAFEBOX_SAVE, pkPeer->GetHandle(), NULL);
}

Change:
void CClientManager::QUERY_SAFEBOX_SAVE(CPeer * pkPeer, TSafeboxTable * pTable)
{
	char szQuery[QUERY_MAX_LEN];

#ifdef __OFFLINE_SHOP__ //*
	snprintf(szQuery, sizeof(szQuery), "UPDATE safebox%s SET gold=gold WHERE account_id=%u", GetTablePostfix(), pTable->dwID);
#else
	snprintf(szQuery, sizeof(szQuery), "UPDATE safebox%s SET gold='%u' WHERE account_id=%u", GetTablePostfix(), pTable->dwGold, pTable->dwID);
#endif 
	CDBManager::instance().ReturnQuery(szQuery, QID_SAFEBOX_SAVE, pkPeer->GetHandle(), NULL);
}

http://i.imgur.com/Aga25XE.png
---

Search:
void CClientManager::QUERY_ITEM_SAVE(CPeer * pkPeer, const char * c_pData)
{
	TPlayerItem * p = (TPlayerItem *) c_pData;

	// Ã¢°í¸é Ä³½¬ÇÏÁö ¾Ê°í, Ä³½¬¿¡ ÀÖ´ø °Íµµ »©¹ö·Á¾ß ÇÑ´Ù.

	if (p->window == SAFEBOX || p->window == MALL)
	{

Change:
void CClientManager::QUERY_ITEM_SAVE(CPeer * pkPeer, const char * c_pData)
{
	TPlayerItem * p = (TPlayerItem *) c_pData;

	// Ã¢°í¸é Ä³½¬ÇÏÁö ¾Ê°í, Ä³½¬¿¡ ÀÖ´ø °Íµµ »©¹ö·Á¾ß ÇÑ´Ù.

#ifdef __OFFLINE_SHOP__
	if (p->window == SAFEBOX || p->window == MALL || p->window == OFFLINE_SHOP || p->window == SAFEBOX_OFFLINE_SHOP)
#else
	if (p->window == SAFEBOX || p->window == MALL)
#endif
	{

http://i.imgur.com/ACMEiyw.png
---

Search:

void CClientManager::FlushItemCacheSet(DWORD pid)
{
	TItemCacheSetPtrMap::iterator it = m_map_pkItemCacheSetPtr.find(pid);

	if (it == m_map_pkItemCacheSetPtr.end())
	{
		sys_log(0, "FLUSH_ITEMCACHESET : No ItemCacheSet pid(%d)", pid);
		return;
	}

	TItemCacheSet * pSet = it->second;
	TItemCacheSet::iterator it_set = pSet->begin();

	while (it_set != pSet->end())
	{
		CItemCache * c = *it_set++;
		c->Flush();

		m_map_itemCache.erase(c->Get()->id);
		delete c;
	}

	pSet->clear();
	delete pSet;

	m_map_pkItemCacheSetPtr.erase(it);

	if (g_log)
		sys_log(0, "FLUSH_ITEMCACHESET : Deleted pid(%d)", pid);
}

Change:
void CClientManager::FlushItemCacheSet(DWORD pid)
{
	TItemCacheSetPtrMap::iterator it = m_map_pkItemCacheSetPtr.find(pid);

	if (it == m_map_pkItemCacheSetPtr.end())
	{
		sys_log(0, "FLUSH_ITEMCACHESET : No ItemCacheSet pid(%d)", pid);
		return;
	}

	TItemCacheSet * pSet = it->second;
	TItemCacheSet::iterator it_set = pSet->begin();

	while (it_set != pSet->end())
	{
		CItemCache * c = *it_set++;
#ifdef __OFFLINE_SHOP__
		if (c->Get()->window == OFFLINE_SHOP)
			continue;
#endif

		c->Flush();

		m_map_itemCache.erase(c->Get()->id);
#ifdef __OFFLINE_SHOP__
		pSet->erase(c);
#endif
		delete c;
	}

#ifdef __OFFLINE_SHOP__
	if (pSet->size() == 0)
	{
		delete pSet;

		m_map_pkItemCacheSetPtr.erase(it);

		if (g_log)
			sys_log(0, "FLUSH_ITEMCACHESET : Deleted pid(%d)", pid);
	}
	else
	{
		if (g_log)
			sys_log(0, "FLUSH_ITEMCACHESET : not Deleted pid(%d)", pid);
	}
#else
	pSet->clear();
	delete pSet;

	m_map_pkItemCacheSetPtr.erase(it);

	if (g_log)
		sys_log(0, "FLUSH_ITEMCACHESET : Deleted pid(%d)", pid);
#endif
}

http://i.imgur.com/6bkaA12.png
http://i.imgur.com/Yt482BG.png

---

Search:
			case HEADER_GD_MALL_LOAD:
				QUERY_SAFEBOX_LOAD(peer, dwHandle, (TSafeboxLoadPacket *) data, 1);
				break;

Add it under:
#ifdef __OFFLINE_SHOP__
			case HEADER_GD_COLLECT_OFFLINE_SHOP_ITEM:
				QUERY_COLLECT_OFFLINE_SHOP_ITEM(peer, dwHandle, *(DWORD *)data);
				break;
#endif

http://i.imgur.com/X7YpSIJ.png

---

Search:
			case HEADER_GD_REQUEST_CHANNELSTATUS:
				RequestChannelStatus(peer, dwHandle);
				break;

Add it under:
#ifdef __OFFLINE_SHOP__
			case HEADER_GD_SAFEBOX_MONEY:
				SafeboxMoney((TSafeboxMoney*)data);
				break;

			case HEADER_GD_OFFLINE_SHOP_ENTRY:
				PrivateShopEntry((TOfflineShopTable*)data);
				break;

			case HEADER_GD_OFFLINE_SHOP_REMOVE:
				PrivateShopRemove((TOfflineShopTable*)data);
				break;
#endif

http://i.imgur.com/a6F1nyl.png
---

Search:
void CClientManager::ChargeCash(const TRequestChargeCash* packet)
{
	char szQuery[512];

	if (ERequestCharge_Cash == packet->eChargeType)
		sprintf(szQuery, "update account set cash = cash + %d where id = %d limit 1", packet->dwAmount, packet->dwAID);
	else if(ERequestCharge_Mileage == packet->eChargeType)
		sprintf(szQuery, "update account set mileage = mileage + %d where id = %d limit 1", packet->dwAmount, packet->dwAID);
	else
	{
		sys_err ("Invalid request charge type (type : %d, amount : %d, aid : %d)", packet->eChargeType, packet->dwAmount, packet->dwAID);
		return;
	}

	sys_err ("Request Charge (type : %d, amount : %d, aid : %d)", packet->eChargeType, packet->dwAmount, packet->dwAID);

	CDBManager::Instance().AsyncQuery(szQuery, SQL_ACCOUNT);
}

Add it under:

#ifdef __OFFLINE_SHOP__
void CClientManager::SafeboxMoney(TSafeboxMoney* pData)
{
	char szQuery[512];
	if (pData->bType)
		sprintf(szQuery, "UPDATE safebox%s SET `gold`=`gold`+%lld WHERE account_id=%u LIMIT 1", GetTablePostfix(), pData->llAmount, pData->dwAID);
	else
		sprintf(szQuery, "UPDATE safebox%s SET `gold`=`gold`-%lld WHERE account_id=%u LIMIT 1", GetTablePostfix(), pData->llAmount, pData->dwAID);

	std::auto_ptr<SQLMsg> pMsg(CDBManager::instance().DirectQuery(szQuery, SQL_PLAYER));

	if (pData->bType && pMsg->Get()->uiAffectedRows == 0)
	{
		sprintf(szQuery, "INSERT INTO safebox%s (account_id, gold) VALUES(%u, %lld)", GetTablePostfix(), pData->dwAID, (pData->llAmount>0 ? pData->llAmount : 0LL));
		CDBManager::Instance().AsyncQuery(szQuery, SQL_PLAYER);
	}

	CClientManager::instance().ForwardPacket(HEADER_DG_SAFEBOX_MONEY, pData, sizeof(TSafeboxMoney));
}

void CClientManager::PrivateShopEntry(TOfflineShopTable* pData)
{
	static char items[sizeof(pData->items) * 4 + 1], sign[sizeof(pData->szSign) * 4 + 1], 
		price[sizeof(pData->price) * 4 + 1], price2[sizeof(pData->price2) * 4 + 1], price3[sizeof(pData->price3) * 4 + 1], price4[sizeof(pData->price4) * 4 + 1];
	
	CDBManager::instance().EscapeString(sign, pData->szSign, sizeof(pData->szSign));
	CDBManager::instance().EscapeString(items, pData->items2, sizeof(pData->items2));
	
	CDBManager::instance().EscapeString(price, pData->price, sizeof(pData->price));
	CDBManager::instance().EscapeString(price2, pData->price2, sizeof(pData->price2));
	CDBManager::instance().EscapeString(price3, pData->price3, sizeof(pData->price3));
	CDBManager::instance().EscapeString(price4, pData->price4, sizeof(pData->price4));


	static char szQuery[QUERY_MAX_LEN + 1];
	sprintf(szQuery, "REPLACE INTO offline_shop%s (pid,sign,x,y,map_index,channel,duration,installtime,size,gold,item,price,price2,price3,price4,color) VALUES(%u,'%s',%u,%u,%u,%u,%u,UNIX_TIMESTAMP(NOW()),%u,%lld,'%s','%s','%s','%s','%s',%u)",
			GetTablePostfix(), pData->dwPID, sign, pData->dwX, pData->dwY, pData->dwMapIndex, pData->dwChannel, pData->dwDuration, pData->dwSize, pData->ullMoney, items, price, price2, price3, price4, pData->dwColor);

	std::auto_ptr<SQLMsg> pMsg(CDBManager::instance().DirectQuery(szQuery, SQL_PLAYER));

	if (pMsg->Get()->uiAffectedRows == 0)
		sys_err("CClientManager::PrivateShopEntry failed, Query: %s", szQuery);
}

void CClientManager::PrivateShopRemove(TOfflineShopTable* pData)
{
	static char szQuery[1024 + 1];
	sprintf(szQuery, "DELETE FROM offline_shop%s WHERE pid=%u AND x=%u AND y=%u AND map_index=%u AND channel=%u",
			GetTablePostfix(), pData->dwPID, pData->dwX, pData->dwY, pData->dwMapIndex, pData->dwChannel);

	std::auto_ptr<SQLMsg> pMsg(CDBManager::instance().DirectQuery(szQuery, SQL_PLAYER));

	if (pMsg->Get()->uiAffectedRows == 0)
		sys_err("CClientManager::PrivateShopRemove failed, Query: %s", szQuery);
}
#endif
