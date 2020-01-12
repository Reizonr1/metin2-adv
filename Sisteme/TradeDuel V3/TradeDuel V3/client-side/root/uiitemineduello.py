import ui
import player
import mouseModule
import net
import app
import chat
import snd
import item
import grp
import uiScriptLocale
import playerSettingModule
import locale
import guild
import ime
import time
import grpText
import uiToolTip
import uiCommon
import systemSetting

import os
import localegame
import gameInfo
import event
import uiPickMoney
import wndMgr

YOL = str(gameInfo.CONFIG_YOL)+"itemine_ws/"

FACE_IMAGE_DICT = {
	playerSettingModule.RACE_WARRIOR_M : YOL+"0_karakter.tga",
	playerSettingModule.RACE_WARRIOR_W : YOL+"0_1_karakter.tga",
	playerSettingModule.RACE_ASSASSIN_M : YOL+"1_karakter.tga",
	playerSettingModule.RACE_ASSASSIN_W : YOL+"1_1_karakter.tga",
	playerSettingModule.RACE_SURA_M : YOL+"2_karakter.tga",
	playerSettingModule.RACE_SURA_W : YOL+"2_1_karakter.tga",
	playerSettingModule.RACE_SHAMAN_M : YOL+"3_karakter.tga",
	playerSettingModule.RACE_SHAMAN_W : YOL+"3_1_karakter.tga",
}

Item_Slot_Eklenen = 0

DUELLO_START = 0
DUELLO_PARA_EKLENDI = 0
DUELLO_PARA_EKLENDI_BENIM = 0
DUELLO_ROUND_EKLENDI = 0
DUELLO_YENDIN = 0
DUELLO_YENILDIN = 0
SEND_START = 0
ItemSlot_Benim = []
ItemSlot_Benim2 = []
ItemSlot_R_Ekle = ""
ItemSlot_R_Ekle_Ekipman = ""
ItemSlot = []
ItemEkle_DURUM = 0
ItemEkle_DURUM_Ekipman = 0

