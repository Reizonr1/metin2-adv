--[[

TR: Tüm özel sistemler, fonksiyonlar, methodlar, ve yol...
TRL : All Special Systems, funcs, method and the way to...

Geliþtirici : .. Fatihbab34™ ..
Paketler ; LuaToPython, PythonToLua, PythonIslem
Fonksiyonlar ; "split('#blabla#blabla#', '#'), systems.getinput('PythonIslem'), io funcs(open, remove, write, read, readline, readlines), table forms, pc.getqf(), pc.setqf()"

--]]

quest systems begin
	state start begin
	
		-- Bahis Sistemi --
		
		function bahis_sistemi_kontrolleri(ad, vid, kazanan)
			local isim = pc.get_name()
			local ac_rakipadi = io.open(SYSTEM_PATH..'bahis/'..pc.get_name()..'_rakipisim.cfg', 'r')
			if not ac_rakipadi then
				return
			end
			local item_slot = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'ile'..tostring(ad)..'_slot.cfg', "r")
			
			local item_slot_kontrol = 0 -- 1: sorun var.
			
			local ac5x2 = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'_rakipisim.cfg', 'r')
			if not ac5x2 then return end
			
			pc.delqf("bahis_sistemi")

			if pc.getqf("kontrolbahis") <= get_time() then
				if item_slot then -- Ekipman slot
					for itemx in item_slot:lines() do
						item_slot_kontrol = 1
						local bol = systems.split(itemx,"#")
						local items_sec = systems.split(itemx,"#")[3]
						item.select_cell(tonumber(items_sec))

						if tonumber(item.get_cell()) != tonumber(items_sec) then
							systems.bahis_sistemi_problem(vid, isim)
							return
						end

						local attr = {{item.get_attribute_type(0),item.get_attribute_value(0)}, {item.get_attribute_type(1),item.get_attribute_value(1)}, {item.get_attribute_type(2),item.get_attribute_value(2)}, {item.get_attribute_type(3),item.get_attribute_value(3)},{item.get_attribute_type(4),item.get_attribute_value(4)},{item.get_attribute_type(5),item.get_attribute_value(5)},{item.get_attribute_type(6),item.get_attribute_value(6)}}
						local socket, itemVnum, itemCount = {item.get_socket(0), item.get_socket(1), item.get_socket(2),item.get_socket(3),item.get_socket(4),item.get_socket(5)}, item.get_vnum(), item.get_count()

						if tonumber(bol[1]) == tonumber(itemVnum) and tonumber(bol[2]) == tonumber(itemCount) and tonumber(bol[4]) == tonumber(socket[1]) and tonumber(bol[5]) == tonumber(socket[2]) and tonumber(bol[6]) == tonumber(socket[3]) and tonumber(bol[7]) == tonumber(socket[4]) and tonumber(bol[8]) == tonumber(socket[5]) and tonumber(bol[9]) == tonumber(socket[6]) and tonumber(bol[10]) == tonumber(attr[1][1]) and tonumber(bol[11]) == tonumber(attr[1][2]) and tonumber(bol[12]) == tonumber(attr[2][1]) and tonumber(bol[13]) == tonumber(attr[2][2]) and tonumber(bol[14]) == tonumber(attr[3][1]) and tonumber(bol[15]) == tonumber(attr[3][2]) and tonumber(bol[16]) == tonumber(attr[4][1]) and tonumber(bol[17]) == tonumber(attr[4][2]) and tonumber(bol[18]) == tonumber(attr[5][1]) and tonumber(bol[19]) == tonumber(attr[5][2]) and tonumber(bol[20]) == tonumber(attr[6][1]) and tonumber(bol[21]) == tonumber(attr[6][2]) and tonumber(bol[22]) == tonumber(attr[7][1]) and tonumber(bol[23]) == tonumber(attr[7][2]) then
							item_slot_kontrol = 0
						else
							item_slot_kontrol = 1
							
							systems.bahis_sistemi_problem(vid, isim)
							return
						
						end
					end
				end
				systems.zaman()
			else
				item_slot_kontrol = 1
				systems.bahis_sistemi_problem(vid, isim)
				return
			end

			if item_slot_kontrol == 0 then
				pc.select(tonumber(vid))
				pc.delqf("bahis_sistemi")
				local item_slot_r = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'ile'..tostring(isim)..'_slot.cfg', "r")
			
				local item_slot_kontrol_rakip = 0 -- 1: sorun var.
				
				local ac5x2 = io.open(SYSTEM_PATH..'bahis/'..tostring(isim)..'_rakipisim.cfg', 'r')
				if not ac5x2 then return end

				if pc.getqf("kontrolbahis") <= get_time() then
					if item_slot_r then -- Ekipman slot
						for itemt in item_slot_r:lines() do
							item_slot_kontrol_rakip = 1
							local bol = systems.split(itemt,"#")
							local items_sec = systems.split(itemt,"#")[3]
							item.select_cell(tonumber(items_sec))

							if tonumber(item.get_cell()) != tonumber(items_sec) then
								systems.bahis_sistemi_problem(find_pc_by_name(isim), ad)
								return
							end

							local attr = {{item.get_attribute_type(0),item.get_attribute_value(0)}, {item.get_attribute_type(1),item.get_attribute_value(1)}, {item.get_attribute_type(2),item.get_attribute_value(2)}, {item.get_attribute_type(3),item.get_attribute_value(3)},{item.get_attribute_type(4),item.get_attribute_value(4)},{item.get_attribute_type(5),item.get_attribute_value(5)},{item.get_attribute_type(6),item.get_attribute_value(6)}}
							local socket, itemVnum, itemCount = {item.get_socket(0), item.get_socket(1), item.get_socket(2),item.get_socket(3),item.get_socket(4),item.get_socket(5)}, item.get_vnum(), item.get_count()

							if tonumber(bol[1]) == tonumber(itemVnum) and tonumber(bol[2]) == tonumber(itemCount) and tonumber(bol[4]) == tonumber(socket[1]) and tonumber(bol[5]) == tonumber(socket[2]) and tonumber(bol[6]) == tonumber(socket[3]) and tonumber(bol[7]) == tonumber(socket[4]) and tonumber(bol[8]) == tonumber(socket[5]) and tonumber(bol[9]) == tonumber(socket[6]) and tonumber(bol[10]) == tonumber(attr[1][1]) and tonumber(bol[11]) == tonumber(attr[1][2]) and tonumber(bol[12]) == tonumber(attr[2][1]) and tonumber(bol[13]) == tonumber(attr[2][2]) and tonumber(bol[14]) == tonumber(attr[3][1]) and tonumber(bol[15]) == tonumber(attr[3][2]) and tonumber(bol[16]) == tonumber(attr[4][1]) and tonumber(bol[17]) == tonumber(attr[4][2]) and tonumber(bol[18]) == tonumber(attr[5][1]) and tonumber(bol[19]) == tonumber(attr[5][2]) and tonumber(bol[20]) == tonumber(attr[6][1]) and tonumber(bol[21]) == tonumber(attr[6][2]) and tonumber(bol[22]) == tonumber(attr[7][1]) and tonumber(bol[23]) == tonumber(attr[7][2]) then
								--print "hiç birþey yapma..."
								item_slot_kontrol_rakip = 0
							else
								item_slot_kontrol_rakip = 1
								systems.bahis_sistemi_problem(find_pc_by_name(isim), ad)
								return
							end
						end
					end
					systems.zaman()
				else
					item_slot_kontrol_rakip = 1
					systems.bahis_sistemi_problem(find_pc_by_name(isim), ad)
					return
				end

				if item_slot_kontrol_rakip == 0 then
					if kazanan == 1 then
						systems.bahis_sistemi_kaybettin(isim)
						pc.select(tonumber(find_pc_by_name(isim)))
						systems.bahis_sistemi_kazandin(ad)
					else
						systems.bahis_sistemi_kazandin(isim)
						pc.select(tonumber(find_pc_by_name(isim)))
						systems.bahis_sistemi_kaybettin(ad)
					end
				else
					systems.bahis_sistemi_problem(find_pc_by_name(isim), ad)
				end

			else
				systems.bahis_sistemi_problem(vid, isim)
			end
		end
		
		function bahis_sistemi_kazandin(name)
			local item_slot = io.open(SYSTEM_PATH..'bahis/'..tostring(name)..'ile'..tostring(pc.get_name())..'_slot.cfg', "r")
			
			if item_slot then
				for item in item_slot:lines() do
					local items = systems.split(item,"#")
					if items[25] == pc.get_name() then
						--table.insert(item_ve_para, item.."slot#"..bol[1].."#")
						systems.bahis_sistemi_itemiver(item)
					else
						syschat("<System> : Bahis'te bir bug tespit edildi!")
					end
				end
			end

			local bahis_liste = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'_bahislerim.cfg', "r")
			if bahis_liste then 
				bahis_liste:close()
				local bahis_liste_yaz = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'_bahislerim.cfg', "w+")
				bahis_liste_yaz:write(tostring(name).."\\n")
				bahis_liste_yaz:close()
			else
				local bahis_liste_yaz = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'_bahislerim.cfg', "w")
				bahis_liste_yaz:write(tostring(name).."\\n")
				bahis_liste_yaz:close()
			end
			
			if pc.getqf("kontrolbahis") != 0 then pc.delqf("kontrolbahis") end
			
		end
		
		function bahis_sistemi_kaybettin(name)
			local item_slot = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'ile'..tostring(name)..'_slot.cfg', "r")
		
			if item_slot then -- 45'lik slot
				for item in item_slot:lines() do
					local items = systems.split(item,"#")
					systems.bahis_sistemi_itemisil(item)
				end
			end

			local bahis_liste = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'_bahislerim.cfg', "r")
			if bahis_liste then 
				bahis_liste:close()
				local bahis_liste_yaz = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'_bahislerim.cfg', "w+")
				bahis_liste_yaz:write(tostring(name).."\\n")
				bahis_liste_yaz:close()
			else
				local bahis_liste_yaz = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'_bahislerim.cfg', "w")
				bahis_liste_yaz:write(tostring(name).."\\n")
				bahis_liste_yaz:close()
			end
			
			if pc.getqf("kontrolbahis") != 0 then pc.delqf("kontrolbahis") end
		end
		
		function bahis_sistemi_itemiver(itemTab)
			pc.give_item2_select(tonumber(systems.split(itemTab, "#")[1]),tonumber(systems.split(itemTab, "#")[2]))
			local attr,socket = {},{}
			for i = 10,23 do table.insert(attr,{systems.split(itemTab, "#")[i],systems.split(itemTab,"#")[i+1]}) i = i+1 end
			for i = 4,6 do table.insert(socket,systems.split(itemTab, "#")[i]) end
			for i = 1, table.getn(attr) do 
				item.set_value(i-1, attr[i][1], attr[i][2]) 
			end 
			for i = 1, table.getn(socket) do if tonumber(socket[i]) > 0 then item.set_socket(i-1, socket[i]) end end
		end

		function bahis_sistemi_itemisil(itemTab)
			local item_yer = systems.split(itemTab, "#")[3]
			item.select_cell(tonumber(item_yer))
			item.remove()
		end
		
		function bahis_sistemi_problem(vid, name)
			local bahis_liste = io.open(SYSTEM_PATH..'bahis/hackers.cfg', "r")
			if bahis_liste then 
				bahis_liste:close()
				local bahis_liste_yaz = io.open(SYSTEM_PATH..'bahis/hackers.cfg', "w+")
				bahis_liste_yaz:write(tostring(name).."\\n")
				bahis_liste_yaz:close()
			else
				local bahis_liste_yaz = io.open(SYSTEM_PATH..'bahis/hackers.cfg', "w")
				bahis_liste_yaz:write(tostring(name).."\\n")
				bahis_liste_yaz:close()
			end
			syschat("<System> : Bahis'te bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
			pc.select(tonumber(vid))
			syschat("<System> : Bahis'te bir usülsüzlük oluþtu ve bu yüzden duello iptal oldu.")
		end
		
		function bahis_sistemi_itemekle(gelen)
			local yer = systems.split(gelen, "#")[2].."#"..systems.split(gelen, "#")[3].."#"..systems.split(gelen, "#")[4]
			local bol = systems.split(yer, "#")
			local bug_fixed = 0
			local fxd = 0

			local ac_k = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'ile'..tostring(bol[2])..'_kabul.cfg', 'r')
			if ac_k then
				syschat("þuanda panele item koyamazsýn, bu iþlem karþýda gözükmeyecektir.")
				return
			end

			local ac_k2 = io.open(SYSTEM_PATH..'bahis/'..tostring(bol[2])..'ile'..tostring(pc.get_name())..'_kabul.cfg', 'r')
			if ac_k2 then
				syschat("þuanda panele item koyamazsýn, bu iþlem karþýda gözükmeyecektir.")
				return
			end

			item.select_cell(bol[1])

			if tonumber(item.get_id()) == 0 then
				syschat("Bu itemi panele koyamazsýn, bu iþlem karþýda gözükmeyecektir.")
				return
			end
			
			--if not systems.check_antiflag(item.get_vnum()) then
			--	syschat("Bu nesne konulamaz, bu iþlem karþýda gözükmeyecektir.")
			--	return
			--end

			local attr = {{item.get_attribute_type(0),item.get_attribute_value(0)}, {item.get_attribute_type(1),item.get_attribute_value(1)}, {item.get_attribute_type(2),item.get_attribute_value(2)}, {item.get_attribute_type(3),item.get_attribute_value(3)},{item.get_attribute_type(4),item.get_attribute_value(4)},{item.get_attribute_type(5),item.get_attribute_value(5)},{item.get_attribute_type(6),item.get_attribute_value(6)}}
			local socket, itemVnum, itemCount = {item.get_socket(0), item.get_socket(1), item.get_socket(2),item.get_socket(3),item.get_socket(4),item.get_socket(5)}, item.get_vnum(), item.get_count()
			if bug_fixed == 0 then
				local ac_kontrol = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'ile'..tostring(bol[2])..'_slot.cfg', 'r')
				local vidBENIM = pc.get_vid()
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
						local ac = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'ile'..tostring(bol[2])..'_slot.cfg', 'a+')
						ac:write(itemVnum.."#"..itemCount.."#"..(bol[1]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[2]).."#"..(bol[3]).."#"..item.get_id().."#".."\\n")
						ac:close()
						local adam = find_pc_by_name(bol[2])
						pc.select(tonumber(adam))
						if tonumber(vidBENIM) == pc.get_vid() then syschat("<System>: Rakip çevrimdýþý veya uzakta.") cmdchat("LuaToPython bahis_sistemi#kapat#") return end
						cmdchat("LuaToPython bahis_sistemi#itemekle#|#"..itemVnum.."#"..itemCount.."#"..(bol[1]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[2]).."#"..(bol[3]).."#"..item.get_id().."#")
					end
					
				else
					local ac = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'ile'..tostring(bol[2])..'_slot.cfg', 'a+')
					ac:write(itemVnum.."#"..itemCount.."#"..(bol[1]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[2]).."#"..(bol[3]).."#"..item.get_id().."#".."\\n")
					ac:close()
					local adam = find_pc_by_name(bol[2])
					pc.select(tonumber(adam))
					if tonumber(vidBENIM) == pc.get_vid() then syschat("<System>: Rakip çevrimdýþý veya uzakta.") cmdchat("LuaToPython bahis_sistemi#kapat#") return end
					cmdchat("LuaToPython bahis_sistemi#itemekle#|#"..itemVnum.."#"..itemCount.."#"..(bol[1]).."#"..socket[1].."#"..socket[2].."#"..socket[3].."#"..socket[4].."#"..socket[5].."#"..socket[6].."#"..attr[1][1].."#"..attr[1][2].."#"..attr[2][1].."#"..attr[2][2].."#"..attr[3][1].."#"..attr[3][2].."#"..attr[4][1].."#"..attr[4][2].."#"..attr[5][1].."#"..attr[5][2].."#"..attr[6][1].."#"..attr[6][2].."#"..attr[7][1].."#"..attr[7][2].."#"..pc.get_name().."#"..(bol[2]).."#"..(bol[3]).."#"..item.get_id().."#")
					
				end
				bug_fixed = 1
			end
		end
		
		function bahis_sistemi_sil_kapat(isim)
			local ac_kontrol_slot = io.open(SYSTEM_PATH.."bahis/"..tostring(pc.get_name())..'ile'..tostring(isim)..'_slot.cfg', 'r')
			local ac_kontrol_kabul = io.open(SYSTEM_PATH.."bahis/"..tostring(pc.get_name())..'ile'..tostring(isim)..'_kabul.cfg', 'r')
			local ac_kontrol_rakipisim = io.open(SYSTEM_PATH.."bahis/"..tostring(pc.get_name())..'_rakipisim.cfg', 'r')
			if ac_kontrol_slot then os.remove(SYSTEM_PATH.."bahis/"..tostring(pc.get_name())..'ile'..tostring(isim)..'_slot.cfg') end
			if ac_kontrol_kabul then os.remove(SYSTEM_PATH.."bahis/"..tostring(pc.get_name())..'ile'..tostring(isim)..'_kabul.cfg') end
			if ac_kontrol_rakipisim then os.remove(SYSTEM_PATH.."bahis/"..tostring(pc.get_name())..'_rakipisim.cfg') end
		end 
		
		function bahis_sistemi_sil()
			local bahis_liste = io.open(SYSTEM_PATH..'bahis/'..pc.get_name()..'_bahislerim.cfg', "r")
			if bahis_liste then
				for line in bahis_liste:lines() do
					local ac = io.open(SYSTEM_PATH..'bahis/bahis_bilgileri.fatihbab34', 'r')
					if ac then
						for line2 in ac:lines() do
							local bol = systems.split(line2,"#")
							
							if string.find(bol[1], "_rakipisim") then
								
								local sil = io.open(SYSTEM_PATH..'bahis/'..pc.get_name().."_rakipisim.cfg", "r")
								local sil_rakip = io.open(SYSTEM_PATH..'bahis/'..line.."_rakipisim.cfg", "r")
								if sil then
									os.remove(SYSTEM_PATH..'bahis/'..pc.get_name().."_rakipisim.cfg")
								end
								if sil_rakip then
									os.remove(SYSTEM_PATH..'bahis/'..line.."_rakipisim.cfg")
								end
							else
								local sil = io.open(SYSTEM_PATH..'bahis/'..pc.get_name()..'ile'..line..bol[1], 'r')
								local sil_rakip = io.open(SYSTEM_PATH..'bahis/'..line..'ile'..pc.get_name()..bol[1], 'r')
								if sil then
									os.remove(SYSTEM_PATH..'bahis/'..pc.get_name()..'ile'..line..bol[1])
								end
								if sil_rakip then
									os.remove(SYSTEM_PATH..'bahis/'..line..'ile'..pc.get_name()..bol[1])
								end
							end
						end
					else
						syschat("bahis_bilgieri.fatihbab34 % bulunamiyor.")
					end
				end
				os.remove(SYSTEM_PATH..'bahis/'..pc.get_name()..'_bahislerim.cfg')
			end
		end
		
		function bahis_sistemi_open(isim)
			local ac_kontrol_slot = io.open(SYSTEM_PATH.."bahis/"..tostring(pc.get_name())..'ile'..tostring(isim)..'_slot.cfg', 'r')
			local ac_kontrol_kabul = io.open(SYSTEM_PATH.."bahis/"..tostring(pc.get_name())..'ile'..tostring(isim)..'_kabul.cfg', 'r')
			if ac_kontrol_slot then os.remove(SYSTEM_PATH.."bahis/"..tostring(pc.get_name())..'ile'..tostring(isim)..'_slot.cfg') end
			if ac_kontrol_kabul then os.remove(SYSTEM_PATH.."bahis/"..tostring(pc.get_name())..'ile'..tostring(isim)..'_kabul.cfg') end
			
			local ac_yaz_rakipisim = io.open(SYSTEM_PATH.."bahis/"..tostring(pc.get_name())..'_rakipisim.cfg', 'w')
			ac_yaz_rakipisim:write(tostring(isim).."#")
			ac_yaz_rakipisim:close()
		end
		
		function bahis_sistemi(isim)
			local nameBENIM = pc.get_name()
			local vidBENIM = pc.get_vid()
			local vidBUL = find_pc_by_name(isim)
			--
			pc.select(tonumber(vidBUL))
			if tostring(nameBENIM) == tostring(pc.get_name()) then syschat("<System>: Rakip çevrimdýþý veya uzakta. ") return end
			cmdchat("LuaToPython bahis_sistemi#oyna#"..tostring(nameBENIM))
			systems.bahis_sistemi_open(nameBENIM)
			pc.setqf("bahis_sistemi", 1)
			--
			pc.select(tonumber(vidBENIM))
			cmdchat("LuaToPython bahis_sistemi#oyna#"..tostring(isim))
			systems.bahis_sistemi_open(isim)
			pc.setqf("bahis_sistemi", 1)
			
		end
		
		function zaman()
			pc.setqf("kontrolbahis", get_time()+30)
		end
		
		-- Bahis Sistemi --
		
		when logout begin
			-- Bahis Sistemi --
			if pc.getqf("bahis_sistemi") != 0 then pc.delqf("bahis_sistemi") end
			--if pc.getqf("iteminevskontrol") != 0 then pc.delqf("iteminevskontrol") end
			systems.bahis_sistemi_sil()
			
			local ac_rakipadi = io.open(SYSTEM_PATH..'bahis/'..pc.get_name()..'_rakipisim.cfg', 'r')
			local pc_get_vid = find_pc_by_name(ac_rakipadi:read())
			pc.select(tonumber(pc_get_vid))
			if pc.getqf("bahis_sistemi") != 0 then pc.delqf("bahis_sistemi") end
			
			systems.bahis_sistemi_sil()
			cmdchat("LuaToPython bahis_sistemi#kapat#")
			-- Bahis Sistemi -- 
		end
		
		when login begin
			cmdchat("PythonToLua "..q.getcurrentquestindex())
			
			-- Bahis Sistemi --
			if pc.getqf("bahis_sistemi") != 0 then pc.delqf("bahis_sistemi") end
			--if pc.getqf("iteminevskontrol") != 0 then pc.delqf("iteminevskontrol") end
			systems.bahis_sistemi_sil()
			cmdchat("LuaToPython bahis_sistemi#kapat#")
			-- Bahis Sistemi -- 
			
		end

		when button begin
			local gelen = systems.getinput("PYTHONISLEM")

			if string.find(gelen, "bahis_kabul#") then
				local ac_kontrol_rakipisim = io.open(SYSTEM_PATH.."bahis/"..tostring(pc.get_name())..'_rakipisim.cfg', 'r')
				if ac_kontrol_rakipisim then
					local isim = systems.split(ac_kontrol_rakipisim:read(), "#")
					local bahis_oyna = 0 local bahis_random_me = -1 local bahis_random_target = -1 local bahis_kazanan = 0
					local ac_kontrol_kabul = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'ile'..tostring(isim[1])..'_kabul.cfg', 'r')
					local ac_kontrol_kabul_rakip = io.open(SYSTEM_PATH..'bahis/'..tostring(isim[1])..'ile'..tostring(pc.get_name())..'_kabul.cfg', 'r')
					if ac_kontrol_kabul then
						syschat("<System>: Zaten kabul ettin.")
						ac_kontrol_kabul:close()
						return
					end
					if ac_kontrol_kabul_rakip then bahis_oyna = 1 end
					local ac_yaz_kabul = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'ile'..tostring(isim[1])..'_kabul.cfg', 'w')
					ac_yaz_kabul:write("@byfatihbab34;")
					ac_yaz_kabul:close()
					ac_kontrol_rakipisim:close()
					local nameBENIM = pc.get_name()
					local vidBENIM = pc.get_vid()
					local vidBUL = find_pc_by_name(isim[1])
					if bahis_oyna == 1 then
						for i=1, 20 do
							bahis_random_me = number(BAHIS_RANDOM[1],BAHIS_RANDOM[2])
							bahis_random_target = number(BAHIS_RANDOM[1],BAHIS_RANDOM[2])
							if bahis_random_me > bahis_random_target then bahis_kazanan = 1 end
							if bahis_random_me != bahis_random_target then break end 
						end
						systems.bahis_sistemi_kontrolleri(isim[1], vidBUL, bahis_kazanan)
					end
					cmdchat("LuaToPython bahis_sistemi#kabul#"..tostring(nameBENIM).."#"..tostring(bahis_random_me).."#"..tostring(bahis_random_target))
					pc.select(tonumber(vidBUL))
					if tonumber(vidBENIM) == pc.get_vid() then syschat("<System>: Rakip çevrimdýþý veya uzakta.") cmdchat("LuaToPython bahis_sistemi#kapat#") pc.delqf("bahis_sistemi") return end
					
					cmdchat("LuaToPython bahis_sistemi#kabul#"..tostring(nameBENIM).."#"..tostring(bahis_random_me).."#"..tostring(bahis_random_target))
					pc.select(tonumber(vidBUL))
					if tonumber(vidBENIM) == pc.get_vid() then syschat("<System>: Rakip çevrimdýþý veya uzakta.") cmdchat("LuaToPython bahis_sistemi#kapat#") pc.delqf("bahis_sistemi") return end
					cmdchat("LuaToPython bahis_sistemi#kabul#"..tostring(nameBENIM).."#"..tostring(bahis_random_target).."#"..tostring(bahis_random_me))
				end
			end
			
			if string.find(gelen, "bahis_kapat#") then
				if pc.getqf("bahis_sistemi") != 4 then
					local ac_kontrol_rakipisim = io.open(SYSTEM_PATH.."bahis/"..tostring(pc.get_name())..'_rakipisim.cfg', 'r')
					if not ac_kontrol_rakipisim then return end
					if ac_kontrol_rakipisim then
						local isim = systems.split(ac_kontrol_rakipisim:read(), "#")
						local nameBENIM = pc.get_name()
						local ac_kontrol_kabul = io.open(SYSTEM_PATH..'bahis/'..tostring(pc.get_name())..'ile'..tostring(isim[1])..'_kabul.cfg', 'r')
						local ac_kontrol_kabul2 = io.open(SYSTEM_PATH..'bahis/'..tostring(isim[1])..'ile'..tostring(pc.get_name())..'_kabul.cfg', 'r')
						if ac_kontrol_kabul or ac_kontrol_kabul2 then
							syschat("<System>: Þuanda pencereyi kapatamazsýn.")
							return
						end
						ac_kontrol_rakipisim:close()
						cmdchat("LuaToPython bahis_sistemi#kapat#")
						pc.delqf("bahis_sistemi")
						systems.bahis_sistemi_sil_kapat(isim[1])
						local vidBUL = find_pc_by_name(isim[1])
						pc.select(tonumber(vidBUL))
						systems.bahis_sistemi_sil_kapat(nameBENIM)
						cmdchat("LuaToPython bahis_sistemi#kapat#")
						pc.delqf("bahis_sistemi")
					end
				end
			end
			
			if string.find(gelen, "bahis_itemekle_slot#") then
				--if BAHIS_SISTEMI == 1 then return end
				systems.bahis_sistemi_itemekle(gelen)
			end
			
			if string.find(gelen, "bahis_teklif#") then
				local bol = systems.split(gelen, "#")
				local nameBENIM = pc.get_name()
				local vidBUL = find_pc_by_name(bol[3])
				pc.select(tonumber(vidBUL))
				if pc.getqf("bahis_sistemi") == 3 then
					if tonumber(bol[2]) == 0 then syschat("<System>: Rakip bahis teklifi reddetti.") pc.delqf("bahis_sistemi") return else end
					if tonumber(bol[2]) == 1 then
						systems.bahis_sistemi(nameBENIM)
					end
				end
			end
			
			if string.find(gelen, "bahis_oyna#") then
				if BAHIS_SISTEMI == 1 then return end
				local bol = systems.split(gelen, "#")
				if pc.getqf("bahis_sistemi") == 1 then
					syschat("<System>: Þuanda biriyle zaten oynuyorsun.")
					return
				end
				local vidBENIM = pc.get_vid()
				local nameBENIM = pc.get_name()
				local vidBUL = find_pc_by_name(bol[2])
				local oyunKONTROL = 0
				pc.select(tonumber(vidBUL))
				if pc.get_vid()==vidBENIM then syschat("<System>: Rakip çevrimdýþý veya uzakta.") return end
				if pc.getqf("bahis_sistemi") == 1 then oyunKONTROL=1 pc.select(tonumber(vidBENIM)) end
				if oyunKONTROL == 1 then 
					syschat("<System>: Rakip þuanda zaten biriyle oynamakta.")
					return
				end
				
				cmdchat("LuaToPython bahis_sistemi#teklif#"..tostring(nameBENIM))
				pc.select(tonumber(vidBENIM))
				pc.setqf("bahis_sistemi", 3)
				
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