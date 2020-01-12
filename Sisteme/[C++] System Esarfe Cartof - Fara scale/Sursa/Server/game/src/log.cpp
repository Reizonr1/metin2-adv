// 1) Search: void LogManager::CubeLog(DWORD dwPID, DWORD x, DWORD y, DWORD item_vnum, DWORD item_uid, int item_count, bool success)
// 2) After make a new line and paste:
void LogManager::AcceLog(DWORD dwPID, DWORD x, DWORD y, DWORD item_vnum, DWORD item_uid, int item_count, int abs_chance, bool success)
{
	Query("INSERT DELAYED INTO acce%s (pid, time, x, y, item_vnum, item_uid, item_count, item_abs_chance, success) VALUES(%u, NOW(), %u, %u, %u, %u, %d, %d, %d)", get_table_postfix(), dwPID, x, y, item_vnum, item_uid, item_count, abs_chance, success?1:0);
}