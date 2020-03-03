import ui
import player
import uiCommon
import uiToolTip
import changelook
import localeInfo
import mouseModule

class Window(ui.ScriptWindow):
	def NumberToMoneyString(self, number):
		number = str(number)
		strNumber = "%s" % (','.join([number[::-1][k : k + 3][::-1] for k in xrange(len(number)+1, -1, -3)]))
		strNumber = strNumber[1:]
		return "%s" % (strNumber)

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = 0
		self.PositionOut = 0
		self.PositionStartX = 0
		self.PositionStartY = 0
		self.dialog = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearDictionary()
		self.titleBar = None
		self.titleName = None
		self.accept = None
		self.cancel = None
		self.slot = None
		self.cost = None
		self.PositionOut = 0
		self.PositionStartX = 0
		self.PositionStartY = 0
		self.dialog = None

	def LoadWindow(self):
		if self.isLoaded:
			return
		
		self.isLoaded = 1
		
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/changelookwindow.py")
			
		except:
			import exception
			exception.Abort("ChangeLookWindow.LoadDialog.LoadScript")
		
		try:
			self.titleBar = self.GetChild("TitleBar")
			self.titleName = self.GetChild("TitleName")
			self.accept = self.GetChild("AcceptButton")
			self.cancel = self.GetChild("CancelButton")
			self.cost = self.GetChild("Cost")
			self.slot = self.GetChild("ChangeLookSlot")
		except:
			import exception
			exception.Abort("ChangeLookWindow.LoadDialog.BindObject")
		
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.OnClose))
		self.titleName.SetText(localeInfo.CHANGE_LOOK_TITLE)
		self.cancel.SetEvent(ui.__mem_func__(self.OnClose))
		self.accept.SetEvent(ui.__mem_func__(self.OnPressAccept))
		self.cost.SetText(localeInfo.CHANGE_LOOK_COST % (self.NumberToMoneyString(changelook.GetCost())))
		self.slot.SetSelectEmptySlotEvent(ui.__mem_func__(self.OnSelectEmptySlot))
		self.slot.SetUnselectItemSlotEvent(ui.__mem_func__(self.OnSelectItemSlot))
		self.slot.SetUseSlotEvent(ui.__mem_func__(self.OnSelectItemSlot))
		self.slot.SetOverInItemEvent(ui.__mem_func__(self.OnOverInItem))
		self.slot.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
		self.tooltipItem = None

	def SetItemToolTip(self, itemTooltip):
		self.tooltipItem = itemTooltip

	def IsOpened(self):
		if self.IsShow() and self.isLoaded:
			return True
		
		return False

	def Open(self):
		self.PositionOut = 0
		(self.PositionStartX, self.PositionStartY, z) = player.GetMainCharacterPosition()
		self.cost.SetText(localeInfo.CHANGE_LOOK_COST % (self.NumberToMoneyString(changelook.GetCost())))
		for i in xrange(changelook.WINDOW_MAX_MATERIALS):
			self.slot.ClearSlot(i)
		
		self.Show()

	def Close(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
		
		self.OnCancelAccept()
		self.Hide()

	def OnClose(self):
		changelook.SendCloseRequest()

	def OnPressEscapeKey(self):
		self.OnClose()
		return True

	def OnPressAccept(self):
		(isHere, iCell) = changelook.GetAttachedItem(1)
		if not isHere:
			return
		
		dialog = uiCommon.QuestionDialog()
		dialog.SetText(localeInfo.CHANGE_LOOK_CHANGE_ITEM)
		dialog.SetAcceptEvent(ui.__mem_func__(self.OnAccept))
		dialog.SetCancelEvent(ui.__mem_func__(self.OnCancelAccept))
		dialog.Open()
		self.dialog = dialog

	def OnAccept(self):
		changelook.SendRefineRequest()
		self.OnCancelAccept()

	def OnCancelAccept(self):
		if self.dialog:
			self.dialog.Close()
		
		self.dialog = None
		return True

	def OnUpdate(self):
		LIMIT_RANGE = changelook.LIMIT_RANGE
		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.PositionStartX) >= LIMIT_RANGE or abs(y - self.PositionStartY) >= LIMIT_RANGE:
			if not self.PositionOut:
				self.PositionOut += 1
				self.OnClose()

	def OnSelectEmptySlot(self, selectedSlotPos):
		isAttached = mouseModule.mouseController.isAttached()
		if not isAttached:
			return
		
		attachedSlotType = mouseModule.mouseController.GetAttachedType()
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
		mouseModule.mouseController.DeattachObject()
		if attachedSlotType == player.SLOT_TYPE_INVENTORY and attachedInvenType == player.INVENTORY:
			changelook.Add(attachedInvenType, attachedSlotPos, selectedSlotPos)

	def OnSelectItemSlot(self, selectedSlotPos):
		mouseModule.mouseController.DeattachObject()
		changelook.Remove(selectedSlotPos)

	def OnOverInItem(self, selectedSlotPos):
		if self.tooltipItem:
			(isHere, iCell) = changelook.GetAttachedItem(selectedSlotPos)
			if isHere:
				self.tooltipItem.SetInventoryItem(iCell)

	def OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def Refresh(self):
		for i in xrange(changelook.WINDOW_MAX_MATERIALS):
			self.slot.ClearSlot(i)
			(isHere, iCell) = changelook.GetAttachedItem(i)
			if isHere:
				self.slot.SetItemSlot(i, player.GetItemIndex(iCell), 1)

