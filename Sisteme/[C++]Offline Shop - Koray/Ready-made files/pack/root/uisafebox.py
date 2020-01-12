import ui
import mouseModule
import player
import net
import snd
import safebox
import chat
import app
import localeInfo
import uiScriptLocale

class PasswordDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadDialog()

		self.sendMessage = "/safebox_password "

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "passworddialog.py")
		except:
			import exception
			exception.Abort("PasswordDialog.__LoadDialog.LoadObject")

		try:
			self.passwordValue = self.GetChild("password_value")
			self.acceptButton = self.GetChild("accept_button")
			self.cancelButton = self.GetChild("cancel_button")
			self.titleName = self.GetChild("TitleName")
			self.GetChild("titlebar").SetCloseEvent(ui.__mem_func__(self.CloseDialog))
		except:
			import exception
			exception.Abort("PasswordDialog.__LoadDialog.BindObject")

		self.passwordValue.OnIMEReturn = self.OnAccept
		self.passwordValue.OnPressEscapeKey = self.OnCancel
		self.acceptButton.SetEvent(ui.__mem_func__(self.OnAccept))
		self.cancelButton.SetEvent(ui.__mem_func__(self.OnCancel))

	def Destroy(self):
		self.ClearDictionary()
		self.passwordValue = None
		self.acceptButton = None
		self.cancelButton = None
		self.titleName = None

	def SetTitle(self, title):
		self.titleName.SetText(title)

	def SetSendMessage(self, msg):
		self.sendMessage = msg

	def ShowDialog(self):
		self.passwordValue.SetText("")
		self.passwordValue.SetFocus()
		self.SetCenterPosition()
		self.Show()

	def CloseDialog(self):
		self.passwordValue.KillFocus()
		self.Hide()

	def OnAccept(self):
		net.SendChatPacket(self.sendMessage + self.passwordValue.GetText())
		self.CloseDialog()
		return True

	def OnCancel(self):
		self.CloseDialog()
		return True

class ChangePasswordDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		self.dlgMessage = ui.ScriptWindow()
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self.dlgMessage, "uiscript/popupdialog.py")
			self.dlgMessage.GetChild("message").SetText(localeInfo.SAFEBOX_WRONG_PASSWORD)
			self.dlgMessage.GetChild("accept").SetEvent(ui.__mem_func__(self.OnCloseMessageDialog))
		except:
			import exception
			exception.Abort("SafeboxWindow.__LoadDialog.LoadObject")

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/changepassworddialog.py")

		except:
			import exception
			exception.Abort("ChangePasswordDialog.LoadDialog.LoadObject")

		try:
			self.GetChild("accept_button").SetEvent(ui.__mem_func__(self.OnAccept))
			self.GetChild("cancel_button").SetEvent(ui.__mem_func__(self.OnCancel))
			self.GetChild("titlebar").SetCloseEvent(ui.__mem_func__(self.OnCancel))
			oldPassword = self.GetChild("old_password_value")
			newPassword = self.GetChild("new_password_value")
			newPasswordCheck = self.GetChild("new_password_check_value")
		except:
			import exception
			exception.Abort("ChangePasswordDialog.LoadDialog.BindObject")

		oldPassword.SetTabEvent(lambda arg=1: self.OnNextFocus(arg))
		newPassword.SetTabEvent(lambda arg=2: self.OnNextFocus(arg))
		newPasswordCheck.SetTabEvent(lambda arg=3: self.OnNextFocus(arg))
		oldPassword.SetReturnEvent(lambda arg=1: self.OnNextFocus(arg))
		newPassword.SetReturnEvent(lambda arg=2: self.OnNextFocus(arg))
		newPasswordCheck.SetReturnEvent(ui.__mem_func__(self.OnAccept))
		oldPassword.OnPressEscapeKey = self.OnCancel
		newPassword.OnPressEscapeKey = self.OnCancel
		newPasswordCheck.OnPressEscapeKey = self.OnCancel

		self.oldPassword = oldPassword
		self.newPassword = newPassword
		self.newPasswordCheck = newPasswordCheck

	def OnNextFocus(self, arg):
		if 1 == arg:
			self.oldPassword.KillFocus()
			self.newPassword.SetFocus()
		elif 2 == arg:
			self.newPassword.KillFocus()
			self.newPasswordCheck.SetFocus()
		elif 3 == arg:
			self.newPasswordCheck.KillFocus()
			self.oldPassword.SetFocus()

	def Destroy(self):
		self.ClearDictionary()
		self.dlgMessage.ClearDictionary()
		self.oldPassword = None
		self.newPassword = None
		self.newPasswordCheck = None

	def Open(self):
		self.oldPassword.SetText("")
		self.newPassword.SetText("")
		self.newPasswordCheck.SetText("")
		self.oldPassword.SetFocus()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.oldPassword.SetText("")
		self.newPassword.SetText("")
		self.newPasswordCheck.SetText("")
		self.oldPassword.KillFocus()
		self.newPassword.KillFocus()
		self.newPasswordCheck.KillFocus()
		self.Hide()

	def OnAccept(self):
		oldPasswordText = self.oldPassword.GetText()
		newPasswordText = self.newPassword.GetText()
		newPasswordCheckText = self.newPasswordCheck.GetText()
		if newPasswordText != newPasswordCheckText:
			self.dlgMessage.SetCenterPosition()
			self.dlgMessage.SetTop()
			self.dlgMessage.Show()
			return True
		net.SendChatPacket("/safebox_change_password %s %s" % (oldPasswordText, newPasswordText))
		self.Close()
		return True

	def OnCancel(self):
		self.Close()
		return True

	def OnCloseMessageDialog(self):
		self.newPassword.SetText("")
		self.newPasswordCheck.SetText("")
		self.newPassword.SetFocus()
		self.dlgMessage.Hide()


