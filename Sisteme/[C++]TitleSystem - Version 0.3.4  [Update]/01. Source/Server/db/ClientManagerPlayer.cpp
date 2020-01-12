// 1) Search:			"alignment = %ld, "
// 2) After make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
			"prestige = %ld, "
#endif			
			
// 1) Search:		pkTab->lAlignment,
// 2) After make a new line and paste:					
#ifdef ENABLE_TITLE_SYSTEM			
		pkTab->lPrestige,			
#endif				
			
// 1) Search: 					
		snprintf(queryStr, sizeof(queryStr),
				"SELECT "
				"id,name,job,voice,dir,x,y,z,map_index,exit_x,exit_y,exit_map_index,hp,mp,stamina,random_hp,random_sp,playtime,"
				"gold,level,level_step,st,ht,dx,iq,exp,"
				"stat_point,skill_point,sub_skill_point,stat_reset_count,part_base,part_hair,part_acce,"
				"skill_level,quickslot,skill_group,alignment,mobile,horse_level,horse_riding,horse_hp,horse_hp_droptime,horse_stamina,"
				"UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(last_play),horse_skill_point FROM player%s WHERE id=%d",
				GetTablePostfix(), packet->player_id);			
// 2) Delete their function and paste:			
#ifdef ENABLE_TITLE_SYSTEM	
		snprintf(queryStr, sizeof(queryStr),
				"SELECT "
				"id,name,job,voice,dir,x,y,z,map_index,exit_x,exit_y,exit_map_index,hp,mp,stamina,random_hp,random_sp,playtime,"
				"gold,level,level_step,st,ht,dx,iq,exp,"
				"stat_point,skill_point,sub_skill_point,stat_reset_count,part_base,part_hair,part_acce,"
				"skill_level,quickslot,skill_group,alignment,prestige,mobile,horse_level,horse_riding,horse_hp,horse_hp_droptime,horse_stamina,"
				"UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(last_play),horse_skill_point FROM player%s WHERE id=%d",
				GetTablePostfix(), packet->player_id);			
#else			
		snprintf(queryStr, sizeof(queryStr),
				"SELECT "
				"id,name,job,voice,dir,x,y,z,map_index,exit_x,exit_y,exit_map_index,hp,mp,stamina,random_hp,random_sp,playtime,"
				"gold,level,level_step,st,ht,dx,iq,exp,"
				"stat_point,skill_point,sub_skill_point,stat_reset_count,part_base,part_hair,part_acce,"
				"skill_level,quickslot,skill_group,alignment,mobile,horse_level,horse_riding,horse_hp,horse_hp_droptime,horse_stamina,"
				"UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(last_play),horse_skill_point FROM player%s WHERE id=%d",
				GetTablePostfix(), packet->player_id);							
#endif	
		
// 1) Search:	str_to_number(pkTab->lAlignment, row[col++]);
// 2) After make a new line and paste:			
#ifdef ENABLE_TITLE_SYSTEM			
	str_to_number(pkTab->lPrestige, row[col++]);			
#endif				