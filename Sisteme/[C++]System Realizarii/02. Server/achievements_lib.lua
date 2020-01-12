--[[
	
	## Achievementsystem v1.0 ~ Shang ##
	####################################
	
	To set level achievements syntax = achievements['Level'] = {{level, points}, {level, points}}
	To set played time achievements syntax = achievements['PlayedTime'] = {{time, points}, {time, points}}
	To set pvp kills achievements syntax = achievements['Pvp'] = {{kills, points}, {kills, points}}
	To set mobs, bosses and metinstones achievements syntax = 
		
		achievements['Mobs']['MIDX'] = {
			[map_idx_from_mob] = {mob_vnums}
		}
		achievements['Mobs'][mob_vnum] = {{kills, points}, {kills, points}}
		
		achievements['Bosses']['MIDX'] = {
			[map_idx_from_boss] = {boss_vnums}
		}
		achievements['Bosses'][boss_vnum] = {{kills, points}, {kills, points}}
		
		achievements['Metins']['MIDX'] = {
			[map_idx_from_metinstone] = {metinstone_vnums}
		}		
		achievements['Metins'][metinstone_vnum] = {{kills, points}, {kills, points}}
	
	example:
]]

achievements = {}
achievements['Level'] = {{5, 10}, {10, 20},	{20, 40}, {30, 60}, {110, 80}, {120, 130}, {127, 180}}
achievements['Mobs'] = {}
achievements['Mobs']['MIDX'] = {
	[1] = {101, 102},
	[21] = {101, 102, 103},
	[41] = {101, 102, 104},
}
achievements['Mobs'][101] = {{10, 5}, {15, 10}, {20, 15}, {25, 20}, {30, 25}}
achievements['Mobs'][102] = {{29, 29}}
achievements['Mobs'][103] = {{88, 88}, {1337, 1000}}
achievements['Mobs'][104] = {{99, 99}, {2674, 2000}}
achievements['Metins'] = {}
achievements['Metins']['MIDX'] = {
	[1] = {8001},
	[21] = {8001},
	[41] = {8001},
}
achievements['Metins'][8001] = {{2, 10}, {5, 15}}
achievements['Bosses'] = {}
achievements['Bosses']['MIDX'] = {
	[1] = {691},
	[21] = {691},
	[41] = {691},
}
achievements['Bosses'][691] = {{5, 50}, {10, 100}}
achievements['PlayedTime'] = {{500, 50}, {2000, 200}, {5000, 500}, {10000, 1000}, {17500, 3000}, {25000, 5000}, {40000, 8000}, {50000, 10000}}
achievements['Pvp'] = {{2, 300}, {5, 600}, {8, 900}, {10, 1200}, {1750, 1500}, {2000, 1800}, {2650, 2200}, {3000, 2600}, {4250, 3200}, {5000, 4000}}

function achievements.getf(flag)
	return pc.getf("achievements", flag)
end

function achievements.setf(flag, value)
	pc.setf("achievements", flag, value)
end

function achievements.load_achievements()
	local levels,mobs,bosses,metins,played_time,pvp = achievements['Level'],achievements['Mobs'],achievements['Bosses'],achievements['Metins'],achievements['PlayedTime'],achievements['Pvp']
	if achievements['Mobs']['MIDX'][pc.get_map_index()] ~= nil then
		for index, value in pairs(achievements['Mobs']['MIDX'][pc.get_map_index()]) do local mobInfoTab = achievements.getAchievementInfo(value, 'Mobs') if mobInfoTab ~= nil then for i = 1, table.getn(mobInfoTab) do cmdchat(string.format("ACHIEVEMENTS SET_ACHIEVEMENT#2#%d#%d#%d#%d", achievements.getf(string.format("mob_kills_%d", value)), mobInfoTab[i][1], mobInfoTab[i][2], value)) end end end
	end
	if achievements['Bosses']['MIDX'][pc.get_map_index()] ~= nil then
		for index, value in pairs(achievements['Bosses']['MIDX'][pc.get_map_index()]) do local bossInfoTab = achievements.getAchievementInfo(value, 'Bosses') if bossInfoTab ~= nil then for i = 1, table.getn(bossInfoTab) do cmdchat(string.format("ACHIEVEMENTS SET_ACHIEVEMENT#3#%d#%d#%d#%d", achievements.getf(string.format("boss_kills_%d", value)), bossInfoTab[i][1], bossInfoTab[i][2], value)) end end end
	end
	if achievements['Metins']['MIDX'][pc.get_map_index()] ~= nil then 
		for index, value in pairs(achievements['Metins']['MIDX'][pc.get_map_index()]) do local metinInfoTab = achievements.getAchievementInfo(value, 'Metins') if metinInfoTab ~= nil then for i = 1, table.getn(metinInfoTab) do cmdchat(string.format("ACHIEVEMENTS SET_ACHIEVEMENT#4#%d#%d#%d#%d", achievements.getf(string.format("metin_kills_%d", value)), metinInfoTab[i][1], metinInfoTab[i][2], value)) end end end
	end
	for i = 1, table.getn(levels) do
		cmdchat(string.format("ACHIEVEMENTS SET_ACHIEVEMENT#1#%d#%d#%d#%d", pc.get_level(), levels[i][1], levels[i][2], 0))
	end
	for i = 1, table.getn(played_time) do
		cmdchat(string.format("ACHIEVEMENTS SET_ACHIEVEMENT#5#%d#%d#%d#%d", pc.get_playtime(), played_time[i][1], played_time[i][2], 0))
	end
	for i = 1, table.getn(pvp) do
		cmdchat(string.format("ACHIEVEMENTS SET_ACHIEVEMENT#6#%d#%d#%d#%d", achievements.getf("pc_kills"), pvp[i][1], pvp[i][2], 0))
	end
	achievements.get_ap()