class itemineduello(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.wndEquip = None
		self.tokens = None		
		self.activeslot = 1
		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()
		self.saveName = "lib/"+str(player.GetName())+"1.ddr"

		self.ItemSlotList = {}
		self.ItemSlotList_Ekipman = {}
		self.ItemSlotList_R = {}
		self.ItemSlotList_R_Ekipman = {}
		self.ItemSlotList_R_I = {}
		self.ItemSlotList_R_I_Ekipman = {}
		self.ItemSlot = []
		self.ItemSlot_Ekipman = []
		self.kapat = 0
		self.param = 0
		self.teksefer = 0
		self.timeAFK = 0
		self.timeSira = 0
		self.zaman = 0

		self.dlgPickMoney = Duello_para_ayarlari()
		self.dlgPickMoney.LoadDialog()
		self.dlgPickMoney.Hide()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		global ItemSlot
		global DUELLO_START
		global DUELLO_PARA_EKLENDI
		global DUELLO_PARA_EKLENDI_BENIM
		global DUELLO_ROUND_EKLENDI
		global DUELLO_YENDIN
		global DUELLO_YENILDIN
		global SEND_START
		global ItemSlot_Benim
		global ItemSlot_Benim2
		global ItemSlot_R_Ekle
		global ItemSlot_R_Ekle_Ekipman
		global ItemSlot
		global ItemEkle_DURUM
		global ItemEkle_DURUM_Ekipman
		
		self.__LoadWindow()
		self.SetCenterPosition()
		ui.ScriptWindow.Show(self)
		
		self.teksefer = 0
		
		gameInfo.DUELLO_RAKIP_PARA = 0
		gameInfo.DUELLO_BENIM_PARA = 0
		gameInfo.DUELLO_KABUL = 0
		gameInfo.DUELLO_KABUL_RAKIP = 0

		gameInfo.DUELLO_ROUND = 1
		gameInfo.DUELLO_ROUND_BASLAT = 0
		gameInfo.DUELLO_ROUND_ZAMAN_IN = 0
		gameInfo.DUELLO_ROUND_ZAMAN_KALAN = 0
		gameInfo.DUELLO_ROUND_DURUM = 0
		gameInfo.DUELLO_SKOR_MY = 0
		gameInfo.DUELLO_SKOR_TARGET = 0
		gameInfo.DUELLO_KAPAT = 0

		self.kapat = 0
		self.param = int(player.GetElk())
		self.ItemSlotList = {}
		self.ItemSlotList_Ekipman = {}
		self.ItemSlotList_R = {} ## Rakibin Item Listesi ##
		self.ItemSlotList_R_Ekipman = {} ## Rakibin Ekipman Item Listesi ##
		self.ItemSlotList_R_I = {}
		self.ItemSlotList_R_I_Ekipman = {}
		self.ItemSlot = []
		self.ItemSlot_Ekipman = []

		DUELLO_START = 0
		DUELLO_PARA_EKLENDI = 0
		DUELLO_PARA_EKLENDI_BENIM = 0
		DUELLO_ROUND_EKLENDI = 0
		DUELLO_YENDIN = 0
		DUELLO_YENILDIN = 0
		SEND_START = 0
		ItemSlot_Benim = []
		ItemSlot_Benim2 = []
		ItemSlot_R_Ekle = ""
		ItemSlot_R_Ekle_Ekipman = ""
		ItemSlot = []
		ItemEkle_DURUM = 0
		ItemEkle_DURUM_Ekipman = 0

	def Close(self,gelen=0):
		global DUELLO_START
		global DUELLO_PARA_EKLENDI
		global DUELLO_PARA_EKLENDI_BENIM
		global DUELLO_ROUND_EKLENDI
		global DUELLO_YENDIN
		global DUELLO_YENILDIN
		global SEND_START
		global ItemSlot_Benim
		global ItemSlot_Benim2
		global ItemSlot_R_Ekle
		global ItemSlot_R_Ekle_Ekipman
		global ItemSlot
		global ItemEkle_DURUM
		global ItemEkle_DURUM_Ekipman
		
		if self.kapat == 0:
			net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34dsadsanxsadadsadaafsafafsxasxawqwqdsaafafasfafsafafsafsa#")
			
		if gelen==1:
			gameInfo.PYTHONISLEM="itemine_duello_sil#"+str(gameInfo.DUELLO_RAKIP)
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		
		self.roundWindow.Hide()
		gameInfo.DUELLO_ROUND = 1
		gameInfo.DUELLO_ROUND_BASLAT = 0
		gameInfo.DUELLO_ROUND_ZAMAN_IN = 0
		gameInfo.DUELLO_ROUND_ZAMAN_KALAN = 0
		gameInfo.DUELLO_ROUND_DURUM = 0
		gameInfo.DUELLO_SKOR_MY = 0
		gameInfo.DUELLO_SKOR_TARGET = 0
		gameInfo.DUELLO_DURUM = 0
		gameInfo.DUELLO_VID = 0
		gameInfo.DUELLO_BASLATAN = 0
		gameInfo.DUELLO_RAKIP_PARA = 0
		gameInfo.DUELLO_BENIM_PARA = 0
		gameInfo.DUELLO_KABUL = 0
		gameInfo.DUELLO_KABUL_RAKIP = 0
		if "#"+str(gameInfo.DUELLO_RAKIP)+"#" in gameInfo.DUELLO_YOLLAYANLAR:
			gameInfo.DUELLO_YOLLAYANLAR.remove("#"+str(gameInfo.DUELLO_RAKIP)+"#")
		
		if "#"+str(gameInfo.DUELLO_RAKIP)+"#" in gameInfo.DUELLO_YOLLANANLAR:
			gameInfo.DUELLO_YOLLANANLAR.remove("#"+str(gameInfo.DUELLO_RAKIP)+"#")

		gameInfo.DUELLO_RAKIP = ""
		gameInfo.DUELLO_KAPAT = 0

		self.kapat = 0
		self.ItemSlotList = {}
		self.ItemSlotList_Ekipman = {}
		self.ItemSlotList_R = {} ## Rakibin Item Listesi ##
		self.ItemSlotList_R_Ekipman = {} ## Rakibin Ekipman Item Listesi ##
		self.ItemSlotList_R_I = {}
		self.ItemSlotList_R_I_Ekipman = {}
		self.ItemSlot = []
		self.ItemSlot_Ekipman = []

		DUELLO_START = 0
		DUELLO_PARA_EKLENDI = 0
		DUELLO_PARA_EKLENDI_BENIM = 0
		DUELLO_ROUND_EKLENDI = 0
		DUELLO_YENDIN = 0
		DUELLO_YENILDIN = 0
		SEND_START = 0
		ItemSlot_Benim = []
		ItemSlot_Benim2 = []
		ItemSlot_R_Ekle = ""
		ItemSlot_R_Ekle_Ekipman = ""
		ItemSlot = []
		ItemEkle_DURUM = 0
		ItemEkle_DURUM_Ekipman = 0

		self.Hide()

	def __LoadWindow(self):
		global ItemSlot
		try:			
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/iteminewsdialog.py")
		except:
			import exception
			exception.Abort("ItemineDuelloWindow.LoadWindow.LoadObject")
			
		self.wndSlot = self.GetChild("ItemSlot") ## Benim 6x6 ~ 36 Tane Item Slot Ekraným ##
		self.wndSlot_R = self.GetChild("ItemSlot_Rakip") ## Rakibin 6x6 ~ 36 Tane Item Slot Ekraný ##
		self.wndEquip = self.GetChild("My_EquipSlot") ## Benim Ekipman Item Slot Ekraný ##
		self.wndEquip_R = self.GetChild("Target_EquipSlot") ## Rakibin Ekipman Item Slot Ekraný ##
		
		self.GetChild("board").Hide()
		self.GetChild("Duello_Gecmis").Hide()
		self.GetChild("Target_Character_Info_Board").Hide()
		self.GetChild("My_Character_Info_Board").Hide()
		self.GetChild("Round_Sayisi").SetEscapeEvent(ui.__mem_func__(self.OnPressEscapeKey))
		
		self.Animage = self.GetChild("Animage")
		self.zaman = app.GetTime()

		#self.wndEquip = self.GetChild("equipslot")
		self.kabulet_button = self.GetChild("kabulet_button")
		self.iptal_button = self.GetChild("iptal_button")

		self.TitleBar = self.GetChild("TitleBar")		
		self.TitleName = self.GetChild("TitleName")
		
		self.senin_Para = self.GetChild("Money_Slot")
		self.senin_Para_Text = self.GetChild("Money")
		self.rakip_Para_Text = self.GetChild("Money_Rakip")
		self.round_text = self.GetChild("Round_Text")
		self.round_value = self.GetChild("Round_Sayisi")
		self.round_okbutton = self.GetChild("Round_Ok_Button")
		self.ListBox = self.GetChild("Duello_Gecmis_Scroll")
		self.round_okbutton.SetEvent(ui.__mem_func__(self.roundDEGISTIR))
		self.roundWindow=Duello_SkorTabelasi()
		self.roundWindow.Hide()
		
		self.ListBox.InsertItem(0, " |cFF0080FF|H|hitemine ws paneli açýldý.")
		gameInfo.DUELLO_LOG=[]
		
		self.GetChild("Target_Level").SetFontColor(255, 43, 255)
		self.GetChild("My_Level").SetFontColor(255, 43, 255)
		self.GetChild("My_Name").SetFontColor(255*255, 0*255, 8*255)

		self.kabuletti_benim = self.GetChild("kabuletti_benim")
		self.kabuletti_rakip = self.GetChild("kabuletti_rakip")
		self.kabuletti_benim.Hide()
		self.kabuletti_rakip.Hide()
		
		if gameInfo.DUELLO_BASLATAN==1:
			self.round_text.Hide()
			self.round_value.Show()
			self.round_okbutton.Show()
		else:
			self.round_text.Show()
			self.round_value.Hide()
			self.round_okbutton.Hide()
			
		#chat.AppendChat(chat.CHAT_TYPE_INFO, str(gameInfo.DUELLO_BILGILERI[str(gameInfo.DUELLO_RAKIP)+"_info1"].split("#")[3]))

		self.wndSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		##self.wndSlot.SAFE_SetButtonEvent("RIGHT", "EXIST", self.UnselectItemSlot)
		self.wndSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.wndSlot.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))

		#self.wndEkipmanSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectItemSlot_Ekipman))

		self.wndSlot_R.SetOverInItemEvent(ui.__mem_func__(self.OverInItem_R))
		self.wndSlot_R.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))

		self.TitleBar.SetCloseEvent(ui.__mem_func__(self.TitleBarClose))
		self.wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectItemSlot))
		self.wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		self.wndEquip.SetOverInItemEvent(ui.__mem_func__(self.OverInItem_Ekipman))
		self.wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
		self.wndEquip_R.SetOverInItemEvent(ui.__mem_func__(self.OverInItem_R_Ekipman))
		self.wndEquip_R.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
		self.kabulet_button.SetEvent(ui.__mem_func__(self.__kabulet_button))
		self.iptal_button.SetEvent(ui.__mem_func__(self.Close),1)

		self.senin_Para.SetEvent(ui.__mem_func__(self.__para_button))

		self.LoadData()
		
	def TitleBarClose(self):
		self.Close(1)

	def __para_button(self):
		if gameInfo.DUELLO_KABUL == 0 and gameInfo.DUELLO_KABUL_RAKIP == 0:
			gameInfo.MONEY_INPUT = 2
			self.dlgPickMoney.SetTitleName('Miktar gir')
			self.dlgPickMoney.SetAcceptText('Koy')
			self.dlgPickMoney.Open(player.GetElk())
			self.dlgPickMoney.SetMax(11)
			self.dlgPickMoney.Show()
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<Düello> : Düello'ya hazýrken bu iþlem yapýlamaz.")

	def __kabulet_button(self):
		questionDialog = uiCommon.QuestionDialog2()
		questionDialog.SetText1(localegame.DUELLO_KABUL_BILGI)
		questionDialog.SetText2(localegame.DUELLO_KABUL_BILGI_2)
		questionDialog.SetAcceptEvent(ui.__mem_func__(self.kabulETBUTTON))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.kabulETMEBUTTON))
		questionDialog.SetAcceptText("Evet")
		questionDialog.SetCancelText("Hayýr")
		questionDialog.Open()
		self.questionDialog = questionDialog
		
	def kabulETBUTTON(self):
		net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34ndsawgqwqdhsabdsabdsabwbqdsnandsadnasndas#")
		gameInfo.PYTHONISLEM = "duello_kabul_ediyorum#"+str(gameInfo.DUELLO_RAKIP)
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		self.kabuletti_benim.Show()
		self.kabulet_button.Down()
		gameInfo.DUELLO_KABUL = 1
		self.questionDialog.Close()
		
	def kabulETMEBUTTON(self):
		self.questionDialog.Close()

	def __clear_button(self):
		pass				
					
	def	LoadData(self):
		pass

	def SelectEmptySlot(self, selectedSlotPos):
		global ItemSlot
		global ItemSlot_Benim
		global ItemSlot_Benim2
		global Item_Slot_Eklenen
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			if player.IsEquipmentSlot(attachedSlotPos) and gameInfo.DUELLO_UST==1:
				return

			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				if attachedSlotPos in self.ItemSlot:
					mouseModule.mouseController.DeattachObject()
				else:
				
					if gameInfo.DUELLO_KABUL == 0 and gameInfo.DUELLO_KABUL_RAKIP == 0:
						pass
					else:
						chat.AppendChat(chat.CHAT_TYPE_INFO, "<Düello> : Düello'ya hazýrken bu iþlem yapýlamaz.")
						mouseModule.mouseController.DeattachObject()
						return
				
					itemVnum2 = player.GetItemIndex(attachedSlotPos) 
					itemCount = player.GetItemCount(attachedSlotPos) 
					item.SelectItem(itemVnum2)
					itemName = item.GetItemName()
					
					if item.IsAntiFlag(item.ANTIFLAG_GIVE):
						chat.AppendChat(chat.CHAT_TYPE_INFO, locale.EXCHANGE_CANNOT_GIVE)
						mouseModule.mouseController.DeattachObject()
						return
						
					if gameInfo.sistemENGEL(2,attachedSlotPos):
						chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.ITEM_KILIT_KOYAMAZSIN)
						mouseModule.mouseController.DeattachObject()
						return
				
					if int(player.GetItemCount(int(attachedSlotPos))) == 1:
						self.wndSlot.SetItemSlot(int(selectedSlotPos), int(player.GetItemIndex(int(attachedSlotPos))), 0)
					else:
						self.wndSlot.SetItemSlot(int(selectedSlotPos), int(player.GetItemIndex(int(attachedSlotPos))), int(player.GetItemCount(int(attachedSlotPos))))
					self.ItemSlotList["slot"+str(selectedSlotPos)] = attachedSlotPos
					self.ItemSlot.append(attachedSlotPos)
					ItemSlot.append(attachedSlotPos)
					
					gameInfo.DUELLO_LOG.insert(0, "#"+str(player.GetName())+"#"+str(itemName)+"#"+str(itemCount)+"#"+str(selectedSlotPos)+"#"+str(time.strftime("[%d.%m.%y, %H:%M:%S]"))+"#slot")
					self.duelloGuncelle()
					#self.ListBox.InsertItem(0, "|cFFFF0000|H|hSen: " + "|cFFFFFF00|H|h" + str(itemName) + " (" + str(itemCount) + "x - " + str(selectedSlotPos) + ".Slot)" + " ekledin. |c000000|H|h" + str(time.strftime("[%d.%m.%y, %H:%M:%S]")))

					Item_Slot_Eklenen = str(attachedSlotPos)+"#"+str(gameInfo.DUELLO_RAKIP)+"#"+str(selectedSlotPos)
					gameInfo.PYTHONISLEM = "duello_itemekle_slot#"+str(attachedSlotPos)+"#"+str(gameInfo.DUELLO_RAKIP)+"#"+str(selectedSlotPos)
					event.QuestButtonClick(gameInfo.PYTHONTOLUA)

					## Itemi koyduðu zaman rakibe koyduðu itemi belirtme ##
					slotIndex = attachedSlotPos

					itemVnum = player.GetItemIndex(slotIndex)
					itemCount = player.GetItemCount(slotIndex)
					
					metin = ""
					attr = ""

					metinSlot = [player.GetItemMetinSocket(slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
					attrSlot = [player.GetItemAttribute(slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

					#net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34dsaxaw22121a123q#"+str(selectedSlotPos)+"#"+str(attachedSlotPos)+"#"+str(itemVnum)+"#"+str(itemCount)+"#"+str(metinSlot)+"#"+str(attrSlot)+"#")


		mouseModule.mouseController.DeattachObject()

	def __SetSlot(self, arg):
		self.saveName = "lib/"+str(player.GetName())+str(arg)+".ddr"
		self.LoadData()

	def OverInItem(self, slotNumber):
		#if self.tooltipItem:
		#	self.tooltipItem.SetInventoryItem(int(self.tokens[slotNumber-1]))
		self.tooltipItem.ClearToolTip()
		if "slot"+str(slotNumber) in self.ItemSlotList.keys():
			slotIndex = self.ItemSlotList["slot"+str(slotNumber)]
			#slotIndex = self.ItemSlot

			itemVnum = player.GetItemIndex(slotIndex)
			itemCount = player.GetItemCount(slotIndex)
			
			metinSlot = [player.GetItemMetinSocket(slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			attrSlot = [player.GetItemAttribute(slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(metinSlot))
			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(attrSlot))

			self.tooltipItem.AddRefineItemData(itemVnum, metinSlot, attrSlot)

	def OverInItem_R(self, slotNumber):
		self.tooltipItem.ClearToolTip()
		if "slot"+str(slotNumber) in self.ItemSlotList_R.keys():
			slotIndex = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")
			#item_adet = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")[3].count("@")
			#item_adet2 = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")[4].count("@")
			#items = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")[3].split("@")
			#items2 = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")[4].split("@")

			#metinList = {}
			#metinList["metin"] = list(eval(slotIndex[3]))
				
			#attrList = {}
			#attrList["attr"] = list(eval(slotIndex[4]))
			
			itemVnum = player.GetItemIndex(int(slotIndex[1]))
			itemCount = player.GetItemCount(int(slotIndex[2]))

			items = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")

			metinAttr = [int(items[4]),int(items[5]),int(items[6]),int(items[7]),int(items[8]),int(items[9])]
			slotAttr =  [(int(items[10]),int(items[11])),(int(items[12]),int(items[13])),(int(items[14]),int(items[15])),(int(items[16]),int(items[17])),(int(items[18]),int(items[19])),(int(items[20]),int(items[21])),(int(items[22]),int(items[23]))]
	
			self.tooltipItem.AddRefineItemData(int(slotIndex[1]), metinAttr, slotAttr)
			
			#metinSlot = [slotIndex[3].split("|")[i] for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			#attrSlot = [slotIndex[4].split("|")[i] for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

			#mtn = [items[1],items[2],items[3],items[4],items[5],items[6]]
			#attr = [items2[1],items2[2],items2[3],items2[4],items2[5],items2[6],items2[7],items2[8],items2[9],items2[10],items2[11],items2[12],items2[13],items2[14]]

			#metinSlot = [items[i] for i in xrange(item_adet)]
			#attrSlot = [items2[i] for i in xrange(item_adet2)]

			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(slotIndex[3]))
			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(slotIndex[4]))

			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(metinSlot))
			#chat.AppendChat(chat.CHAT_TYPE_INFO, str(attrSlot))
			
			#self.tooltipItem.AddRefineItemData(int(itemVnum), metinSlot, attrSlot)
			#self.tooltipItem.AddRefineItemData(int(itemVnum), metinSlot, attrSlot)

			###self.tooltipItem.AddRefineItemData(int(slotIndex[1]), metinList["metin"], attrList["attr"])

	def OverInItem_Ekipman(self, slotNumber):
		#if self.tooltipItem:
		#	self.tooltipItem.SetInventoryItem(int(self.tokens[slotNumber-1]))
		self.tooltipItem.ClearToolTip()
		#if slotNumber-1 in self.ItemSlotList_Ekipman.keys():
		if "slot_"+str(slotNumber) in self.ItemSlotList_Ekipman.keys():
			slotIndex = self.ItemSlotList_Ekipman["slot_"+str(slotNumber)]
			self.tooltipItem.SetInventoryItem(int(slotIndex))

	def OverInItem_R_Ekipman(self, slotNumber):
		self.tooltipItem.ClearToolTip()
		#if slotNumber-1 in self.ItemSlotList_Ekipman.keys():
		if "slot_"+str(slotNumber) in self.ItemSlotList_R_Ekipman.keys():
			#slotIndex = self.ItemSlotList_R_Ekipman["slot_"+str(slotNumber)].split("#")
			slotIndex = self.ItemSlotList_R_I_Ekipman["slot_"+str(slotNumber)].split("#")

			#metinList = {}
			#metinList["metin"] = list(eval(slotIndex[3]))
				
			#attrList = {}
			#attrList["attr"] = list(eval(slotIndex[4]))
			
			itemVnum = player.GetItemIndex(int(slotIndex[1]))
			itemCount = player.GetItemCount(int(slotIndex[2]))

			items = self.ItemSlotList_R_I_Ekipman["slot_"+str(slotNumber)].split("#")

			metinAttr = [int(items[4]),int(items[5]),int(items[6]),int(items[7]),int(items[8]),int(items[9])]
			slotAttr =  [(int(items[10]),int(items[11])),(int(items[12]),int(items[13])),(int(items[14]),int(items[15])),(int(items[16]),int(items[17])),(int(items[18]),int(items[19])),(int(items[20]),int(items[21])),(int(items[22]),int(items[23]))]
	
			self.tooltipItem.AddRefineItemData(int(slotIndex[1]), metinAttr, slotAttr)
			
			#self.tooltipItem.AddRefineItemData(int(slotIndex[1]), metinList["metin"], attrList["attr"])

	def OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
			
	def roundDEGISTIR(self):
		roundSAYISI=self.round_value.GetText()
		if int(roundSAYISI)==gameInfo.DUELLO_ROUND:
			return
			
		if gameInfo.DUELLO_KABUL == 0 and gameInfo.DUELLO_KABUL_RAKIP == 0:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<Düello> : Düello'ya hazýrken bu iþlem yapýlamaz.")
			self.round_value.SetText(str(gameInfo.DUELLO_ROUND))
			return
		
		gameInfo.DUELLO_ROUND=int(roundSAYISI)
		gameInfo.PYTHONISLEM="duello_round#"+str(roundSAYISI)+"#"+str(gameInfo.DUELLO_RAKIP)+"#0"
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34dsaxxsadsajdsajroundxsd122121dcxsa#"+str(roundSAYISI))
		gameInfo.DUELLO_LOG.insert(0, "#"+str(player.GetName())+"#"+str(roundSAYISI)+"#0#0#"+str(time.strftime("[%d.%m.%y, %H:%M:%S]"))+"#round")
		self.duelloGuncelle()
			
	def SelectItemSlot(self, itemSlotIndex):
		global ItemSlot
		global Item_Equip_Eklenen
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			#slotIndex = self.ItemSlotList_Ekipman[itemSlotIndex-1].split("#")
		
			#itemVnum = player.GetItemIndex(int(slotIndex[1]))
			#itemCount = player.GetItemCount(int(slotIndex[2]))

			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()

			if player.IsEquipmentSlot(attachedSlotPos) and gameInfo.DUELLO_UST==1:
				return

			if itemSlotIndex in self.ItemSlot_Ekipman or attachedSlotPos in self.ItemSlot:
				pass
			else:
			
				if gameInfo.DUELLO_KABUL == 0 and gameInfo.DUELLO_KABUL_RAKIP == 0:
					pass
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "<Düello> : Düello'ya hazýrken bu iþlem yapýlamaz.")
					mouseModule.mouseController.DeattachObject()
					return

				itemIndex = player.GetItemIndex(attachedSlotPos)
				itemCount = player.GetItemCount(attachedSlotPos)
				item.SelectItem(itemIndex)
				itemType = item.GetItemType()
				itemName = item.GetItemName()
				itemSubType = item.GetItemSubType()

				if itemSlotIndex == 1 and item.IsWearableFlag(item.WEARABLE_BODY):	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos
				elif itemSlotIndex == 2 and item.IsWearableFlag(item.WEARABLE_HEAD):	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos
				elif itemSlotIndex == 3 and item.IsWearableFlag(item.WEARABLE_FOOTS):	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos
				elif itemSlotIndex == 4 and item.IsWearableFlag(item.WEARABLE_WRIST):	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos
				elif itemSlotIndex == 5 and item.IsWearableFlag(item.WEARABLE_WEAPON):	
					#self.ItemSlotList_Ekipman[int(itemSlotIndex)-1] = attachedSlotPos	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos	
				elif itemSlotIndex == 6 and item.IsWearableFlag(item.WEARABLE_NECK):		
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos	
				elif itemSlotIndex == 7 and item.IsWearableFlag(item.WEARABLE_EAR):	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos
				elif itemSlotIndex == 8 and item.IsWearableFlag(item.WEARABLE_SHIELD):	
					self.ItemSlotList_Ekipman["slot_"+str(itemSlotIndex)] = attachedSlotPos
				else:		
					return
					
				gameInfo.DUELLO_LOG.insert(0, "#"+str(player.GetName())+"#"+str(itemName)+"#"+str(itemCount)+"#"+str(itemSlotIndex)+"#"+str(time.strftime("[%d.%m.%y, %H:%M:%S]"))+"#equip")
				self.duelloGuncelle()
				#self.ListBox.InsertItem(0, "|cFFFF0000|H|hSen: " + "|cFFFFFF00|H|h" + str(itemName) + " (" + str(itemCount) + "x - " + str(selectedSlotPos) + ".Ekipman Slot)" + " ekledin. |c000000|H|h" + str(time.strftime("[%d.%m.%y, %H:%M:%S]")))

				Item_Equip_Eklenen = str(attachedSlotPos)+"#"+str(gameInfo.DUELLO_RAKIP)+"#"+str(itemSlotIndex)
				gameInfo.PYTHONISLEM = "duello_itemekle_equip#"+str(attachedSlotPos)+"#"+str(gameInfo.DUELLO_RAKIP)+"#"+str(itemSlotIndex)
				event.QuestButtonClick(gameInfo.PYTHONTOLUA)
			
				self.ItemSlot_Ekipman.append(itemSlotIndex)
				self.ItemSlot.append(attachedSlotPos)
				ItemSlot.append(attachedSlotPos)

				if itemCount == 1:
					self.wndEquip.SetItemSlot(int(itemSlotIndex), int(itemIndex), 0)
				else:
					self.wndEquip.SetItemSlot(int(itemSlotIndex), int(itemIndex), int(itemCount))

				metinSlot = [player.GetItemMetinSocket(attachedSlotPos, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
				attrSlot = [player.GetItemAttribute(attachedSlotPos, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

				#net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34dsaxaw2x2121a123q#"+str(itemSlotIndex)+"#"+str(attachedSlotPos)+"#"+str(itemIndex)+"#"+str(itemCount)+"#"+str(metinSlot)+"#"+str(attrSlot)+"#")
					
				#open(self.saveName, "w").write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % tuple(self.tokens))	
					
				mouseModule.mouseController.DeattachObject()
				
	def duelloGuncelle(self):
		self.ListBox.ClearItem()
		for i in xrange(0, len(gameInfo.DUELLO_LOG)):
			bol = gameInfo.DUELLO_LOG[i].split("#")
			if bol[1] == player.GetName() and bol[6] == "slot":
				self.ListBox.InsertItem(0, "|cFFFF0000|H|hSen: " + "|cFFFFFF00|H|h" + str(bol[2]) + " (" + str(bol[3]) + "x - " + str(bol[4]) + ".Slot)" + " ekledin. |c000000|H|h" + str(bol[5]))
			elif bol[1] == player.GetName() and bol[6] == "equip":
				self.ListBox.InsertItem(0, "|cFFFF0000|H|hSen: " + "|cFFFFFF00|H|h" + str(bol[2]) + " (" + str(bol[3]) + "x - " + str(bol[4]) + ".Ekipman Slot)" + " ekledin. |c000000|H|h" + str(bol[5]))
			elif bol[1] == player.GetName() and bol[6] == "para":
				self.ListBox.InsertItem(0, "|cFFFF0000|H|hSen: " + "|cFFFFFF00|H|h" + str(locale.NumberToMoneyString(gameInfo.DUELLO_BENIM_PARA)) + " ekledin. |c000000|H|h" + str(bol[5]))
			elif bol[1] == player.GetName() and bol[6] == "round":
				self.ListBox.InsertItem(0, "|cFFFF0000|H|hSen: " + "|cFFFFFF00|H|hRound sayýsýný " + str(bol[2]) + " olarak deðiþtirdin. |c000000|H|h" + str(bol[5]))
			elif bol[1] != player.GetName() and bol[6] == "slot":
				self.ListBox.InsertItem(0, "|cFF32CD32|H|h" + str(bol[1]) + ": " + "|cFFFFFF00|H|h" + str(bol[2]) + " (" + str(bol[3]) + "x - " + str(bol[4]) + ".Slot)" + " ekledi. |c000000|H|h" + str(bol[5]))
			elif bol[1] != player.GetName() and bol[6] == "para":
				self.ListBox.InsertItem(0, "|cFF32CD32|H|h" + str(bol[1]) + ": " + "|cFFFFFF00|H|h" + str(locale.NumberToMoneyString(gameInfo.DUELLO_RAKIP_PARA)) + " ekledi. |c000000|H|h" + str(bol[5]))
			elif bol[1] != player.GetName() and bol[6] == "equip":
				self.ListBox.InsertItem(0, "|cFF32CD32|H|h" + str(bol[1]) + ": " + "|cFFFFFF00|H|h" + str(bol[2]) + " (" + str(bol[3]) + "x - " + str(bol[4]) + ".Ekipman Slot)" + " ekledi. |c000000|H|h" + str(bol[5]))
			elif bol[1] != player.GetName() and bol[6] == "round":
				self.ListBox.InsertItem(0, "|cFF32CD32|H|h" + str(bol[1]) + ": " + "|cFFFFFF00|H|hRound sayýsýný " + str(bol[2]) + " olarak deðiþtirdi. |c000000|H|h" + str(bol[5]))
				
	def OnUpdate(self):
		global ItemEkle_DURUM
		global ItemEkle_DURUM_Ekipman
		global ItemSlot_R_Ekle
		global ItemSlot_R_Ekle_Ekipman
		global DUELLO_START
		global DUELLO_PARA_EKLENDI
		global DUELLO_PARA_EKLENDI_BENIM
		global DUELLO_ROUND_EKLENDI
		global DUELLO_YENDIN
		global DUELLO_YENILDIN
		global SEND_START
					
		""" eskiZAMAN_AFK = self.timeAFK
		yeniZAMAN_AFK = app.GetTime()
		suanZAMAN_AFK = yeniZAMAN_AFK - eskiZAMAN_AFK
		if suanZAMAN_AFK > 0.1000 and self.timeSira != 131:
			self.Animage.LoadImage(str(gameInfo.CONFIG_YOL)+"itemine_ws/"+str(self.timeSira)+".tga")
			self.timeSira += 1
			if self.timeSira == 16:
				self.timeSira = 131
				self.GetChild("board").Show()
			self.timeAFK=yeniZAMAN_AFK """
			
		if app.GetTime() >= self.zaman + 2:
			self.Animage.Hide()
			self.GetChild("board").Show()
			self.GetChild("Duello_Gecmis").Show()
			self.GetChild("Target_Character_Info_Board").Show()
			self.GetChild("My_Character_Info_Board").Show()
			self.zaman = 0

		self.TitleName.SetText(str(gameInfo.DUELLO_RAKIP) + " adlý oyuncuyla eþyalý düello panelin.")
		self.senin_Para_Text.SetText(str(locale.NumberToMoneyString(gameInfo.DUELLO_BENIM_PARA)))
		self.rakip_Para_Text.SetText(str(locale.NumberToMoneyString(gameInfo.DUELLO_RAKIP_PARA)))
		self.round_text.SetText(str(gameInfo.DUELLO_ROUND))
		
		if str(gameInfo.DUELLO_RAKIP)+"_info1" in gameInfo.DUELLO_BILGILERI.keys():
			if str(gameInfo.DUELLO_RAKIP) != "":
				self.GetChild("My_Level").SetText("Lv. " + str(player.GetStatus(player.LEVEL)))
				self.GetChild("My_Name").SetText(str(player.GetName()))
				self.GetChild("My_Character_Image").LoadImage(FACE_IMAGE_DICT[net.GetMainActorRace()])
				self.GetChild("Target_Character_Image").LoadImage(FACE_IMAGE_DICT[int(gameInfo.DUELLO_BILGILERI[str(gameInfo.DUELLO_RAKIP)+"_info1"].split("#")[3])])
				self.GetChild("Target_Name").SetText(str(gameInfo.DUELLO_RAKIP))
				self.GetChild("Target_Level").SetText("Lv. " + str(gameInfo.DUELLO_BILGILERI[str(gameInfo.DUELLO_RAKIP)+"_info1"].split("#")[1]))
				self.GetChild("Target_Guild").SetText(str(gameInfo.DUELLO_BILGILERI[str(gameInfo.DUELLO_RAKIP)+"_info1"].split("#")[2]))
				
				if not guild.IsGuildEnable():
					self.GetChild("My_Guild").SetText("Lonca Yok")
				else:
					self.GetChild("My_Guild").SetText(str(player.GetGuildName()))
				
		if str(gameInfo.DUELLO_RAKIP)+"_info2" in gameInfo.DUELLO_BILGILERI.keys():
			self.GetChild("Target_MacBilgileri_1").SetText("Toplam Maç:" + str(gameInfo.DUELLO_BILGILERI[str(gameInfo.DUELLO_RAKIP)+"_info2"].split("#")[1]))
			self.GetChild("Target_MacBilgileri_2").SetText("G/M : " + str(gameInfo.DUELLO_BILGILERI[str(gameInfo.DUELLO_RAKIP)+"_info2"].split("#")[2])+"/"+str(gameInfo.DUELLO_BILGILERI[str(gameInfo.DUELLO_RAKIP)+"_info2"].split("#")[3]))
			self.GetChild("Target_MacBilgileri_3").SetText("Kaçma : " + str(gameInfo.DUELLO_BILGILERI[str(gameInfo.DUELLO_RAKIP)+"_info2"].split("#")[4]))
			
		if str(player.GetName())+"_info2" in gameInfo.DUELLO_BILGILERI.keys():
			self.GetChild("My_MacBilgileri_1").SetText("Toplam Maç:" + str(gameInfo.DUELLO_BILGILERI[str(player.GetName())+"_info2"].split("#")[1]))
			self.GetChild("My_MacBilgileri_2").SetText("G/M : " + str(gameInfo.DUELLO_BILGILERI[str(player.GetName())+"_info2"].split("#")[2])+"/"+str(gameInfo.DUELLO_BILGILERI[str(player.GetName())+"_info2"].split("#")[3]))
			self.GetChild("My_MacBilgileri_3").SetText("Kaçma : " + str(gameInfo.DUELLO_BILGILERI[str(player.GetName())+"_info2"].split("#")[4]))

		if gameInfo.DUELLO_DURUM==1:
			self.roundWindow.Show()
		else:
			self.roundWindow.Hide()
			
		if int(gameInfo.DUELLO_RAKIP_PARA) != 0:
			if int(gameInfo.DUELLO_RAKIP_PARA)+int(self.param) >= 1999999999:
				self.Close()
		
		if gameInfo.DUELLO_KABUL_RAKIP == 1:
			self.kabuletti_rakip.Show()
			if gameInfo.DUELLO_KABUL == 1:
				if gameInfo.DUELLO_BASLATAN == 2 and DUELLO_START == 0:
					net.SendChatPacket("/pvp %d" % (int(gameInfo.DUELLO_VID)))
					gameInfo.PYTHONISLEM = "duello_basladi#"+str(gameInfo.DUELLO_RAKIP)
					event.QuestButtonClick(gameInfo.PYTHONTOLUA)
					DUELLO_START = 1
				if SEND_START == 0:
					gameInfo.DUELLO_DURUM = 1
					SEND_START = 1

		if gameInfo.DUELLO_KABUL_RAKIP == 1 and gameInfo.DUELLO_KABUL == 1:
			gameInfo.DUELLO_DURUM = 1
			self.SetPosition(9000, 5000)

		if gameInfo.DUELLO_KABUL == 1:
			self.kabulet_button.Down()

		#if gameInfo.DUELLO_RAKIP == "":
		if gameInfo.DUELLO_KAPAT == 1:
			self.kapat = 1
			self.roundWindow.Hide()
			self.Close()
			
		if gameInfo.UZAKTAN_TICARET_DURUM != 0:
			self.Close()
			
		if DUELLO_PARA_EKLENDI == 1:
			gameInfo.DUELLO_LOG.insert(0, "#"+str(gameInfo.DUELLO_RAKIP)+"#0#0#0#"+str(time.strftime("[%d.%m.%y, %H:%M:%S]"))+"#para")
			self.duelloGuncelle()
			#self.ListBox.InsertItem(0, "|cFF32CD32|H|h"+str(gameInfo.DUELLO_RAKIP) + ": " + "|cFFFFFF00|H|h" + str(locale.NumberToMoneyString(gameInfo.DUELLO_RAKIP_PARA)) + " ekledi. |c000000|H|h" + str(time.strftime("[%d.%m.%y, %H:%M:%S]")))
			DUELLO_PARA_EKLENDI = 0
			
		if DUELLO_PARA_EKLENDI_BENIM == 1:
			gameInfo.DUELLO_LOG.insert(0, "#"+str(player.GetName())+"#0#0#0#"+str(time.strftime("[%d.%m.%y, %H:%M:%S]"))+"#para")
			self.duelloGuncelle()
			#self.ListBox.InsertItem(0, "|cFF32CD32|H|hSen: " + "|cFFFFFF00|H|h" + str(locale.NumberToMoneyString(gameInfo.DUELLO_BENIM_PARA)) + " ekledin. |c000000|H|h" + str(time.strftime("[%d.%m.%y, %H:%M:%S]")))
			DUELLO_PARA_EKLENDI_BENIM = 0
			
		if DUELLO_ROUND_EKLENDI == 1:
			self.duelloGuncelle()
			DUELLO_ROUND_EKLENDI = 0

		if ItemEkle_DURUM == 1:
			bol = ItemSlot_R_Ekle.split("#")
			#self.ItemSlotList_R["slot"+str(bol[1])] = int(bol[2])
			self.ItemSlotList_R["slot"+str(bol[26])] = int(bol[3])
			#self.ItemSlotList_R_I["slot"+str(bol[1])] = "#"+str(bol[3])+"#"+str(bol[4])+"#"+str(bol[5])+"#"+str(bol[6])+"#"
			self.ItemSlotList_R_I["slot"+str(bol[26])] = ItemSlot_R_Ekle
			if int(bol[2]) == 1:
				self.wndSlot_R.SetItemSlot(int(bol[26]), int(bol[1]), 0)
			else:
				self.wndSlot_R.SetItemSlot(int(bol[26]), int(bol[1]), int(bol[2]))
			item.SelectItem(int(bol[1]))
			itemName = item.GetItemName()
			itemAdet = int(bol[2])
			gameInfo.DUELLO_LOG.insert(0, "#"+str(gameInfo.DUELLO_RAKIP)+"#"+str(itemName)+"#"+str(itemAdet)+"#"+str(bol[26])+"#"+str(time.strftime("[%d.%m.%y, %H:%M:%S]"))+"#equip")
			self.duelloGuncelle()
			#self.ListBox.InsertItem(0, "|cFF32CD32|H|h"+str(gameInfo.DUELLO_RAKIP) + ": " + "|cFFFFFF00|H|h" + str(itemName) + " (" + str(itemAdet) + "x - " + str(bol[26]) + ".Slot)" + " ekledi. |c000000|H|h" + str(time.strftime("[%d.%m.%y, %H:%M:%S]")))
			ItemEkle_DURUM = 0
			##self.ItemSlot_R.append(attachedSlotPos)

		if ItemEkle_DURUM_Ekipman == 1:
			bol = ItemSlot_R_Ekle_Ekipman.split("#")
			#self.ItemSlotList_R_Ekipman["slot_"+str(bol[1])] = int(bol[2])
			self.ItemSlotList_R_Ekipman["slot_"+str(bol[26])] = int(bol[3])
			#self.ItemSlotList_R_I_Ekipman["slot_"+str(bol[1])] = "#"+str(bol[3])+"#"+str(bol[4])+"#"+str(bol[5])+"#"+str(bol[6])+"#"
			self.ItemSlotList_R_I_Ekipman["slot_"+str(bol[26])] = ItemSlot_R_Ekle_Ekipman
			if int(bol[2]) == 1:
				self.wndEquip_R.SetItemSlot(int(bol[26]), int(bol[1]), 0)
			else:
				self.wndEquip_R.SetItemSlot(int(bol[26]), int(bol[1]), int(bol[2]))
			item.SelectItem(int(bol[1]))
			itemName = item.GetItemName()
			itemAdet = int(bol[2])
			gameInfo.DUELLO_LOG.insert(0, "#"+str(gameInfo.DUELLO_RAKIP)+"#"+str(itemName)+"#"+str(itemAdet)+"#"+str(bol[26])+"#"+str(time.strftime("[%d.%m.%y, %H:%M:%S]"))+"#equip")
			self.duelloGuncelle()
			#self.ListBox.InsertItem(0, "|cFF32CD32|H|h"+str(gameInfo.DUELLO_RAKIP) + ": " + "|cFFFFFF00|H|h" + str(itemName) + " (" + str(itemAdet) + "x - " + str(bol[26]) + ".Ekipman Slot)" + " ekledi. |c000000|H|h" + str(time.strftime("[%d.%m.%y, %H:%M:%S]")))
			ItemEkle_DURUM_Ekipman = 0
			
		if player.IsOpenPrivateShop():
			self.Close()
			
		if gameInfo.PAZAR_ITEMLI == 1:
			self.kapat = 1
			self.Close()
					
	def OnPressEscapeKey(self):
		gameInfo.DUELLO_BILGILERI["ESC"] = "1"
		return TRUE
		
	def OnPressExitKey(self):
		gameInfo.DUELLO_BILGILERI["ESC"] = "1"
		return TRUE
		
class Duello_SkorTabelasi(ui.Window):

	def __init__(self):
		ui.Window.__init__(self)
		
		self.Config()

	def __del__(self):
		ui.Window.__del__(self)
		
	def Config(self):
		global YOL
		self.SetSize(400, 138)
		self.SetPosition(3,int(systemSetting.GetHeight()-215))
		y=8
		y2=18
		
		self.roundHAZIR_T=0
		self.roundHAZIR_ISLEM=0
		
		self.arkaPlan = ui.ImageBox()
		self.arkaPlan.SetParent(self)
		self.arkaPlan.SetPosition(0,0)
		self.arkaPlan.LoadImage(YOL+"skorboard.tga")
		self.arkaPlan.Show()
		
		self.iconSenin = ui.ImageBox()
		self.iconSenin.SetParent(self)
		self.iconSenin.SetPosition(47,7)
		self.iconSenin.LoadImage(FACE_IMAGE_DICT[int(net.GetMainActorRace())])
		self.iconSenin.Show()
		
		self.iconRakip = ui.ImageBox()
		self.iconRakip.SetParent(self)
		self.iconRakip.SetPosition(264,7)
		self.iconRakip.Show()
		
		self.isimArkaSENIN = ui.ImageBox()
		self.isimArkaSENIN.SetParent(self)
		self.isimArkaSENIN.SetPosition(24,107)
		self.isimArkaSENIN.LoadImage(YOL+"skorboard_slot.tga")
		self.isimArkaSENIN.Show()
		
		self.isimSENIN = ui.TextLine()
		self.isimSENIN.SetParent(self.isimArkaSENIN)
		self.isimSENIN.SetDefaultFontName()
		#self.isimSENIN.SetPosition(- 137, 138 - 29)
		self.isimSENIN.SetPosition(0, - 1)
		self.isimSENIN.SetText(str(player.GetName()))
		#self.isimSENIN.SetWindowVerticalAlignCenter()
		self.isimSENIN.SetHorizontalAlignCenter()
		self.isimSENIN.SetVerticalAlignCenter()
		self.isimSENIN.SetWindowHorizontalAlignCenter()
		self.isimSENIN.SetWindowVerticalAlignCenter()
		self.isimSENIN.Show()
		
		self.isimArkaRAKIP = ui.ImageBox()
		self.isimArkaRAKIP.SetParent(self)
		self.isimArkaRAKIP.SetPosition(239,107)
		self.isimArkaRAKIP.LoadImage(YOL+"skorboard_slot.tga")
		self.isimArkaRAKIP.Show()
		
		self.isimRAKIP = ui.TextLine()
		self.isimRAKIP.SetParent(self.isimArkaRAKIP)
		self.isimRAKIP.SetDefaultFontName()
		#self.isimRAKIP.SetPosition(65 + 28, 138 - 29)
		self.isimRAKIP.SetPosition(0,  - 1)
		self.isimRAKIP.SetText("HasskTR")
		#self.isimRAKIP.SetWindowVerticalAlignCenter()
		self.isimRAKIP.SetHorizontalAlignCenter()
		self.isimRAKIP.SetVerticalAlignCenter()
		self.isimRAKIP.SetWindowHorizontalAlignCenter()
		self.isimRAKIP.SetWindowVerticalAlignCenter()
		self.isimRAKIP.Show()
		
		self.skorSENIN = ui.TextLine()
		self.skorSENIN.SetParent(self)
		self.skorSENIN.SetFontName("Tahoma:26")
		self.skorSENIN.SetPosition(-23, 52 - 18)
		self.skorSENIN.SetText("2 -")
		self.skorSENIN.SetWindowHorizontalAlignCenter()
		self.skorSENIN.Show()	

		self.skorRAKIP = ui.TextLine()
		self.skorRAKIP.SetParent(self)
		self.skorRAKIP.SetFontName("Tahoma:26")
		self.skorRAKIP.SetPosition(13, 52 - 18)
		self.skorRAKIP.SetText("1")
		self.skorRAKIP.SetWindowHorizontalAlignCenter()
		self.skorRAKIP.Show()
		
		self.roundSAYISI = ui.TextLine()
		self.roundSAYISI.SetParent(self)
		self.roundSAYISI.SetDefaultFontName()
		self.roundSAYISI.SetPosition(-16,69)
		self.roundSAYISI.SetText("fatihbab34, 2015.9.21 <3")
		self.roundSAYISI.SetWindowHorizontalAlignCenter()
		self.roundSAYISI.Show()
		
		self.roundDurum_Senin = ui.ImageBox()
		self.roundDurum_Senin.SetParent(self)
		self.roundDurum_Senin.SetPosition(47,7)
		self.roundDurum_Senin.LoadImage(YOL+"skorboard_kirmizi.tga")
		self.roundDurum_Senin.Hide()
		
		self.roundDurum_Rakip = ui.ImageBox()
		self.roundDurum_Rakip.SetParent(self)
		self.roundDurum_Rakip.SetPosition(264,7)
		self.roundDurum_Rakip.LoadImage(YOL+"skorboard_kirmizi.tga")
		self.roundDurum_Rakip.Hide()
		
		print "fatihbab34, 2016.1.22 <3"
		print "versiyon v3.0"
		
		self.roundHazirBUTTON = self.Button(self, 'Hazýr', '', 71 + 98, 93, self.__roundHAZIR, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.roundBildirBUTTON = self.Button(self, 'Rakibi bildir', 'Eðer rakip düellodayken çýktýysa bildir!', 71 + 98, 0, self.__roundBildir, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.roundHazirBUTTON.Hide()
		
	def __roundHAZIR(self):
		if int(player.GetStatus(player.HP)) <= 0:
			return
		gameInfo.DUELLO_ROUND_HAZIR_MY=1
		net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34dasddjsadjsajmwmwqroundhazirndsandsad#")
		
	def __roundBildir(self):
		gameInfo.PYTHONISLEM = "duello_rakipbildir#"
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button
		
	def OnUpdate(self):
		global DUELLO_YENDIN
		global DUELLO_YENILDIN
		global YOL
		self.isimRAKIP.SetText(str(gameInfo.DUELLO_RAKIP))
		self.skorSENIN.SetText(str(gameInfo.DUELLO_SKOR_MY) + " -")
		self.skorRAKIP.SetText(str(gameInfo.DUELLO_SKOR_TARGET))
		#self.roundSAYISI.SetText("Kalan Round : " + str(8-(gameInfo.DUELLO_SKOR_MY+gameInfo.DUELLO_SKOR_TARGET)))
		self.roundSAYISI.SetText("Bitiþ : " + str(gameInfo.DUELLO_ROUND))
		
		if str(gameInfo.DUELLO_RAKIP)+"_info1" in gameInfo.DUELLO_BILGILERI.keys():
			self.iconRakip.LoadImage(FACE_IMAGE_DICT[int(gameInfo.DUELLO_BILGILERI[str(gameInfo.DUELLO_RAKIP)+"_info1"].split("#")[3])])
			
		if DUELLO_YENDIN == 1:
			self.roundDurum_Senin.LoadImage(YOL+"skorboard_mavi.tga")
			self.roundDurum_Rakip.LoadImage(YOL+"skorboard_kirmizi.tga")
			self.roundDurum_Senin.Show()
			self.roundDurum_Rakip.Show()
		elif DUELLO_YENILDIN == 1:
			self.roundDurum_Senin.LoadImage(YOL+"skorboard_kirmizi.tga")
			self.roundDurum_Rakip.LoadImage(YOL+"skorboard_mavi.tga")
			self.roundDurum_Senin.Show()
			self.roundDurum_Rakip.Show()
		
		if gameInfo.DUELLO_ROUND_HAZIR_TARGET==1:
			self.roundDurum_Rakip.LoadImage(YOL+"skorboard_yesil.tga")
			self.roundDurum_Rakip.Show()
		
		if gameInfo.DUELLO_ROUND_HAZIR_MY==1:
			self.roundDurum_Senin.LoadImage(YOL+"skorboard_yesil.tga")
			self.roundDurum_Senin.Show()
			
		if gameInfo.DUELLO_ROUND_HAZIR_MY==1 and gameInfo.DUELLO_ROUND_HAZIR_TARGET==1:
			if player.IsRevengeInstance(gameInfo.DUELLO_VID):
				net.SendChatPacket("/pvp %d" % (int(gameInfo.DUELLO_VID)))
			self.roundDurum_Senin.Hide()
			self.roundDurum_Rakip.Hide()
			gameInfo.DUELLO_ROUND_HAZIR_MY=0
			gameInfo.DUELLO_ROUND_HAZIR_TARGET=0
			DUELLO_YENDIN = 0
			DUELLO_YENILDIN = 0
			self.roundHAZIR_ISLEM=0

		if self.roundHAZIR_T==0 and gameInfo.DUELLO_ROUND_HAZIR_MY==0:
			self.roundHazirBUTTON.SetUp()
			self.roundHazirBUTTON.Enable()
			self.roundHAZIR_T=1
			
		if gameInfo.DUELLO_ROUND_YENILE==1:
			self.roundHAZIR_T=0
			self.roundHAZIR_ISLEM=1
			gameInfo.DUELLO_ROUND_YENILE=0
			
		if self.roundHAZIR_ISLEM==1:
			self.roundHazirBUTTON.Show()
			self.roundBildirBUTTON.Show()
		else:
			self.roundHazirBUTTON.Hide()
			self.roundBildirBUTTON.Show()
		
		if gameInfo.DUELLO_ROUND_HAZIR_MY == 1:
			self.roundHazirBUTTON.Down()
			self.roundHazirBUTTON.Disable()
			
		if gameInfo.DUELLO_RAKIP=="" or gameInfo.DUELLO_DURUM == 0:
			self.Hide()
			
class itemineduello_depo(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem = tooltipItem
		
		self.dlgPickMoney = Duello_para_ayarlari()
		self.dlgPickMoney.LoadDialog()
		self.dlgPickMoney.Hide()
		
		self.zaman = 0
		self.duellosonu = 0
		self.name = ""

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self, name=""):
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			chat.AppendChat(chat.CHAT_TYPE_INFO, str(localegame.DUELLO_DEPO_ACAMAZSIN))
			return
		
		if name != "":
			self.duellosonu=1
			self.name = name
		else:
			self.duelloVERILERIAL()
			
		gameInfo.DUELLO_BILGILERI["PANEL"] = "1"
			
		self.__LoadWindow()
		self.SetCenterPosition()
		ui.ScriptWindow.Show(self)
		
	def duelloVERILERIAL(self):
		gameInfo.DUELLO_BILGILERI = {}
		gameInfo.PYTHONISLEM = "duello_depo_al#"
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)

	def Close(self):
		gameInfo.DUELLO_BILGILERI["PANEL"] = "0"
		snd.PlaySound("sound/ui/click.wav")
		self.Hide()

	def __LoadWindow(self):
		try:			
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/iteminewsdialog_depo.py")
			
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.GetChild("board").Hide()
			
			self.Animage = self.GetChild("Animage")
			
			self.wndSlot = self.GetChild("ItemSlot_Rakip") ## Rakibin 6x6 ~ 36 Tane Item Slot Ekraný ##
			self.wndEquip = self.GetChild("Target_EquipSlot") ## Rakibin Ekipman Item Slot Ekraný ##
			self.moneySlotButton = self.GetChild("Money_Slot_Rakip")
			
			self.wndSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			self.wndSlot.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
			self.wndEquip.SetOverInItemEvent(ui.__mem_func__(self.OverInItem_Ekipman))
			self.wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
			self.wndSlot.SetUnselectItemSlotEvent(ui.__mem_func__(self.UnselectItemSlot))	
			self.wndSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
			self.wndSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))	
			self.wndEquip.SetUnselectItemSlotEvent(ui.__mem_func__(self.UnselectItemSlotEquip))
			self.wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlotEquip))
			self.wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlotEquip))
			
			self.moneySlotButton.SetEvent(ui.__mem_func__(self.paraEKRANIAC))
			self.GetChild("hepsinial_button").SetEvent(lambda durum="hepsi":self.duelloISLEMLERI(durum))
			self.GetChild("sil_button").SetEvent(lambda durum="sil": self.duelloISLEMLERI(durum))
			self.GetChild("yenile_button").SetEvent(lambda durum="yenile": self.duelloISLEMLERI(durum))
			
			self.zaman = app.GetTime()
			
			self.GetChild("My_Level").SetFontColor(255, 43, 255)
			self.GetChild("My_Name").SetFontColor(255*255, 0*255, 8*255)
					
		except:
			import exception
			exception.Abort("itemineduello_depo.LoadWindow.LoadObject")
			
	def SelectEmptySlot(self, selectedSlotPos, gelen="slot"):
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				chat.AppendChat(chat.CHAT_TYPE_INFO, str(localegame.DUELLO_DEPO_ITEM_KOYAMAZSIN))
			elif player.SLOT_TYPE_INVENTORY != attachedSlotType and player.SLOT_TYPE_MALL != attachedSlotType and player.SLOT_TYPE_SAFEBOX != attachedSlotType and player.SLOT_TYPE_SHOP != attachedSlotType:
				chat.AppendChat(chat.CHAT_TYPE_INFO, str(localegame.DUELLO_DEPO_ITEM_HAREKET_ETTIREMEZSIN))
				
		mouseModule.mouseController.DeattachObject()
			
	def UnselectItemSlot(self, selectedSlotPos, gelen="slot"):
		self.depoGERIALPAKET(selectedSlotPos, gelen)
		mouseModule.mouseController.DeattachObject()
		self.OnOverOutItem()
		
	def SelectItemSlot(self, selectedSlotPos, gelen="slot"):
		#items = gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_"+str(gelen)][selectedSlotPos].split("#")
		slotIndex = gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_"+str(gelen)]
		index = 0
		for i in xrange(0, len(slotIndex)):
			bol = slotIndex[i].split("#")
			if str(bol[26]) == str(selectedSlotPos):
				index = i
		items = gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_"+str(gelen)][index].split("#")
		selectedSlotPos = selectedSlotPos
		selectedItemID = items[1]
		itemCount = items[2]
		self.selectedSlotPos=selectedSlotPos

		type = player.SLOT_TYPE_PRIVATE_SHOP
		mouseModule.mouseController.AttachObject(self, type, int(selectedSlotPos), int(selectedItemID), int(itemCount))
		#self.temporaryTab = self.tab
		mouseModule.mouseController.SetCallBack("INVENTORY", lambda durum=gelen:self.DropToInventory(durum))
		snd.PlaySound("sound/ui/pick.wav")
		
	def DropToInventory(self, gelen):
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		self.depoGERIALPAKET(attachedSlotPos, gelen)
		self.OnOverOutItem()
		
	def UnselectItemSlotEquip(self, selectedSlotPos):
		self.UnselectItemSlot(selectedSlotPos, "equip")
		
	def SelectEmptySlotEquip(self, selectedSlotPos):
		self.SelectEmptySlot(selectedSlotPos, "equip")
		
	def SelectItemSlotEquip(self, selectedSlotPos):
		self.SelectItemSlot(selectedSlotPos, "equip")
		
	def duelloISLEMLERI(self, gelen):
		self.depoGERIALPAKET(0, gelen)
		
	def depoGERIALPAKET(self, selectedSlotPos, gelen):
		durum = 0
		if gelen == "hepsi":
			gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_slot"] = []
			gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_equip"] = []
			gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_para"] = []
			gameInfo.DUELLO_BILGILERI["YENILE"] = "1"
			self.name = ""
			durum = 1
		elif gelen == "yenile":
			self.duelloVERILERIAL()
			durum = 1
			
		if gelen == "sil":
			questionDialog = uiCommon.QuestionDialog()
			questionDialog.SetText(str(localegame.DUELLO_DEPO_SIL))
			questionDialog.SetAcceptEvent(lambda durum="1":self.depoSIL(durum))
			questionDialog.SetCancelEvent(lambda durum="0":self.depoSIL(durum))
			questionDialog.SetAcceptText("Evet")
			questionDialog.SetCancelText("Hayýr")
			questionDialog.Open()
			self.questionDialog = questionDialog
			return
			
		if durum == 0:
			if "depo_"+str(self.name)+"_"+str(gelen) in gameInfo.DUELLO_BILGILERI:
				#slotIndex = gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_"+str(gelen)]
				index = 0
				for i in xrange(0, len(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_"+str(gelen)])):
					if gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_"+str(gelen)][i] != None:
						bol = gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_"+str(gelen)][i].split("#")
						if str(bol[26]) == str(selectedSlotPos):
							#chat.AppendChat(chat.CHAT_TYPE_INFO, str(i))
							gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_"+str(gelen)].remove(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_"+str(gelen)][i])
							gameInfo.DUELLO_BILGILERI["YENILE"] = "1"
							break
			
		#if duelloKONTROL():
		#	gameInfo.PYTHONISLEM = "duello_depo_itemislemleri#"+str(gelen)+"#"+str(selectedSlotPos)+"#1"
		#else:
		#	gameInfo.PYTHONISLEM = "duello_depo_itemislemleri#"+str(gelen)+"#"+str(selectedSlotPos)+"#0"
		
		gameInfo.PYTHONISLEM = "duello_depo_itemislemleri#"+str(gelen)+"#"+str(selectedSlotPos)+"#0"	
		event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		
	def depoSIL(self, gelen):
		if gelen == "1":
		
			gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_slot"] = []
			gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_equip"] = []
			gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_para"] = []
			gameInfo.DUELLO_BILGILERI["YENILE"] = "1"
			self.name = ""
		
			gameInfo.PYTHONISLEM = "duello_depo_itemislemleri#sil#0#0"	
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)
		self.questionDialog.Close()
		
	def duelloKONTROL(self):
		equip = 0
		slot = 0
		para = 0
		if "depo_"+str(self.name)+"_equip" in gameInfo.DUELLO_BILGILERI.keys():
			if len(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_equip"]) <= 0:
				equip = 0
			else:
				equip = 1
		else:
			equip = 0
			
		if "depo_"+str(self.name)+"_slot" in gameInfo.DUELLO_BILGILERI.keys():
			if len(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_slot"]) <= 0:
				slot = 0
			else:
				slot = 1
		else:
			slot = 0
			
		if "depo_"+str(self.name)+"_para" in gameInfo.DUELLO_BILGILERI.keys():
			if gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_slot"] == "[]" or gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_slot"] == "0":
				slot = 0
			else:
				slot = 1
		else:
			slot = 0
			
		if equip == 0 and slot == 0 and para == 0:
			return TRUE
			
		return FALSE

	def OverInItem(self, slotNumber):
		self.tooltipItem.ClearToolTip()
		
		slotIndex = gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_slot"]
		index = 0
		for i in xrange(0, len(slotIndex)):
			bol = slotIndex[i].split("#")
			if str(bol[26]) == str(slotNumber):
				index = i
				
		slotIndex = gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_slot"][index].split("#")
		itemVnum = player.GetItemIndex(int(slotIndex[1]))
		itemCount = player.GetItemCount(int(slotIndex[2]))

		items = slotIndex

		metinAttr = [int(items[4]),int(items[5]),int(items[6]),int(items[7]),int(items[8]),int(items[9])]
		slotAttr =  [(int(items[10]),int(items[11])),(int(items[12]),int(items[13])),(int(items[14]),int(items[15])),(int(items[16]),int(items[17])),(int(items[18]),int(items[19])),(int(items[20]),int(items[21])),(int(items[22]),int(items[23]))]

		self.tooltipItem.AddRefineItemData(int(slotIndex[1]), metinAttr, slotAttr)

	def OverInItem_Ekipman(self, slotNumber):
		self.tooltipItem.ClearToolTip()
		
		slotIndex = gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_equip"]
		index = 0
		for i in xrange(0, len(slotIndex)):
			bol = slotIndex[i].split("#")
			if str(bol[26]) == str(slotNumber):
				index = i
				
		slotIndex = gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_equip"][index].split("#")

		itemVnum = player.GetItemIndex(int(slotIndex[1]))
		itemCount = player.GetItemCount(int(slotIndex[2]))

		items = slotIndex

		metinAttr = [int(items[4]),int(items[5]),int(items[6]),int(items[7]),int(items[8]),int(items[9])]
		slotAttr =  [(int(items[10]),int(items[11])),(int(items[12]),int(items[13])),(int(items[14]),int(items[15])),(int(items[16]),int(items[17])),(int(items[18]),int(items[19])),(int(items[20]),int(items[21])),(int(items[22]),int(items[23]))]

		self.tooltipItem.AddRefineItemData(int(slotIndex[1]), metinAttr, slotAttr)
		
		#self.tooltipItem.AddRefineItemData(int(slotIndex[1]), metinList["metin"], attrList["attr"])

	def OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
			
	def paraEKRANIAC(self):
		if "depo_"+str(self.name)+"_para" in gameInfo.DUELLO_BILGILERI.keys() and str(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_para"]) != "[]" and str(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_para"]) != "0":
			self.dlgPickMoney.SetTitleName('Miktar gir')
			self.dlgPickMoney.SetAcceptText('Çek')
			self.dlgPickMoney.Open(int(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_para"]), 1, 1, self.name)
			self.dlgPickMoney.SetMax(11)
			self.dlgPickMoney.Show()
			
	def duelloBilgiYENILE(self):
	
		## Silme Ýþlemleri
		for i in xrange(0, 36):
			self.wndSlot.ClearSlot(i)
			
		for i in xrange(1, 9):
			self.wndEquip.ClearSlot(i)
			
		self.GetChild("Money_Rakip").SetText("0 Yang")
			
		## Ekleme Ýþlemleri
		if "depo_"+str(self.name)+"_slot" in gameInfo.DUELLO_BILGILERI.keys():
			if len(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_slot"]) != 0:
				for i in xrange(0, len(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_slot"])):
					bol = gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_slot"][i].split("#")
					self.wndSlot.ClearSlot(int(bol[26]))
					if int(bol[2]) == 1:
						self.wndSlot.SetItemSlot(int(bol[26]), int(bol[1]), 0)
					else:
						self.wndSlot.SetItemSlot(int(bol[26]), int(bol[1]), int(bol[2]))
		
		if "depo_"+str(self.name)+"_equip" in gameInfo.DUELLO_BILGILERI.keys():
			if len(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_equip"]) != 0:
				for i in xrange(0, len(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_equip"])):
					bol = gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_equip"][i].split("#")
					self.wndEquip.ClearSlot(int(bol[26]))
					if int(bol[2]) == 1:
						self.wndEquip.SetItemSlot(int(bol[26]), int(bol[1]), 0)
					else:
						self.wndEquip.SetItemSlot(int(bol[26]), int(bol[1]), int(bol[2]))
				
		if "depo_"+str(self.name)+"_para" in gameInfo.DUELLO_BILGILERI.keys():
			if str(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_para"]) != "[]":
				self.GetChild("Money_Rakip").SetText(str(locale.NumberToMoneyString(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_para"])))
			
	def OnUpdate(self):
		if app.GetTime() >= self.zaman + 2:
			self.Animage.Hide()
			self.GetChild("board").Show()
			self.duelloBilgiYENILE()
			if self.name == "":
				self.GetChild("TitleName").SetText("Ýtemine ws depon boþ.")
			self.zaman = 0
			
		if "PANEL" in gameInfo.DUELLO_BILGILERI.keys() and gameInfo.DUELLO_BILGILERI["PANEL"] == "2":
			self.Close()
			
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			self.Close()
			
		self.GetChild("My_Level").SetText("Lv. " + str(player.GetStatus(player.LEVEL)))
		self.GetChild("My_Name").SetText(str(player.GetName()))
		self.GetChild("My_Character_Image").LoadImage(FACE_IMAGE_DICT[net.GetMainActorRace()])
			
		if str(player.GetName())+"_info100" in gameInfo.DUELLO_BILGILERI.keys():
			if self.name != "":
				self.GetChild("TitleName").SetText(str(self.name) + " ile yaptýðýn itemine ws'de kazandýðýn son eþyalar (Round : " + str(gameInfo.DUELLO_BILGILERI["depo_"+str(self.name)+"_round"]) + " )")
			else:
				self.GetChild("TitleName").SetText("Ýtemine ws depon boþ.")
			self.GetChild("My_MacBilgileri_1").SetText("Toplam Maç: " + str(gameInfo.DUELLO_BILGILERI[str(player.GetName())+"_info100"].split("#")[1]))
			self.GetChild("My_MacBilgileri_2").SetText("G/M : " + str(gameInfo.DUELLO_BILGILERI[str(player.GetName())+"_info100"].split("#")[2])+"/"+str(gameInfo.DUELLO_BILGILERI[str(player.GetName())+"_info100"].split("#")[3]))
			self.GetChild("My_MacBilgileri_3").SetText("Kaçma : " + str(gameInfo.DUELLO_BILGILERI[str(player.GetName())+"_info100"].split("#")[4]))
			
		if "YENILE" in gameInfo.DUELLO_BILGILERI.keys() and gameInfo.DUELLO_BILGILERI["YENILE"] == "1":
			self.duelloBilgiYENILE()
			del gameInfo.DUELLO_BILGILERI["YENILE"]
				
		if "ISIM" in gameInfo.DUELLO_BILGILERI.keys():
			self.name = gameInfo.DUELLO_BILGILERI["ISIM"]
			del gameInfo.DUELLO_BILGILERI["ISIM"]
			
	def OnPressEscapeKey(self):
		if self.zaman == 0:
			self.Close()
			return TRUE	
		
class Duello_para_ayarlari(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.unitValue = 1
		self.maxValue = 0
		self.eventAccept = 0
		self.depo = 0
		self.depo_rakip_name = ""

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PickMoneyDialog.py")
		except:
			import exception
			exception.Abort("MoneyDialog.LoadDialog.LoadScript")

		try:
			self.board = self.GetChild("board")
			self.maxValueTextLine = self.GetChild("max_value")
			self.pickValueEditLine = self.GetChild("money_value")
			self.acceptButton = self.GetChild("accept_button")
			self.cancelButton = self.GetChild("cancel_button")
		except:
			import exception
			exception.Abort("MoneyDialog.LoadDialog.BindObject")

		self.pickValueEditLine.SetReturnEvent(ui.__mem_func__(self.OnAlisveris))
		self.pickValueEditLine.SetEscapeEvent(ui.__mem_func__(self.Close))
		self.acceptButton.SetEvent(ui.__mem_func__(self.OnAlisveris))
		self.cancelButton.SetEvent(ui.__mem_func__(self.Close))
		self.board.SetCloseEvent(ui.__mem_func__(self.Close))

	def Destroy(self):
		self.ClearDictionary()
		self.eventAccept = 0
		self.maxValue = 0
		self.pickValueEditLine = 0		
		self.acceptButton = 0
		self.cancelButton = 0
		self.board = None

	def SetTitleName(self, text):
		self.board.SetTitleName(text)

	def SetAcceptText(self, gelen):
		self.acceptButton.SetText(str(gelen))
		
	def SetAcceptEvent(self, event):
		self.eventAccept = event

	def SetMax(self, max):
		self.pickValueEditLine.SetMax(max)

	def Open(self, maxValue, unitValue=1, durum=0, name=""):

		if locale.IsYMIR() or locale.IsCHEONMA() or locale.IsHONGKONG():
			unitValue = ""
			
		if durum == 1:
			self.depo = 1
			
		if name != "":
			self.depo_rakip_name = name

		width = self.GetWidth()
		(mouseX, mouseY) = wndMgr.GetMousePosition()

		if mouseX + width/2 > wndMgr.GetScreenWidth():
			xPos = wndMgr.GetScreenWidth() - width
		elif mouseX - width/2 < 0:
			xPos = 0
		else:
			xPos = mouseX - width/2

		self.SetPosition(xPos, mouseY - self.GetHeight() - 20)

		if locale.IsARABIC():
			self.maxValueTextLine.SetText("/" + str(maxValue))
		else:
			self.maxValueTextLine.SetText(" / " + str(maxValue))
		
		if durum == 1:
			self.pickValueEditLine.SetText(str(maxValue))
		else:
			self.pickValueEditLine.SetText(str(unitValue))
		self.pickValueEditLine.SetFocus()

		ime.SetCursorPosition(1)

		self.unitValue = unitValue
		self.maxValue = maxValue
		self.Show()
		self.SetTop()

	def Close(self):
		self.pickValueEditLine.KillFocus()
		gameInfo.MONEY_INPUT = 0
		self.Hide()

	def OnAlisveris(self):
		global DUELLO_PARA_EKLENDI_BENIM
		text = self.pickValueEditLine.GetText()

		if len(text) > 0 and text.isdigit():

			money = int(text)
			money = min(money, self.maxValue)

			if money > 0:
				if self.eventAccept:
					self.eventAccept(money)

			if self.depo == 1:
				if int(text) > int(gameInfo.DUELLO_BILGILERI["depo_"+str(self.depo_rakip_name)+"_para"]):
					chat.AppendChat(chat.CHAT_TYPE_INFO, str(localegame.DUELLO_DEPO_YETERLI_PARA_YOK))
					return
					
				gameInfo.DUELLO_BILGILERI["depo_"+str(self.depo_rakip_name)+"_para"] = int(gameInfo.DUELLO_BILGILERI["depo_"+str(self.depo_rakip_name)+"_para"]) - int(text)
				gameInfo.DUELLO_BILGILERI["YENILE"] = "1"
				gameInfo.PYTHONISLEM = "duello_depo_paracek#"+str(text)
				event.QuestButtonClick(gameInfo.PYTHONTOLUA)
				self.Close()
				return
					
			if player.GetElk() < int(text):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localegame.DUELLO_PARA_YOK)
				return

			#net.SendWhisperPacket(gameInfo.DUELLO_RAKIP, "#xsbyfatihbab34sdajdsamdasdnsawnwqwusdadxasmdasdasxasbndadasnas#"+str(text)+"#")
			gameInfo.DUELLO_BENIM_PARA = int(text)
			DUELLO_PARA_EKLENDI_BENIM = 1
			gameInfo.PYTHONISLEM = "duello_para_ekle#"+str(text)+"#"+str(gameInfo.DUELLO_RAKIP)+"#"
			event.QuestButtonClick(gameInfo.PYTHONTOLUA)


		self.Close()

class Bug_Fatihbab34(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)
