quest attr_transfer begin
	state start begin
		when 20406.chat."Transfer the costume bonuses" begin
			say_title(mob_name(20406))
			say("")
			say("You can transfer the bonuses from costume 2 to")
			say("costume 1.")
			say("")
			say("Before add the costumes in the slots, you")
			say("must place the Transfer Scroll in their slot.")
			say("")
			say("The second costume will be destroyed.")
			say("")
			say("You want to continue?")
			say("")
			local confirm = select("Yes", "No")
			if confirm == 2 then
				return
			end
			
			setskin(NOWINDOW)
			command("attrtransfer open")
		end
	end
end