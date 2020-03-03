import localeInfo
import uiCommon
import constInfo
import exception
import item
import player
import net
import grp
import app
import ui
import mouseModule
import dbg
import uiToolTip
import chat

class ChangeLookWindow(ui.ScriptWindow):
	popupDialog = None
	questionDialog = None
	SlotsIndexes = [-1, -1]
	isLoad = False

	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/changelookwindow.py")
		except:
			import exception
			exception.Abort("ChangeLookWindow.__LoadWindow.LoadObject")

		try:
			self.wndItem = self.GetChild("ChangeLookSlot")
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.GetChild("TitleName").SetText(localeInfo.CHANGE_LOOK_TITLE)
			self.GetChild("Cost").SetText(localeInfo.CHANGE_LOOK_COST)
			self.GetChild("AcceptButton").SetEvent(self.SendAccept)
			self.GetChild("CancelButton").SetEvent(self.OnCloseEvent)
			self.ChangeLookToolTIpButton = self.GetChild("ChangeLookToolTIpButton")
			self.wndItem.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
			self.wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			self.wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			self.wndItem.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
			self.wndItem.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))

			self.tl = uiToolTip.ItemToolTip()
			self.tlInfo = uiToolTip.ItemToolTip()
			self.tl.Hide()
			self.tlInfo.Hide()
			self.tooltipItem = self.tl
			self.tooltipInfo = [self.tlInfo]*5
			self.InformationText = [localeInfo.CHANGE_TOOLTIP_TITLE,
									localeInfo.CHANGE_TOOLTIP_LINE1,
									localeInfo.CHANGE_TOOLTIP_LINE2,
									localeInfo.CHANGE_TOOLTIP_LINE3,
									localeInfo.CHANGE_TOOLTIP_LINE4
			]

			for i in xrange(5):
				self.tooltipInfo[i].SetFollow(True, True)
				self.tooltipInfo[i].AlignHorizonalCenter()
				if i == 0:
					TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
					self.tooltipInfo[i].AppendTextLine(self.InformationText[i], TITLE_COLOR)
				else:
					self.tooltipInfo[i].AppendTextLine(self.InformationText[i])
				self.tooltipInfo[i].Hide()
				self.tooltipInfo[i].toolTipWidth += 55

			self.popupDialog = uiCommon.PopupDialog()
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.CHANGE_LOOK_CHANGE_ITEM)
			self.questionDialog.SetAcceptEvent(self.Accept)
			self.questionDialog.SetCancelEvent(self.Cancel)		
		except:
			import exception
			exception.Abort("ChangeLookWindow.__LoadWindow.BindObject")

	def Accept(self):
		net.SendChatPacket("/transmutate %d %d" % (self.SlotsIndexes[0], self.SlotsIndexes[1]))
		for i in xrange(2):
			self.wndItem.SetItemSlot(i, 0, 0)
			player.SetChangeLookActivedItemSlot(i, -1)
			self.questionDialog.Close()
			self.SlotsIndexes[i] = -1

	def Cancel(self):
		self.questionDialog.Close()

	def OnPressEscapeKey(self):
		self.isLoad = False
		constInfo.IsChangeLookWindowOpen = False
		self.tlInfo.Hide()
		self.Close()

	def Open(self):
		constInfo.IsChangeLookWindowOpen = True
		if not self.isLoad:
			self.isLoad = True
			self.__LoadWindow()

			self.SetTop()
			self.SetCenterPosition()
			self.Show()

	def Close(self):
		constInfo.IsChangeLookWindowOpen = False
		for i in xrange(2):
			player.SetChangeLookActivedItemSlot(i, -1)
		self.isLoad = False
		self.Hide()

	def SendAccept(self):
		if self.SlotsIndexes[0] == -1 or self.SlotsIndexes[1] == -1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHANGE_LOOK_INSERT_ITEM)
		else:
			self.questionDialog.Open()

	def SetItemToolTip(self, itemTooltip):
		self.tooltipItem = itemTooltip

	def __ShowToolTip(self, slotIndex):
		if self.tooltipItem:
			self.tooltipItem.SetChangeLookWindowItem(self.SlotsIndexes[slotIndex])

	def OnUpdate(self):
		for i in xrange(5):
			if self.ChangeLookToolTIpButton.IsIn():
				self.tooltipInfo[i].Show()
			else:
				self.tooltipInfo[i].Hide()

		for i in xrange(2):
			if self.SlotsIndexes[i] and player.GetItemLook(self.SlotsIndexes[i]):
				self.wndItem.EnableSlotCoverImage(i)
			else:
				self.wndItem.DisableSlotCoverImage(i)

	def OverInItem(self, slotIndex):
		slotIndex = slotIndex
		self.__ShowToolTip(slotIndex)

	def OverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def ExcludeItems(self, vnum):
		ExVnums = [11901, 11902, 11903, 11904, 11907, 11908, 11909, 11910, 11911, 11912, 11913, 11914, 50201, 50202]
		if vnum in ExVnums:
			return True
		else:
			return False

	def SelectEmptySlot(self, selectedSlotPos):
		if selectedSlotPos > 1 or selectedSlotPos < 0:
			return

		if selectedSlotPos == 1 and self.SlotsIndexes[0] == -1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHANGE_LOOK_INSERT_CHANGE_LOOK_ITEM)
			return

		getItemVNum = player.GetItemIndex

		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()

			attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
			if player.RESERVED_WINDOW == attachedInvenType:
				return

			if selectedSlotPos == 1:
				if attachedSlotPos in self.SlotsIndexes:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHANGE_ALREADY_REGISTER)
					return

			item.SelectItem(getItemVNum(attachedSlotPos))

			if (self.ExcludeItems(getItemVNum(attachedSlotPos))):
				return

			# If you have WEAPON_QUIVER
			# Disable the line without WEAPON_QUIVER and Enable the line with WEAPON_QUIVER
			# if item.ITEM_TYPE_WEAPON == item.GetItemType() and not item.GetItemSubType() in (item.WEAPON_ARROW, item.WEAPON_QUIVER) or (item.ITEM_TYPE_ARMOR == item.GetItemType() and item.GetItemSubType() == item.ARMOR_BODY):
			if item.ITEM_TYPE_WEAPON == item.GetItemType() and not item.GetItemSubType() == item.WEAPON_ARROW or (item.ITEM_TYPE_ARMOR == item.GetItemType() and item.GetItemSubType() == item.ARMOR_BODY):
				self.wndItem.SetItemSlot(selectedSlotPos, getItemVNum(attachedSlotPos), 0)
				self.SlotsIndexes[selectedSlotPos] = attachedSlotPos
				player.SetChangeLookActivedItemSlot(selectedSlotPos, attachedSlotPos)
				if selectedSlotPos == 1:
					self.popupDialog.SetText(localeInfo.CHANGE_LOOK_DEL_ITEM)
					self.popupDialog.Open()
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHANGE_LOOK_DO_NOT_CHANGE_LOOK_ITEM)
				return

			mouseModule.mouseController.DeattachObject()

	def UseItemSlot(self, selectedSlotPos):
		self.wndItem.SetItemSlot(selectedSlotPos, 0, 0)
		mouseModule.mouseController.DeattachObject()
		player.SetChangeLookActivedItemSlot(selectedSlotPos, -1)
		self.SlotsIndexes[selectedSlotPos] = -1
		self.OverOutItem()

	def OnCloseEvent(self):
		constInfo.IsChangeLookWindowOpen = False
		self.isLoad = False
		self.Close()

	def __OnClosePopupDialog(self):
		pass
