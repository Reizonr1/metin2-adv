quest acce begin
	state start begin
		when 20008.chat."Ce este o e�arf� ? " begin
			say_title("-- "..mob_name(20008).." --")
			say("")
			say("E�arfa ��i ofer� 2 op�iuni:")
			say("Combina�ia �i Absor�ia.")
			say("")
			say("Po�i �ncerca s� combini 2 e�arfe de")
			say("acela�i grad. 2 e�arfe combinate pot")
			say("genera o alt� e�arf� cu grad mai mare.")
			say("")
			say("�n absor�ie e�arfa ia bonusurile armei")
			say("sau armuri tale �n func�ie de rata de absor�ie")
			say("a e�arfei. Rata de absor�ie poate varia, iar")
			say("atunci c�nd bonusurile sunt absorbite, arma")
			say("sau armura introdus� va fi distrus�.")
			say("")
		end
		
		when 20008.chat."Combina�ie" begin
			say_title("-- "..mob_name(20008).." --")
			say("")
			say("Vrei s� combini 2 e�arfe?")
			say("")
			local confirm = select("Da", "Nu")
			if confirm == 2 then
				return
			end
			
			setskin(NOWINDOW)
			command("acce open")
		end
		
		when 20008.chat."Absorb�ie" begin
			say_title("-- "..mob_name(20008).." --")
			say("")
			say("Vrei s� absorbi bonusurile unei arme")
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