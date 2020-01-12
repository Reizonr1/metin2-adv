quest command_changeRace begin
	state start begin
		when 30534.use begin
			cmdchat("change_race")
			pc.removeitem(30534, 1)
		end
	end
end