//1.0 suchen:
			"alignment = %ld, "
//1.0 dahinter:			
#ifdef ENABLE_VIP_SYSTEM
			"vip = %ld, "
#endif	
			
//1.1 suchen:
		pkTab->lAlignment,	
//1.1 dahinter:		
#ifdef ENABLE_VIP_SYSTEM			
		pkTab->lVip,			
#endif			

//1.2 suchen:
		snprintf(queryStr, sizeof(queryStr),
				"SELECT "
				"id,title,name,job,voice,dir,x,y,z,map_index,exit_x,exit_y,exit_map_index,hp,mp,stamina,random_hp,random_sp,playtime,"
				"gold,level,level_step,st,ht,dx,iq,exp,"
				"stat_point,skill_point,sub_skill_point,stat_reset_count,part_base,part_hair,"
				"skill_level,quickslot,skill_group,alignment,mobile,horse_level,horse_riding,horse_hp,horse_hp_droptime,horse_stamina,"
				"UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(last_play),horse_skill_point FROM player%s WHERE id=%d",
				GetTablePostfix(), packet->player_id);
	
//1.2 anpassen:	
		snprintf(queryStr, sizeof(queryStr),
				"SELECT "
				"id,title,name,job,voice,dir,x,y,z,map_index,exit_x,exit_y,exit_map_index,hp,mp,stamina,random_hp,random_sp,playtime,"
				"gold,level,level_step,st,ht,dx,iq,exp,"
				"stat_point,skill_point,sub_skill_point,stat_reset_count,part_base,part_hair,"
				"skill_level,quickslot,skill_group,alignment,"
#ifdef ENABLE_VIP_SYSTEM				
				"vip,"
#endif				
				"mobile,horse_level,horse_riding,horse_hp,horse_hp_droptime,horse_stamina,"
				"UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(last_play),horse_skill_point FROM player%s WHERE id=%d",
				GetTablePostfix(), packet->player_id);

//1.3 suchen:
	str_to_number(pkTab->lAlignment, row[col++]);
//1.3 dahinter:	
#ifdef ENABLE_VIP_SYSTEM			
	str_to_number(pkTab->lVip, row[col++]);			
#endif	
	