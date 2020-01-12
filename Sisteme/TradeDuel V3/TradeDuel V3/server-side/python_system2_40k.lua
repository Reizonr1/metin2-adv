--[[

!! Dont remember to change as your locale path. (usr/game/share/locale/turkey/quest) !!

TR: Tüm özel sistemler, fonksiyonlar, methodlar, ve yol...
TRL : All Special Systems, funcs, method, the way to...

Geliþtirici : .. Fatihbab34™ ..
Paketler ; LuaToPython, PythonToLua, PythonIslem
Fonksiyonlar ; "split('#blabla#blabla#', '#'), systems.getinput('PythonIslem'), io funcs(open, remove, write, read, readline, readlines), table forms, pc.getqf(), pc.setqf()"

--]]

quest systems begin
	state start begin

		function duello_kazandin(name)
			local item_slot = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..name..'ile'..pc.get_name()..'_slot.cfg', "r")
			local item_equip = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..name..'ile'..pc.get_name()..'_equip.cfg', "r")
			local item_para = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..name..'ile'..pc.get_name()..'_para.cfg', "r")
			local round_info = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..name..'_round.cfg', 'r')
			
			local item_ve_para = {}
			local bol = systems.split(round_info:read(), "#")
			
			if item_equip then -- Ekipman slot
				for item in item_equip:lines() do
					local items = systems.split(item,"#")
					if items[25] == pc.get_name() then
						
						table.insert(item_ve_para, item.."equip#"..bol[1].."#")
						--systems.duello_itemiver(item)
					else
						syschat("<Düello> : Düello'da bir bug tespit edildi!")
					end
				end
				--os.remove("/usr/game/share/locale/turkey/quest/systems/itemineduello/"..name.."ile"..pc.get_name().."_equip.cfg")
			end

			if item_slot then -- 45'lik slot
				for item in item_slot:lines() do
					local items = systems.split(item,"#")
					if items[25] == pc.get_name() then
						table.insert(item_ve_para, item.."slot#"..bol[1].."#")
						--systems.duello_itemiver(item)
					else
						syschat("<Düello> : Düello'da bir bug tespit edildi!")
					end
				end
				--os.remove("/usr/game/share/locale/turkey/quest/systems/itemineduello/"..name.."ile"..pc.get_name().."_slot.cfg")
			end

			if item_para then
				local para = item_para:read()
				table.insert(item_ve_para, para.."#para#"..name.."#"..bol[1].."#")
				--pc.change_money(tonumber(para))
			end
			
			local duello_liste = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_duellom.cfg', "r")
			if duello_liste then 
				duello_liste:close()
				local duello_liste_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_duellom.cfg', "w+")
				duello_liste_yaz:write(tostring(name).."\\n")
				duello_liste_yaz:close()
			else
				local duello_liste_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_duellom.cfg', "w")
				duello_liste_yaz:write(tostring(name).."\\n")
				duello_liste_yaz:close()
			end
			
			local duello_info = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_bilgiler.cfg', "r")
			if duello_info then
				local duello_info_bol = systems.split(tostring(duello_info:read()),"#")
				local duello_info_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_bilgiler.cfg', "w")
				duello_info_yaz:write(tostring(tonumber(duello_info_bol[1])+1).."#"..tostring(tonumber(duello_info_bol[2])+1).."#"..tostring(duello_info_bol[3]).."#"..tostring(duello_info_bol[4]).."#")
				duello_info_yaz:close()
			end
			
			if table.getn(item_ve_para) > 0 then
				systems.duello_depo_ekle(item_ve_para)
			else
				syschat("<Düello>: Rakip birþey koymadýðý için hiçbir þey kazanamadýn.")
			end
			
			round_info:close()
			
			pc.delqf("iteminews_basladi")
			
			os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..name..'_round.cfg')
			os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..name..'ile'..pc.get_name()..'_round.cfg')

		end
		
		function duello_depo_ekle(items)
			local isim = ""
			local kontrol = 0
			local items_var = {}
			
			for i=1, table.getn(items) do
				local bolx = systems.split(items[i], "#")
				if tostring(bolx[2]) == "para" then
					isim = bolx[3]
				else
					isim = systems.split(items[i],"#")[24]
				end
			end
			
			local ac_kontrol = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg', "r")
			if ac_kontrol then
				--local seek_eski = ac_kontrol:seek()
				--syschat(ac_kontrol:seek("end"))
				
				local items_ac = {}
				local pos = 0
				for fx in ac_kontrol:lines() do
					--syschat(fx)
					kontrol=1
					local bol = systems.split(fx, "#")
					table.insert(items_var, fx)
					--if tostring(bol[2]) == "para" then
					--	syschat("para varmi konbtrol")
					--	if bol[3] == isim then
					--		syschat("para daha önce var.")
					--		kontrol = 1
					
					--	else
					--		table.insert(items_ac, fx)
					--	end
					--else
					--	if bol[24] == isim then
					--		kontrol = 1
					--		table.insert(items_var, fx)
					--	else
					--		table.insert(items_ac, fx)
						--end
					--end
				end
				
				--ac_kontrol:seek("set", seek_eski)
				
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg', "w+")
				for i=1, table.getn(items) do
					ac:write(items[i].."\\n")	
				end
				ac:close()
				
				local ci = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg', "a+")
				for i = 1, table.getn(items_ac) do
					ci:write(items_ac[i].."\\n")		
				end
				ci:flush()
				ci:close()
			else
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg', "w+")
				for i=1, table.getn(items) do
					ac:write(items[i].."\\n")	
				end
				ac:close()
			end
			
			local ac_bilgiler = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_bilgiler.cfg', "r")
			local ac_bilgiler_oku = ac_bilgiler:read()
			if kontrol == 1 then
				local tek = 0
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo_sonws.cfg', "w+")
				for i=1, table.getn(items_var) do
					ac:write(items_var[i].."\\n")	
				end
				ac:close()
				
				for i=1, table.getn(items) do
					if tek == 0 then
						cmdchat("LuaToPython duello_depo_ac|1|#"..items[i]..ac_bilgiler_oku)
						tek = 1
					else
						cmdchat("LuaToPython duello_depo_ac|0|#"..items[i]..ac_bilgiler_oku)
					end
				end
				
				--cmdchat("LuaToPython duello_depo_ac|2|#"..isim.."#")
			else
				for i=1, table.getn(items) do
					cmdchat("LuaToPython duello_depo_ac|0|#"..items[i]..ac_bilgiler_oku)
					if i == table.getn(items) then
						cmdchat("LuaToPython duello_depo_ac|2|#"..isim.."#")
						return
					end
				end
			end
		end
		
		function duello_depo_yenile()
			local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg', "r")
			if ac then
				local ac_bilgiler = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_bilgiler.cfg', "r")
				local ac_bilgiler_oku = ac_bilgiler:read()
				local tek = 0
				local items = {}
				for item in ac:lines() do
					table.insert(items, item)
				end
				
				for i=1, table.getn(items) do
					cmdchat("LuaToPython duello_depo_ac|0|#"..items[i]..ac_bilgiler_oku)
					if i == table.getn(items) then
						cmdchat("LuaToPython duello_depo_ac|3|#"..systems.split(items[i],"#")[24].."#")
					end
				end
			else
				local ac_bilgiler = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_bilgiler.cfg', "r")
				local ac_bilgiler_oku = ac_bilgiler:read()
				cmdchat("LuaToPython duello_depo_ac|4|#"..ac_bilgiler_oku)
			end
		end

		function duello_kaybettin(name)
			local item_slot = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..name..'_slot.cfg', "r")
			local item_equip = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..name..'_equip.cfg', "r")
			local item_para = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..name..'_para.cfg', "r")

			if item_equip then -- Ekipman slot
				for item in item_equip:lines() do
					local items = systems.split(item,"#")
					systems.duello_itemisil(item)
				end
			end

			if item_slot then -- 45'lik slot
				for item in item_slot:lines() do
					local items = systems.split(item,"#")
					systems.duello_itemisil(item)
				end
			end

			if item_para then
				local para = item_para:read()
				pc.change_money(-tonumber(para))
			end
			
			local duello_liste = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_duellom.cfg', "r")
			if duello_liste then 
				duello_liste:close()
				local duello_liste_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_duellom.cfg', "w+")
				duello_liste_yaz:write(tostring(name).."\\n")
				duello_liste_yaz:close()
			else
				local duello_liste_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_duellom.cfg', "w")
				duello_liste_yaz:write(tostring(name).."\\n")
				duello_liste_yaz:close()
			end
			
			local duello_info = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_bilgiler.cfg', "r")
			if duello_info then
				local duello_info_bol = systems.split(tostring(duello_info:read()),"#")
				local duello_info_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_bilgiler.cfg', "w")
				duello_info_yaz:write(tostring(tonumber(duello_info_bol[1])+1).."#"..tonumber(duello_info_bol[2]).."#"..tostring(tonumber(duello_info_bol[3])+1).."#"..tostring(duello_info_bol[4]).."#")
				duello_info_yaz:close()
			end
			
			pc.delqf("iteminews_basladi")
		end

		function duello_kontrolleri(op)
			local kontrol = systems.getinput("DUELLO_KONTROL")
			local bol2 = systems.split(kontrol, "#")
			local ad = bol2[2] -- rakip ad
			local adam = find_pc_by_name(ad)
			if tonumber(adam) == tonumber(bol2[3]) then
				if tonumber(bol2[1]) == 1 then
					--syschat("<Düello> : Tebrikler! Rakibini devirdin.") -- itemleri verilicek

					cmdchat("LuaToPython DUELLO_BITTI")
					--chat("çalýþýyomu bu fonksiyon amk?")
					--chat(pc.get_name()..'ile'..ad..'.cfg')

					local item_slot = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..ad..'_slot.cfg', "r")
					local item_equip = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..ad..'_equip.cfg', "r")
					local item_para = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..ad..'_para.cfg', "r")

					--chat("bu local'erin altý çalýþýyomu")

					local item_slot_kontrol = 0 -- 1: sorun var.
					local item_equip_kontrol = 0 -- 1: sorun var.
					local item_para_kontrol = 0 -- 1: sorun var.
					
					local ac5x2 = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_rakipisim.cfg', 'r')
					if not ac5x2 then
						--syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
						local adam = find_pc_by_name(ad)
						pc.select(tonumber(adam))
						--syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
						cmdchat("LuaToPython DUELLO_BITTI")
					end

					if item_slot then -- Ekipman slot
						--syschat("klasör var...")
						for itemx in item_slot:lines() do
							item_slot_kontrol = 1
							local bol = systems.split(itemx,"#")
							local items_sec = systems.split(itemx,"#")[3]
							item.select_cell(tonumber(items_sec))

							if tonumber(item.get_cell()) != tonumber(items_sec) then
								syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
								local adam = find_pc_by_name(ad)
								pc.select(tonumber(adam))
								syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
								cmdchat("LuaToPython DUELLO_BITTI")
								return
							end

							local attr = {{item.get_attribute_type(0),item.get_attribute_value(0)}, {item.get_attribute_type(1),item.get_attribute_value(1)}, {item.get_attribute_type(2),item.get_attribute_value(2)}, {item.get_attribute_type(3),item.get_attribute_value(3)},{item.get_attribute_type(4),item.get_attribute_value(4)},{item.get_attribute_type(5),item.get_attribute_value(5)},{item.get_attribute_type(6),item.get_attribute_value(6)}}
							local socket, itemVnum, itemCount = {item.get_socket(0), item.get_socket(1), item.get_socket(2),item.get_socket(3),item.get_socket(4),item.get_socket(5)}, item.get_vnum(), item.get_count()

							--[[syschat(bol[1].." = "..itemVnum.." |||||||||| ".. bol[2].." = "..itemCount)
							chat(bol[4].." = "..socket[1])
							chat(bol[5].." = "..socket[2])
							chat(bol[6].." = "..socket[3])
							chat(bol[7].." = "..socket[4])
							chat(bol[8].." = "..socket[5])
							chat(bol[9].." = "..socket[6])
							chat(bol[10].." = "..attr[1][1])
							chat(bol[11].." = "..attr[1][2])
							chat(bol[12].." = "..attr[2][1])
							chat(bol[13].." = "..attr[2][2])
							chat(bol[14].." = "..attr[3][1])
							chat(bol[15].." = "..attr[3][2])
							chat(bol[16].." = "..attr[4][1])
							chat(bol[17].." = "..attr[4][2])
							chat(bol[18].." = "..attr[5][1])
							chat(bol[19].." = "..attr[5][2])
							chat(bol[20].." = "..attr[6][1])
							chat(bol[21].." = "..attr[6][2])
							chat(bol[22].." = "..attr[7][1])
							chat(bol[23].." = "..attr[7][2])
							chat(bol[25].." = "..ad) --]]
							
							if tonumber(bol[1]) == tonumber(itemVnum) and tonumber(bol[2]) == tonumber(itemCount) and tonumber(bol[4]) == tonumber(socket[1]) and tonumber(bol[5]) == tonumber(socket[2]) and tonumber(bol[6]) == tonumber(socket[3]) and tonumber(bol[7]) == tonumber(socket[4]) and tonumber(bol[8]) == tonumber(socket[5]) and tonumber(bol[9]) == tonumber(socket[6]) and tonumber(bol[10]) == tonumber(attr[1][1]) and tonumber(bol[11]) == tonumber(attr[1][2]) and tonumber(bol[12]) == tonumber(attr[2][1]) and tonumber(bol[13]) == tonumber(attr[2][2]) and tonumber(bol[14]) == tonumber(attr[3][1]) and tonumber(bol[15]) == tonumber(attr[3][2]) and tonumber(bol[16]) == tonumber(attr[4][1]) and tonumber(bol[17]) == tonumber(attr[4][2]) and tonumber(bol[18]) == tonumber(attr[5][1]) and tonumber(bol[19]) == tonumber(attr[5][2]) and tonumber(bol[20]) == tonumber(attr[6][1]) and tonumber(bol[21]) == tonumber(attr[6][2]) and tonumber(bol[22]) == tonumber(attr[7][1]) and tonumber(bol[23]) == tonumber(attr[7][2]) then
								item_slot_kontrol = 0
								--chat("item_slot eþit...")
								--print "birþey yapma..."
							else
								--if bol[1] == itemVnum and bol[2] == itemCount then
								--	syschat('bol[1] == itemVnum and bol[2] == itemCount')
								--end
								--if bol[4] == socket[1] and bol[5] == socket[2] then
								--	syschat('bol[4] == socket[1] and bol[5] == socket[5]')
								--end
								--if bol[6] == socket[3] and bol[7] == socket[3] then
								--	syschat('bol[6] == socket[3] and bol[7] == socket[3]')
								--end
								--if bol[10] == attr[1][1] and bol[11] == attr[1][2] then
								--	syschat('bol[10] == attr[1][1] and bol[11] == attr[1][2]')
								--end
								--if tonumber(bol[10]) == tonumber(attr[1][1]) and tonumber(bol[11]) == tonumber(attr[1][2]) then
								--	syschat('bol[10] == attr[1][1] and bol[11] == attr[1][2]')
								--end
								--chat("item_slot eþit deðil aq ...")
								item_slot_kontrol = 1
								syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
								local adam = find_pc_by_name(ad)
								pc.select(tonumber(adam))
								syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
								cmdchat("LuaToPython DUELLO_BITTI")
								return
							end
						end
					end 

					if item_equip then -- Ekipman slot
						for itemd in item_equip:lines() do
							item_equip_kontrol = 1
							local bol = systems.split(itemd,"#")
							local items_sec = systems.split(itemd,"#")[3]
							item.select_cell(tonumber(items_sec))

							if tonumber(item.get_cell()) != tonumber(items_sec) then
								syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
								local adam = find_pc_by_name(ad)
								pc.select(tonumber(adam))
								syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
								cmdchat("LuaToPython DUELLO_BITTI")
								return
							end

							local attr = {{item.get_attribute_type(0),item.get_attribute_value(0)}, {item.get_attribute_type(1),item.get_attribute_value(1)}, {item.get_attribute_type(2),item.get_attribute_value(2)}, {item.get_attribute_type(3),item.get_attribute_value(3)},{item.get_attribute_type(4),item.get_attribute_value(4)},{item.get_attribute_type(5),item.get_attribute_value(5)},{item.get_attribute_type(6),item.get_attribute_value(6)}}
							local socket, itemVnum, itemCount = {item.get_socket(0), item.get_socket(1), item.get_socket(2),item.get_socket(3),item.get_socket(4),item.get_socket(5)}, item.get_vnum(), item.get_count()

							if tonumber(bol[1]) == tonumber(itemVnum) and tonumber(bol[2]) == tonumber(itemCount) and tonumber(bol[4]) == tonumber(socket[1]) and tonumber(bol[5]) == tonumber(socket[2]) and tonumber(bol[6]) == tonumber(socket[3]) and tonumber(bol[7]) == tonumber(socket[4]) and tonumber(bol[8]) == tonumber(socket[5]) and tonumber(bol[9]) == tonumber(socket[6]) and tonumber(bol[10]) == tonumber(attr[1][1]) and tonumber(bol[11]) == tonumber(attr[1][2]) and tonumber(bol[12]) == tonumber(attr[2][1]) and tonumber(bol[13]) == tonumber(attr[2][2]) and tonumber(bol[14]) == tonumber(attr[3][1]) and tonumber(bol[15]) == tonumber(attr[3][2]) and tonumber(bol[16]) == tonumber(attr[4][1]) and tonumber(bol[17]) == tonumber(attr[4][2]) and tonumber(bol[18]) == tonumber(attr[5][1]) and tonumber(bol[19]) == tonumber(attr[5][2]) and tonumber(bol[20]) == tonumber(attr[6][1]) and tonumber(bol[21]) == tonumber(attr[6][2]) and tonumber(bol[22]) == tonumber(attr[7][1]) and tonumber(bol[23]) == tonumber(attr[7][2]) then
								--chat("item_equip eþit...")
								--print "hiç birþey yapma..."
								item_equip_kontrol = 0
							else
								item_equip_kontrol = 1
								syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
								local adam = find_pc_by_name(ad)
								pc.select(tonumber(adam))
								syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
								cmdchat("LuaToPython DUELLO_BITTI")
								return
							end
						end
					end 

					if item_para then
						local param = item_para:read()
						if pc.get_money() >= tonumber(param) then
							print "bir þey yapma..."
						else
							item_para_kontrol = 1
							syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
							local adam = find_pc_by_name(ad)
							pc.select(tonumber(adam))
							syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
							cmdchat("LuaToPython DUELLO_BITTI")
							return
						end
					end
			
					--syschat("deneme kontrol")

					if item_slot_kontrol == 0 and item_equip_kontrol == 0 and item_para_kontrol == 0 then
						--print "hiç birþey yapma..."
						pc.select(tonumber(adam))
						cmdchat("LuaToPython DUELLO_BITTI")
						--chat("Düello'yu kaybettin...")
						--chat(pc.get_name()..'ile'..bol2[4]..'.cfg')

						local item_slot_r = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol2[4]..'_slot.cfg', "r")
						local item_equip_r = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol2[4]..'_equip.cfg', "r")
						local item_para_r = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol2[4]..'_para.cfg', "r")

						local item_slot_kontrol_rakip = 0 -- 1: sorun var.
						local item_equip_kontrol_rakip = 0 -- 1: sorun var.
						local item_para_kontrol_rakip = 0 -- 1: sorun var. 
						
						local ac5x2 = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol2[4]..'_rakipisim.cfg', 'r')
						if not ac5x2 then
							--syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
							local adam = find_pc_by_name(bol2[4])
							pc.select(tonumber(adam))
							--syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
						end

						if item_slot_r then -- Ekipman slot
							for itemt in item_slot_r:lines() do
								item_slot_kontrol_rakip = 1
								local bol = systems.split(itemt,"#")
								local items_sec = systems.split(itemt,"#")[3]
								item.select_cell(tonumber(items_sec))

								if tonumber(item.get_cell()) != tonumber(items_sec) then
									syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
									local adam = find_pc_by_name(bol2[4])
									pc.select(tonumber(adam))
									syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
									return
								end

								local attr = {{item.get_attribute_type(0),item.get_attribute_value(0)}, {item.get_attribute_type(1),item.get_attribute_value(1)}, {item.get_attribute_type(2),item.get_attribute_value(2)}, {item.get_attribute_type(3),item.get_attribute_value(3)},{item.get_attribute_type(4),item.get_attribute_value(4)},{item.get_attribute_type(5),item.get_attribute_value(5)},{item.get_attribute_type(6),item.get_attribute_value(6)}}
								local socket, itemVnum, itemCount = {item.get_socket(0), item.get_socket(1), item.get_socket(2),item.get_socket(3),item.get_socket(4),item.get_socket(5)}, item.get_vnum(), item.get_count()

								if tonumber(bol[1]) == tonumber(itemVnum) and tonumber(bol[2]) == tonumber(itemCount) and tonumber(bol[4]) == tonumber(socket[1]) and tonumber(bol[5]) == tonumber(socket[2]) and tonumber(bol[6]) == tonumber(socket[3]) and tonumber(bol[7]) == tonumber(socket[4]) and tonumber(bol[8]) == tonumber(socket[5]) and tonumber(bol[9]) == tonumber(socket[6]) and tonumber(bol[10]) == tonumber(attr[1][1]) and tonumber(bol[11]) == tonumber(attr[1][2]) and tonumber(bol[12]) == tonumber(attr[2][1]) and tonumber(bol[13]) == tonumber(attr[2][2]) and tonumber(bol[14]) == tonumber(attr[3][1]) and tonumber(bol[15]) == tonumber(attr[3][2]) and tonumber(bol[16]) == tonumber(attr[4][1]) and tonumber(bol[17]) == tonumber(attr[4][2]) and tonumber(bol[18]) == tonumber(attr[5][1]) and tonumber(bol[19]) == tonumber(attr[5][2]) and tonumber(bol[20]) == tonumber(attr[6][1]) and tonumber(bol[21]) == tonumber(attr[6][2]) and tonumber(bol[22]) == tonumber(attr[7][1]) and tonumber(bol[23]) == tonumber(attr[7][2]) then
									--print "hiç birþey yapma..."
									item_slot_kontrol_rakip = 0
								else
									item_slot_kontrol_rakip = 1
									syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
									local adam = find_pc_by_name(bol2[4])
									pc.select(tonumber(adam))
									syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
									return
								end
							end
						end

						if item_equip_r then -- Ekipman slot
							for itemn in item_equip_r:lines() do
								item_equip_kontrol_rakip = 1
								local bol = systems.split(itemn,"#")
								local items_sec = systems.split(itemn,"#")[3]
								item.select_cell(tonumber(items_sec))

								if tonumber(item.get_cell()) != tonumber(items_sec) then
									syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
									local adam = find_pc_by_name(bol2[4])
									pc.select(tonumber(adam))
									syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
									return
								end

								local attr = {{item.get_attribute_type(0),item.get_attribute_value(0)}, {item.get_attribute_type(1),item.get_attribute_value(1)}, {item.get_attribute_type(2),item.get_attribute_value(2)}, {item.get_attribute_type(3),item.get_attribute_value(3)},{item.get_attribute_type(4),item.get_attribute_value(4)},{item.get_attribute_type(5),item.get_attribute_value(5)},{item.get_attribute_type(6),item.get_attribute_value(6)}}
								local socket, itemVnum, itemCount = {item.get_socket(0), item.get_socket(1), item.get_socket(2),item.get_socket(3),item.get_socket(4),item.get_socket(5)}, item.get_vnum(), item.get_count()

								if tonumber(bol[1]) == tonumber(itemVnum) and tonumber(bol[2]) == tonumber(itemCount) and tonumber(bol[4]) == tonumber(socket[1]) and tonumber(bol[5]) == tonumber(socket[2]) and tonumber(bol[6]) == tonumber(socket[3]) and tonumber(bol[7]) == tonumber(socket[4]) and tonumber(bol[8]) == tonumber(socket[5]) and tonumber(bol[9]) == tonumber(socket[6]) and tonumber(bol[10]) == tonumber(attr[1][1]) and tonumber(bol[11]) == tonumber(attr[1][2]) and tonumber(bol[12]) == tonumber(attr[2][1]) and tonumber(bol[13]) == tonumber(attr[2][2]) and tonumber(bol[14]) == tonumber(attr[3][1]) and tonumber(bol[15]) == tonumber(attr[3][2]) and tonumber(bol[16]) == tonumber(attr[4][1]) and tonumber(bol[17]) == tonumber(attr[4][2]) and tonumber(bol[18]) == tonumber(attr[5][1]) and tonumber(bol[19]) == tonumber(attr[5][2]) and tonumber(bol[20]) == tonumber(attr[6][1]) and tonumber(bol[21]) == tonumber(attr[6][2]) and tonumber(bol[22]) == tonumber(attr[7][1]) and tonumber(bol[23]) == tonumber(attr[7][2]) then
									item_equip_kontrol_rakip = 0
									--print "hiç birþey yapma..."
								else
									item_equip_kontrol_rakip = 1
									
									syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
									local adam = find_pc_by_name(bol2[4])
									pc.select(tonumber(adam))
									syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
									return
								
								end
							end
						end

						if item_para_r then
							local param = item_para_r:read()
							if pc.get_money() >= tonumber(param) then
								print "bir þey yapma..."
							else
								item_para_kontrol_rakip = 1
								syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
								local adam = find_pc_by_name(bol2[4])
								pc.select(tonumber(adam))
								syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
								return
							end
						end

						if item_slot_kontrol_rakip == 0 and item_equip_kontrol_rakip == 0 and item_para_kontrol_rakip == 0 then
							syschat("<Düello> : Düello'yu Kaybettin! Bu yüzden yatýrdýðýn item veya paralarý kaybettin.")
							systems.duello_kaybettin(bol2[4])
							local pc_kazanan = find_pc_by_name(bol2[4])
							
							pc.select(tonumber(pc_kazanan))
							syschat("<Düello> : Tebrikler! Rakibini devirdin.")
							systems.duello_kazandin(bol2[2])
						else
							syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
							local pc_kazanan = find_pc_by_name(bol2[4])
							pc.select(tonumber(pc_kazanan))
							syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
						end

						--if item_slot_kontrol == 0 and item_equip_kontrol == 0 and item_para_kontrol == 0 and item_slot_kontrol_rakip == 0 and item_equip_kontrol_rakip == 0 and item_para_kontrol_rakip == 0 then
								
						--	systems.duello_kaybettin(bol2[4])
						--	local pc_kazanan = find_pc_by_name(bol2[4])
							
						--	pc.select(tonumber(pc_kazanan))
						--	systems.duello_kazandin(bol2[2])
						--else
						--	pc.select(tonumber(pc_kazanan))
						--	syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
						--end	
						--chat("sorun yok")
					else
						syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
						pc.select(tonumber(adam))
						syschat("<Düello> : Düello'da bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
						cmdchat("LuaToPython DUELLO_BITTI")
					end
					
				end 
			end
			
		end

		function duello_itemiver(itemTab)
			pc.give_item2_select(tonumber(systems.split(itemTab, "#")[1]),tonumber(systems.split(itemTab, "#")[2]))
			local attr,socket = {},{}
			for i = 10,23 do table.insert(attr,{systems.split(itemTab, "#")[i],systems.split(itemTab,"#")[i+1]}) i = i+1 end
			for i = 4,6 do table.insert(socket,systems.split(itemTab, "#")[i]) end
			for i = 1, table.getn(attr) do 
				item.set_value(i-1, attr[i][1], attr[i][2]) 
			end 
			for i = 1, table.getn(socket) do if tonumber(socket[i]) > 0 then item.set_socket(i-1, socket[i]) end end
		end

		function duello_itemisil(itemTab)
			local item_yer = systems.split(itemTab, "#")[3]
			item.select_cell(tonumber(item_yer))
			item.remove()
		end

		when kill begin
			if npc.is_pc() then
				local kontrol = systems.getinput("DUELLO_KONTROL")
				local bol = systems.split(kontrol, "#")
				local ad = bol[2] -- rakip ad
				local adam = find_pc_by_name(ad)
				--if tonumber(adam) == tonumber(bol[3]) then
				local vid = 0
				
				
				
				--pc.select(tonumber(bol[4]))
				if tonumber(adam) == tonumber(npc.get_vid()) then
					if tonumber(bol[1]) == 1 then
						local ac_round = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..ad..'_round.cfg', 'r')
						local ac_round_r = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..ad..'ile'..pc.get_name()..'_round.cfg', 'r')
						local ac_round_oku = ac_round:read()
						local ac_round_oku_r = ac_round_r:read()
						ac_round:close()
						ac_round_r:close()
						local bol_ = systems.split(ac_round_oku, "#")
						local bol_2 = systems.split(ac_round_oku_r, "#")
						if tonumber(bol_[1]) != tonumber(bol_2[1]) then
							syschat("<Düello> : Düello'da bir usulsüzlük oluþtu ve duello iptal oldu.")
							cmdchat("LuaToPython DUELLO_BITTI")
							os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..ad..'_round.cfg')
							os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..ad..'ile'..pc.get_name()..'_round.cfg')
							pc.select(tonumber(bol_[3]))
							syschat("<Düello> : Düello'da bir usulsüzlük oluþtu ve duello iptal oldu.")
							cmdchat("LuaToPython DUELLO_BITTI")
							return
						end
						local skor_benim = bol_[2]
						local skor_rakip = bol_2[2]
						local round_sayisi = bol_[1]
						
						if tonumber(bol_[2])+1 == tonumber(bol_[1]) then
							systems.duello_kontrolleri(bol[1])
						else
							local skor_yenile = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..ad..'_round.cfg', 'w')
							skor_yenile:write(bol_[1].."#"..tostring(tonumber(bol_[2]+1)))
							skor_yenile:close()
							cmdchat("LuaToPython duello_skor#"..tostring(tonumber(bol_[2])+1).."-"..bol_2[2])
							pc.select(tonumber(bol[3]))
							cmdchat("LuaToPython duello_skor#"..bol_2[2].."-"..tostring(tonumber(bol_[2])+1))
						end
						--syschat("<Düello> : Tebrikler! Rakibini devirdin.") -- itemleri verilicek
						
						--pc.select(tonumber(bol[3])) -- itemleri silinicek
						--systems.duello_kazandin(bol[2])
						
						--systems.duello_kaybettin(bol[4])
					end
				end
			end
		end
		
		when logout begin
			local duello_liste = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_duellom.cfg', "r")
			if duello_liste then
				for line in duello_liste:lines() do
					local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/duello_bilgileri.fatihbab34', 'r')
					if ac then
						for line2 in ac:lines() do
							local bol = systems.split(line2,"#")
							
							if string.find(bol[1], "_rakipisim") then
								
								local sil = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name().."_rakipisim.cfg", "r")
								local sil_rakip = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..line.."_rakipisim.cfg", "r")
								if sil then
									os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name().."_rakipisim.cfg")
								end
								if sil_rakip then
									os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..line.."_rakipisim.cfg")
								end
							else
								local sil = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..line..bol[1], 'r')
								local sil_rakip = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..line..'ile'..pc.get_name()..bol[1], 'r')
								if sil then
									os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..line..bol[1])
								end
								if sil_rakip then
									os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..line..'ile'..pc.get_name()..bol[1])
								end
							end
						end
					else
						syschat("duello_bilgileri.fatihbab34 % bulunamiyor.")
					end
				end
				os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_duellom.cfg')
			end
		end

		when login begin
			cmdchat("PythonToLua "..q.getcurrentquestindex())
			
			if pc.getqf("iteminews_basladi") == 1 then
				syschat("<Düello> : Ýtemine Ws'den kaçtýðýn için bitmeyen düello puanýn arttý.")
				local duello_info = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_bilgiler.cfg', "r")
				if duello_info then
					local duello_info_bol = systems.split(tostring(duello_info:read()),"#")
					local duello_info_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_bilgiler.cfg', "w")
					duello_info_yaz:write(tostring(tonumber(duello_info_bol[1])+1).."#"..tostring(duello_info_bol[2]).."#"..tostring(duello_info_bol[3]).."#"..tostring(tonumber(duello_info_bol[4])+1).."#")
					duello_info_yaz:close()
				end
				pc.delqf("iteminews_basladi")
			end
			
			local duello_liste = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_duellom.cfg', "r")
			if duello_liste then
				for line in duello_liste:lines() do
					local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/duello_bilgileri.fatihbab34', 'r')
					if ac then
						for line2 in ac:lines() do
							local bol = systems.split(line2,"#")
							
							if string.find(bol[1], "_rakipisim") then
								
								local sil = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name().."_rakipisim.cfg", "r")
								local sil_rakip = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..line.."_rakipisim.cfg", "r")
								if sil then
									os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name().."_rakipisim.cfg")
								end
								if sil_rakip then
									os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..line.."_rakipisim.cfg")
								end
							else
								local sil = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..line..bol[1], 'r')
								local sil_rakip = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..line..'ile'..pc.get_name()..bol[1], 'r')
								if sil then
									os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..line..bol[1])
								end
								if sil_rakip then
									os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..line..'ile'..pc.get_name()..bol[1])
								end
							end
						end
					else
						syschat("duello_bilgileri.fatihbab34 % bulunamiyor.")
					end
				end
				os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_duellom.cfg')
			end
			
			
		end

		when button begin
			local gelen = systems.getinput("PYTHONISLEM")
			
			if string.find(gelen, "itemine_duello_sil#") then
				local bol = systems.split(gelen, "#")
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/duello_bilgileri.fatihbab34', 'r')
				if ac then
					for line in ac:lines() do
						local bol2 = systems.split(line,"#")
						if string.find(bol2[1], "_rakipisim") then
							local sil = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name().."_rakipisim.cfg", "r")
							local sil_rakip = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2].."_rakipisim.cfg", "r")
							if sil then
								os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name().."_rakipisim.cfg")
							end
							if sil_rakip then
								os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2].."_rakipisim.cfg")
							end
						else
							local sil = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..bol2[1], 'r')
							local sil_rakip = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2]..'ile'..pc.get_name()..bol2[1], 'r')
							if sil then
								os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..bol2[1])
							end
							if sil_rakip then
								os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2]..'ile'..pc.get_name()..bol2[1])
							end
						end
					end
				else
					syschat("duello_bilgileri.fatihbab34 % bulunamiyor.")
				end
			end
			
			if string.find(gelen, "duello_depo_al#") then
				systems.duello_depo_yenile()
			end
			
			if string.find(gelen, "duello_depo_paracek#") then
				local bol = systems.split(gelen,"#")
				local items = {}
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg', 'r')
				if ac then
					for item in ac:lines() do
						local bol2 = systems.split(item, "#")
						if bol2[2] == "para" then
							if tonumber(bol[2]) <= tonumber(bol2[1]) then
								pc.change_money(tonumber(bol[2]))
							end
						else
							table.insert(items, item)
						end
					end
				else
					syschat("% itemine ws deposuna eriþilemiyor.")
				end
					
				local ac_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg', 'w+')
				for i=1, table.getn(items) do
					ac_yaz:write(items[i].."\\n")
				end
				ac_yaz:flush()
				ac_yaz:close()
				
				if table.getn(items) <= 0 then
					cmdchat("LuaToPython duello_depo_ac|5|")
					os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg')
				end
				
			end
			
			if string.find(gelen, "duello_depo_itemislemleri#") then
				local bol = systems.split(gelen, "#")
				
				if bol[2] == "hepsi" then
					local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg', 'r')
					if ac then
						for item in ac:lines() do
							local bol2 = systems.split(item, "#")
							if bol2[2] == "para" then
								pc.change_money(tonumber(bol2[1]))
							else
								systems.duello_itemiver(item)
							end
						end
					else
						syschat("% itemine ws deposuna eriþilemiyor.")
					end
					
					os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg')
					return
					
				elseif bol[2] == "sil" then
					os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg')
					return
					
				elseif bol[2] == "yenile" then
					systems.duello_depo_yenile()
					return
				end
				
				local items = {}
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg', 'r')
				if ac then
					for item in ac:lines() do
						local bol2 = systems.split(item, "#")
						if tonumber(bol2[26]) == tonumber(bol[3]) and bol2[28] == bol[2] then
							systems.duello_itemiver(item)
						else
							table.insert(items, item)
						end
					end
				else
					syschat("% itemine ws deposuna eriþilemiyor.")
				end
				
				local ac_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg', 'w+')
				for i=1, table.getn(items) do
					ac_yaz:write(items[i].."\\n")
				end
				ac_yaz:flush()
				ac_yaz:close()
				
				if table.getn(items) <= 0 then
					cmdchat("LuaToPython duello_depo_ac|5|")
					os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name()..'_depo.cfg')
				end
			end
			
			if string.find(gelen,"duello_round#") then
				local bol = systems.split(gelen, "#")
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[3]..'_kabul.cfg', 'r')
				local ac_2 = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[3]..'ile'..pc.get_name()..'_kabul.cfg', 'r')
				if ac then
					syschat("<Düello>: Düello'yu kabul ettikten sonra round iþlemlerini yapamazsýn.")
					return
				end
				if ac_2 then
					syschat("<Düello>: Rakip Düello'yu kabul ettikten sonra round iþlemlerini yapamazsýn.")
					return
				end
				local ac_round_oku = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[3]..'_round.cfg', 'r')
				local ac_round_okundu = ac_round_oku:read()
				ac_round_oku:close()
				local bol2 = systems.split(ac_round_okundu,"#")
				local ac_round = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[3]..'_round.cfg', 'w')
				ac_round:write(bol[2].."#"..bol2[2])
				ac_round:close()
				
				if tonumber(bol[4]) == 1 then
					syschat("<Düello> : Düello'da round sayýsý "..bol[2].." olarak baþarýyla "..bol[3].. " tarafýndan deðiþtirildi.")
				else
					syschat("<Düello> : Bu düello'daki round sayýsý baþarýyla "..bol[2].." olarak deðiþtirildi.")
				end
			end
			
			if string.find(gelen, "duello_sonws_depo_itemlerial#") then
				local bol = systems.split(gelen, "#")
				if tonumber(bol[2]) == 1 then
					local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name().."_depo_sonws.cfg", "r")
					if ac then
						for line in ac:lines() do
							--chat(line)
							local bol = systems.split(line,"#")
							if tostring(bol[2]) == "para" then
								pc.change_money(tonumber(bol[1]))
							else
								systems.duello_itemiver(line)
							end
						end
						
						os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name().."_depo_sonws.cfg")
					else
						syschat("% eski item kayitlarý bulunamiyor.")
					end
				else
					os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/depo/'..pc.get_name().."_depo_sonws.cfg")
				end
			end
			
			if string.find(gelen,"duello_basladi#") then
				local bol = systems.split(gelen, "#")
				local adam = find_pc_by_name(bol[2])
				pc.setqf("iteminews_basladi",1)
				pc.select(tonumber(adam))
				pc.setqf("iteminews_basladi",1)
			end
			
			if string.find(gelen, "duello_rakipbildir#") then
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name().."_rakipisim.cfg", "r")
				local adam_my_isim = ""
				local adam_target_isim = ac:read()
				local adam_my = find_pc_by_name(pc.get_name())
				local adam_rakip = find_pc_by_name(adam_target_isim)
				
				pc.select(tonumber(adam_rakip))
				adam_my_isim = pc.get_name()
				pc.select(tonumber(adam_my))
				
				if adam_my_isim == pc.get_name() and adam_my_isim != "" then
					pc.delqf("iteminews_basladi")
					syschat("<Düello>: "..adam_target_isim.." adlý oyuncuyu baþarýyla bildirdin.")
					local ac_bildir = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/duello_bildirilenler.fatihbab34', "r")
					if ac_bildir then
						local ac_bildir_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/duello_bildirilenler.fatihbab34', "a+")
						ac_bildir_yaz:write("bildiren: "..pc.get_name().. " | bildirilen: "..adam_target_isim.."\\n")
						ac_bildir_yaz:close()
					else
						local ac_bildir_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/duello_bildirilenler.fatihbab34', "w")
						ac_bildir_yaz:write("bildiren: "..pc.get_name().. " | bildirilen: "..adam_target_isim.."\\n")
						ac_bildir_yaz:close()
					end
					cmdchat("LuaToPython DUELLO_BITTI")
				else
					syschat("<Düello>: Oyuncu zaten þuanda düello'da.")
				end
			end

			if string.find(gelen, "duello_baslat#") then
				
				chat("<Düello> : Düello paneli açýldý, risk'e atmak istediðiniz eþyalarýný koy.")
				local bol = systems.split(gelen, "#")
				
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/duello_bilgileri.fatihbab34', 'r')
				if ac then
					for line in ac:lines() do
						local bol2 = systems.split(line,"#")
						if string.find(bol2[1], "_rakipisim") then
							local sil = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name().."_rakipisim.cfg", "r")
							local sil_rakip = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2].."_rakipisim.cfg", "r")
							if sil then
								os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name().."_rakipisim.cfg")
							end
							if sil_rakip then
								os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2].."_rakipisim.cfg")
							end
						else
							local sil = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..bol2[1], 'r')
							local sil_rakip = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2]..'ile'..pc.get_name()..bol2[1], 'r')
							if sil then
								os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..bol2[1])
							end
							if sil_rakip then
								os.remove('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2]..'ile'..pc.get_name()..bol2[1])
							end
						end
					end
				else
					syschat("duello_bilgileri.fatihbab34 % bulunamiyor.")
				end
				
				local ac_rakipisim = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_rakipisim.cfg', 'w')
				ac_rakipisim:write(bol[2])
				ac_rakipisim:close()
				
				local ac_rakipisim2 = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2]..'_rakipisim.cfg', 'w')
				ac_rakipisim2:write(pc.get_name())
				ac_rakipisim2:close()
				
				local ac_round = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..'_round.cfg', 'w')
				ac_round:write("1#0")
				ac_round:close()
				
				local ac_rakipround = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2]..'ile'..pc.get_name()..'_round.cfg', 'w')
				ac_rakipround:write("1#0")
				ac_rakipround:close()
				
				local ac_rakip_bilgileri = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2]..'_bilgiler.cfg', 'r')
				if not ac_rakip_bilgileri then
					local ac_rakip_bilgileri_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2]..'_bilgiler.cfg', 'w')
					ac_rakip_bilgileri_yaz:write("0#0#0#0#")
					ac_rakip_bilgileri_yaz:close()
				end
				
				local ac_benim_bilgilerim = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_bilgiler.cfg', 'r')
				if not ac_benim_bilgilerim then
					local ac_benim_bilgilerim_yaz = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_bilgiler.cfg', 'w')
					ac_benim_bilgilerim_yaz:write("0#0#0#0#")
					ac_benim_bilgilerim_yaz:close()
				end
				
				local ac_oku_rakip_bilgileri = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2]..'_bilgiler.cfg', 'r')
				local ac_oku_benim_bilgilerim = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'_bilgiler.cfg', 'r')
				local ac_oku_rakip_bilgileri_x = ac_oku_rakip_bilgileri:read()
				local ac_oku_benim_bilgilerim_x = ac_oku_benim_bilgilerim:read()
				
				cmdchat("LuaToPython duello_bilgileri|"..bol[2].."|#"..ac_oku_rakip_bilgileri_x.."|#"..ac_oku_benim_bilgilerim_x)
				ac_rakip_bilgileri:close()
				
			end 

			if string.find(gelen, "duello_para_ekle#") then -- test code 21.04 --
				--chat(gelen)
				local bol = systems.split(gelen, "#")
	
				local ac_kontrol = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[3]..'_para.cfg', 'r')

				local ac_k = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[3]..'_kabul.cfg', 'r')
				if ac_k then
					syschat("Þuanda panele para koyamazsýn, bu iþlem karþýda gözükmeyecektir.")
					return
				end

				local ac_k2 = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[3]..'ile'..pc.get_name()..'_kabul.cfg', 'r')
				if ac_k2 then
					syschat("Þuanda panele para koyamazsýn, bu iþlem karþýda gözükmeyecektir.")
					return
				end

				if pc.get_money() < tonumber(bol[2]) then
					syschat('<Düello> : Yeterli Paran Yok.')
					return
				end
				
				if tonumber(bol[2]) <= 0 then
					return
				end

				if ac_kontrol then
					syschat("<Düello> : Þuan'da toplamý deðiþtirmezsiniz.Bu iþlem karþý oyuncuda gözükmeyecektir.")
					return
				end

				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[3]..'_para.cfg', 'w')
				ac:write(tostring(bol[2]))
				ac:close()

				local adam = find_pc_by_name(bol[3])
				pc.select(tonumber(adam))
				cmdchat("LuaToPython duello_para_ekle#"..bol[2])
			end
			
			if string.find(gelen, "duello_kabul_ediyorum") then
				local bol = systems.split(gelen, "#")
				local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..'_kabul.cfg', 'w')
				ac:write("byfatihbab34")
				ac:close()
			end

			if string.find(gelen, "duello_itemekle_slot#") then
				--local item_yeri = systems.getinput("DUELLO_ITEM_SLOT_YERI")
				local yer = systems.split(gelen, "#")[2].."#"..systems.split(gelen, "#")[3].."#"..systems.split(gelen, "#")[4]
				local bol = systems.split(yer, "#")
				local bug_fixed = 0
				local fxd = 0
				--chat("testttt")
				--chat(bol[1])
				--chat(bol[1])

				local ac_k = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..'_kabul.cfg', 'r')
				if ac_k then
					syschat("Þuanda panele item koyamazsýn, bu iþlem karþýda gözükmeyecektir.")
					return
				end

				local ac_k2 = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2]..'ile'..pc.get_name()..'_kabul.cfg', 'r')
				if ac_k2 then
					syschat("Þuanda panele item koyamazsýn, bu iþlem karþýda gözükmeyecektir.")
					return
				end

				item.select_cell(bol[1])

				if tonumber(item.get_id()) == 0 then
					syschat("Bu itemi panele koyamazsýn, bu iþlem karþýda gözükmeyecektir.")
					return
				end
				
				if tonumber(item.get_vnum()) == 70011 or tonumber(item.get_vnum()) == 70042 or tonumber(item.get_vnum()) == 40001 or tonumber(item.get_vnum()) == 40004 or tonumber(item.get_vnum()) == 25041 or tonumber(item.get_vnum()) == 50125 or tonumber(item.get_vnum()) == 71135 then
					syschat("Bu nesne konulamaz.Bu iþlem karþýda gözükmeyecektir.")
					return
				end

				if tonumber(item.get_vnum()) >= 72723 and tonumber(item.get_vnum()) <= 72730 then
					syschat("Bu nesne konulamaz.Bu iþlem karþýda gözükmeyecektir.")
					return
				end
				
				local attr = {{item.get_attribute_type(0),item.get_attribute_value(0)}, {item.get_attribute_type(1),item.get_attribute_value(1)}, {item.get_attribute_type(2),item.get_attribute_value(2)}, {item.get_attribute_type(3),item.get_attribute_value(3)},{item.get_attribute_type(4),item.get_attribute_value(4)},{item.get_attribute_type(5),item.get_attribute_value(5)},{item.get_attribute_type(6),item.get_attribute_value(6)}}
				local socket, itemVnum, itemCount = {item.get_socket(0), item.get_socket(1), item.get_socket(2),item.get_socket(3),item.get_socket(4),item.get_socket(5)}, item.get_vnum(), item.get_count()
				if bug_fixed == 0 then
					local ac_kontrol = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..'_slot.cfg', 'r')
					if ac_kontrol then
						for fx in ac_kontrol:lines() do
							
							local bol = systems.split(fx,"#")
							if tonumber(bol[27]) == tonumber(item.get_id()) then
								chat("Ayný id'li itemi tekrardan koyamazsýn.")
								fxd = 1
							end
							
						end
						ac_kontrol:close()
						if fxd == 0 then
							local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..'_slot.cfg', 'a+')
							ac:write(itemVnum.."#"..itemCount.."#"..(bol[1]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[2]).."#"..(bol[3]).."#"..item.get_id().."#".."\\n")
							ac:close()
							local adam = find_pc_by_name(bol[2])
							pc.select(tonumber(adam))
							cmdchat("LuaToPython duello_item_ekle_slot|#"..itemVnum.."#"..itemCount.."#"..(bol[1]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[2]).."#"..(bol[3]).."#"..item.get_id().."#")
						end
						
					else
						local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..'_slot.cfg', 'a+')
						ac:write(itemVnum.."#"..itemCount.."#"..(bol[1]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[2]).."#"..(bol[3]).."#"..item.get_id().."#".."\\n")
						ac:close()
						local adam = find_pc_by_name(bol[2])
						pc.select(tonumber(adam))
						cmdchat("LuaToPython duello_item_ekle_slot|#"..itemVnum.."#"..itemCount.."#"..(bol[1]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[2]).."#"..(bol[3]).."#"..item.get_id().."#")
						
					end
					bug_fixed = 1
				end
			end
			
			if string.find(gelen, "duello_itemekle_equip#") then
				local yer = systems.split(gelen, "#")[2].."#"..systems.split(gelen, "#")[3].."#"..systems.split(gelen, "#")[4]
				local bol = systems.split(yer, "#")
				local bug_fixed = 0
				local fxd = 0
				--chat(item_yeri)
	
				local ac_k = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..'_kabul.cfg', 'r')
				if ac_k then
					syschat("Þuanda panele item koyamazsýn, bu iþlem karþýda gözükmeyecektir.")
					return
				end

				local ac_k2 = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..bol[2]..'ile'..pc.get_name()..'_kabul.cfg', 'r')
				if ac_k2 then
					syschat("Þuanda panele item koyamazsýn, bu iþlem karþýda gözükmeyecektir.")
					return
				end

				item.select_cell(bol[1])

				if tonumber(item.get_id()) == 0 then
					syschat("Bu itemi panele koyamazsýn, bu iþlem karþýda gözükmeyecektir.")
					return
				end
				
				if tonumber(item.get_vnum()) == 70011 or tonumber(item.get_vnum()) == 70042 or tonumber(item.get_vnum()) == 40001 or tonumber(item.get_vnum()) == 40004 or tonumber(item.get_vnum()) == 25041 or tonumber(item.get_vnum()) == 50125 or tonumber(item.get_vnum()) == 71135 then
					syschat("Bu nesne konulamaz.Bu iþlem karþýda gözükmeyecektir.")
					return
				end
				
				if tonumber(item.get_vnum()) >= 72723 and tonumber(item.get_vnum()) <= 72730 then
					syschat("Bu nesne konulamaz.Bu iþlem karþýda gözükmeyecektir.")
					return
				end

				local attr = {{item.get_attribute_type(0),item.get_attribute_value(0)}, {item.get_attribute_type(1),item.get_attribute_value(1)}, {item.get_attribute_type(2),item.get_attribute_value(2)}, {item.get_attribute_type(3),item.get_attribute_value(3)},{item.get_attribute_type(4),item.get_attribute_value(4)},{item.get_attribute_type(5),item.get_attribute_value(5)},{item.get_attribute_type(6),item.get_attribute_value(6)}}
				local socket, itemVnum, itemCount = {item.get_socket(0), item.get_socket(1), item.get_socket(2),item.get_socket(3),item.get_socket(4),item.get_socket(5)}, item.get_vnum(), item.get_count()
				if bug_fixed == 0 then
					local ac_kontrol = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..'_equip.cfg', 'r')
					if ac_kontrol then
						for fx in ac_kontrol:lines() do
							
							local bol = systems.split(fx,"#")
							if tonumber(bol[27]) == tonumber(item.get_id()) then
								fxd = 1
							end
							
						end
						ac_kontrol:close()
						if fxd == 0 then
							local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..'_equip.cfg', 'a+')
							ac:write(itemVnum.."#"..itemCount.."#"..(bol[1]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[2]).."#"..(bol[3]).."#"..item.get_id().."#".."\\n")
							ac:close()
							local adam = find_pc_by_name(bol[2])
							pc.select(tonumber(adam))
							cmdchat("LuaToPython duello_item_ekle_equip|#"..itemVnum.."#"..itemCount.."#"..(bol[1]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[2]).."#"..(bol[3]).."#"..item.get_id().."#")
						
						end
					else
						local ac = io.open('/usr/game/share/locale/turkey/quest/systems/itemineduello/'..pc.get_name()..'ile'..bol[2]..'_equip.cfg', 'a+')
						ac:write(itemVnum.."#"..itemCount.."#"..(bol[1]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[2]).."#"..(bol[3]).."#"..item.get_id().."#".."\\n")
						ac:close()
						local adam = find_pc_by_name(bol[2])
						pc.select(tonumber(adam))
						cmdchat("LuaToPython duello_item_ekle_equip|#"..itemVnum.."#"..itemCount.."#"..(bol[1]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[2]).."#"..(bol[3]).."#"..item.get_id().."#")
						
					end
					bug_fixed = 1
				end
			end 

		end

		function getinput(gelen)
			local input1 = "#quest_input#"
			local input0 = "#quest_inputbitir#"
			cmdchat("LuaToPython "..input1)
			local al = input(cmdchat("PythonIslem "..gelen))
			cmdchat("LuaToPython "..input0)
			return al
		end

		function split(command_, ne)
			return systems.split_(command_,ne)
		end
		
		function split_(string_,delimiter)
			local result = { }
			local from  = 1
			local delim_from, delim_to = string.find( string_, delimiter, from  )
			while delim_from do
				table.insert( result, string.sub( string_, from , delim_from-1 ) )
				from  = delim_to + 1
				delim_from, delim_to = string.find( string_, delimiter, from  )
			end
			table.insert( result, string.sub( string_, from  ) )
			return result
		end
	end
end