// 1) Search: extern std::string g_stLocale;
// 2) Delete up to "} of else" and paste:
	extern std::string g_stLocale;
	if (g_stLocale == "gb2312")
	{
		snprintf(szQuery, sizeof(szQuery), "SELECT id, name, job, level, alignment, st, ht, dx, iq, part_main, part_hair, part_acce, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
	}
	else
	{
		snprintf(szQuery, sizeof(szQuery), "SELECT id, name, job, level, playtime, st, ht, dx, iq, part_main, part_hair, part_acce, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
	}

// 1) Search: void CreateAccountPlayerDataFromRes(MYSQL_RES * pRes, TAccountTable * pkTab)
// 2) Delete their function and paste:
void CreateAccountPlayerDataFromRes(MYSQL_RES * pRes, TAccountTable * pkTab)
{
	if (!pRes)
		return;
	
	for (DWORD i = 0; i < mysql_num_rows(pRes); ++i)
	{
		MYSQL_ROW row = mysql_fetch_row(pRes);
		int col = 0;
		
		DWORD player_id = 0;
		!row[col++] ? 0 : str_to_number(player_id, row[col - 1]);
		
		if (!player_id)
			continue;
		
		int j;
		for (j = 0; j < PLAYER_PER_ACCOUNT; ++j)
		{
			if (pkTab->players[j].dwID == player_id)
			{
				CPlayerTableCache * pc = CClientManager::instance().GetPlayerCache(player_id);
				TPlayerTable * pt = pc ? pc->Get(false) : NULL;
				if (pt)
				{
					strlcpy(pkTab->players[j].szName, pt->name, sizeof(pkTab->players[j].szName));
					pkTab->players[j].byJob = pt->job;
					pkTab->players[j].byLevel = pt->level;
					pkTab->players[j].dwPlayMinutes = pt->playtime;
					pkTab->players[j].byST = pt->st;
					pkTab->players[j].byHT = pt->ht;
					pkTab->players[j].byDX = pt->dx;
					pkTab->players[j].byIQ = pt->iq;
					pkTab->players[j].wMainPart = pt->parts[PART_MAIN];
					pkTab->players[j].wHairPart = pt->parts[PART_HAIR];
					pkTab->players[j].wAccePart = pt->parts[PART_ACCE];
					pkTab->players[j].x = pt->x;
					pkTab->players[j].y = pt->y;
					pkTab->players[j].skill_group = pt->skill_group;
					pkTab->players[j].bChangeName = 0;
				}
				else
				{
					if (!row[col++])
						*pkTab->players[j].szName = '\0';
					else
						strlcpy(pkTab->players[j].szName, row[col - 1], sizeof(pkTab->players[j].szName));
					
					pkTab->players[j].byJob = 0;
					pkTab->players[j].byLevel = 0;
					pkTab->players[j].dwPlayMinutes = 0;
					pkTab->players[j].byST = 0;
					pkTab->players[j].byHT = 0;
					pkTab->players[j].byDX = 0;
					pkTab->players[j].byIQ = 0;
					pkTab->players[j].wMainPart = 0;
					pkTab->players[j].wHairPart = 0;
					pkTab->players[j].x = 0;
					pkTab->players[j].y = 0;
					pkTab->players[j].skill_group = 0;
					pkTab->players[j].bChangeName = 0;
					
					str_to_number(pkTab->players[j].byJob, row[col++]);
					str_to_number(pkTab->players[j].byLevel, row[col++]);
					str_to_number(pkTab->players[j].dwPlayMinutes, row[col++]);
					str_to_number(pkTab->players[j].byST, row[col++]);
					str_to_number(pkTab->players[j].byHT, row[col++]);
					str_to_number(pkTab->players[j].byDX, row[col++]);
					str_to_number(pkTab->players[j].byIQ, row[col++]);
					str_to_number(pkTab->players[j].wMainPart, row[col++]);
					str_to_number(pkTab->players[j].wHairPart, row[col++]);
					str_to_number(pkTab->players[j].wAccePart, row[col++]);
					str_to_number(pkTab->players[j].x, row[col++]);
					str_to_number(pkTab->players[j].y, row[col++]);
					str_to_number(pkTab->players[j].skill_group, row[col++]);
					str_to_number(pkTab->players[j].bChangeName, row[col++]);
				}
				
				sys_log(0, "%s %lu %lu hair %u acce %u", pkTab->players[j].szName, pkTab->players[j].x, pkTab->players[j].y, pkTab->players[j].wHairPart, pkTab->players[j].wAccePart);
				break;
			}
		}
	}
}

// 1) Search: void CClientManager::RESULT_LOGIN(CPeer * peer, SQLMsg * msg)
// 2) Delete their function and paste:
void CClientManager::RESULT_LOGIN(CPeer * peer, SQLMsg * msg)
{
	CQueryInfo * qi = (CQueryInfo *) msg->pvUserData;
	ClientHandleInfo * info = (ClientHandleInfo *) qi->pvData;
	if (info->account_index == 0)
	{
		if (msg->Get()->uiNumRows == 0)
		{
			sys_log(0, "RESULT_LOGIN: no account");
			peer->EncodeHeader(HEADER_DG_LOGIN_NOT_EXIST, info->dwHandle, 0);
			delete info;
			return;
		}
		
		info->pAccountTable = CreateAccountTableFromRes(msg->Get()->pSQLResult);
		if (!info->pAccountTable)
		{
			sys_log(0, "RESULT_LOGIN: no account : WRONG_PASSWD");
			peer->EncodeReturn(HEADER_DG_LOGIN_WRONG_PASSWD, info->dwHandle);
			delete info;
		}
		else
		{
			++info->account_index;
			
			char queryStr[512];
			extern std::string g_stLocale;
			if (g_stLocale == "gb2312")
			{
				snprintf(queryStr, sizeof(queryStr), "SELECT id, name, job, level, alignment, st, ht, dx, iq, part_main, part_hair, part_acce, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
			}
			else
			{
				snprintf(queryStr, sizeof(queryStr), "SELECT id, name, job, level, playtime, st, ht, dx, iq, part_main, part_hair, part_acce, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
			}
			
			CDBManager::instance().ReturnQuery(queryStr, QID_LOGIN, peer->GetHandle(), info);
		}
		return;
	}
	else
	{
		if (!info->pAccountTable)
		{
			peer->EncodeReturn(HEADER_DG_LOGIN_WRONG_PASSWD, info->dwHandle);
			delete info;
			return;
		}
		
		if (!InsertLogonAccount(info->pAccountTable->login, peer->GetHandle(), info->ip))
		{
			sys_log(0, "RESULT_LOGIN: already logon %s", info->pAccountTable->login);
			
			TPacketDGLoginAlready p;
			strlcpy(p.szLogin, info->pAccountTable->login, sizeof(p.szLogin));
			
			peer->EncodeHeader(HEADER_DG_LOGIN_ALREADY, info->dwHandle, sizeof(TPacketDGLoginAlready));
			peer->Encode(&p, sizeof(p));
		}
		else
		{
			sys_log(0, "RESULT_LOGIN: login success %s rows: %lu", info->pAccountTable->login, msg->Get()->uiNumRows);
			if (msg->Get()->uiNumRows > 0)
				CreateAccountPlayerDataFromRes(msg->Get()->pSQLResult, info->pAccountTable);
			
			CLoginData * p = GetLoginDataByLogin(info->pAccountTable->login);
			memcpy(&p->GetAccountRef(), info->pAccountTable, sizeof(TAccountTable));
			
			peer->EncodeHeader(HEADER_DG_LOGIN_SUCCESS, info->dwHandle, sizeof(TAccountTable));
			peer->Encode(info->pAccountTable, sizeof(TAccountTable));

		}
		
		delete info->pAccountTable;
		info->pAccountTable = NULL;
		delete info;
	}
}