if app.ENABLE_OFFLINE_SHOP:
	class OfflineShopListItem(ui.ListBoxEx.Item):
		def __init__(self, idx, text, vidOfShop, mapIndex, posX, posY):
			ui.ListBoxEx.Item.__init__(self)
			
			self.idx = idx
			self.vidOfShop = vidOfShop
			self.mapIndex = mapIndex
			self.posX = posX
			self.posY = posY
			self.text = text
	
			self.mapNameOld = str(background.GetMapName(long(self.posX), long(self.posY)))
			self.mapName = self.realMapName(self.mapNameOld)
	
			self.textLine = self.__CreateTextLine("%s" % (str(text)[:50]), (2, 5))
			self.textLineMap = self.__CreateTextLine("%s" % self.mapName, (150, 5))
			self.gotoShop = self.__CreateButton((280, 1), "Go", self.gotoShopFunc)
			self.warpShop = self.__CreateButton((340, 1), "Warp", self.warpShopFunc)
			self.closeShop = self.__CreateButton((400, 1), "Close", self.closeShopFunc)
			
		def __del__(self):
			self.idx = None
			self.vidOfShop = None
			self.mapIndex = None
			self.posX = None
			self.posY = None
			self.text = None
	
			if self.textLine and self.textLine.IsShow():
				self.textLine.Hide()
				self.textLine = None
			if self.gotoShop and self.gotoShop.IsShow():
				self.gotoShop.Hide()
				self.gotoShop = None
			if self.warpShop and self.warpShop.IsShow():
				self.warpShop.Hide()
				self.warpShop = None
			if self.closeShop and self.closeShop.IsShow():
				self.closeShop.Hide()
				self.closeShop = None
	
			ui.ListBoxEx.Item.__del__(self)
	
		def realMapName(self, oldName):
			mapNames = {"metin2_map_trent02": "Kizil Orman", "metin2_map_trent": "Orman", "metin2_map_WL_01": "Yilan Vadisi",
						 "metin2_map_nusluck01": "Devler Diyari", "metin2_map_devilscatacomb": "Seytan Katakombu", "metin2_map_duel": "VS Arenasi",
						 "metin2_map_a1": "Yongan Bolgesi(Shinsoo)", "metin2_map_b1 ": "Joan Bolgesi(Chunjo)", "metin2_map_c1": "Pyungmoo Bolgesi(Jinno)",
						 "metin2_map_a3": "Jayang Bolgesi(Shinsoo)", "metin2_map_b3 ": "Bokjung Bolgesi(Chunjo)", "metin2_map_c3": "Bakra Bolgesi(Jinno)",
						 "map_a2": "Seungryong Vadisi", "map_n_snowm_01 ": "Sohan Dagi", "metin2_map_n_desert_01": "Yongbi Colu",
						 "metin2_map_deviltower1": "Åeytan Kulesi", "metin2_map_guild_01 ": "Jungrang(Lonca BÃ¶lgesi)", "metin2_map_guild_02": "Waryong(Lonca BÃ¶lgesi)",
						 "metin2_map_guild_03": "Imha(Lonca BÃ¶lgesi)", "metin2_guild_village_01 ": "Miryan(Lonca SavaÅŸÄ±)", "metin2_guild_village_02": "Songpa(Lonca SavaÅŸÄ±)",
						 "metin2_guild_village_03": "Daeyami(Lonca SavaÅŸÄ±)", "metin2_map_milgyo ": "Hwang TapÄ±naÄŸÄ±", "metin2_map_monkeydungeon": "Maymun ZindanÄ±(Kolay)",
						 "metin2_map_monkeydungeon_02": "Maymun ZindanÄ±(Normal)", "metin2_map_monkeydungeon_03 ": "Maymun ZindanÄ±(Uzman)", "metin2_map_n_flame_01": "AteÅŸ DiyarÄ±",
						 "metin2_map_spiderdungeon": "Ã–rÃ¼mcek ZindanÄ± 1.Kat", "metin2_map_spiderdungeon_02 ": "Ã–rÃ¼mcek ZindanÄ± 2.Kat", "metin2_map_spiderdungeon_03": "Ã–rÃ¼mcek ZindanÄ± 3.Kat",
						 "metin2_map_skipia_dungeon_01": "SÃ¼rgÃ¼n MaÄŸarasÄ± 1.Kat", "metin2_map_skipia_dungeon_02 ": "SÃ¼rgÃ¼n MaÄŸarasÄ± 2.Kat"
			}
			if oldName in mapNames:
				return mapNames[oldName]
			return oldName
	
		def gotoShopFunc(self):
			net.SendChatPacket("/offlineshop_goto %s" % str(self.vidOfShop))
	
		def warpShopFunc(self):
			net.SendChatPacket("/offlineshop_warp %s" % str(self.vidOfShop))
	
		def closeShopFunc(self):
			net.SendChatPacket("/offlineshop_close %s" % str(self.vidOfShop))
		
	
		def SetSize(self, width, height):
			ui.ListBoxEx.Item.SetSize(self, 460, height + 7)
			
		def __CreateTextLine(self, text, pos):
			textLine=ui.TextLine()
			textLine.SetParent(self)
			textLine.SetPosition(pos[0], pos[1])
			textLine.SetText(text)
			textLine.Show()
			return textLine
			
		def __CreateButton(self, pos, buttonName, func):
			tmpButton = ui.Button()
			tmpButton.SetParent(self)
			tmpButton.SetPosition(pos[0], pos[1])
			
			tmpButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
			tmpButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
			tmpButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
	
			tmpButton.SetText(buttonName)
			tmpButton.SetEvent(func)
			tmpButton.Show()
			
			return tmpButton
	
	class OfflineShopUI(ui.BoardWithTitleBar):
		def __init__(self):
			ui.BoardWithTitleBar.__init__(self)
			self.LastIdx = 0
			self.BuildUI()
	
		def __del__(self):
			ui.BoardWithTitleBar.__del__(self)
	
		def BuildUI(self):
			posX = 500
			self.AddFlag('movable')
			self.AddFlag('float')
			self.SetSize(posX, 150)
			self.SetTitleName("Offline Shop Panel")
			self.SetCloseEvent(self.OpenWindow)
			self.SetCenterPosition()
			self.Show()
	
			self.bar = ui.Bar()
			self.bar.SetParent(self)
			self.bar.SetPosition(10, 35)
			self.bar.SetSize(posX - 20, 100)
			self.bar.SetColor(0x77000000)
			self.bar.Show()
	
			self.ListBox = ui.ListBoxEx()
			self.ListBox.SetParent(self.bar)
			self.ListBox.SetPosition(0, 0)
			self.ListBox.SetSize(posX, 100)
			self.ListBox.SetViewItemCount(5)
			self.ListBox.Show()
	
			self.scroll = ui.ScrollBar()
			self.scroll.SetParent(self.ListBox)
			self.scroll.SetPosition(posX-35, 0)
			self.scroll.SetScrollBarSize(200/2)
			self.scroll.Show()
			self.ListBox.SetScrollBar(self.scroll)
	
			self.refresh = ui.Button()
			self.refresh.SetParent(self)
			self.refresh.SetPosition(self.GetWidth() - 50, 8)
			self.refresh.SetUpVisual("d:/ymir work/ui/game/guild/Refresh_Button_01.sub")
			self.refresh.SetOverVisual("d:/ymir work/ui/game/guild/Refresh_Button_02.sub")
			self.refresh.SetDownVisual("d:/ymir work/ui/game/guild/Refresh_Button_03.sub")
			self.refresh.SetText("")
			self.refresh.SetEvent(self.Refresh)
			self.refresh.Show()
	
		def AppendOfflineShop(self, name, vid, mapIdx, x, y):
			if not self.IsShowWindow():
				self.LastIdx = 0
				self.ListBox.RemoveAllItems()
				self.ShowWindow()
	
			self.LastIdx += 1
			self.ListBox.AppendItem(OfflineShopListItem(self.LastIdx, name, vid, mapIdx, x, y))
			
		def Refresh(self):
			self.Close()
			net.SendChatPacket("/do_myshops")
	
		def IsShowWindow(self):
			return self.IsShow()
	
		def OpenWindow(self):
			if self.IsShow():
				self.Hide()
			else:
				self.Show()
	
		def ShowWindow(self):
			self.Show()
	
		def Close(self):
			self.Hide()
			return True
	
		def OnPressEscapeKey(self):
			self.Close()
			return True


