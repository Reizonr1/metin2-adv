import localegame
import gameInfo
import event
import time
import uiitemineduello

	def Open(self):
		gameInfo.DUELLO_DURUM = 0
		gameInfo.DUELLO_KAPAT = 1
		gameInfo.DUELLO_YOLLANANLAR = []
		gameInfo.DUELLO_YOLLAYANLAR = []
		
	def __PressQuickSlot(self, localSlotIndex):
		if gameInfo.DUELLO_DURUM == 4:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Düello paneli açıkken item kullanamazsın.")
			return

	def __ServerCommand_Build(self):
		serverCommandList={
	
			"PythonToLua"			: self.__PythonToLua, # .python to Quest
			"PythonIslem"			: self.__PythonIslem, # .python to Quest
			"LuaToPython"			: self.__LuaToPython, # Quest to .python
	
		}

		
	def __PythonToLua(self, id):
		gameInfo.PYTHONTOLUA = int(id)

	def __PythonIslem(self, PythonIslem):
		if PythonIslem == "PYTHONISLEM":
			net.SendQuestInputStringPacket(gameInfo.PYTHONISLEM)
		elif PythonIslem == "DUELLO_TOPLAM_ITEM_SLOT":
			net.SendQuestInputStringPacket(str(len(uiitemineduello.ItemSlot)))
		elif PythonIslem == "DUELLO_ITEM_SLOT_YERI":
			net.SendQuestInputStringPacket(str(uiitemineduello.Item_Slot_Eklenen))
		elif PythonIslem == "DUELLO_ITEM_EQUIP_YERI":
			net.SendQuestInputStringPacket(str(uiitemineduello.Item_Equip_Eklenen))
		elif PythonIslem == "DUELLO_KONTROL":
			net.SendQuestInputStringPacket(str(gameInfo.DUELLO_DURUM)+"#"+str(gameInfo.DUELLO_RAKIP)+"#"+str(gameInfo.DUELLO_VID)+"#"+str(player.GetName())+"#")

	def __LuaToPython(self, LuaToPython):
		if LuaToPython.find("#quest_input#") != -1:
			gameInfo.INPUT = 1
		elif LuaToPython.find("#quest_inputbitir#") != -1:
			gameInfo.INPUT = 0
		elif LuaToPython.find("duello_item_ekle_slot") != -1:
			bol_2 = LuaToPython.split("|")
			bol = LuaToPython.split("#")
			#uiExchange_Multi.ITEMSLOT_INFO = "#"+str(bol[2])+"#"+str(bol[3])+"#"+str(bol[4])+"#"+str(bol[5])+"#"+bol[6]+"#"+bol[7]+"#"
			uiitemineduello.ItemSlot_R_Ekle = bol_2[1]
			uiitemineduello.ItemEkle_DURUM = 1

		elif LuaToPython.find("duello_item_ekle_equip") != -1:
			bol_2 = LuaToPython.split("|")
			bol = LuaToPython.split("#")
			#uiExchange_Multi.ITEMSLOT_INFO = "#"+str(bol[2])+"#"+str(bol[3])+"#"+str(bol[4])+"#"+str(bol[5])+"#"+bol[6]+"#"+bol[7]+"#"
			uiitemineduello.ItemSlot_R_Ekle_Ekipman = bol_2[1]
			uiitemineduello.ItemEkle_DURUM_Ekipman = 1

		elif LuaToPython.find("duello_para_ekle") != -1:
			bol = LuaToPython.split("#")
			gameInfo.DUELLO_RAKIP_PARA = int(bol[1])
			
		elif LuaToPython.find("duello_skor") != -1:
			bol = LuaToPython.split("-")
			gameInfo.DUELLO_ROUND_YENILE=1
			gameInfo.DUELLO_ROUND_HAZIR_MY=0
			gameInfo.DUELLO_ROUND_HAZIR_TARGET=0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<Düello> Diğer round için hazırlıklarını yap ve hazır butonuna tıkla!")
			
			gameInfo.DUELLO_ROUND_DURUM = 0
			gameInfo.DUELLO_ROUND_ZAMAN_IN = app.GetTime() + 1
			gameInfo.DUELLO_SKOR_MY = bol[0].split("#")[1]
			gameInfo.DUELLO_SKOR_TARGET = bol[1]
			
		elif LuaToPython.find("DUELLO_BITTI") != -1:
			gameInfo.DUELLO_BILGILERI["depo_"+str(gameInfo.DUELLO_RAKIP)+"_slot"] = []
			gameInfo.DUELLO_BILGILERI["depo_"+str(gameInfo.DUELLO_RAKIP)+"_equip"] = []
			gameInfo.DUELLO_BILGILERI["depo_"+str(gameInfo.DUELLO_RAKIP)+"_para"] = []
			gameInfo.DUELLO_KAPAT = 1
			
		elif LuaToPython.find("duello_bilgileri") != -1:
			bol = LuaToPython.split("|")
			bol_rakip = bol[2].split("#")
			bol_benim = bol[3].split("#")
			gameInfo.DUELLO_BILGILERI[str(bol[1])+"_info2"] = "#"+str(bol_rakip[1])+"#"+str(bol_rakip[2])+"#"+str(bol_rakip[3])+"#"+str(bol_rakip[4])+"#"
			gameInfo.DUELLO_BILGILERI[str(player.GetName())+"_info2"] = "#"+str(bol_benim[1])+"#"+str(bol_benim[2])+"#"+str(bol_benim[3])+"#"+str(bol_benim[4])+"#"
			
		elif LuaToPython.find("duello_depo_ac") != -1:
			bol = LuaToPython.split("|")
		
			if str(bol[1]) == "1":
				rakip = ""
				if str(bol[2].split("#")[2]) == "para":
					rakip = str(bol[2].split("#")[3])
				else:
					rakip = str(bol[2].split("#")[24])
				questionDialog = uiCommon.QuestionDialog2()
				questionDialog.SetText1(localegame.DUELLO_DEPO_KAYITLARI_VAR)
				questionDialog.SetText2(localegame.DUELLO_DEPO_KAYITLARI_VAR2)
				questionDialog.SetWidth(460)
				questionDialog.EscapeKeyStat(1)
				questionDialog.SetAcceptEvent(lambda rakip_isim=rakip, durum="1":self.duelloDEPOAL(rakip_isim, durum))
				questionDialog.SetCancelEvent(lambda rakip_isim=rakip, durum="0":self.duelloDEPOAL(rakip_isim, durum))
				questionDialog.SetAcceptText("Evet")
				questionDialog.SetCancelText("Hayır")
				questionDialog.Open()
				self.questionDialog = questionDialog
			elif str(bol[1]) == "2":
				self.__PressJKey(str(LuaToPython.split("#")[1]))
				return
			elif str(bol[1]) == "3":
				gameInfo.DUELLO_BILGILERI["ISIM"] = str(LuaToPython.split("#")[1])
				return
			elif str(bol[1]) == "4":
				gameInfo.DUELLO_BILGILERI[str(player.GetName())+"_info100"] = "#"+str(bol[2].split("#")[1])+"#"+str(bol[2].split("#")[2])+"#"+str(bol[2].split("#")[3])+"#"+str(bol[2].split("#")[4])
				return
			elif str(bol[1]) == "5":
				gameInfo.DUELLO_BILGILERI["ISIM"] = ""
				return
			
			if str(bol[2].split("#")[2]) == "para":
				gameInfo.DUELLO_BILGILERI["depo_"+str(bol[2].split("#")[3])+"_para"] = str(bol[2].split("#")[1])
				gameInfo.DUELLO_BILGILERI["depo_"+str(bol[2].split("#")[24])+"_round"] = str(bol[2].split("#")[4])
				gameInfo.DUELLO_BILGILERI[str(player.GetName())+"_info100"] = "#"+str(bol[2].split("#")[5])+"#"+str(bol[2].split("#")[6])+"#"+str(bol[2].split("#")[7])+"#"+str(bol[2].split("#")[8])+"#"+str(bol[2].split("#")[4])+"#"
				return
			
			if not "depo_"+str(bol[2].split("#")[24])+"_"+str(bol[2].split("#")[28]) in gameInfo.DUELLO_BILGILERI.keys():
				gameInfo.DUELLO_BILGILERI["depo_"+str(bol[2].split("#")[24])+"_"+str(bol[2].split("#")[28])] = []
			
			gameInfo.DUELLO_BILGILERI["depo_"+str(bol[2].split("#")[24])+"_"+str(bol[2].split("#")[28])].append(str(bol[2]))
			gameInfo.DUELLO_BILGILERI["depo_"+str(bol[2].split("#")[24])+"_round"] = str(bol[2].split("#")[29])
			gameInfo.DUELLO_BILGILERI[str(player.GetName())+"_info100"] = "#"+str(bol[2].split("#")[30])+"#"+str(bol[2].split("#")[31])+"#"+str(bol[2].split("#")[32])+"#"+str(bol[2].split("#")[33])
				
			
	def duelloDEPOAL(self, rakipisim, durum):
		gameInfo.PYTHONISLEM = "duello_sonws_depo_itemlerial#"+str(durum)+"#"
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		
		self.ac = uiitemineduello.itemineduello_depo()
		self.ac.Show(rakipisim)
		
		self.questionDialog.Close()

	""" Değiştir """
	def	__PressJKey(self, gelen=""):
		if gelen != "":
			if "PANEL" in gameInfo.DUELLO_BILGILERI.keys() and gameInfo.DUELLO_BILGILERI["PANEL"] == "1":
				gameInfo.DUELLO_BILGILERI["PANEL"] = "2"
				return
				
			self.ac = uiitemineduello.itemineduello_depo()
			self.ac.Show(gelen)
			
			return
			
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			if player.IsMountingHorse():
				net.SendChatPacket("/unmount")
			else:
				if not uiPrivateShopBuilder.IsBuildingPrivateShop():
					for i in xrange(player.INVENTORY_PAGE_SIZE):
						if player.GetItemIndex(i) in (71114, 71116, 71118, 71120):
							net.SendItemUsePacket(i)
							break
		else:
			if "PANEL" in gameInfo.DUELLO_BILGILERI.keys() and gameInfo.DUELLO_BILGILERI["PANEL"] == "1":
				gameInfo.DUELLO_BILGILERI["PANEL"] = "2"
				return
				
			if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
				chat.AppendChat(chat.CHAT_TYPE_INFO, str(localegame.DUELLO_DEPO_ACAMAZSIN))
				return
				
			self.ac = uiitemineduello.itemineduello_depo()
			self.ac.Show()
		
	""" İçine Ekle """
	def OpenQuestWindow(self, skin, idx):
		if gameInfo.INPUT == 1:
			return
			
	def OnUpdate(self):
		if "ESC" in gameInfo.DUELLO_BILGILERI.keys() and gameInfo.DUELLO_BILGILERI["ESC"] == "1":
			self.interface.ToggleSystemDialog()
			gameInfo.DUELLO_BILGILERI["ESC"] = "0"
			
		if gameInfo.DUELLO_DURUM==1 or gameInfo.DUELLO_DURUM==4:
			if player.GetPKMode() == player.PK_MODE_FREE or player.GetPKMode() == player.PK_MODE_GUILD: #or player.GetPKMode() == player.PK_MODE_REVENGE:
				net.SendChatPacket("/pkmode 0", chat.CHAT_TYPE_TALKING)


	## Message CMD ##

	def OnRecvWhisper(self, mode, name, line):
		if line.find("#xsbyfatihbab34ndsawgqwqdhsabdsabdsabwbqdsnandsadnasndas#") != -1:
			gameInfo.DUELLO_KABUL_RAKIP = 1
			return

		if line.find("#xsbyfatihbab34dasddjsadjsajmwmwqroundhazirndsandsad#") != -1:
			gameInfo.DUELLO_ROUND_HAZIR_TARGET=1
			return
			
		if line.find("#xsbyfatihbab34dsaxxsadsajdsajroundxsd122121dcxsa#") != -1:
			bol=line.split("#")
			if int(bol[2]) == gameInfo.DUELLO_ROUND:
				return
			if gameInfo.DUELLO_DURUM != 4:
				return
			gameInfo.DUELLO_ROUND=int(bol[2])
			gameInfo.DUELLO_LOG.insert(0, "#"+str(name)+"#"+str(bol[2])+"#0#0#"+str(time.strftime("[%d.%m.%y, %H:%M:%S]"))+"#round")
			uiitemineduello.DUELLO_ROUND_EKLENDI = 1
			
			gameInfo.PYTHONISLEM="duello_round#"+str(bol[2])+"#"+str(gameInfo.DUELLO_RAKIP)+"#1"
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)
			return
				
		if line.find("#xsbyfatihbab34dndndddsround_iptalhdan#") != -1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<Düello> Rakip 15 saniye içinde kalkmadığı için duello iptal olmuştur.")
			self.__LuaToPython("DUELLO_BITTI")
			return
				
		if line.find("#xsbyfatihbab34dsadsanxsadadsadaafsafafsxasxawqwqdsaafafasfafsafafsafsa#") != -1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_IPTAL % (name))
			gameInfo.DUELLO_DURUM = 0
			gameInfo.DUELLO_VID = 0
			gameInfo.DUELLO_BASLATAN = 0
			gameInfo.DUELLO_RAKIP_PARA = 0
			gameInfo.DUELLO_BENIM_PARA = 0
			gameInfo.DUELLO_KABUL_RAKIP = 0
			gameInfo.DUELLO_KABUL = 0
			gameInfo.DUELLO_RAKIP = ""
			gameInfo.DUELLO_KAPAT = 1
			gameInfo.DUELLO_ROUND = 1
			gameInfo.DUELLO_ROUND_BASLAT = 0
			gameInfo.DUELLO_ROUND_ZAMAN_IN = 0
			gameInfo.DUELLO_ROUND_ZAMAN_KALAN = 0
			gameInfo.DUELLO_ROUND_DURUM = 0
			gameInfo.DUELLO_SKOR_MY = 0
			gameInfo.DUELLO_SKOR_TARGET = 0
			if "#"+str(name)+"#" in gameInfo.DUELLO_YOLLAYANLAR:
				gameInfo.DUELLO_YOLLAYANLAR.remove("#"+str(name)+"#")
			
			if "#"+str(name)+"#" in gameInfo.DUELLO_YOLLANANLAR:
				gameInfo.DUELLO_YOLLANANLAR.remove("#"+str(name)+"#")
			return

		if line.find("##xsbyfatihbab34dsaxsasamnwwdsaxsadjjahdsajwqwq##") != -1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_YAPAMAZ % (name))
			gameInfo.DUELLO_YOLLANANLAR.remove("#"+str(name)+"#")
			gameInfo.DUELLO_VID = 0
			return

		if line.find("##xsbyfatihbab34dsadjsamxansxasndamwwdsadsadjashdasdasdas##") != -1:
			if os.path.exists(str(gameInfo.CLIENT_YOL) + "iteminevs_"+str(player.GetName())+".kf"):
				net.SendWhisperPacket(name, "##xsbyfatihbab34dsaxsasamnwwdsaxsadjjahdsajwqwq##")
				gameInfo.DUELLO_DURUM = 0
				return
				
			if "#"+str(name)+"#" in gameInfo.DUELLO_YOLLAYANLAR:
				if gameInfo.DUELLO_DURUM == 0 or gameInfo.DUELLO_DURUM == 2 or gameInfo.DUELLO_DURUM == 3 or gameInfo.DUELLO_DURUM == 5:
					gameInfo.DUELLO_RAKIP = name
					gameInfo.DUELLO_DURUM = 4
					gameInfo.DUELLO_BASLATAN = 2
					gameInfo.DUELLO_KAPAT = 0
					self.ac = uiitemineduello.itemineduello()
					self.ac.Show()
					gameInfo.PYTHONISLEM = "duello_baslat#"+str(name)
					event.QuestButtonClick(gameInfo.PYTHONTOLUA)
				else:
					net.SendWhisperPacket(name,"##byfatihbab34asdaxsa31321312sacaxasxas##")
			return

		if line.find("##xsbyfatihbab34-dsadjsamxansxasndamwwdsadsadjashdasdasdas##") != -1:
			if os.path.exists(str(gameInfo.CLIENT_YOL) + "iteminevs_"+str(player.GetName())+".kf"):
				net.SendWhisperPacket(name, "##xsbyfatihbab34dsaxsasamnwwdsaxsadjjahdsajwqwq##")
				chat.AppendChat(chat.CHAT_TYPE_INFO, "<Itemine VS:> : İtemine vs engelliyken, itemine vs yapamazsın.")
				return
				
			if "#"+str(name)+"#" in gameInfo.DUELLO_YOLLAYANLAR:
				if gameInfo.DUELLO_DURUM == 0 or gameInfo.DUELLO_DURUM == 2 or gameInfo.DUELLO_DURUM == 3 or gameInfo.DUELLO_DURUM == 5:
					gameInfo.DUELLO_RAKIP = name
					gameInfo.DUELLO_DURUM = 4
					gameInfo.DUELLO_BASLATAN = 1
					gameInfo.DUELLO_KAPAT = 0
					self.ac = uiitemineduello.itemineduello()
					self.ac.Show()
					gameInfo.PYTHONISLEM = "duello_baslat#"+str(name)
					event.QuestButtonClick(gameInfo.PYTHONTOLUA)
				else:
					net.SendWhisperPacket(name,"##byfatihbab34asdaxsa31321312sacaxasxas##")
			return

		if line.find("#xsbyfatihbab34sdajdsadnsadmnasdmnaswmqwmnmdsnaddasawq#") != -1:
			if os.path.exists(str(gameInfo.CLIENT_YOL) + "iteminevs_"+str(player.GetName())+".kf"):
				net.SendWhisperPacket(name, "##xsbyfatihbab34dsaxsasamnwwdsaxsadjjahdsajwqwq##")
				chat.AppendChat(chat.CHAT_TYPE_INFO, "<Itemine VS:> : İtemine vs engelliyken, itemine vs yapamazsın.")
				return
				
			if "#"+str(name)+"#" in gameInfo.DUELLO_YOLLANANLAR:
				if gameInfo.DUELLO_DURUM == 0 or gameInfo.DUELLO_DURUM == 2 or gameInfo.DUELLO_DURUM == 3 or gameInfo.DUELLO_DURUM == 5:
				
					bol = str(line).split("#")
					gameInfo.DUELLO_BILGILERI[str(name)+"_info1"] = "#"+str(bol[2])+"#"+str(bol[3])+"#"+str(bol[4])+"#"
				
					gameInfo.DUELLO_RAKIP = name
					gameInfo.DUELLO_DURUM = 4
					gameInfo.DUELLO_BASLATAN = 1
					gameInfo.DUELLO_KAPAT = 0
					self.ac = uiitemineduello.itemineduello()
					self.ac.Show()
					net.SendWhisperPacket(name, "##xsbyfatihbab34dsadjsamxansxasndamwwdsadsadjashdasdasdas##")
					gameInfo.PYTHONISLEM = "duello_baslat#"+str(name)
					event.QuestButtonClick(gameInfo.PYTHONTOLUA)
				else:
					net.SendWhisperPacket(name,"##byfatihbab34asdaxsa31321312sacaxasxas##")
			else:
				net.SendWhisperPacket(name, "##xsbyfatihbab34dsaxsasamnwwdsaxsadjjahdsajwqwq##")
			return

		if line.find("#xsbyfatihbab34-sdajdsadnsadmnasdmnaswmqwmnmdsnaddasawq#") != -1:
			if os.path.exists(str(gameInfo.CLIENT_YOL) + "iteminevs_"+str(player.GetName())+".kf"):
				net.SendWhisperPacket(name, "##xsbyfatihbab34dsaxsasamnwwdsaxsadjjahdsajwqwq##")
				chat.AppendChat(chat.CHAT_TYPE_INFO, "<Itemine VS:> : İtemine vs engelliyken, itemine vs yapamazsın.")
				return
				
			if "#"+str(name)+"#" in gameInfo.DUELLO_YOLLANANLAR:
				if gameInfo.DUELLO_DURUM == 0 or gameInfo.DUELLO_DURUM == 2 or gameInfo.DUELLO_DURUM == 3 or gameInfo.DUELLO_DURUM == 5:
				
					bol = str(line).split("#")
					gameInfo.DUELLO_BILGILERI[str(name)+"_info1"] = "#"+str(bol[2])+"#"+str(bol[3])+"#"+str(bol[4])+"#"
					
					gameInfo.DUELLO_RAKIP = name
					gameInfo.DUELLO_DURUM = 4
					gameInfo.DUELLO_BASLATAN = 2
					gameInfo.DUELLO_KAPAT = 0
					self.ac = uiitemineduello.itemineduello()
					self.ac.Show()
					net.SendWhisperPacket(name, "##xsbyfatihbab34-dsadjsamxansxasndamwwdsadsadjashdasdasdas##")
					gameInfo.PYTHONISLEM = "duello_baslat#"+str(name)
					event.QuestButtonClick(gameInfo.PYTHONTOLUA)
				else:
					net.SendWhisperPacket(name,"##byfatihbab34asdaxsa31321312sacaxasxas##")
			else:
				net.SendWhisperPacket(name, "##xsbyfatihbab34dsaxsasamnwwdsaxsadjjahdsajwqwq##")
			return

		if line.find("##xsbyfatihbab34axsadsahdgsadsadassadjadada##") != -1:
			if os.path.exists(str(gameInfo.CLIENT_YOL) + "iteminevs_"+str(player.GetName())+".kf"):
				net.SendWhisperPacket(name, "##xsbyfatihbab34dsaxsasamnwwdsaxsadjjahdsajwqwq##")
				return
				
			if gameInfo.DUELLO_DURUM == 0 or gameInfo.DUELLO_DURUM == 2 or gameInfo.DUELLO_DURUM == 3 or gameInfo.DUELLO_DURUM == 5:
				chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, "Sana itemine vs teklifi yolluyor.")
				self.interface.RecvWhisper(name)
				chat.AppendChat(chat.CHAT_TYPE_INFO, str(name) + " adli oyuncu sana itemine vs teklifi yolluyor.")
				if not "#"+str(name)+"#" in gameInfo.DUELLO_YOLLAYANLAR:
					gameInfo.DUELLO_YOLLAYANLAR.append("#"+str(name)+"#")
				gameInfo.DUELLO_DURUM = 3
				bol = str(line).split("#")
				gameInfo.DUELLO_BILGILERI[str(name)+"_info1"] = "#"+str(bol[4])+"#"+str(bol[5])+"#"+str(bol[6])+"#"
			else:
				net.SendWhisperPacket(name,"##byfatihbab34asdaxsa31321312sacaxasxas##")
			return
			
		if line.find("##byfatihbab34asdaxsa31321312sacaxasxas##") != -1:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Bu oyuncu şuanda itemine düello yapamaz.")
			if "#"+str(name)+"#" in gameInfo.DUELLO_YOLLANANLAR:
				gameInfo.DUELLO_YOLLANANLAR.remove("#"+str(name)+"#")
				gameInfo.DUELLO_VID = 0
			return

		if line.find("##xsbyfatihbab34-axsadsahdgsadsadassadjadada##") != -1:
			if os.path.exists(str(gameInfo.CLIENT_YOL) + "iteminevs_"+str(player.GetName())+".kf"):
				net.SendWhisperPacket(name, "##xsbyfatihbab34dsaxsasamnwwdsaxsadjjahdsajwqwq##")
				chat.AppendChat(chat.CHAT_TYPE_INFO, "<Itemine VS:> : İtemine vs engelliyken, itemine vs yapamazsın.")
				return
				
			if gameInfo.DUELLO_DURUM == 0 or gameInfo.DUELLO_DURUM == 2 or gameInfo.DUELLO_DURUM == 3 or gameInfo.DUELLO_DURUM == 5:
			
				bol = str(line).split("#")
				gameInfo.DUELLO_BILGILERI[str(name)+"_info1"] = "#"+str(bol[4])+"#"+str(bol[5])+"#"+str(bol[6])+"#"
				
				chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, "Sana itemine vs teklifi yolluyor.")
				self.interface.RecvWhisper(name)
				chat.AppendChat(chat.CHAT_TYPE_INFO, str(name) + " adli oyuncu sana itemine vs teklifi yolluyor.")
				if not "#"+str(name)+"#" in gameInfo.DUELLO_YOLLAYANLAR:
					gameInfo.DUELLO_YOLLAYANLAR.append("#"+str(name)+"#")
				gameInfo.DUELLO_DURUM = 5
			else:
				net.SendWhisperPacket(name,"##byfatihbab34asdaxsa31321312sacaxasxas##")
			return

	def RequestDropItem(self, answer):
		#if attachedItemSlotPos in uiitemineduello.ItemSlot or attachedItemIndex in uiitemineduello.ItemSlot:
		#	chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_ITEMI_HAREKET_ETTIREMESSIN)
		#	return

		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_ITEMI_HAREKET_ETTIREMESSIN)
			self.itemDropQuestionDialog.Close()
			self.itemDropQuestionDialog = None
			return