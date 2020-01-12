import net
import grp
import snd
import item
import chat
import player
import localeInfo
import mouseModule

import ui
import uiToolTip
import uiScriptLocale
import uiinventory

## If your system can transfer the bonuses from others costumes subtypes set ATTR_TRANSFER_LIMIT to 1 ##
ATTR_TRANSFER_LIMIT = 0
########################################################################################################

class TransferWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isUsable = FALSE
		self.isLoaded = 0
		self.xShopStart = 0
		self.yShopStart = 0
		self.def_mediumSlot = 999
		self.def_combSlot_1 = 999
		self.def_combSlot_2 = 999

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		if self.isLoaded == 1:
			return
		
		self.isLoaded = 1
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/itemcombinationwindow.py")
		except:
			import exception
			exception.Abort("AcceWindow.LoadDialog.LoadScript")
		
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("TitleBar")
			self.btnAccept = GetObject("AcceptButton")
			self.btnCancel = GetObject("CancelButton")
			self.mediumSlot = GetObject("MediumSlot")
			self.combSlot = GetObject("CombSlot")
		except:
			import exception
			exception.Abort("AcceWindow.LoadDialog.BindObject")
		
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.btnCancel.SetEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.btnAccept.SetEvent(ui.__mem_func__(self.__OnAcceptButtonClick))
		self.combSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
		self.combSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.__OnSelectItemSlot))
		self.combSlot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.combSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		self.mediumSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
		self.mediumSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.__OnSelectItemSlot))
		self.mediumSlot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.mediumSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		
		self.tooltipItem = None
		self.SLOT_SIZEX	= 32
		self.SLOT_SIZEY	= 32
		self.itemInfo = {}

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
		self.combSlot = None
		self.mediumSlot = None
		self.tooltipItem = None
		self.def_mediumSlot = None
		self.def_combSlot_1 = None
		self.def_combSlot_2 = None

	def Open(self):
		self.Refresh()
		self.Show()
		self.isUsable = TRUE
		(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()
		for i in xrange(4):
			self.combSlot.ClearSlot(i)
		
		self.mediumSlot.ClearSlot(0)
		self.def_mediumSlot = 999
		self.def_combSlot_1 = 999
		self.def_combSlot_2 = 999
		self.itemInfo = {}

	def OnPressEscapeKey(self):
		self.__OnCloseButtonClick()
		return TRUE

	def Close(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
		
		self.Hide()	

	def Clear(self):
		for i in xrange(4):
			if i > 0:
				self.combSlot.ClearSlot(i)
				net.SendChatPacket("/attrtransfer del %d" % (i))
		
		self.def_combSlot_1 = 999
		self.def_combSlot_2 = 999

	def Refresh(self):
		pass

	def Success(self):
		self.mediumSlot.ClearSlot(0)
		self.def_mediumSlot = 999
		self.Clear()

	def __OnCloseButtonClick(self):
		if self.isUsable:
			self.isUsable = FALSE
			
			print "Bonus Transer closed!"
			net.SendChatPacket("/attrtransfer close")
		
		self.Close()

	def __OnAcceptButtonClick(self):
		print "Bonus Transer make!"
		net.SendChatPacket("/attrtransfer make")

	def __OnSelectEmptySlot(self, selectedSlotPos):
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			targetIndex = player.GetItemIndex(attachedSlotPos)
			if attachedSlotType != player.SLOT_TYPE_INVENTORY:
				return
			
			if selectedSlotPos == 0:
				item.SelectItem(targetIndex)
				if item.GetItemType() == item.ITEM_TYPE_TRANSFER_SCROLL:
					if self.def_mediumSlot != 999:
						self.mediumSlot.ClearSlot(0)
						self.def_mediumSlot = 999
					
					self.mediumSlot.SetItemSlot(0, player.GetItemIndex(attachedSlotPos), player.GetItemCount(attachedSlotPos))
					net.SendChatPacket("/attrtransfer add %d %d" % (0, attachedSlotPos))
					self.def_mediumSlot = selectedSlotPos
					
					for slotPos, invenPos in self.itemInfo.items():
						if invenPos == attachedSlotPos:
							del self.itemInfo[slotPos]
					
					self.itemInfo[selectedSlotPos] = attachedSlotPos
				
				mouseModule.mouseController.DeattachObject()
			else:
				mouseModule.mouseController.DeattachObject()
				if self.def_mediumSlot == 999:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.COMB_ALERT1)
					return
				
				if self.def_combSlot_1 == 999 and selectedSlotPos == 2:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.COMB_ALERT2)
					return
				
				item.SelectItem(targetIndex)
				itemType = item.GetItemType()
				itemSubType = item.GetItemSubType()
				if itemType != item.ITEM_TYPE_COSTUME:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.COMB_ALERT3)
					return
				
				if ATTR_TRANSFER_LIMIT == 1:
					if not itemSubType in (item.COSTUME_TYPE_BODY, item.COSTUME_TYPE_HAIR, item.COSTUME_TYPE_ACCE):
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.COMB_ALERT4)
						return
				else:
					if itemSubType != item.COSTUME_TYPE_BODY:
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.COMB_ALERT5)
						return
				
				if ATTR_TRANSFER_LIMIT == 1 and selectedSlotPos == 2:
					item.SelectItem(player.GetItemIndex(self.def_combSlot_1))
					Costume_1_SubType = item.GetItemSubType()
					if Costume_1_SubType != itemSubType:
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.COMB_ALERT6)
						return
				
				self.combSlot.SetItemSlot(selectedSlotPos, player.GetItemIndex(attachedSlotPos), player.GetItemCount(attachedSlotPos))
				net.SendChatPacket("/attrtransfer add %d %d" % (selectedSlotPos, attachedSlotPos))
				if selectedSlotPos == 1:
					self.def_combSlot_1 = attachedSlotPos
				elif selectedSlotPos == 2:
					self.def_combSlot_2 = attachedSlotPos
				
				for slotPos, invenPos in self.itemInfo.items():
					if invenPos == attachedSlotPos:
						del self.itemInfo[slotPos]
				
				self.itemInfo[selectedSlotPos] = attachedSlotPos
				if selectedSlotPos == 2:
					self.combSlot.SetItemSlot(3, player.GetItemIndex(self.def_combSlot_1), 1)

	def __OnSelectItemSlot(self, selectedSlotPos):
		if selectedSlotPos == 3:
			return
		
		self.Clear()
		if selectedSlotPos == 0:
			if self.def_mediumSlot != 999:
				self.mediumSlot.ClearSlot(0)
				self.def_mediumSlot = 999

	def __OnOverInItem(self, slotIndex):
		if self.tooltipItem:
			if slotIndex == 3:
				self.tooltipItem.SetInventoryItemAttrTransfer(self.itemInfo[1], self.itemInfo[2])
			else:
				if self.itemInfo.has_key(slotIndex):
					self.tooltipItem.SetInventoryItem(self.itemInfo[slotIndex])

	def __OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnUpdate(self):
		USE_SHOP_LIMIT_RANGE = 1000
		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xShopStart) > USE_SHOP_LIMIT_RANGE or abs(y - self.yShopStart) > USE_SHOP_LIMIT_RANGE:
			self.__OnCloseButtonClick()

if __name__ == "__main__":
	import app
	import grp
	import wndMgr
	import localeInfo
	import mouseModule
	import systemSetting
	
	import ui
	import uiToolTip
	
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
			self.TransferWindow = TransferWindow()
			self.TransferWindow.LoadWindow()
			self.TransferWindow.SetItemToolTip(self.tooltipItem)
			self.TransferWindow.Open()

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

