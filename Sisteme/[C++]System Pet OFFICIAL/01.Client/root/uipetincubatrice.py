import os
import ui
import player
import mouseModule
import net
import app
import snd
import item
import player
import chat
import grp
import uiScriptLocale
import localeInfo
import constInfo
import ime
import wndMgr


class PetSystemIncubator(ui.ScriptWindow):
	
	def __init__(self, new_pet):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()
		self.LoadPetIncubatorImg(new_pet)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()
	
	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/PetHatchingWindow.py")
		except:
			import exception
			exception.Abort("PetHatchingWindow.LoadWindow.LoadObject")
			
		try:
			self.board = self.GetChild("board")
			self.boardtitle = self.GetChild("PetHatching_TitleBar")
			
			self.petimg = self.GetChild("HatchingItemSlot")
			self.petname = self.GetChild("pet_name")
			self.HatchingButton = self.GetChild("HatchingButton")
			
			
			#Event
			self.boardtitle.SetCloseEvent(ui.__mem_func__(self.Close))
			self.HatchingButton.SetEvent(ui.__mem_func__(self.RequestHatching,))
			
			
		except:
			import exception
			exception.Abort("PetHatchingWindow.LoadWindow.BindObject")
			
	def LoadPetIncubatorImg(self, new_pet):
		petarryname = ["Ou de Maimutica", "Ou de Paianjen", "Ou de Razador", "Ou de Nemere"]
		petarryimg = [55701, 55702, 55703, 55704]
		chat.AppendChat(chat.CHAT_TYPE_INFO, "[Pet-Incubator] "+petarryname[int(new_pet)]+".")
		self.petimg.SetItemSlot(0,petarryimg[int(new_pet)], 0)
		self.petimg.SetAlwaysRenderCoverButton(0, TRUE)
		#self.petimg.SetSlotBaseImage("icon/item/"+petarryimg[new_pet], 0, 0, 0, 0)
		
		
			
			
	def RequestHatching(self):
		if self.petname.GetText() == "" or len(self.petname.GetText()) < 4:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "[Pet-Incubator] Il nome del pet non e' valido.")
			return
			
		if player.GetElk() < 100000:
			#chat.AppendChat(chat.CHAT_TYPE_INFO, "[Pet-Incubator]Devi possedere "+str(localeInfo.NumberToMoneyString(100000)) +".")
			return
			
		chat.AppendChat(chat.CHAT_TYPE_INFO, "[Pet-Incubator]Invio pacchetto schiudi pet.")
		import chr
		chr.RequestPetName(self.petname.GetText())
		self.Close()


			


