import gameInfo
import event
import net
import uidice
import localegame

	def __ServerCommand_Build(self):
		serverCommandList={
			## New System Plugin ##
			"PythonToLua"			: self.__PythonToLua, # .python to Quest
			"PythonIslem"			: self.__PythonIslem, # .python to Quest
			"LuaToPython"			: self.__LuaToPython, # Quest to .python
			## END - New System Plugin - END ##
		}

	#degistir#
	def OpenQuestWindow(self, skin, idx):
		if gameInfo.INPUT == 1:
			return
		self.interface.OpenQuestWindow(skin, idx)


	def __PythonToLua(self, id):
		gameInfo.PYTHONTOLUA = int(id)

	def __PythonIslem(self, PythonIslem):
		if PythonIslem == "PYTHONISLEM":
			net.SendQuestInputStringPacket(gameInfo.PYTHONISLEM)

	def __LuaToPython(self, LuaToPython):
		if LuaToPython.find("#quest_input#") != -1:
			gameInfo.INPUT = 1
		elif LuaToPython.find("#quest_inputbitir#") != -1:
			gameInfo.INPUT = 0
		## Bahis Sistemi ##
		elif LuaToPython.find("bahis_sistemi#") != -1:
			bol = LuaToPython.split("#")
			if LuaToPython.find("#teklif#") != -1:
				bahisRequestQuestionDialog = uiCommon.QuestionDialog()
				bahisRequestQuestionDialog.SetText(str(localegame.DICE_SYSTEM_TEKLIF) % (bol[2]))
				bahisRequestQuestionDialog.SetAcceptText(localeInfo.UI_ACCEPT)
				bahisRequestQuestionDialog.SetCancelText(localeInfo.UI_DENY)
				bahisRequestQuestionDialog.SetAcceptEvent(lambda arg=1: self.__AnswerBahisTeklifi(arg))
				bahisRequestQuestionDialog.SetCancelEvent(lambda arg=0: self.__AnswerBahisTeklifi(arg))
				
				bahisRequestQuestionDialog.name = bol[2]
				self.bahisRequestQuestionDialog = bahisRequestQuestionDialog
				if "OYUN_RAKIP" in gameInfo.DICE_SYSTEM.keys():
					self.__AnswerBahisTeklifi(0)
					return
				bahisRequestQuestionDialog.Open()
			elif LuaToPython.find("#oyna#") != -1:
				self.bahisSistemiAC(str(bol[2]))
			elif LuaToPython.find("#kapat#") != -1:
				gameInfo.DICE_SYSTEM["KAPAT"] = 1
			elif LuaToPython.find("#itemekle#") != -1:
				bol_2 = LuaToPython.split("|")
				uidice.ItemSlot_R_Ekle = bol_2[1]
				uidice.ItemEkle_DURUM = 1
			elif LuaToPython.find("#kabul#") != -1:
				if bol[2] == str(player.GetName()): gameInfo.DICE_SYSTEM["KABUL_SEN"] = 1
				else: gameInfo.DICE_SYSTEM["KABUL_RAKIP"] = 1
				
				if int(bol[3]) != -1 and int(bol[3]) != -1:
					gameInfo.DICE_SYSTEM["CALISTIR"] = 1
					gameInfo.DICE_SYSTEM["RANDOM"] = [int(bol[3]),int(bol[4])]
					gameInfo.DICE_SYSTEM["TIME"] = app.GetTime()+0.4;gameInfo.DICE_SYSTEM["TIME_OPEN"]=1
					
	def bahisSistemiAC(self, isim):
		self.ac5 = uidice.DiceSystem()
		self.ac5.Show(isim)

	def __AnswerBahisTeklifi(self, gelen):
		#gelen3=gelen
		#if gelen == 2: gelen3=0
		gameInfo.sendPacket("bahis_teklif#"+str(gelen)+"#"+str(self.bahisRequestQuestionDialog.name))
			
		#if gelen != 2:
		self.bahisRequestQuestionDialog.Close()
		
		
	## icine-ekle ##
	def RequestDropItem(self, answer):
		
		if len(gameInfo.DICE_SYSTEM) > 0:
			self.itemDropQuestionDialog.Close()
			self.itemDropQuestionDialog = None
			return