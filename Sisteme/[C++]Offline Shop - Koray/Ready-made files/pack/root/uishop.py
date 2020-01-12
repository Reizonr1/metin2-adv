import net
import player
import item
import snd
import shop
import net
import wndMgr
import app
import chat

import ui
import uiCommon
import mouseModule
import localeInfo
import constInfo
import chr

###################################################################################################
## Shop
class ShopDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		if app.ENABLE_OFFLINE_SHOP:
			self.SizeToGridSize = { 0: 40, 1: 50, 2: 60, 3: 70, 4: 80, 5: 90 }
			self.itemSlotList = { }
			self.GridSize = 40

		self.tooltipItem = 0
		self.xShopStart = 0
		self.yShopStart = 0
		self.questionDialog = None
		self.popup = None
		self.itemBuyQuestionDialog = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)
	
	def __GetRealIndex(self, i):
		return self.tabIdx * shop.SHOP_SLOT_COUNT + i
	
	if app.ENABLE_OFFLINE_SHOP:
		def Refresh(self):
			getItemID=shop.GetItemID
			getItemCount=shop.GetItemCount
			setItemID=self.itemSlotList["ItemSlot_%d" % self.GridSize].SetItemSlot
			for i in xrange(self.GridSize):
				itemCount = getItemCount(i)
	
				if itemCount <= 1:
					itemCount = 0
				setItemID(i, getItemID(i), itemCount)
				if shop.GetItemIsSold(i) == 1:
					self.RegisterShopSold(i)
				else:
					if self.itemSlotList["ItemSlot_%d" % self.GridSize].HasCoverButton(i):
						self.itemSlotList["ItemSlot_%d" % self.GridSize].DeleteCoverButton(i)
	
			wndMgr.RefreshSlot(self.itemSlotList["ItemSlot_%d" % self.GridSize].GetWindowHandle())
	else:
		def Refresh(self):
			getItemID=shop.GetItemID
			getItemCount=shop.GetItemCount
			setItemID=self.itemSlotWindow.SetItemSlot
			for i in xrange(shop.SHOP_SLOT_COUNT):
				idx = self.__GetRealIndex(i)
				itemCount = getItemCount(idx)
				if itemCount <= 1:
					itemCount = 0
				setItemID(i, getItemID(idx), itemCount)
	
			wndMgr.RefreshSlot(self.itemSlotWindow.GetWindowHandle())

	if app.ENABLE_OFFLINE_SHOP:
		def RegisterShopSold(self, pos):
			if pos < 0 or not shop.GetItemID(pos):
				return
			item.SelectItem(int(shop.GetItemID(pos)))
			(itemWidth, itemHeight) = item.GetItemSize()
	
			targetSlot = self.itemSlotList["ItemSlot_%d" % self.GridSize]
			imageName = "d:/ymir work/slot_disabled_%d.tga" % itemHeight
	
			targetSlot.SetCoverButton(pos, imageName, imageName, imageName, "d:/ymir work/ui/game/belt_inventory/slot_disabled.tga", False, False)
			targetSlot.EnableSlot(pos)
			wndMgr.RefreshSlot(targetSlot.GetWindowHandle())

		def RefreshMoney(self):
			self.wndMoney.SetText(localeInfo.NumberToMoneyString(shop.GetMoney()))

	def SetItemData(self, pos, itemID, itemCount, itemPrice):
		if app.ENABLE_OFFLINE_SHOP:
			targetSlot = self.itemSlotList["ItemSlot_%d" % self.GridSize]
		shop.SetItemData(pos, itemID, itemCount, itemPrice)
		if app.ENABLE_OFFLINE_SHOP:
			targetSlot.DisableSlot(pos)

	def LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/shopdialog.py")
		except:
			import exception
			exception.Abort("ShopDialog.LoadDialog.LoadObject")

		smallTab1 = None
		smallTab2 = None
		smallTab3 = None
		middleTab1 = None
		middleTab2 = None
		
		try:
			GetObject = self.GetChild
			if app.ENABLE_OFFLINE_SHOP:
				self.board = GetObject("board")
				for i in range(40, 90 + 10, 10):
					self.itemSlotList["ItemSlot_%d" % i] = GetObject("ItemSlot_%d" % i)
					self.itemSlotList["ItemSlot_%d" % i].Hide()
			else:
				self.itemSlotWindow = GetObject("ItemSlot")
			self.btnBuy = GetObject("BuyButton")
			self.btnSell = GetObject("SellButton")
			self.btnClose = GetObject("CloseButton")
			if app.ENABLE_OFFLINE_SHOP:
				self.btnMove = GetObject("MoveButton")
			self.titleBar = GetObject("TitleBar")
			if app.ENABLE_OFFLINE_SHOP:
				self.wndMoney = self.GetChild("Money")
				self.wndMoneySlot = self.GetChild("MoneySlot")
			middleTab1 = GetObject("MiddleTab1")
			middleTab2 = GetObject("MiddleTab2")
			smallTab1 = GetObject("SmallTab1")
			smallTab2 = GetObject("SmallTab2")
			smallTab3 = GetObject("SmallTab3")
		except:
			import exception
			exception.Abort("ShopDialog.LoadDialog.BindObject")

		if app.ENABLE_OFFLINE_SHOP:
			# Store real positions
			self.realWidth, self.realHeight = self.GetWidth(), self.GetHeight()
			self.realBoardWidth, self.realBoardHeight = self.board.GetWidth(), self.board.GetHeight()
			self.realTitleBarX = self.titleBar.GetWidth()
	
			(self.realBuyBtnX, self.realBuyBtnY) = self.btnBuy.GetLocalPosition()
			(self.realSellBtnX, self.realSellBtnY) = self.btnSell.GetLocalPosition()
			(self.realCloseBtnX, self.realCloseBtnY) = self.btnClose.GetLocalPosition()
			(self.realMoveBtnX, self.realMoveBtnY) = self.btnMove.GetLocalPosition()
			(self.realMoneySlotX, self.realMoneySlotY) = self.wndMoneySlot.GetLocalPosition()
	
			self.height = self.GetHeight()
			self.width = self.GetWidth()
		else:
			self.itemSlotWindow.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
			self.itemSlotWindow.SAFE_SetButtonEvent("LEFT", "EMPTY", self.SelectEmptySlot)
			self.itemSlotWindow.SAFE_SetButtonEvent("LEFT", "EXIST", self.SelectItemSlot)
			self.itemSlotWindow.SAFE_SetButtonEvent("RIGHT", "EXIST", self.UnselectItemSlot)
	
			self.itemSlotWindow.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			self.itemSlotWindow.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		self.btnBuy.SetToggleUpEvent(ui.__mem_func__(self.CancelShopping))
		self.btnBuy.SetToggleDownEvent(ui.__mem_func__(self.OnBuy))

		self.btnSell.SetToggleUpEvent(ui.__mem_func__(self.CancelShopping))
		self.btnSell.SetToggleDownEvent(ui.__mem_func__(self.OnSell))

		self.btnClose.SetEvent(ui.__mem_func__(self.AskClosePrivateShop))
		if app.ENABLE_OFFLINE_SHOP:
			self.btnMove.SetEvent(ui.__mem_func__(self.MoveShop))

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

		self.smallRadioButtonGroup = ui.RadioButtonGroup.Create([[smallTab1, lambda : self.OnClickTabButton(0), None], [smallTab2, lambda : self.OnClickTabButton(1), None], [smallTab3, lambda : self.OnClickTabButton(2), None]])
		self.middleRadioButtonGroup = ui.RadioButtonGroup.Create([[middleTab1, lambda : self.OnClickTabButton(0), None], [middleTab2, lambda : self.OnClickTabButton(1), None]])

		self.__HideMiddleTabs()
		self.__HideSmallTabs()
		
		self.tabIdx = 0
		self.coinType = shop.SHOP_COIN_TYPE_GOLD
		if app.ENABLE_OFFLINE_SHOP:
			shop.ClearPrivateShopStock()

		self.Refresh()
	
	def __ShowBuySellButton(self):
		self.btnBuy.Show()
		self.btnSell.Show()
		
	def __ShowMiddleTabs(self):
		self.middleRadioButtonGroup.Show()
	
	def __ShowSmallTabs(self):
		self.smallRadioButtonGroup.Show()
	
	def __HideBuySellButton(self):
		self.btnBuy.Hide()
		self.btnSell.Hide()
	
	def __HideMiddleTabs(self):
		self.middleRadioButtonGroup.Hide()
	
	def __HideSmallTabs(self):
		self.smallRadioButtonGroup.Hide()
		
	def __SetTabNames(self):
		if shop.GetTabCount() == 2:
			self.middleRadioButtonGroup.SetText(0, shop.GetTabName(0))
			self.middleRadioButtonGroup.SetText(1, shop.GetTabName(1))
		elif shop.GetTabCount() == 3:
			self.smallRadioButtonGroup.SetText(0, shop.GetTabName(0))
			self.smallRadioButtonGroup.SetText(1, shop.GetTabName(1))
			self.smallRadioButtonGroup.SetText(2, shop.GetTabName(2))
	 
 
	def Destroy(self):
		self.Close()
		self.ClearDictionary()
		if app.ENABLE_OFFLINE_SHOP:
			constInfo.SHOP_LAST_VID = 0

		self.tooltipItem = 0
		self.itemSlotWindow = 0
		if app.ENABLE_OFFLINE_SHOP:
			self.GridSize = 0
			for i in range(40, 90 + 10, 10):
				if self.itemSlotList["ItemSlot_%d" % i]:
					del self.itemSlotList["ItemSlot_%d" % i]
			self.itemSlotList.clear()
			self.itemSlotList = None
	
			self.board = 0
		else:
			self.itemSlotWindow = 0

		self.btnBuy = 0
		self.btnSell = 0
		self.btnClose = 0
		if app.ENABLE_OFFLINE_SHOP:
			self.btnMove = 0
		self.titleBar = 0
		if app.ENABLE_OFFLINE_SHOP:
			self.wndMoney = 0
			self.wndMoneySlot = 0
		self.questionDialog = None
		self.popup = None

	if app.ENABLE_OFFLINE_SHOP:
		def Open(self, vid, owner_vid, grid_type):
	
			isPrivateShop = False
			isMainPlayerPrivateShop = False
			
			self.isMyShop = owner_vid > 0 and player.IsMainCharacterIndex(owner_vid)
			self.lastShopVID = vid
			
			if chr.IsNPC(vid) and owner_vid == 0:
				isPrivateShop = False
			else:
				isPrivateShop = True
	
			if isPrivateShop:
				self.GridSize = self.SizeToGridSize[grid_type]
			else:
				self.GridSize = 40
	
			for i in range(40, 90 + 10, 10):
				if self.itemSlotList["ItemSlot_%d" % i].IsShow():
					self.itemSlotList["ItemSlot_%d" % i].Hide()
	
			self.SetSize(self.realWidth, self.realHeight)	
			self.board.SetSize(self.realBoardWidth, self.realBoardHeight)
			self.titleBar.SetWidth(self.realTitleBarX)
			
			self.btnBuy.SetPosition(self.realBuyBtnX, self.realBuyBtnY)
			self.btnSell.SetPosition(self.realSellBtnX, self.realSellBtnY)
			self.btnMove.SetPosition(self.realMoveBtnX, self.realMoveBtnY)
			self.btnClose.SetPosition(self.realCloseBtnX, self.realCloseBtnY)
			self.wndMoneySlot.SetPosition(self.realMoneySlotX, self.realMoneySlotY)
		
	
			if self.btnBuy.IsShow(): self.btnBuy.Hide()
			if self.btnSell.IsShow(): self.btnSell.Hide()
			if self.btnMove.IsShow(): self.btnMove.Hide()
			if self.btnClose.IsShow(): self.btnClose.Hide()
			if self.wndMoneySlot.IsShow(): self.wndMoneySlot.Hide()
	
	
			self.itemSlotList["ItemSlot_%d" % self.GridSize].Show()
			self.itemSlotList["ItemSlot_%d" % self.GridSize].SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
			self.itemSlotList["ItemSlot_%d" % self.GridSize].SAFE_SetButtonEvent("LEFT", "EMPTY", self.SelectEmptySlot)
			self.itemSlotList["ItemSlot_%d" % self.GridSize].SAFE_SetButtonEvent("LEFT", "EXIST", self.SelectItemSlot)
			self.itemSlotList["ItemSlot_%d" % self.GridSize].SAFE_SetButtonEvent("RIGHT", "EXIST", self.UnselectItemSlot)
	
			self.itemSlotList["ItemSlot_%d" % self.GridSize].SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			self.itemSlotList["ItemSlot_%d" % self.GridSize].SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
	
			if player.IsMainCharacterIndex(vid) or self.isMyShop or (chr.IsGameMaster(player.GetMainCharacterIndex()) and isPrivateShop):
				isMainPlayerPrivateShop = True
	
				self.btnBuy.Hide()
				self.btnSell.Hide()
				self.btnClose.Show()
				if self.isMyShop:
					self.btnMove.Show()
				self.wndMoneySlot.Show()
	
				self.SetSize(self.width, self.height + 16)
				self.board.SetSize(self.width, self.height + 16)
				self.UpdateRect()
			else:
	
				isMainPlayerPrivateShop = False
	
				self.btnBuy.Show()
				self.btnSell.Show()
				self.btnClose.Hide()
				self.btnMove.Hide()
				self.wndMoneySlot.Hide()
	
				self.SetSize(self.width, self.height)
				self.board.SetSize(self.width, self.height)
				self.UpdateRect()
			
			shop.Open(isPrivateShop, isMainPlayerPrivateShop)
	
			self.tabIdx = 0
	
			heightDifference = 80
			widthDifferenceBase = 32
			btnDifference = 20
			gridSizeToWindowPos = grid_type - 1
			fixDifference = 14
	
			if self.GridSize >= 50:
				self.SetSize(self.realWidth + widthDifferenceBase * gridSizeToWindowPos, self.realHeight + heightDifference)	
				self.board.SetSize(self.realBoardWidth + widthDifferenceBase * gridSizeToWindowPos, self.realBoardHeight + heightDifference)
				if self.GridSize != 50:
					self.titleBar.SetWidth(self.realTitleBarX + widthDifferenceBase * gridSizeToWindowPos)
					self.wndMoneySlot.SetPosition(self.realMoneySlotX * gridSizeToWindowPos, self.realMoneySlotY + heightDifference - fixDifference)
				else:
					self.wndMoneySlot.SetPosition(self.realMoneySlotX, self.realMoneySlotY + heightDifference - fixDifference)
				self.btnBuy.SetPosition(self.realBuyBtnX + btnDifference, self.realBuyBtnY + heightDifference)
				self.btnSell.SetPosition(self.realSellBtnX + btnDifference, self.realSellBtnY + heightDifference)
				self.btnMove.SetPosition(self.realMoveBtnX + btnDifference - fixDifference, self.realMoveBtnY + heightDifference - fixDifference)
				self.btnClose.SetPosition(self.realCloseBtnX + btnDifference, self.realCloseBtnY + heightDifference - fixDifference)
			
	
			#self.UpdateRect()
			if isPrivateShop:
				self.__HideMiddleTabs()
				self.__HideSmallTabs()
			else:
				if shop.GetTabCount() == 1:
					self.__ShowBuySellButton()
					self.__HideMiddleTabs()
					self.__HideSmallTabs()
				elif shop.GetTabCount() == 2:
					self.__HideBuySellButton()
					self.__ShowMiddleTabs()
					self.__HideSmallTabs()
					self.__SetTabNames()
					self.middleRadioButtonGroup.OnClick(0)
				elif shop.GetTabCount() == 3:
					self.__HideBuySellButton()
					self.__HideMiddleTabs()
					self.__ShowSmallTabs()
					self.__SetTabNames()
					self.middleRadioButtonGroup.OnClick(1)
	
			self.Refresh()
			self.SetTop()
	
			self.Show()
	
			(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()
	else:
		def Open(self, vid):
	
			isPrivateShop = False
			isMainPlayerPrivateShop = False
	
			if chr.IsNPC(vid):
				isPrivateShop = False
			else:
				isPrivateShop = True
	
			if player.IsMainCharacterIndex(vid):
	
				isMainPlayerPrivateShop = True
	
				self.btnBuy.Hide()
				self.btnSell.Hide()
				self.btnClose.Show()
	
			else:
	
				isMainPlayerPrivateShop = False
	
				self.btnBuy.Show()
				self.btnSell.Show()
				self.btnClose.Hide()
	
			shop.Open(isPrivateShop, isMainPlayerPrivateShop)
	
			self.tabIdx = 0
	
			if isPrivateShop:
				self.__HideMiddleTabs()
				self.__HideSmallTabs()
			else:
				if shop.GetTabCount() == 1:
					self.__ShowBuySellButton()
					self.__HideMiddleTabs()
					self.__HideSmallTabs()
				elif shop.GetTabCount() == 2:
					self.__HideBuySellButton()
					self.__ShowMiddleTabs()
					self.__HideSmallTabs()
					self.__SetTabNames()
					self.middleRadioButtonGroup.OnClick(0)
				elif shop.GetTabCount() == 3:
					self.__HideBuySellButton()
					self.__HideMiddleTabs()
					self.__ShowSmallTabs()
					self.__SetTabNames()
					self.middleRadioButtonGroup.OnClick(1)
	
			self.Refresh()
			self.SetTop()
	
			self.Show()
	
			(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()

	def Close(self):
		if app.ENABLE_OFFLINE_SHOP:
			if constInfo.SHOP_MOVE_FLAG:
				return
		if self.itemBuyQuestionDialog:
			self.itemBuyQuestionDialog.Close()
			self.itemBuyQuestionDialog = None		
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
		if self.questionDialog:
			self.OnCloseQuestionDialog()
		shop.Close()
		net.SendShopEndPacket()
		self.CancelShopping()
		self.tooltipItem.HideToolTip()
		self.Hide()

	def GetIndexFromSlotPos(self, slotPos):
		return self.tabIdx * shop.SHOP_SLOT_COUNT + slotPos
		
	def OnClickTabButton(self, idx):
		self.tabIdx = idx
		self.Refresh()
		
	def AskClosePrivateShop(self):
		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.PRIVATE_SHOP_CLOSE_QUESTION)
		questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnClosePrivateShop))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		questionDialog.Open()
		self.questionDialog = questionDialog

		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

		return True

	def OnClosePrivateShop(self):
		if app.ENABLE_OFFLINE_SHOP and constInfo.SHOP_MOVE_FLAG:
			return
		net.SendChatPacket("/close_shop")
		self.OnCloseQuestionDialog()
		return True
	if app.ENABLE_OFFLINE_SHOP:
		def MoveShop(self):
			if constInfo.SHOP_MOVE_FLAG == 1:
				return
			if not self.isMyShop:
				return
			
			net.SetShopMoveMode(1)
			constInfo.SHOP_LAST_VID = self.lastShopVID
			constInfo.SHOP_MOVE_FLAG = 1

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnPressExitKey(self):
		self.Close()
		return True

	def OnBuy(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_BUY_INFO)
		app.SetCursor(app.BUY)
		self.btnSell.SetUp()

	def OnSell(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_SELL_INFO)
		app.SetCursor(app.SELL)
		self.btnBuy.SetUp()

	def CancelShopping(self):
		self.btnBuy.SetUp()
		self.btnSell.SetUp()
		app.SetCursor(app.NORMAL)

	def __OnClosePopupDialog(self):
		self.pop = None
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

	## ¿ëÈ¥¼® ÆÈ¸®´Â ±â´É Ãß°¡.
	def SellAttachedItem(self):

		if shop.IsPrivateShop():
			mouseModule.mouseController.DeattachObject()
			return

		attachedSlotType = mouseModule.mouseController.GetAttachedType()
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		attachedCount = mouseModule.mouseController.GetAttachedItemCount()
		
		if player.SLOT_TYPE_INVENTORY == attachedSlotType or player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedSlotType:

			item.SelectItem(attachedItemIndex)
			
			if item.IsAntiFlag(item.ANTIFLAG_SELL):
				popup = uiCommon.PopupDialog()
				popup.SetText(localeInfo.SHOP_CANNOT_SELL_ITEM)
				popup.SetAcceptEvent(self.__OnClosePopupDialog)
				popup.Open()
				self.popup = popup
				return
				
			itemtype = player.INVENTORY
			
			if player.IsValuableItem(itemtype, attachedSlotPos):

				itemPrice = player.GetISellItemPrice(attachedSlotPos)

				itemName = item.GetItemName()

				questionDialog = uiCommon.QuestionDialog()
				questionDialog.SetText(localeInfo.DO_YOU_SELL_ITEM(itemName, attachedCount, itemPrice))

				questionDialog.SetAcceptEvent(lambda arg1=attachedSlotPos, arg2=attachedCount, arg3 = itemtype: self.OnSellItem(arg1, arg2, arg3))
				questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
				questionDialog.Open()
				self.questionDialog = questionDialog
		
				constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

			else:
				self.OnSellItem(attachedSlotPos, attachedCount, itemtype)

		else:
			snd.PlaySound("sound/ui/loginfail.wav")

		mouseModule.mouseController.DeattachObject()

	def OnSellItem(self, slotPos, count, itemtype):
		net.SendShopSellPacketNew(slotPos, count, itemtype)
		snd.PlaySound("sound/ui/money.wav")
		self.OnCloseQuestionDialog()

	def OnCloseQuestionDialog(self):
		if not self.questionDialog:
			return
			
		self.questionDialog.Close()
		self.questionDialog = None
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

	def SelectEmptySlot(self, selectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			self.SellAttachedItem()

	def UnselectItemSlot(self, selectedSlotPos):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return
		if shop.IsPrivateShop():
			self.AskBuyItem(selectedSlotPos)
		else:
			if app.ENABLE_OFFLINE_SHOP:
				net.SendShopBuyPacket(selectedSlotPos)
			else:
				net.SendShopBuyPacket(self.__GetRealIndex(selectedSlotPos))

	def SelectItemSlot(self, selectedSlotPos):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return

		isAttached = mouseModule.mouseController.isAttached()
		selectedSlotPos = self.__GetRealIndex(selectedSlotPos)
		if isAttached:
			self.SellAttachedItem()

		else:

			if shop.IsMainPlayerPrivateShop():
				return

			curCursorNum = app.GetCursor()
			if app.BUY == curCursorNum:
				self.AskBuyItem(selectedSlotPos)

			elif app.SELL == curCursorNum:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_SELL_INFO)

			else:
				selectedItemID = shop.GetItemID(selectedSlotPos)
				itemCount = shop.GetItemCount(selectedSlotPos)

				type = player.SLOT_TYPE_SHOP
				if shop.IsPrivateShop():
					type = player.SLOT_TYPE_PRIVATE_SHOP

				mouseModule.mouseController.AttachObject(self, type, selectedSlotPos, selectedItemID, itemCount)
				mouseModule.mouseController.SetCallBack("INVENTORY", ui.__mem_func__(self.DropToInventory))
				snd.PlaySound("sound/ui/pick.wav")

	def DropToInventory(self):
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		self.AskBuyItem(attachedSlotPos)

	def AskBuyItem(self, slotPos):
		if not app.ENABLE_OFFLINE_SHOP:
			slotPos = self.__GetRealIndex(slotPos)

		itemIndex = shop.GetItemID(slotPos)
		itemPrice = shop.GetItemPrice(slotPos)
		if app.ENABLE_OFFLINE_SHOP:
			itemPriceTwo = shop.GetItemPrice2(slotPos)
			itemPriceThree = shop.GetItemPrice3(slotPos)
			itemPriceFour = shop.GetItemPrice4(slotPos)
		itemCount = shop.GetItemCount(slotPos)

		item.SelectItem(itemIndex)
		itemName = item.GetItemName()

		if app.ENABLE_OFFLINE_SHOP:
			if not itemPriceTwo and not itemPriceThree and not itemPriceFour:
				itemBuyQuestionDialog = uiCommon.QuestionDialog()
				itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, itemPrice))
			else:
				itemBuyQuestionDialog = uiCommon.QuestionDialog2()
				itemBuyQuestionDialog.SetText1(localeInfo.DO_YOU_BUY_ITEM_NEW(itemName, itemCount, localeInfo.NumberToMoneyString(itemPrice), localeInfo.NumberToPriceString(itemPriceTwo, "Coin"), localeInfo.NumberToPriceString(itemPriceThree, "Goldbar"), localeInfo.NumberToPriceString(itemPriceFour, "Won"))[0])	
				itemBuyQuestionDialog.SetText2(localeInfo.DO_YOU_BUY_ITEM_NEW(itemName, itemCount, localeInfo.NumberToMoneyString(itemPrice), localeInfo.NumberToPriceString(itemPriceTwo, "Coin"), localeInfo.NumberToPriceString(itemPriceThree, "Goldbar"), localeInfo.NumberToPriceString(itemPriceFour, "Won"))[1])
		else:
			itemBuyQuestionDialog = uiCommon.QuestionDialog()
			itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToMoneyString(itemPrice)))

		itemBuyQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerBuyItem(arg))
		if app.ENABLE_OFFLINE_SHOP:
			if itemPriceTwo or itemPriceThree or itemPriceFour:
				itemBuyQuestionDialog.SetWidth(550)
		itemBuyQuestionDialog.Open()
		itemBuyQuestionDialog.pos = slotPos
		self.itemBuyQuestionDialog = itemBuyQuestionDialog

		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

	def AnswerBuyItem(self, flag):

		if flag:
			pos = self.itemBuyQuestionDialog.pos
			net.SendShopBuyPacket(pos)

		self.itemBuyQuestionDialog.Close()
		self.itemBuyQuestionDialog = None
		
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def OverInItem(self, slotIndex):
		if not app.ENABLE_OFFLINE_SHOP:
			slotIndex = self.__GetRealIndex(slotIndex)

		if mouseModule.mouseController.isAttached():
			return

		if 0 != self.tooltipItem:
			if app.ENABLE_OFFLINE_SHOP:
				IsPc = shop.IsPrivateShop()
				self.tooltipItem.SetShopItem(IsPc, slotIndex)
			else:
				if shop.SHOP_COIN_TYPE_GOLD == shop.GetTabCoinType(self.tabIdx):
					self.tooltipItem.SetShopItem(slotIndex)
				else:
					self.tooltipItem.SetShopItemBySecondaryCoin(slotIndex)
	def OverOutItem(self):
		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnUpdate(self):

		USE_SHOP_LIMIT_RANGE = 1000

		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xShopStart) > USE_SHOP_LIMIT_RANGE or abs(y - self.yShopStart) > USE_SHOP_LIMIT_RANGE:
			self.Close()


class MallPageDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearDictionary()

	def Open(self):
		scriptLoader = ui.PythonScriptLoader()
		scriptLoader.LoadScriptFile(self, "uiscript/mallpagedialog.py")

		self.GetChild("titlebar").SetCloseEvent(ui.__mem_func__(self.Close))
		
		(x, y)=self.GetGlobalPosition()
		x+=10
		y+=30
		
		MALL_PAGE_WIDTH = 600
		MALL_PAGE_HEIGHT = 480
		
		app.ShowWebPage(
			"http://metin2.co.kr/08_mall/game_mall/login_fail.htm", 
			(x, y, x+MALL_PAGE_WIDTH, y+MALL_PAGE_HEIGHT))

		self.Lock()
		self.Show()
		
	def Close(self):			
		app.HideWebPage()
		self.Unlock()
		self.Hide()
		
	def OnPressEscapeKey(self):
		self.Close()
		return True
