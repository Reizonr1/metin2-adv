#<----------------------------------------------------------->#
#     _ +----------------------------------------------+ _    #
#    /o)|           Coded by VegaS              	   |(o\   #
#   / / |                                              | \ \  #
#  ( (_ |  _   Client War-Time - All Copryght     	_  | _) ) #
# ((\ \)+-/o)--------------------------------------(o\-+(/ /))#
#(\\\ \_/ /                                        \ \_/ ///) #
# \      /                                          \      /  #
#  \____/                                            \____/   #
#  - Coded by VegaS - Client  for War-Time  II 		 		  #
#  - Skype: 	   sacadatt.amazon						   	  #
#  - Phone:    0748576910 / 0764295843				     	  #
#  - Y!M: 	   contact_titan2@yahoo.com 			     	  #
#  - Y!M2: 	   dany.sem76@yahoo.com 			     	  	  #
#  - Author:    VegaS              		  	 		     	  #
#<----------------------------------------------------------->#
import ui
import net
import grp
import snd
import item
import chat
import player
import localeInfo
import constInfo
import uiToolTip
import mouseModule
import uiScriptLocale
import uiinventory

class AcceWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.xShopStart = 0
		self.yShopStart = 0
		self.slot_pos_index = 999
		self.slot_index1 = 999
		self.slot_index2 = 999
		self.isUsable = FALSE
		self.isLoaded = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		if self.isLoaded == 1:
			return
		
		self.isLoaded = 1
		
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/acce_combinewindow.py")
			
		except:
			import exception
			exception.Abort("AcceWindow.LoadDialog.LoadScript")
		
		try:
			GetObject=self.GetChild
			if localeInfo.IsARABIC():
				self.board = GetObject("board")
				self.board.SetScale(-1.0, 1.0)
				self.board.SetRenderingRect(-1.0, 0.0, 1.0, 0.0)
			
			self.titleBar = GetObject("TitleBar")
			self.btnAccept = GetObject("AcceptButton")
			self.btnCancel = GetObject("CancelButton")
			self.acceSlot = GetObject("AcceSlot")
			self.needMoney = GetObject("NeedMoney")
			self.Result = GetObject("Result")
		except:
			import exception
			exception.Abort("AcceWindow.LoadDialog.BindObject")
		
		self.acceSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
		self.acceSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.__OnSelectItemSlot))
		self.acceSlot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.acceSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.btnCancel.SetEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.btnAccept.SetEvent(ui.__mem_func__(self.__OnAcceptButtonClick))
		self.needMoney.SetText(localeInfo.ACCE_ABSORB_COST % (0))
		
		self.acceItemInfo = {}
		self.tooltipItem = None
		self.firstSlotIndex = 0
		self.SLOT_SIZEX	= 32
		self.SLOT_SIZEY	= 32

	def IsOpened(self):
		if self.isLoaded == 1:
			return TRUE
		
		return FALSE

	def SetItemToolTip(self, itemTooltip):
		self.tooltipItem = itemTooltip

	def Destroy(self):
		self.ClearDictionary()
		self.titleBar = None
		self.btnAccept = None
		self.btnCancel = None
		self.acceSlot = None
		self.tooltipItem = None
		self.needMoney = None
		self.Result = None
		self.slot_pos_index = None
		self.slot_index1 = None
		self.slot_index2 = None

	def Open(self):
		constInfo.ACCE_WINDOW = 1
		self.acceItemInfo = {}
		self.Refresh()
		self.Show()
		self.isUsable = TRUE
		(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()

		self.slot_index1 = 999
		self.slot_index2 = 999
		self.acceSlot.ClearSlot(0)
		self.acceSlot.ClearSlot(1)
		self.acceSlot.ClearSlot(2)
		self.needMoney.SetText(localeInfo.ACCE_ABSORB_COST % (0))

	def UpdateInfo(self, gold, itemVnum, count, rItemVnum, rCount):
		self.needMoney.Show()
		if self.needMoney:
			self.needMoney.SetText(localeInfo.ACCE_ABSORB_COST % (gold))
		
		self.acceSlot.SetItemSlot(2, rItemVnum, rCount)
		self.Refresh()

	def OnPressEscapeKey(self):
		self.__OnCloseButtonClick()
		return TRUE

	def Close(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
		
		self.Hide()
		self.aceeResultInfos = {}
		self.firstSlotIndex = 0
		if self.needMoney:
			self.needMoney.SetText("0")		

	def Clear(self):
		self.slot_index2 = 999
		self.acceSlot.ClearSlot(1)
		del self.acceItemInfo[1]
		constInfo.ACCE_WINDOW = 0
		self.needMoney.SetText(localeInfo.ACCE_ABSORB_COST % (0))

	def ClearSuccess(self):
		self.slot_pos_index = 999
		self.slot_index1 = 999
		self.slot_index2 = 999
		self.acceSlot.ClearSlot(0)
		self.acceSlot.ClearSlot(1)
		self.acceSlot.ClearSlot(2)
		del self.acceItemInfo[1]
		constInfo.ACCE_WINDOW = 0
		self.needMoney.SetText(localeInfo.ACCE_ABSORB_COST % (0))

	def Refresh(self):
		pass

	def __OnCloseButtonClick(self):
		if self.isUsable:
			self.isUsable = FALSE
			
			print "Acce close!"
			net.SendChatPacket("/acce close")
		
		self.Close()

	def __OnAcceptButtonClick(self):
		print "Acce make!"
		net.SendChatPacket("/acce make")

	def __OnSelectEmptySlot(self, selectedSlotPos):
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			mouseModule.mouseController.DeattachObject()
			if player.SLOT_TYPE_INVENTORY != attachedSlotType:
				return
			
			if constInfo.IS_ACCE_ITEM(player.GetItemIndex(attachedSlotPos), 0) == TRUE:
				if selectedSlotPos == 1 and self.slot_pos_index == 999:
					return
				
				if self.slot_index1 == attachedSlotPos and selectedSlotPos == 0 or self.slot_index2 == attachedSlotPos and selectedSlotPos == 1:
					return
				elif self.slot_index2 == attachedSlotPos and selectedSlotPos == 0 or self.slot_index1 == attachedSlotPos and selectedSlotPos == 1:
					return
				
				if selectedSlotPos == 0:
					self.slot_index1 = attachedSlotPos
				elif selectedSlotPos == 1:
					self.slot_index2 = attachedSlotPos
				
				for slotPos, invenPos in self.acceItemInfo.items():
					if invenPos == attachedSlotPos:
						del self.acceItemInfo[slotPos]
				
				self.acceItemInfo[selectedSlotPos] = attachedSlotPos
				self.slot_pos_index = attachedSlotPos
				self.acceSlot.ClearSlot(selectedSlotPos)
				self.acceSlot.SetItemSlot(selectedSlotPos, player.GetItemIndex(attachedSlotPos), player.GetItemCount(attachedSlotPos))
				net.SendChatPacket("/acce add %d %d" % (selectedSlotPos, attachedSlotPos))
			
			self.Refresh()

	def __OnSelectItemSlot(self, selectedSlotPos):
		if selectedSlotPos == 2:
			return
		
		snd.PlaySound("sound/ui/loginfail.wav")
		self.acceSlot.ClearSlot(selectedSlotPos)
		net.SendChatPacket("/acce del %d " % selectedSlotPos)
		if selectedSlotPos == 0:
			self.slot_pos_index = 999
			self.slot_index1 = 999
			self.acceSlot.ClearSlot(2)
		elif selectedSlotPos == 1:
			self.slot_index2 = 999
			self.acceSlot.ClearSlot(2)
		
		if not selectedSlotPos in self.acceItemInfo:
			return
		
		del self.acceItemInfo[selectedSlotPos]
		
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			if constInfo.IS_ACCE_ITEM(player.GetItemIndex(attachedSlotPos), 0) == TRUE:
				if selectedSlotPos == 2:
					return
				
				if selectedSlotPos == 0:
					self.slot_pos_index = attachedSlotPos
				
				if self.slot_index1 == attachedSlotPos and selectedSlotPos == 0 or self.slot_index2 == attachedSlotPos and selectedSlotPos == 1:
					return
				elif self.slot_index2 == attachedSlotPos and selectedSlotPos == 0 or self.slot_index1 == attachedSlotPos and selectedSlotPos == 1:
					return
				
				if selectedSlotPos == 0:
					self.slot_index1 = attachedSlotPos
				elif selectedSlotPos == 1:
					self.slot_index2 = attachedSlotPos
				
				for slotPos, invenPos in self.acceItemInfo.items():
					if invenPos == attachedSlotPos:
						del self.acceItemInfo[slotPos]
				
				self.acceItemInfo[selectedSlotPos] = attachedSlotPos
				self.acceSlot.ClearSlot(selectedSlotPos)
				self.acceSlot.SetItemSlot(selectedSlotPos, player.GetItemIndex(attachedSlotPos), player.GetItemCount(attachedSlotPos))
				net.SendChatPacket("/acce add %d %d" % (selectedSlotPos, attachedSlotPos))
			
			mouseModule.mouseController.DeattachObject()
		
		self.Refresh()

	def __OnOverInItem(self, slotIndex):
		if slotIndex == 2:
			if self.slot_index1 != 999:
				itemVnum = player.GetItemIndex(self.slot_index1)
				self.tooltipItem.SetItemToolTip(itemVnum+1)
			
			return
		
		if self.tooltipItem:
			if self.acceItemInfo.has_key(slotIndex):
				self.tooltipItem.SetInventoryItem(self.acceItemInfo[slotIndex])

	def __OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnUpdate(self):
		USE_SHOP_LIMIT_RANGE = 1000
		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xShopStart) > USE_SHOP_LIMIT_RANGE or abs(y - self.yShopStart) > USE_SHOP_LIMIT_RANGE:
			self.__OnCloseButtonClick()

class AcceAbsorbWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.xShopStart = 0
		self.yShopStart = 0
		self.slot_pos_index = 999
		self.slot_index1 = 999
		self.slot_index2 = 999
		self.isUsable = FALSE
		self.isLoaded = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		if self.isLoaded == 1:
			return
		
		self.isLoaded = 1
		
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/acce_absorbwindow.py")
			
		except:
			import exception
			exception.Abort("AcceWindow.LoadDialog.LoadScript")
		
		try:
			GetObject=self.GetChild
			if localeInfo.IsARABIC():
				self.board = GetObject("board")
				self.board.SetScale(-1.0, 1.0)
				self.board.SetRenderingRect(-1.0, 0.0, 1.0, 0.0)
			
			self.titleBar = GetObject("TitleBar")
			self.btnAccept = GetObject("AcceptButton")
			self.btnCancel = GetObject("CancelButton")
			self.acceSlot = GetObject("AcceSlot")
		except:
			import exception
			exception.Abort("AcceWindow.LoadDialog.BindObject")
		
		self.acceSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
		self.acceSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.__OnSelectItemSlot))
		self.acceSlot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.acceSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.btnCancel.SetEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.btnAccept.SetEvent(ui.__mem_func__(self.__OnAcceptButtonClick))
		
		self.acceItemInfo = {}
		self.tooltipItem = None
		self.firstSlotIndex = 0
		self.SLOT_SIZEX	= 32
		self.SLOT_SIZEY	= 32

	def IsOpened(self):
		if self.isLoaded == 1:
			return TRUE
		
		return FALSE

	def SetItemToolTip(self, itemTooltip):
		self.tooltipItem = itemTooltip

	def Destroy(self):
		self.ClearDictionary()
		self.titleBar = None
		self.btnAccept = None
		self.btnCancel = None
		self.acceSlot = None
		self.tooltipItem = None
		self.slot_pos_index = None
		self.slot_index1 = None
		self.slot_index2 = None

	def Open(self):
		constInfo.ACCE_WINDOW = 1
		self.acceItemInfo = {}
		self.Refresh()
		self.Show()
		self.isUsable = TRUE
		(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()

		self.slot_index1 = 999
		self.slot_index2 = 999
		self.acceSlot.ClearSlot(0)
		self.acceSlot.ClearSlot(1)
		self.acceSlot.ClearSlot(2)

	def UpdateInfo(self, gold, itemVnum, count, rItemVnum, rCount):
		self.acceSlot.SetItemSlot(2, rItemVnum, rCount)
		self.Refresh()

	def OnPressEscapeKey(self):
		self.__OnCloseButtonClick()
		return TRUE

	def Close(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
		
		self.Hide()
		self.aceeResultInfos = {}
		self.firstSlotIndex = 0

	def Clear(self):
		net.SendChatPacket("/acce del %d " % 0)
		self.slot_pos_index = 999
		self.slot_index1 = 999
		self.slot_index2 = 999
		self.acceSlot.ClearSlot(0)
		self.acceSlot.ClearSlot(1)
		self.acceSlot.ClearSlot(2)
		del self.acceItemInfo[1]
		constInfo.ACCE_WINDOW = 0

	def Refresh(self):
		pass

	def __OnCloseButtonClick(self):
		if self.isUsable:
			self.isUsable = FALSE
			
			print "Acce close!"
			net.SendChatPacket("/acce close")
		
		self.Close()

	def __OnAcceptButtonClick(self):
		print "Acce absorption!"
		net.SendChatPacket("/acce absorption")

	def __OnSelectEmptySlot(self, selectedSlotPos):
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			mouseModule.mouseController.DeattachObject()
			if player.SLOT_TYPE_INVENTORY != attachedSlotType:
				return
			
			item.SelectItem(player.GetItemIndex(attachedSlotPos))
			if constInfo.IS_ACCE_ITEM(player.GetItemIndex(attachedSlotPos), 1) == TRUE and selectedSlotPos == 0 or item.GetItemSubType() == item.ARMOR_BODY and selectedSlotPos == 1 or item.GetItemType() == item.ITEM_TYPE_WEAPON and selectedSlotPos == 1:
				if selectedSlotPos == 1 and self.slot_pos_index == 999:
					return
				
				if self.slot_index1 == attachedSlotPos and selectedSlotPos == 0 or self.slot_index2 == attachedSlotPos and selectedSlotPos == 1:
					return
				elif self.slot_index2 == attachedSlotPos and selectedSlotPos == 0 or self.slot_index1 == attachedSlotPos and selectedSlotPos == 1:
					return
				
				if selectedSlotPos == 0:
					self.slot_index1 = attachedSlotPos
				elif selectedSlotPos == 1:
					self.slot_index2 = attachedSlotPos
				
				for slotPos, invenPos in self.acceItemInfo.items():
					if invenPos == attachedSlotPos:
						del self.acceItemInfo[slotPos]
				
				self.acceItemInfo[selectedSlotPos] = attachedSlotPos
				self.slot_pos_index = attachedSlotPos
				self.acceSlot.ClearSlot(selectedSlotPos)
				self.acceSlot.SetItemSlot(selectedSlotPos, player.GetItemIndex(attachedSlotPos), player.GetItemCount(attachedSlotPos))
				net.SendChatPacket("/acce add %d %d" % (selectedSlotPos, attachedSlotPos))
				if selectedSlotPos == 1:
					self.acceSlot.SetItemSlot(2, player.GetItemIndex(self.slot_index1), player.GetItemCount(self.slot_index1))
			
			self.Refresh()

	def __OnSelectItemSlot(self, selectedSlotPos):
		if selectedSlotPos == 2:
			return
		
		snd.PlaySound("sound/ui/loginfail.wav")
		self.acceSlot.ClearSlot(selectedSlotPos)
		net.SendChatPacket("/acce del %d " % selectedSlotPos)
		if selectedSlotPos == 0:
			self.slot_pos_index = 999
			self.slot_index1 = 999
			self.acceSlot.ClearSlot(1)
			net.SendChatPacket("/acce del %d " % 1)
			self.slot_index2 = 999
			self.acceSlot.ClearSlot(2)
		elif selectedSlotPos == 1:
			self.slot_index1 = 999
			self.acceSlot.ClearSlot(0)
			self.slot_index2 = 999
			self.acceSlot.ClearSlot(2)
			net.SendChatPacket("/acce del %d " % 0)
		
		if not selectedSlotPos in self.acceItemInfo:
			return
		
		del self.acceItemInfo[selectedSlotPos]
		
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			if constInfo.IS_ACCE_ITEM(player.GetItemIndex(attachedSlotPos), 1) == TRUE:
				if selectedSlotPos == 2:
					return
				
				if selectedSlotPos == 0:
					self.slot_pos_index = attachedSlotPos
				
				if self.slot_index1 == attachedSlotPos and selectedSlotPos == 0 or self.slot_index2 == attachedSlotPos and selectedSlotPos == 1:
					return
				elif self.slot_index2 == attachedSlotPos and selectedSlotPos == 0 or self.slot_index1 == attachedSlotPos and selectedSlotPos == 1:
					return
				
				if selectedSlotPos == 0:
					self.slot_index1 = attachedSlotPos
				elif selectedSlotPos == 1:
					self.slot_index2 = attachedSlotPos
				
				for slotPos, invenPos in self.acceItemInfo.items():
					if invenPos == attachedSlotPos:
						del self.acceItemInfo[slotPos]
				
				self.acceItemInfo[selectedSlotPos] = attachedSlotPos
				self.acceSlot.ClearSlot(selectedSlotPos)
				self.acceSlot.SetItemSlot(selectedSlotPos, player.GetItemIndex(attachedSlotPos), player.GetItemCount(attachedSlotPos))
				net.SendChatPacket("/acce add %d %d" % (selectedSlotPos, attachedSlotPos))
				if selectedSlotPos == 1:
					self.acceSlot.SetItemSlot(2, player.GetItemIndex(self.slot_index1), player.GetItemCount(self.slot_index1))
			
			mouseModule.mouseController.DeattachObject()
		
		self.Refresh()

	def __OnOverInItem(self, slotIndex):
		if slotIndex == 2:
			if self.slot_index1 != 999:
				abs_chance = 0
				itemVnum = player.GetItemIndex(self.slot_index1)
				self.tooltipItem.SetItemToolTip(itemVnum)
				self.tooltipItem.SetInventoryItem(self.acceItemInfo[0])
				
				item.SelectItem(player.GetItemIndex(self.slot_index1))
				metinSlot = []
				for i in xrange(player.METIN_SOCKET_MAX_NUM):
					metinSlot.append(player.GetItemMetinSocket(self.slot_index1, i))
				
				abs_chance = int(metinSlot[1])
				
				item.SelectItem(player.GetItemIndex(self.slot_index2))
				itemType = item.GetItemType()
				if item.ITEM_TYPE_WEAPON == itemType:
					a = int(item.GetValue(3) * abs_chance / 100)
					b = int(item.GetValue(4) * abs_chance / 100)
					c = int(item.GetValue(5) * abs_chance / 100)
					d = int(item.GetValue(1) * abs_chance / 100)
					e = int(item.GetValue(2) * abs_chance / 100)
					
					min_power = a + c
					max_power = b + c
					min_magic_power = d + c
					max_magic_power = e + c
					if b > a:
						if a > 0 or b > 0:
							self.tooltipItem.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_POWER % (max_power - min_power, max_power), self.tooltipItem.POSITIVE_COLOR)
					else:
						if a > 0:
							self.tooltipItem.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_POWER_ONE_ARG % (min_power), self.tooltipItem.POSITIVE_COLOR)
					
					if e > d:
						if e > 0 or d > 0:
							self.tooltipItem.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_ATT_POWER % (max_magic_power - min_magic_power, max_magic_power), self.tooltipItem.POSITIVE_COLOR)
					else:
						if e > 0:
							self.tooltipItem.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_ATT_POWER_ONE_ARG % (min_magic_power), self.tooltipItem.POSITIVE_COLOR)
				elif item.ITEM_TYPE_ARMOR == itemType:
					defGradeCalc = item.GetValue(5) * 2 + item.GetValue(1) * abs_chance / 100
					defGrade = defGradeCalc * abs_chance / 100
					if defGrade > 0:
						self.tooltipItem.AppendTextLine(localeInfo.TOOLTIP_ITEM_DEF_GRADE % (defGrade), self.GetChangeTextLineColor(defGrade))
				
				for g in xrange(item.ITEM_APPLY_MAX_NUM):
					item.SelectItem(player.GetItemIndex(self.slot_index2))
					(affectType, affectValue) = item.GetAffect(g)
					affectValue = affectValue * abs_chance / 100
					if affectValue <= 0:
						if affectType != 0:
							affectValue = 1
						else:
							affectValue = 0
					
					affectString = self.GetAffectString(affectType, affectValue)
					if affectString:
						affectColor = self.GetChangeTextLineColor(affectValue)
						self.tooltipItem.AppendTextLine(affectString, affectColor)
				
				attrSlot = []
				for w in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
					attrSlot.append(player.GetItemAttribute(self.slot_index2, w))
				
				if 0 != attrSlot:
					for q in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
						if q >= 7:
							continue
						else:
							type = attrSlot[q][0]
							value = attrSlot[q][1]
							if 0 == value:
								continue
							
							value = value * abs_chance / 100
							
							if value <= 0:
								if type != 0:
									value = 1
								else:
									value = 0
							
							affectString = self.GetAffectString(type, value)
							if affectString:
								affectColor = self.GetAttributeColor(q, value)
								self.tooltipItem.AppendTextLine(affectString, affectColor)
			return
		
		if self.tooltipItem:
			if self.acceItemInfo.has_key(slotIndex):
				self.tooltipItem.SetInventoryItem(self.acceItemInfo[slotIndex])

	def __OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnUpdate(self):
		USE_SHOP_LIMIT_RANGE = 1000
		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xShopStart) > USE_SHOP_LIMIT_RANGE or abs(y - self.yShopStart) > USE_SHOP_LIMIT_RANGE:
			self.__OnCloseButtonClick()

	def GetAffectString(self, affectType, affectValue):
		if 0 == affectType:
			return None

		if 0 == affectValue:
			return None

		try:
			return self.tooltipItem.AFFECT_DICT[affectType](affectValue)
		except TypeError:
			return "UNKNOWN_VALUE[%s] %s" % (affectType, affectValue)
		except KeyError:
			return "UNKNOWN_TYPE[%s] %s" % (affectType, affectValue)

	def GetAttributeColor(self, index, value):
		if value > 0:
			if index >= 5 and index <= 6:
				return self.tooltipItem.SPECIAL_POSITIVE_COLOR2
			elif index >= 7:
				return self.tooltipItem.POSITIVE_COLOR
			else:
				return self.tooltipItem.SPECIAL_POSITIVE_COLOR
		elif value == 0:
			return self.tooltipItem.NORMAL_COLOR
		else:
			return self.tooltipItem.NEGATIVE_COLOR

	def GetChangeTextLineColor(self, value, isSpecial=FALSE):
		if value > 0:
			if isSpecial:
				return self.tooltipItem.SPECIAL_POSITIVE_COLOR
			else:
				return self.tooltipItem.POSITIVE_COLOR
		
		if 0 == value:
			return self.tooltipItem.NORMAL_COLOR
		
		return self.tooltipItem.NEGATIVE_COLOR

if __name__ == "__main__":
	import app
	import wndMgr
	import systemSetting
	import mouseModule
	import grp
	import ui
	import uiToolTip
	import locale
	
	app.SetMouseHandler(mouseModule.mouseController)
	app.SetHairColorEnable(TRUE)
	wndMgr.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetScreenSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	app.Create(localeInfo.APP_TITLE, systemSetting.GetWidth(), systemSetting.GetHeight(), 1)
	mouseModule.mouseController.Create()
	
	class TestGame(ui.Window):
		def __init__(self):
			ui.Window.__init__(self)
			
			localeInfo.LoadLocaleData()
			
			self.tooltipItem = uiToolTip.ItemToolTip()
			self.tooltipItem.Hide()
			
			self.acceWindow = acceWindow()
			self.acceWindow.LoadWindow()
			self.acceWindow.SetItemToolTip(self.tooltipItem)
			self.acceWindow.Open()

		def __del__(self):
			ui.Window.__del__(self)

		def OnUpdate(self):
			app.UpdateGame()

		def OnRender(self):
			app.RenderGame()
			grp.PopState()
			grp.SetInterfaceRenderState()
	
	game = TestGame()
	game.SetSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	game.Show()
	
	app.Loop()

