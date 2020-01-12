--[[ *quest fonksiyonları
	deathmatch.get_attender_count
	deathmatch.get_spectator_count
	deathmatch.get_status
	deathmatch.get_mapindex
	deathmatch.open
	deathmatch.start_event
	deathmatch.end_event
	deathmatch.check_status
	deathmatch.join_spectator
	deathmatch.give_item
	deathmatch.get_high_score_owner
	deathmatch.get_high_score
]]--

quest qDeathMatchPanel begin
	state start begin
		when 11001.chat."GM: Deathmatch " or 11003.chat."GM: Deathmatch " or 11005.chat."GM: Deathmatch " with pc.is_gm() begin
			local flag = "deathmatch_status"
			local statu = deathmatch.get_status()
			local savasci = deathmatch.get_attender_count()
			local izleyici = deathmatch.get_spectator_count()
			local map_index = deathmatch.get_mapindex()

			if statu == 0 then
				say_npc()
				say("")
				local baslatildimenu = select("Etkinligin girisleri ac ","Item ver ", "Vazgec ")
				if baslatildimenu == 1 then
					say_npc("")
					say("Deathmatch etkinliginin girisleri suan kapali acmak ")
					say("istiyor musun? ")
					say("")

					local girisac = select("Evet","Hayir ")
					if girisac == 1 then
						say_npc("")
						say("")
						say("Oldurme limiti kac olsun? ")
						local limit = tonumber(input())
						if limit <= 0 then
							say_npc("")
							say("")
							say("Hatali giris. ")
							return
						end

						say_npc()
						say("")
						say(""..limit.." olarak ayarlandi onayliyor musun? ")
						say("")
						local limitayarla = select("Baslat","Iptal ")
						if limitayarla == 1 then
							deathmatch.open()
							game.set_event_flag("deathmatch_kill_limit",limit)

							say_npc()
							say("")
							say("Deathmatch girisleri acildi. ")
							notice_all("Deathmatch etkinligi girisleri acildi! ")
							notice_all("Etkinlige katilmak icin lutfen Savas Sorumlusu ile gorusun. ")
							notice_all("Oldurme limiti: "..limit.." ")
						else
							return
						end
					else
						return
					end
				elseif baslatildimenu == 2 then
					say_npc()
					say("")
					say("Vermek istedigin itemin kodunu gir")
					local odulkodu = input()
					--if odulkodu <= 0 then
					--	return
					--end

					say_npc()
					say("")
 					say("Vermek istedigin itemin adetini gir")
					local adetkodu = input()
					--if adetkodu <= 0 then
					--	return
					--end

					say_npc()
					say("")
					say("Item kodu: "..odulkodu.." ")
					say("Miktar: "..adetkodu.." ")

					say("Onalıyor musun? ")
					local onay = select("Evet","Hayır ")
					if onay == 1 then
						say_npc()
						say("")
						say("Eşya verildi. ")
						deathmatch.give_item(odulkodu, adetkodu)
					else
						return
					end
				else
					return
				end
			elseif statu == 1 then
				if pc.get_map_index() == map_index then
					local limit = game.get_event_flag("deathmatch_kill_limit")
					say_npc("")
					say("")
					say("Etkinlikte suan "..savasci.." kisi var. Baslatmak istiyor musun? ")

					local baslat = select("Baslat ","Limit degistir ", "Bekle ")
					if baslat == 1 then
						if deathmatch.get_attender_count() < 2 then
							say_npc("")
							say("")
							say("Yeterli oyuncu yok. En az 2 oyuncu gerekli")
							return
						end
						say_npc("")
						say("")
						say("Etkinlik baslatildi. ")
						notice_all("Deathmatch etkinligi girisleri kapatildi. ")
						notice_in_map("Savas basladi! "..limit.." adam olduren ilk oyuncu, savasi kazanir. ", map_index)

						clear_server_timer("deathmatch_control_event")
						server_loop_timer("deathmatch_control_event", 60)
						deathmatch.start_event()
					elseif baslat == 2 then
						say_npc("")
						say("")
						say("Suan limit "..limit.." kisi degistirmek istiyor musun? ")
						local sec = select("Evet","Hayir ")
						if sec == 1 then
							say_npc("")
							say("")
							say("Oldurme limiti kac olsun? ")
							local limityeni = tonumber(input())
							if limityeni <= 0 then
								say_npc("")
								say("")
								say("Hatali giris. ")
								return
							end
							say_npc()
							say("")
							say(""..limityeni.." olarak ayarlandi onayliyor musun? ")
							local onay = select("Evet","Hayir ")
							if onay == 1 then
								say_npc()
								say("")
								say("Limit degistirildi.")
								notice_all("Oldurme limiti "..limityeni.." olarak degistirildi. ")
								game.set_event_flag("deathmatch_kill_limit",limityeni)
							else
								return
							end
						else
							return
						end
					elseif baslat == 3 then
						return
					end
				else
					say_npc("")
					say("")
					say("Yarismayi baslatmak icin savas haritasinda olmaniz gerekiyor. ")
				end
			elseif statu == 2 or statu == 3 then
				if pc.get_map_index() == map_index then
					say_npc()
					say("")
					say("Etkinlik suan devam ediyor. Kapatmak istiyor musun? ")
					say("")

					local kapat = select("Evet","Hayir ")
					if kapat == 1 then
						deathmatch.end_event()
						clear_server_timer("deathmatch_control_event")
						say_npc("")
						say("")
						say("Etkinlik kapatildi. ")
						notice_all("Deathmatch etkinligi sonlandi. ")
					else
						return
					end
				else
					return
				end
			else
				say_npc()
				say("")
				say("Suanda birsey yapamazsin. ")
			end
		end

		when 11001.chat."Deathmatch Etkinligi " or 11003.chat."Deathmatch Etkinligi " or 11005.chat."Deathmatch Etkinligi " begin
			local statu = deathmatch.get_status()
			say_npc()
			say("")
			say("Hey Evet Sen.")
			say("Sen gercekten cok guclu gorunuyorsun.")
			say("Etkinligin ismi Deathmatch. ")
			say("Etkinlikte oldurme limiti kadar adam oldurebilirsen ")
			say("etkinligi kazanirsin. ")

			if statu == 0 then
				wait()
				say_npc()
				say("")
				say("Etkinlige katilmana izin veriyorum. ")
				say("Baslama zamani henuz kararlastirilmadi. ")
				say("Zaman geldiginde seni bilgilendirecegim. ")
				say("Tetikte kal! ")
			elseif statu == 1 then
				wait()
				say_npc()
				say("")

				if pc.get_level() < 15 then
					say_npc()
					say("")
					say("Cok acemisin be!")
				end

				local flagonce = pc.getf("qDeathMatchPanel", "IsInLoginned")
				if flagonce != 0 then
					say_npc()
					say("")
					say("Zaten etkinliktesin!")
				end

				say("Etkinlige katilmak istiyor musun?")
				local s = select("Evet", "Izleyici olarak", "Hayir")
				if s == 1 then
					local yenistatu = deathmatch.get_status()
     				local flag = pc.getf("qDeathMatchPanel", "IsInLoginned")
     				if yenistatu == 1 and flag == 0 then
						pc.setf("qDeathMatchPanel", "IsInLoginned", 1)
						pc.warp(95500, 12500)
					else
						return
					end
				elseif s == 2 then
					local yenistatu = deathmatch.get_status()
     				local flag = pc.getf("qDeathMatchPanel", "IsInLoginned")
     				if yenistatu == 1 and flag == 0 then
						pc.setf("qDeathMatchPanel", "IsInLoginned", 1)
						deathmatch.join_spectator()
					else
						return
					end
				else
					return
				end
			end
		end

		when deathmatch_control_event.server_timer begin
			deathmatch.check_status()

			local owner = deathmatch.get_high_score_owner()
			local skor = deathmatch.get_high_score()
			local attender_count = deathmatch.get_attender_count()
			local spectator_count = deathmatch.get_spectator_count()

			if owner != 0 and skor != 0 then
				notice_all("Deathmatch event continues with " .. spectator_count .. " Spectator and " .. attender_count .. " Player ")
				notice_all("The highest score: " .. skor .. " Owner: " .. owner)
			end
		end
	end
end
