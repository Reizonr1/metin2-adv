quest PetSystems begin
	state start begin
		function get_pet_info(itemVnum)
			pet_info_map = {
			--  [ITEM VNUM] MOB_VNUM, DEFAULT NAME, buff_idx, spawn_effect_idx
				[55701]     = { 34041, "'s Kleiner Affe", 0},
				[55702]     = { 34045, "'s Kleine Spinne", 0},
				[55703]     = { 34049, "'s Kleiner Razador", 0},
				[55704]     = { 34053, "'s Kleiner Nemere", 0},
				
			}
			itemVnum = tonumber(itemVnum)
			return pet_info_map[itemVnum]
		end
		
		when 55701.use or 55702.use or 55703.use or 55704.use begin
			local pet_info = PetSystems.get_pet_info(item.vnum)

			if null != pet_info then

				local mobVnum = pet_info[1]
				local petName = pet_info[2]
				

				if true == newpet.is_summon(mobVnum) then					
					newpet.unsummon(mobVnum)
				else
					if newpet.count_summoned() < 1 then
						newpet.summon(mobVnum, petName, false)
					else
						syschat("You already summoned a pet.")
					end					
				end -- if pet.is_summon
			end  -- if null != pet_info
		end -- when
	end
end