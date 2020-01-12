quest acce begin
	state start begin
		when 20008.chat."Ce este o eºarfã ? " begin
			say_title("-- "..mob_name(20008).." --")
			say("")
			say("Eºarfa îþi oferã 2 opþiuni:")
			say("Combinaþia ºi Absorþia.")
			say("")
			say("Poþi încerca sã combini 2 eºarfe de")
			say("acelaºi grad. 2 eºarfe combinate pot")
			say("genera o altã eºarfã cu grad mai mare.")
			say("")
			say("În absorþie eºarfa ia bonusurile armei")
			say("sau armuri tale în funcþie de rata de absorþie")
			say("a eºarfei. Rata de absorþie poate varia, iar")
			say("atunci când bonusurile sunt absorbite, arma")
			say("sau armura introdusã va fi distrusã.")
			say("")
		end
		
		when 20008.chat."Combinaþie" begin
			say_title("-- "..mob_name(20008).." --")
			say("")
			say("Vrei sã combini 2 eºarfe?")
			say("")
			local confirm = select("Da", "Nu")
			if confirm == 2 then
				return
			end
			
			setskin(NOWINDOW)
			command("acce open")
		end
		
		when 20008.chat."Absorbþie" begin
			say_title("-- "..mob_name(20008).." --")
			say("")
			say("Vrei sã absorbi bonusurile unei arme")
			say("sau armuri?")
			say("")
			local confirm = select("Da", "Nu")
			if confirm == 2 then
				return
			end
			
			setskin(NOWINDOW)
			command("acce open_absorption")
		end
	end
end