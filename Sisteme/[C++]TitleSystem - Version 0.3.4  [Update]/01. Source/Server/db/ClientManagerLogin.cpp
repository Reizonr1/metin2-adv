// 1) Search: 
	snprintf(szQuery, sizeof(szQuery), "SELECT id, name, job, level, alignment, st, ht, dx, iq, part_main, part_hair, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
	
// 2) Delete their function and paste:
#ifdef ENABLE_TITLE_SYSTEM		
		snprintf(szQuery, sizeof(szQuery), "SELECT id, name, job, level, alignment, prestige, st, ht, dx, iq, part_main, part_hair, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
#else	
		snprintf(szQuery, sizeof(szQuery), "SELECT id, name, job, level, alignment, st, ht, dx, iq, part_main, part_hair, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
#endif
	
// 1) Search: 	
	snprintf(queryStr, sizeof(queryStr), "SELECT id, name, job, level, alignment, st, ht, dx, iq, part_main, part_hair, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
// 2) Delete their function and paste:
#ifdef ENABLE_TITLE_SYSTEM					
				snprintf(queryStr, sizeof(queryStr), "SELECT id, name, job, level, alignment, prestige, st, ht, dx, iq, part_main, part_hair, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
#else 				
				snprintf(queryStr, sizeof(queryStr), "SELECT id, name, job, level, alignment, st, ht, dx, iq, part_main, part_hair, x, y, skill_group, change_name FROM player%s WHERE account_id=%u", GetTablePostfix(), info->pAccountTable->id);
#endif