class SafeboxWindow(ui.ScriptWindow):

	BOX_WIDTH = 176

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.tooltipItem = None
		self.sellingSlotNumber = -1
		self.pageButtonList = []
		self.curPageIndex = 0
		self.isLoaded = 0
		self.xSafeBoxStart = 0
		self.ySafeBoxStart = 0

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()

		ui.ScriptWindow.Show(self)		

	def Destroy(self):
		self.ClearDictionary()

		self.dlgPickMoney.Destroy()
		self.dlgPickMoney = None
		self.dlgChangePassword.Destroy()
		self.dlgChangePassword = None

		self.tooltipItem = None
		self.wndMoneySlot = None
		self.wndMoney = None
		self.wndBoard = None
		self.wndItem = None

		self.pageButtonList = []

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "UIScript/SafeboxWindow.py")

		from _weakref import proxy

		## Item
		wndItem = ui.GridSlotWindow()
		wndItem.SetParent(self)
		wndItem.SetPosition(8, 35)
		wndItem.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndItem.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndItem.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		wndItem.Show()

		## PickMoneyDialog
		import uiPickMoney
		dlgPickMoney = uiPickMoney.PickMoneyDialog()
		dlgPickMoney.LoadDialog()
		dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickMoney))
		dlgPickMoney.Hide()

		## ChangePasswrod
		dlgChangePassword = ChangePasswordDialog()
		dlgChangePassword.LoadDialog()
		dlgChangePassword.Hide()

		## Close Button
		self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
		self.GetChild("ChangePasswordButton").SetEvent(ui.__mem_func__(self.OnChangePassword))
		self.GetChild("ExitButton").SetEvent(ui.__mem_func__(self.Close))

		if app.ENABLE_OFFLINE_SHOP:
			self.GetChild("CollectButton").SetEvent(ui.__mem_func__(self.OnCollect))
			self.GetChild("MyShopsButton").SetEvent(ui.__mem_func__(self.MyShops))

		self.wndItem = wndItem
		self.dlgPickMoney = dlgPickMoney
		self.dlgChangePassword = dlgChangePassword
		self.wndBoard = self.GetChild("board")
		if app.ENABLE_OFFLINE_SHOP:
			self.wndMoney = self.GetChild("Money")
			self.wndMoneySlot = self.GetChild("MoneySlot")
			self.wndMoneySlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog))

		## Initialize
		self.SetTableSize(3)
		self.RefreshSafeboxMoney()

	def OpenPickMoneyDialog(self):

		if mouseModule.mouseController.isAttached():

			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			if player.SLOT_TYPE_INVENTORY == mouseModule.mouseController.GetAttachedType():

				if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
					net.SendSafeboxSaveMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")

			mouseModule.mouseController.DeattachObject()

		else:
			curMoney = safebox.GetMoney()

			if curMoney <= 0:
				return

			self.dlgPickMoney.Open(curMoney)
			if app.ENABLE_OFFLINE_SHOP:
				self.dlgPickMoney.SetMax(11)

	def ShowWindow(self, size):

		(self.xSafeBoxStart, self.ySafeBoxStart, z) = player.GetMainCharacterPosition()

		self.SetTableSize(size)
		self.Show()

	def __MakePageButton(self, pageCount):

		self.curPageIndex = 0
		self.pageButtonList = []

		text = "I"
		pos = -int(float(pageCount-1)/2 * 52)
		for i in xrange(pageCount):
			button = ui.RadioButton()
			button.SetParent(self)
			button.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_middle_01.sub")
			button.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_middle_02.sub")
			button.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")
			button.SetWindowHorizontalAlignCenter()
			button.SetWindowVerticalAlignBottom()
			if app.ENABLE_OFFLINE_SHOP:
				button.SetPosition(pos, 100)
			else:
				button.SetPosition(pos, 85)
			button.SetText(text)
			button.SetEvent(lambda arg=i: self.SelectPage(arg))
			button.Show()
			self.pageButtonList.append(button)

			pos += 52
			text += "I"

		self.pageButtonList[0].Down()

	def SelectPage(self, index):

		self.curPageIndex = index

		for btn in self.pageButtonList:
			btn.SetUp()

		self.pageButtonList[index].Down()
		self.RefreshSafebox()

	def __LocalPosToGlobalPos(self, local):
		return self.curPageIndex*safebox.SAFEBOX_PAGE_SIZE + local

	def SetTableSize(self, size):

		pageCount = max(1, size / safebox.SAFEBOX_SLOT_Y_COUNT)
		pageCount = min(3, pageCount)
		size = safebox.SAFEBOX_SLOT_Y_COUNT

		self.__MakePageButton(pageCount)

		self.wndItem.ArrangeSlot(0, safebox.SAFEBOX_SLOT_X_COUNT, size, 32, 32, 0, 0)
		self.wndItem.RefreshSlot()
		self.wndItem.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)

		wnd_height = 130 + 32 * size
		if not app.ENABLE_OFFLINE_SHOP:
			self.wndBoard.SetSize(self.BOX_WIDTH, wnd_height)
			self.SetSize(self.BOX_WIDTH, wnd_height)
			self.UpdateRect()

	def RefreshSafebox(self):
		getItemID=safebox.GetItemID
		getItemCount=safebox.GetItemCount
		setItemID=self.wndItem.SetItemSlot

		for i in xrange(safebox.SAFEBOX_PAGE_SIZE):
			slotIndex = self.__LocalPosToGlobalPos(i)
			itemCount = getItemCount(slotIndex)
			if itemCount <= 1:
				itemCount = 0
			setItemID(i, getItemID(slotIndex), itemCount)

		self.wndItem.RefreshSlot()

	def RefreshSafeboxMoney(self):
		if app.ENABLE_OFFLINE_SHOP:
			self.wndMoney.SetText(localeInfo.NumberToMoneyString(safebox.GetMoney()))

	def SetItemToolTip(self, tooltip):
		self.tooltipItem = tooltip

	def Close(self):
		net.SendChatPacket("/safebox_close")

	def CommandCloseSafebox(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

		self.dlgPickMoney.Close()
		self.dlgChangePassword.Close()
		self.Hide()

	## Slot Event
	def SelectEmptySlot(self, selectedSlotPos):

		selectedSlotPos = self.__LocalPosToGlobalPos(selectedSlotPos)

		if mouseModule.mouseController.isAttached():

			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			
			if app.ENABLE_OFFLINE_SHOP:
				if player.SLOT_TYPE_INVENTORY == attachedSlotType:
					if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
						net.SendSafeboxSaveMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
						snd.PlaySound("sound/ui/money.wav")
	
					else:
						net.SendSafeboxCheckinPacket(attachedSlotPos, selectedSlotPos)
						#snd.PlaySound("sound/ui/drop.wav")
						
				elif player.SLOT_TYPE_SAFEBOX == attachedSlotType:
	
					net.SendSafeboxItemMovePacket(attachedSlotPos, selectedSlotPos, 0)
					#snd.PlaySound("sound/ui/drop.wav")
			else:
				if player.SLOT_TYPE_SAFEBOX == attachedSlotType:
	
					net.SendSafeboxItemMovePacket(attachedSlotPos, selectedSlotPos, 0)
					#snd.PlaySound("sound/ui/drop.wav")
				else:
					attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
					if player.RESERVED_WINDOW == attachedInvenType:
						return
	
					if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
						net.SendSafeboxSaveMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
						snd.PlaySound("sound/ui/money.wav")
	
					else:
						net.SendSafeboxCheckinPacket(attachedInvenType, attachedSlotPos, selectedSlotPos)
						#snd.PlaySound("sound/ui/drop.wav")

			mouseModule.mouseController.DeattachObject()


	def SelectItemSlot(self, selectedSlotPos):

		selectedSlotPos = self.__LocalPosToGlobalPos(selectedSlotPos)

		if mouseModule.mouseController.isAttached():

			attachedSlotType = mouseModule.mouseController.GetAttachedType()

			if player.SLOT_TYPE_INVENTORY == attachedSlotType:

				if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
					net.SendSafeboxSaveMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")

				else:
					attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
					#net.SendSafeboxCheckinPacket(attachedSlotPos, selectedSlotPos)
					#snd.PlaySound("sound/ui/drop.wav")

			mouseModule.mouseController.DeattachObject()

		else:

			curCursorNum = app.GetCursor()
			if app.SELL == curCursorNum:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SAFEBOX_SELL_DISABLE_SAFEITEM)

			elif app.BUY == curCursorNum:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_BUY_INFO)

			else:
				selectedItemID = safebox.GetItemID(selectedSlotPos)
				mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_SAFEBOX, selectedSlotPos, selectedItemID)
				snd.PlaySound("sound/ui/pick.wav")

	def UseItemSlot(self, slotIndex):
		mouseModule.mouseController.DeattachObject()

	def __ShowToolTip(self, slotIndex):
		if self.tooltipItem:
			self.tooltipItem.SetSafeBoxItem(slotIndex)

	def OverInItem(self, slotIndex):
		slotIndex = self.__LocalPosToGlobalPos(slotIndex)
		self.wndItem.SetUsableItem(False)
		self.__ShowToolTip(slotIndex)

	def OverOutItem(self):
		self.wndItem.SetUsableItem(False)
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnPickMoney(self, money):
		mouseModule.mouseController.AttachMoney(self, player.SLOT_TYPE_SAFEBOX, money)

	def OnChangePassword(self):
		self.dlgChangePassword.Open()
		
	if app.ENABLE_OFFLINE_SHOP:
		def OnCollect(self):
			net.SendChatPacket("/do_gather")
	
		def MyShops(self):
			net.SendChatPacket("/do_myshops")

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnUpdate(self):

		USE_SAFEBOX_LIMIT_RANGE = 1000

		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xSafeBoxStart) > USE_SAFEBOX_LIMIT_RANGE or abs(y - self.ySafeBoxStart) > USE_SAFEBOX_LIMIT_RANGE:
			self.Close()

