//1.0 suchen (2x):
			if (g_stLocale == "gb2312")
			{
				snprintf(queryStr, sizeof(queryStr), "SELECT id, name, job, level, alignment, st, ht, dx, iq, part_main, part_hair, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
			}
			else
			{
				snprintf(queryStr, sizeof(queryStr), "SELECT id, name, job, level, playtime, st, ht, dx, iq, part_main, part_hair, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
			}
//1.0 anpassen (2x):			
			if (g_stLocale == "gb2312")
			{
				snprintf(queryStr, sizeof(queryStr), "SELECT id, name, job, level, alignment," 
#ifdef ENABLE_VIP_SYSTEM				
				"vip," 
#endif				
				"st, ht, dx, iq, part_main, part_hair, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
			}
			else
			{
				snprintf(queryStr, sizeof(queryStr), "SELECT id, name, job, level, playtime, st, ht, dx, iq, part_main, part_hair, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
			}
			