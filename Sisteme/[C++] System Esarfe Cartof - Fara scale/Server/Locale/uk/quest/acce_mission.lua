quest acce_mission begin
	state start begin
		when login or levelup with pc.get_level() >= 30 begin
			set_state("information")
		end
	end
	
	state information begin
		when enter begin
			pc.setqf("time_to_wait", 0)
			--pc.setqf("collect_count", 0)
		end
		
		when letter begin
			local v = find_npc_by_vnum(20008)
			if v != 0 then
				target.vid("octavio", v, "Octavio")
			end
			
			send_letter("*Imbracaminte speciala")
		end
		
		when button or info begin
			say_title(mob_name(20008))
			say("")
			say("Octavio te caut�. Timpul trece, du-te �i")
			say("vorbe�te cu el.")
			say("")
		end
		
		when octavio.target.click or 20084.chat."Mareste-ti puterile" begin
			target.delete("octavio")
			
			say_title(mob_name(20008))
			say("")
			say("Ah, aici e�ti! Am descoperit ceva extraordinar.")
			say("O nou� pies� de echipament numit e�arf�.")
			say("")
			say("E�arfa ��i ofer� 2 op�iuni:")
			say("Combina�ia �i Absor�ia.")
			say("")
			say("Po�i �ncerca s� combini 2 e�arfe de")
			say("acela�i grad. 2 e�arfe combinate pot")
			say("genera o alt� e�arf� cu grad mai mare.")
			say("")
			wait()
			say_title(mob_name(20008))
			say("")
			say("�n absor�ie e�arfa ia bonusurile armei")
			say("sau armuri tale �n func�ie de rata de absor�ie")
			say("a e�arfei. Rata de absor�ie poate varia, iar")
			say("atunci c�nd bonusurile sunt absorbite, arma")
			say("sau armura introdus� va fi distrus�.")
			say("")
			say("��i pot creea o e�arf� de gradul 1.")
			say("Dar am nevoie de x10 "..item_name(85000)..".")
			say("")
			say("Doar "..mob_name(20355).." este �n stare s� creeze")
			say("acest material, dute �i vorbe�te cu el.")
			say("")
			set_state("go_to_disciple")
		end
	end
	
	state go_to_disciple begin
		when letter begin
			local v = find_npc_by_vnum(20355)
			if v != 0 then
				target.vid("capitan", v, "Capitan")
			end
			
			send_letter("*Mareste-ti puterile")
		end
		
		when button or info begin
			say_title("Mareste-ti puterile")
			say("")
			say("G�se�te-l pe "..mob_name(20355).." pentru a lua materialele necesare.")
			say("")
		end
		
    	when capitan.target.click or 20355.chat."Mareste-ti puterile" begin
			target.delete("capitan")
			
			say_title(mob_name(20355))
			say("")
			say("Felicitari! "..mob_name(20008).." mi-a zis ca vei veni")
			say("sa ma vizitezi. Am descoperit recent ca Sung Mahi")
			say("a devenit mai puternic.")
			say("")
			say("Cel putin unul din noi trebuie sa aiba puterea ori Sung")
			say("Mahi ne va distruge pe toti.")
			say("")
			say("Pot face un palton, dar nu va fi usor.")
			say("")
			say("Da-mi o ora, si iti voi da materialele de care")
			say("ai nevoie.")
			say("")
			wait()
			say_title(mob_name(20355))
			say("")
			say("Daca vii inapoi intr-o ora, voi avea")
			say("materialele gata pentru tine.")
			say("")
			say("Iti promit!")
			say("")
			say("Nu uita sa ma vizitezi intr-o ora!")
			say("")
			local agree = select("Da", "Nu")
			if agree == 1 then
				pc.setqf("time_to_wait", 60 * 1 + pc.get_playtime())
				set_state("time_to_wait")
			end
		end
	end
	
	state time_to_wait begin
		when letter begin
			local v = find_npc_by_vnum(20355)
			if v != 0 then
				target.vid("capitan", v, "Capitan")
			end
			
			send_letter("*Mareste-ti puterile")
		end
		
		when button or info begin
			say_title("Mareste-ti puterile")
			say("")
			say("Gaseste-l pe "..mob_name(20355)..", el iti va da materialul.")
			say("")
			if pc.getqf("time_to_wait") > pc.get_playtime() then
				local time_to_wait = pc.getqf("time_to_wait") - pc.get_playtime()
				say("Timp ramas: "..time_to_wait.." minute.")
				say("")
			end
		end
		
    	when capitan.target.click or 20355.chat."Mareste-ti puterile" begin
			target.delete("capitan")
			
			say_title(mob_name(20355))
			say("")
			if pc.getqf("time_to_wait") > pc.get_playtime() then
				local time_to_wait = pc.getqf("time_to_wait") - pc.get_playtime()
				say("Timpul de asteptat inca nu au trecut.")
				say("")
				say("Timp ramas: "..time_to_wait.." minute.")
				say("")
			else
				pc.setqf("time_to_wait", 0)
				say("Asa cum am promis, uite materialul.")
				say("")
				if pc.getqf("collect_count") >= 9 then
					pc.setqf("collect_count", pc.getqf("collect_count") + 1)
					set_state("__complete")
				else
					pc.setqf("collect_count", pc.getqf("collect_count") + 1)
					set_state("go_to_disciple")
				end
				
				pc.give_item2(85000, 1)
			end
		end
	end
	
	state __complete begin
		when enter begin
			pc.delqf("time_to_wait")
			pc.delqf("collect_count")
		end
		
		when letter begin
			local v = find_npc_by_vnum(20008)
			if v != 0 then
				target.vid("octavio_reward", v, "Octavio")
			end
			
			send_letter("*Imbracaminte speciala")
		end
		
		when button or info begin
			say_title(mob_name(20008))
			say("")
			say("Octavio vrea sa creeze o e�arfa ")
			say("pentru tine. Du-te �i vorbe�te cu el.")
			say("")
		end
		
		when octavio_reward.target.click or 20084.chat."Mareste-ti puterile" begin
			target.delete("octavio_reward")
			
			say_title(mob_name(20008))
			say("")
			say("Ah, te-ai �ntors! "..mob_name(20355).." mi-a spus ca")
			say("ai facut rost de materialele necesare.")
			say("")
			say("Vreau sa vad...")
			say("")
			wait()
			say_title(mob_name(20008))
			say("")
			if pc.count_item(85000) < 10 then
				say("Ce? Nu ai destule materiale!")
				say("")
				say("Du-te �napoi la capitan �i vorbe�te cu el!")
				say("")
				set_state("go_to_disciple")
			else
				pc.remove_item(85000, 10)
				pc.give_item2(85005, 1)
				say("Ok, totul este �n regula.")
				say("")
				say_reward("Ai primit "..item_name(85005)..".")
				say("")
				say("Pentru a repeta misiunea, doar deschide-mi scrisoarea.")
				say("")
				set_state("information")
			end
		end
	end
end