class MallWindow(ui.ScriptWindow):

	BOX_WIDTH = 176

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.tooltipItem = None
		self.sellingSlotNumber = -1
		self.pageButtonList = []
		self.curPageIndex = 0
		self.isLoaded = 0
		self.xSafeBoxStart = 0
		self.ySafeBoxStart = 0

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()

		ui.ScriptWindow.Show(self)		

	def Destroy(self):
		self.ClearDictionary()

		self.tooltipItem = None
		self.wndBoard = None
		self.wndItem = None

		self.pageButtonList = []

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "UIScript/MallWindow.py")

		from _weakref import proxy

		## Item
		wndItem = ui.GridSlotWindow()
		wndItem.SetParent(self)
		wndItem.SetPosition(8, 35)
		wndItem.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndItem.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndItem.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		wndItem.Show()

		## Close Button
		self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
		self.GetChild("ExitButton").SetEvent(ui.__mem_func__(self.Close))

		self.wndItem = wndItem
		self.wndBoard = self.GetChild("board")

		## Initialize
		self.SetTableSize(3)

	def ShowWindow(self, size):

		(self.xSafeBoxStart, self.ySafeBoxStart, z) = player.GetMainCharacterPosition()

		self.SetTableSize(size)
		self.Show()

	def SetTableSize(self, size):

		pageCount = max(1, size / safebox.SAFEBOX_SLOT_Y_COUNT)
		pageCount = min(3, pageCount)
		size = safebox.SAFEBOX_SLOT_Y_COUNT

		self.wndItem.ArrangeSlot(0, safebox.SAFEBOX_SLOT_X_COUNT, size, 32, 32, 0, 0)
		self.wndItem.RefreshSlot()
		self.wndItem.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)

		if not app.ENABLE_OFFLINE_SHOP:
			self.wndBoard.SetSize(self.BOX_WIDTH, 82 + 32*size)
			self.SetSize(self.BOX_WIDTH, 85 + 32*size)
			self.UpdateRect()

	def RefreshMall(self):
		getItemID=safebox.GetMallItemID
		getItemCount=safebox.GetMallItemCount
		setItemID=self.wndItem.SetItemSlot

		for i in xrange(safebox.GetMallSize()):
			itemID = getItemID(i)
			itemCount = getItemCount(i)
			if itemCount <= 1:
				itemCount = 0
			setItemID(i, itemID, itemCount)

		self.wndItem.RefreshSlot()

	def SetItemToolTip(self, tooltip):
		self.tooltipItem = tooltip

	def Close(self):
		net.SendChatPacket("/mall_close")

	def CommandCloseMall(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

		self.Hide()

	## Slot Event
	def SelectEmptySlot(self, selectedSlotPos):

		if mouseModule.mouseController.isAttached():

			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MALL_CANNOT_INSERT)
			mouseModule.mouseController.DeattachObject()

	def SelectItemSlot(self, selectedSlotPos):

		if mouseModule.mouseController.isAttached():

			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MALL_CANNOT_INSERT)
			mouseModule.mouseController.DeattachObject()

		else:

			curCursorNum = app.GetCursor()
			selectedItemID = safebox.GetMallItemID(selectedSlotPos)
			mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_MALL, selectedSlotPos, selectedItemID)
			snd.PlaySound("sound/ui/pick.wav")

	def UseItemSlot(self, slotIndex):
		mouseModule.mouseController.DeattachObject()

	def __ShowToolTip(self, slotIndex):
		if self.tooltipItem:
			self.tooltipItem.SetMallItem(slotIndex)

	def OverInItem(self, slotIndex):
		self.__ShowToolTip(slotIndex)

	def OverOutItem(self):
		self.wndItem.SetUsableItem(False)
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnUpdate(self):

		USE_SAFEBOX_LIMIT_RANGE = 1000

		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xSafeBoxStart) > USE_SAFEBOX_LIMIT_RANGE or abs(y - self.ySafeBoxStart) > USE_SAFEBOX_LIMIT_RANGE:
			self.Close()


if __name__ == "__main__":

	import app
	import wndMgr
	import systemSetting
	import mouseModule
	import grp
	import ui
	import chr
	import background
	import player

	#wndMgr.SetOutlineFlag(True)

	app.SetMouseHandler(mouseModule.mouseController)
	app.SetHairColorEnable(True)
	wndMgr.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetScreenSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	app.Create("METIN2 CLOSED BETA", systemSetting.GetWidth(), systemSetting.GetHeight(), 1)
	mouseModule.mouseController.Create()


	wnd = SafeboxWindow()
	wnd.ShowWindow(1)
	
	app.Loop()
