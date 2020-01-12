import ui
import os
import player
import net
import app
import chat
import snd
import item
import event
import localeInfo
import localegame
import time
import math
import gameInfo
import uiToolTip
import uiCommon
import musicInfo
import mouseModule
import uiPickMoney
import systemSetting
import playerSettingModule

YOL = str(gameInfo.CONFIG_YOL)+"yarisma/"

RANDOM = [1,100]

ItemSlot_Benim = []
ItemSlot_Benim2 = []
ItemSlot_R_Ekle = ""
ItemSlot = []
ItemEkle_DURUM = 0
Item_Slot_Eklenen = 0

class DiceSystem(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()
		self.time=0;self.timeOPEN=0;self.timeNUMBER=RANDOM[0];self.timeKONTROL=[];self.timeKONTROLTEXT={}
		self.ItemSlotList = {};self.ItemSlotList_Ekipman = {};self.ItemSlotList_R = {};self.ItemSlotList_R_Ekipman = {}
		self.ItemSlotList_R_I = {};self.ItemSlotList_R_I_Ekipman = {};self.ItemSlot = [];self.ItemSlot_Ekipman = []
		self.xStart = 0
		self.yStart = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self, isim):
		self.baslangicISLERI()
		gameInfo.DICE_SYSTEM["OYUN_RAKIP"] = str(isim)
		self.__LoadWindow()
		self.SetCenterPosition()
		ui.ScriptWindow.Show(self)

	def Close(self, gelen=0):
		if gelen==0:
			if "KABUL_RAKIP" in gameInfo.DICE_SYSTEM.keys() or "KABUL_SEN" in gameInfo.DICE_SYSTEM.keys():
				chat.AppendChat(chat.CHAT_TYPE_INFO, str(localegame.DICE_SYSTEM_CIKAMAZSIN))
				return
				
			gameInfo.sendPacket("bahis_kapat#")
			return
		
		self.baslangicISLERI()
		
		snd.PlaySound("sound/ui/click.wav")
		self.Hide()

	def baslangicISLERI(self):
		global ItemSlot, ItemSlot_Benim, ItemSlot_Benim2, Item_Slot_Eklenen
		gameInfo.DICE_SYSTEM = {}
		ItemSlot=[];ItemSlot_Benim = [];ItemSlot_Benim2=[];Item_Slot_Eklenen=0
		self.ItemSlotList = {};self.ItemSlotList_Ekipman = {};self.ItemSlotList_R = {};self.ItemSlotList_R_Ekipman = {}
		self.ItemSlotList_R_I = {};self.ItemSlotList_R_I_Ekipman = {};self.ItemSlot = [];self.ItemSlot_Ekipman = []
		
	def __LoadWindow(self):
		try:			
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/dicesystem.py")
			
			self.wndSlot = self.GetChild("Owner_Slot") ## Benim 6x6 ~ 36 Tane Item Slot Ekranım ##
			self.wndSlot_R = self.GetChild("Target_Slot") ## Rakibin 6x6 ~ 36 Tane Item Slot Ekranı ##
			
			self.TitleName = self.GetChild("TitleName")
			self.GetChild("TitleBar").SetCloseEvent(self.Close)
			self.OwnerAcceptLight = self.GetChild("Owner_Accept_Light")
			self.TargetAcceptLight = self.GetChild("Target_Accept_Light")
			self.OwnerAcceptLight.Disable()
			self.TargetAcceptLight.Disable()
			
			self.GetChild("Owner_Number_Text").SetFontName("Tahoma:22")
			self.GetChild("Target_Number_Text").SetFontName("Tahoma:22")
			
			self.GetChild("Owner_Number_Text").SetText("-")
			self.GetChild("Target_Number_Text").SetText("-")
			
			#gameInfo.DICE_SYSTEM["CALISTIR"] = 1
			#gameInfo.DICE_SYSTEM["RANDOM"] = [benimRANDOM, rakipRANDOM]
			#self.time=app.GetTime()+0.3;self.timeOPEN=1
			
			self.wndSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
			self.wndSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			self.wndSlot.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))			
			self.wndSlot_R.SetOverInItemEvent(ui.__mem_func__(self.OverInItem_R))
			self.wndSlot_R.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
			
			## Button
			
			self.Owner_Accept_Button = self.GetChild("Owner_Accept_Button")
			self.Target_Accept_Button = self.GetChild("Target_Accept_Button")
			self.Owner_Accept_Button.SetToggleDownEvent(ui.__mem_func__(self.bahisKABUL))
			
			self.Target_Accept_Button.Disable()
			
			chat.AppendChat(chat.CHAT_TYPE_INFO, str(localegame.DICE_SYSTEM_ACILDI))
			
			(self.xStart, self.yStart, z) = player.GetMainCharacterPosition()
			
		except:
			import exception
			exception.Abort("DiceSystem.LoadWindow.LoadObject")
			
	def bahisKABUL(self):
		gameInfo.sendPacket("bahis_kabul#")
			
	def SelectEmptySlot(self, selectedSlotPos):
		global ItemSlot, Item_Slot_Eklenen
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			if player.IsEquipmentSlot(attachedSlotPos):
				return

			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				if attachedSlotPos in self.ItemSlot:
					mouseModule.mouseController.DeattachObject()
				else:
				
					if "KABUL_RAKIP" in gameInfo.DICE_SYSTEM.keys() or "KABUL_SEN" in gameInfo.DICE_SYSTEM.keys():
						chat.AppendChat(chat.CHAT_TYPE_INFO, str(localegame.DICE_SYSTEM_ITEMKOYAMAZSIN))
						mouseModule.mouseController.DeattachObject()
						return
				
					itemVnum2 = player.GetItemIndex(attachedSlotPos) 
					itemCount = player.GetItemCount(attachedSlotPos) 
					item.SelectItem(itemVnum2)
					itemName = item.GetItemName()
					
					if item.IsAntiFlag(item.ANTIFLAG_GIVE):
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE)
						mouseModule.mouseController.DeattachObject()
						return
						
					if not "OYUN_RAKIP" in gameInfo.DICE_SYSTEM.keys():
						mouseModule.mouseController.DeattachObject()
						return
				
					if int(player.GetItemCount(int(attachedSlotPos))) == 1:
						self.wndSlot.SetItemSlot(int(selectedSlotPos), int(player.GetItemIndex(int(attachedSlotPos))), 0)
					else:
						self.wndSlot.SetItemSlot(int(selectedSlotPos), int(player.GetItemIndex(int(attachedSlotPos))), int(player.GetItemCount(int(attachedSlotPos))))
					self.ItemSlotList["slot"+str(selectedSlotPos)] = attachedSlotPos
					self.ItemSlot.append(attachedSlotPos)
					ItemSlot.append(attachedSlotPos)
					
					Item_Slot_Eklenen = str(attachedSlotPos)+"#"+str(gameInfo.DICE_SYSTEM["OYUN_RAKIP"])+"#"+str(selectedSlotPos)
					gameInfo.sendPacket("bahis_itemekle_slot#"+str(attachedSlotPos)+"#"+str(gameInfo.DICE_SYSTEM["OYUN_RAKIP"])+"#"+str(selectedSlotPos))

					## Itemi koyduğu zaman rakibe koyduğu itemi belirtme ##
					slotIndex = attachedSlotPos

					itemVnum = player.GetItemIndex(slotIndex)
					itemCount = player.GetItemCount(slotIndex)
					
					metin = ""
					attr = ""

					metinSlot = [player.GetItemMetinSocket(slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
					attrSlot = [player.GetItemAttribute(slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

		mouseModule.mouseController.DeattachObject()

	def OverInItem(self, slotNumber):
		self.tooltipItem.ClearToolTip()
		if "slot"+str(slotNumber) in self.ItemSlotList.keys():
			slotIndex = self.ItemSlotList["slot"+str(slotNumber)]
			
			itemVnum = player.GetItemIndex(slotIndex)
			itemCount = player.GetItemCount(slotIndex)
			
			metinSlot = [player.GetItemMetinSocket(slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			attrSlot = [player.GetItemAttribute(slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

			self.tooltipItem.AddRefineItemData(itemVnum, metinSlot, attrSlot)

	def OverInItem_R(self, slotNumber):
		self.tooltipItem.ClearToolTip()
		if "slot"+str(slotNumber) in self.ItemSlotList_R.keys():
			slotIndex = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")
			
			itemVnum = player.GetItemIndex(int(slotIndex[1]))
			itemCount = player.GetItemCount(int(slotIndex[2]))

			items = self.ItemSlotList_R_I["slot"+str(slotNumber)].split("#")

			metinAttr = [int(items[4]),int(items[5]),int(items[6]),int(items[7]),int(items[8]),int(items[9])]
			slotAttr =  [(int(items[10]),int(items[11])),(int(items[12]),int(items[13])),(int(items[14]),int(items[15])),(int(items[16]),int(items[17])),(int(items[18]),int(items[19])),(int(items[20]),int(items[21])),(int(items[22]),int(items[23]))]
	
			self.tooltipItem.AddRefineItemData(int(slotIndex[1]), metinAttr, slotAttr)
			
	def OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
			
	def PopupMessage(self,gelen):
		self.popupDialog = uiCommon.PopupDialog()
		self.popupDialog.SetText(str(gelen))
		self.popupDialog.Open()
			
	def OnUpdate(self):
		global ItemEkle_DURUM, ItemSlot_R_Ekle
		if "CALISTIR" in gameInfo.DICE_SYSTEM.keys() and "RANDOM" in gameInfo.DICE_SYSTEM.keys():
			if gameInfo.DICE_SYSTEM["TIME_OPEN"] == 1 and app.GetTime()>gameInfo.DICE_SYSTEM["TIME"]:
				 
				if self.timeNUMBER==gameInfo.DICE_SYSTEM["RANDOM"][0]:self.GetChild("Owner_Number_Text").SetText(str(gameInfo.DICE_SYSTEM["RANDOM"][0]));self.timeKONTROL.append(1);self.timeKONTROLTEXT["BENIM"]=1
				if self.timeNUMBER==gameInfo.DICE_SYSTEM["RANDOM"][1]:self.GetChild("Target_Number_Text").SetText(str(gameInfo.DICE_SYSTEM["RANDOM"][1]));self.timeKONTROL.append(1);self.timeKONTROLTEXT["RAKIP"]=1
				
				if len(self.timeKONTROL)>1:
					if gameInfo.DICE_SYSTEM["RANDOM"][0]>gameInfo.DICE_SYSTEM["RANDOM"][1]: self.PopupMessage(str(localegame.DICE_SYSTEM_KAZANDIN) % (str(gameInfo.DICE_SYSTEM["RANDOM"][0]), str(gameInfo.DICE_SYSTEM["RANDOM"][1])))
					else: self.PopupMessage(str(localegame.DICE_SYSTEM_KAYBETTIN) % (str(gameInfo.DICE_SYSTEM["RANDOM"][0]), str(gameInfo.DICE_SYSTEM["RANDOM"][1])))
					del gameInfo.DICE_SYSTEM["CALISTIR"];gameInfo.DICE_SYSTEM["TIME_OPEN"]=2;gameInfo.DICE_SYSTEM["TIME"]=app.GetTime()+1.0;self.timeNUMBER=RANDOM[0]
				
				if len(self.timeKONTROL)<=1:
					if not "BENIM" in self.timeKONTROLTEXT.keys(): self.GetChild("Owner_Number_Text").SetText(str(self.timeNUMBER))
					if not "RAKIP" in self.timeKONTROLTEXT.keys(): self.GetChild("Target_Number_Text").SetText(str(self.timeNUMBER))
					self.timeNUMBER+=1
					if self.timeNUMBER == RANDOM[1]:self.timeNUMBER=RANDOM[0]

		if "TIME_OPEN" in gameInfo.DICE_SYSTEM.keys() and "TIME" in gameInfo.DICE_SYSTEM.keys():
			if gameInfo.DICE_SYSTEM["TIME_OPEN"] == 2 and app.GetTime() > gameInfo.DICE_SYSTEM["TIME"]:
				del gameInfo.DICE_SYSTEM["TIME_OPEN"]; del gameInfo.DICE_SYSTEM["TIME"]
				self.Close(1)
		
		if "OYUN_RAKIP" in gameInfo.DICE_SYSTEM.keys(): self.TitleName.SetText(str(localegame.DICE_SYSTEM_TITLE) % (gameInfo.DICE_SYSTEM["OYUN_RAKIP"]))
		if "KAPAT" in gameInfo.DICE_SYSTEM.keys(): self.Close(1)
		if "KABUL_RAKIP" in gameInfo.DICE_SYSTEM.keys(): self.TargetAcceptLight.Down(); self.Target_Accept_Button.Down()
		if "KABUL_SEN" in gameInfo.DICE_SYSTEM.keys(): self.OwnerAcceptLight.Down(); self.Owner_Accept_Button.Down()
			
		if ItemEkle_DURUM == 1:
			bol = ItemSlot_R_Ekle.split("#")
			self.ItemSlotList_R["slot"+str(bol[26])] = int(bol[3])
			self.ItemSlotList_R_I["slot"+str(bol[26])] = ItemSlot_R_Ekle
			if int(bol[2]) == 1:
				self.wndSlot_R.SetItemSlot(int(bol[26]), int(bol[1]), 0)
			else:
				self.wndSlot_R.SetItemSlot(int(bol[26]), int(bol[1]), int(bol[2]))
			item.SelectItem(int(bol[1]))
			itemName = item.GetItemName()
			itemAdet = int(bol[2])
			ItemEkle_DURUM = 0
		
class Bug_Fatihbab34(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)
