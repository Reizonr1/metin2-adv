Search:
import constInfo

Add it under:
import chr

---

Search:
class ShopDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			self.SizeToGridSize = { 0: 40, 1: 50, 2: 60, 3: 70, 4: 80, 5: 90 }
			self.itemSlotList = { }
			self.GridSize = 40

https://puu.sh/sgTbD/ade0603d23.png

---

Search:
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

Change:

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


https://puu.sh/sgTfh/e0d9780026.png
https://puu.sh/sgTeR/6df80a60db.png

---

Search:
	def SetItemData(self, pos, itemID, itemCount, itemPrice):
		shop.SetItemData(pos, itemID, itemCount, itemPrice)

Change:
	def SetItemData(self, pos, itemID, itemCount, itemPrice):
		if app.ENABLE_OFFLINE_SHOP:
			targetSlot = self.itemSlotList["ItemSlot_%d" % self.GridSize]
		shop.SetItemData(pos, itemID, itemCount, itemPrice)
		if app.ENABLE_OFFLINE_SHOP:
			targetSlot.DisableSlot(pos)

https://puu.sh/sgThv/53c408ff02.png

---

Search:
			self.itemSlotWindow = GetObject("ItemSlot")

Change:
			if app.ENABLE_OFFLINE_SHOP:
				self.board = GetObject("board")
				for i in range(40, 90 + 10, 10):
					self.itemSlotList["ItemSlot_%d" % i] = GetObject("ItemSlot_%d" % i)
					self.itemSlotList["ItemSlot_%d" % i].Hide()
			else:
				self.itemSlotWindow = GetObject("ItemSlot")


Search:
			self.btnClose = GetObject("CloseButton")

Add it under:
			if app.ENABLE_OFFLINE_SHOP:
				self.btnMove = GetObject("MoveButton")


Search:
			self.titleBar = GetObject("TitleBar")

Add it under:
			if app.ENABLE_OFFLINE_SHOP:
				self.wndMoney = self.GetChild("Money")
				self.wndMoneySlot = self.GetChild("MoneySlot")


https://puu.sh/sgTlF/8db56a8e65.png

---

Search:
		self.itemSlotWindow.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		self.itemSlotWindow.SAFE_SetButtonEvent("LEFT", "EMPTY", self.SelectEmptySlot)
		self.itemSlotWindow.SAFE_SetButtonEvent("LEFT", "EXIST", self.SelectItemSlot)
		self.itemSlotWindow.SAFE_SetButtonEvent("RIGHT", "EXIST", self.UnselectItemSlot)

		self.itemSlotWindow.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.itemSlotWindow.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))


Change:
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


https://puu.sh/sgTov/aaad9286b3.png

---

Search:
		self.btnClose.SetEvent(ui.__mem_func__(self.AskClosePrivateShop))

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			self.btnMove.SetEvent(ui.__mem_func__(self.MoveShop))

https://puu.sh/sgTrr/445f62be37.png

---

Search:
		self.coinType = shop.SHOP_COIN_TYPE_GOLD

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			shop.ClearPrivateShopStock()

https://puu.sh/sgTtl/55c07ad042.png

---

Search:
	def Destroy(self):
		self.Close()
		self.ClearDictionary()

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			constInfo.SHOP_LAST_VID = 0


Search:
		self.itemSlotWindow = 0

Change:
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


https://puu.sh/sgTxz/a64b74112f.png

---

Search:
		self.btnClose = 0

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			self.btnMove = 0


Search:
		self.titleBar = 0

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			self.wndMoney = 0
			self.wndMoneySlot = 0


https://puu.sh/sgTAK/8fe60448ac.png

---

Search:
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

Change:
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


https://puu.sh/sgTEj/3bc152d2f7.png
https://puu.sh/sgTEU/10715b1e3a.png

---

Search:
	def Close(self):

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			if constInfo.SHOP_MOVE_FLAG:
				return

https://puu.sh/sgTGc/397de11f94.png

---

Search:
	def OnClosePrivateShop(self):
		net.SendChatPacket("/close_shop")
		self.OnCloseQuestionDialog()
		return True

Change:
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


https://puu.sh/sgTIr/85eced4664.png

---

Search:
				itemPrice = item.GetISellItemPrice()

				if item.Is1GoldItem():
					itemPrice = attachedCount / itemPrice / 5
				else:
					itemPrice = itemPrice * max(1, attachedCount) / 5

Change:
				itemPrice = player.GetISellItemPrice(attachedSlotPos)

https://puu.sh/sgTKW/65eb0dca64.png

---

Search:
	def UnselectItemSlot(self, selectedSlotPos):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return
		if shop.IsPrivateShop():
			self.AskBuyItem(selectedSlotPos)
		else:
			net.SendShopBuyPacket(self.__GetRealIndex(selectedSlotPos))

Change:
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


https://puu.sh/sgTMB/f08c7533cf.png

---

Search:
	def AskBuyItem(self, slotPos):
		slotPos = self.__GetRealIndex(slotPos)

		itemIndex = shop.GetItemID(slotPos)
		itemPrice = shop.GetItemPrice(slotPos)
		itemCount = shop.GetItemCount(slotPos)

		item.SelectItem(itemIndex)
		itemName = item.GetItemName()

		itemBuyQuestionDialog = uiCommon.QuestionDialog()
		itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToMoneyString(itemPrice)))
		itemBuyQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.Open()
		itemBuyQuestionDialog.pos = slotPos
		self.itemBuyQuestionDialog = itemBuyQuestionDialog

		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

Change:
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


https://puu.sh/sgTTc/1ef2664fe6.png

---

Search:
	def OverInItem(self, slotIndex):
		slotIndex = self.__GetRealIndex(slotIndex)
		if mouseModule.mouseController.isAttached():
			return

		if 0 != self.tooltipItem:
			if shop.SHOP_COIN_TYPE_GOLD == shop.GetTabCoinType(self.tabIdx):
				self.tooltipItem.SetShopItem(slotIndex)
			else:
				self.tooltipItem.SetShopItemBySecondaryCoin(slotIndex)

Change:
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

https://puu.sh/sgTUP/b9de5206cc.png





























