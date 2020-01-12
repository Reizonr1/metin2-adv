Search:
	if (!c_rAccountTable.players[pinfo->index].dwID)
	{
		sys_err("PlayerDelete: Wrong Social ID index %d, login: %s", pinfo->index, c_rAccountTable.login);
		d->Packet(encode_byte(HEADER_GC_CHARACTER_DELETE_WRONG_SOCIAL_ID), 1);
		return;
	}

Add it under:
#ifdef __OFFLINE_SHOP__
	char szQuery[QUERY_MAX_LEN];
	snprintf(szQuery, sizeof(szQuery), "SELECT COUNT(*) FROM player.offline_shop%s WHERE pid=%u", get_table_postfix(), c_rAccountTable.players[pinfo->index].dwID);
	std::auto_ptr<SQLMsg> pResMsg(DBManager::instance().DirectQuery(szQuery));
	if (pResMsg->uiSQLErrno != 0 || pResMsg->Get()->uiNumRows > 0)
	{
		sys_err("PlayerDelete: Offline shop owner pid %u", c_rAccountTable.players[pinfo->index].dwID);
		return;
	}
#endif

https://puu.sh/sgGOF/ec11dd7d56.png