end

function achievements.create_categorys()
	for i = 1,6 do
		cmdchat("ACHIEVEMENTS SET_CATEGORY#"..i)
	end
end

function achievements.getAchievementInfo(race, tab)
	if achievements[tab][race] ~= nil then
		return achievements[tab][race]
	else
		return {}
	end
end

function achievements.get_next_achievement(flag, tab)
	local n = achievements.getf(flag)
	return achievements[tab][n] or 0
end

function achievements.get_ap()
	local c,info = mysql_direct_query("SELECT * FROM player.player WHERE name = '"..pc.get_name().."' LIMIT 1;")
	cmdchat("ACHIEVEMENTS SET_AP#"..info[1].pz)
	return info[1].pz or 0
end

function achievements.set_ap(points)
	mysql_direct_query("UPDATE player.player SET pz = pz + "..points.." WHERE name = '"..pc.get_name().."';")
	achievements.get_ap()
end

function achievements.check_if_first()
	if achievements.getf("first_login") == 0 then
		local categorys = {"level", "pvp", "time", "first_login"}
		for i = 1, table.getn(categorys) do
			achievements.setf(categorys[i], 1)
		end
		io.open(get_locale_base_path()..'/quest/Achievementsystem/'..pc.get_player_id()..'.txt', 'w')
	end
end

function achievements.set_finished(category, value, points, mobVnum)
	local file_path = io.open(get_locale_base_path()..'/quest/Achievementsystem/'..pc.get_player_id()..'.txt', 'a+')
	file_path:write(string.format('%d,%d,%d,%d\n', category, value, points, mobVnum))
	file_path:close()
	cmdchat('ACHIEVEMENTS SET_FINISHED#'..category..'#'..value..'#'..points..'#'..mobVnum)
	achievements.load_last_finished_achievements()
end

function achievements.load_last_finished_achievements()
	cmdchat('ACHIEVEMENTS CLEAR_LAST_FINISHED#')
	local file_path = get_locale_base_path()..'/quest/Achievementsystem/'..pc.get_player_id()..'.txt'
	for line in io.lines(file_path, 'r') do
		cmdchat('ACHIEVEMENTS SET_LAST_FINISHED#'..line)
	end
	cmdchat('ACHIEVEMENTS REFRESH_LAST_FINISHED#')
end

function achievements.load_achievementshop_items()
	local c,items = mysql_direct_query("SELECT * FROM account.achievementshop_items;")
	if c > 0 then
		for i = 1,c do
			cmdchat('ACHIEVEMENTS SET_ACHIEVEMENTSHOP_ITEM#'..items[i].category..'#'..items[i].id..'#'..items[i].vnum..'#'..items[i].price)
		end
	end
end

function achievements.set_achievementshop_categories()
	for i = 1,5 do
		cmdchat('ACHIEVEMENTS SET_ACHIEVEMENTSHOP_CATEGORY#'..i)
	end
end

function achievements.buy_achievementshop_item(item_id, amount)
	local c,itemInfo = mysql_direct_query("SELECT * FROM account.achievementshop_items WHERE id = "..item_id..";")
	if c > 0 then
		local price = tonumber(itemInfo[1].price)
		if amount > 1 then price = price*amount end
		if achievements.get_ap() < price then syschat('No tienes suficientes puntos de logro.') return end
		pc.give_item2_select(tonumber(itemInfo[1].vnum), amount)
		achievements.unset_ap(price)
	end
end

function achievements.unset_ap(points)
	mysql_direct_query("UPDATE player.player SET pz = pz - "..points.." WHERE name = '"..pc.get_name().."';")
	achievements.get_ap()
end
