quest auto_afk_system begin
	state start begin
		when login begin
			if pc.is_afk() then
				pc.del_afk()
			end
			loop_timer("auto_afk_system",60)
		end
		when auto_afk_system.timer begin
			if pc.is_afk() and not pc.is_open_shop() then
				pc.set_afk()
			end
		end
	end
end