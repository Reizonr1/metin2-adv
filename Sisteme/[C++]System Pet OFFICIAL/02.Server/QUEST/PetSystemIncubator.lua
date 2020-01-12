quest PetSystemIncubator begin
	state start begin
		when 55401.use or 55402.use or 55403.use or 55404.use begin
			newpet.EggRequest(item.get_vnum())
			cmdchat(string.format("OpenPetIncubator %d ", (item.get_vnum()-55401)))
		end
	end
end