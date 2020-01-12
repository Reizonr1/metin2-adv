// 1) Search: void LogManager::CubeLog(DWORD dwPID, DWORD x, DWORD y, DWORD item_vnum, DWORD item_uid, int item_count, bool success)
// 2) After make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
void LogManager::AttrTransferLog(DWORD dwPID, DWORD x, DWORD y, DWORD item_vnum)
{
	Query("INSERT DELAYED INTO attr_transfer%s (pid, time, x, y, item_vnum) VALUES(%u, NOW(), %u, %u, %u)", get_table_postfix(), dwPID, x, y, item_vnum);
}
#endif