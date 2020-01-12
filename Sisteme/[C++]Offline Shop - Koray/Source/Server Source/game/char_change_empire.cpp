Search:
#include "marriage.h"

Add it under:

#ifdef __OFFLINE_SHOP__
bool CHARACTER::CanChangeEmpireOfflineShopCheck()
{
	char szQuery[QUERY_MAX_LEN];
	DWORD dwMyPID = GetPlayerID();

#ifdef ENABLE_PLAYER_PER_ACCOUNT5
	DWORD dwPID[5];
#else
	DWORD dwPID[4];
#endif
	memset(dwPID, 0, sizeof(dwPID));

#ifdef ENABLE_PLAYER_PER_ACCOUNT5
	snprintf(szQuery, sizeof(szQuery),
		"SELECT pid1, pid2, pid3, pid4, pid5 FROM player_index%s WHERE pid1=%u OR pid2=%u OR pid3=%u OR pid4=%u OR pid5=%u",
		get_table_postfix(), dwMyPID, dwMyPID, dwMyPID, dwMyPID, dwMyPID);
#else
	snprintf(szQuery, sizeof(szQuery),
		"SELECT pid1, pid2, pid3, pid4 FROM player_index%s WHERE pid1=%u OR pid2=%u OR pid3=%u OR pid4=%u",
		get_table_postfix(), dwMyPID, dwMyPID, dwMyPID, dwMyPID, GetEmpire());
#endif

	std::auto_ptr<SQLMsg> pPidMsg(DBManager::instance().DirectQuery(szQuery));
	if (pPidMsg->Get()->uiNumRows == 0)
		return false;

	MYSQL_ROW row = mysql_fetch_row(pPidMsg->Get()->pSQLResult);
	str_to_number(dwPID[0], row[0]);
	str_to_number(dwPID[1], row[1]);
	str_to_number(dwPID[2], row[2]);
	str_to_number(dwPID[3], row[3]);
#ifdef ENABLE_PLAYER_PER_ACCOUNT5
	str_to_number(dwPID[4], row[4]);
#endif

#ifdef ENABLE_PLAYER_PER_ACCOUNT5
	snprintf(szQuery, sizeof(szQuery),
		"SELECT COUNT(*) FROM player.offline_shop%s WHERE pid=%u OR pid=%u OR pid=%u OR pid=%u OR pid=%u",
		get_table_postfix(), dwPID[0], dwPID[1], dwPID[2], dwPID[3], dwPID[4]);
#else
	snprintf(szQuery, sizeof(szQuery),
		"SELECT COUNT(*) FROM player.offline_shop%s WHERE pid=%u OR pid=%u OR pid=%u OR pid=%u",
		get_table_postfix(), dwPID[0], dwPID[1], dwPID[2], dwPID[3]);
#endif

	std::auto_ptr<SQLMsg> pResMsg(DBManager::instance().DirectQuery(szQuery));
	return (pResMsg->Get()->uiNumRows <= 0) ? true : false;
}
#endif


https://puu.sh/sgFfV/36560666a2.png
http://i.imgur.com/xpWTFgx.png