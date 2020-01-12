quest vip begin
    state start begin
		when login with pc.get_vip() != 0 begin
			cmdchat("VIP")
		end
		when 30066.use begin -- Itemvnum
			if pc.get_vip() != 0 then
				pc.reset_vip()
				pc.removeitem(30066, 1)
			else
				syschat("<VIP System> Du bist kein VIP Mitglied!")
			end	
		end	
		when 30065.use begin --Itemvnum
		--	if pc.is_gm then
		--		syschat("<VIP System> Teamler können kein VIP bekommen!")
		--		return
			if pc.get_vip() != 0 then
				syschat("<VIP System> Du bist bereits ein VIP Mitglied!")
				return
			elseif pc.is_polymorphed() then
				syschat("<VIP System> Während du verwandelt bist kannst du kein VIP werden.")
				return
			elseif not pc.can_warp() then
				syschat("<VIP System> Du hast vorkurzem gehandelt, so kannst du kein VIP werden.")
				return
			elseif party.is_party() then
				syschat("<VIP System> Während du in einer Gruppe bist kannst du kein VIP werden.")
				return						
			elseif pc.count_item(30065) < 1 then
				syschat("<VIP System> Fehler!")
				return
			elseif pc.get_vip() == 0 then
				pc.set_vip(1)
				pc.removeitem(30065, 1)
			end
		end	
	end
end