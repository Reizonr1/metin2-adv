Search:
import systemSetting #±èÁØÈ£

Add it under:
import constInfo
import app

---

Search:
class PrivateShopAdvertisementBoard(ui.ThinBoard):
	def __init__(self):
		ui.ThinBoard.__init__(self, "UI_BOTTOM")

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			self.shopAdvertismentBoardSeen = []

https://puu.sh/sgUqg/c9a819bb49.png

---

Search:
	def Open(self, vid, text):
		self.vid = vid

		self.textLine.SetText(text)
		self.textLine.UpdateRect()
		self.SetSize(len(text)*6 + 10*2, 20)


Change:
	def Open(self, vid, text):
		self.vid = vid

		self.textLine.SetText(text)
		if app.ENABLE_OFFLINE_SHOP:
			if vid in self.shopAdvertismentBoardSeen:
				self.textLine.SetPackedFontColor(0xFF00C8FF)
			self.textLine.UpdateRect()
			textWidth, textHeight = self.textLine.GetTextSize()
			self.SetSize(textWidth + 12*2, 36)
		else:
			self.textLine.UpdateRect()
			self.SetSize(len(text)*6 + 10*2, 20)


https://puu.sh/sgUs6/7427787064.png

---

Search:
	def OnMouseLeftButtonUp(self):
		if not self.vid:
			return
		net.SendOnClickPacket(self.vid)

		return True

Change:
	def OnMouseLeftButtonUp(self):
		if not self.vid:
			return
		net.SendOnClickPacket(self.vid)
		if app.ENABLE_OFFLINE_SHOP:
			if self.vid != player.GetMainCharacterIndex():
				self.textLine.SetPackedFontColor(0xFF00C8FF)
				self.shopAdvertismentBoardSeen.append(self.vid)
		return True

https://puu.sh/sgUtY/5e446c0f34.png

---

Search:
class PrivateShopBuilder(ui.ScriptWindow):

	def __init__(self):
		#print "NEW MAKE_PRIVATE_SHOP_WINDOW ----------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)

		self.__LoadWindow()
		self.itemStock = {}
		self.tooltipItem = None
		self.priceInputBoard = None
		self.title = ""

Change:

class PrivateShopBuilder(ui.ScriptWindow):
	if app.ENABLE_OFFLINE_SHOP:
		def __init__(self, wndInventory):
			#print "NEW MAKE_PRIVATE_SHOP_WINDOW ----------------------------------------------------------------"
			ui.ScriptWindow.__init__(self)
	
			self.SizeToGridSize = { 0: 40, 1: 50, 2: 60, 3: 70, 4: 80, 5: 90 }
			self.itemSlotList = { }
			self.wndInventory = wndInventory
			self.__LoadWindow()
			self.itemStock = {}
			self.tooltipItem = None
			self.priceInputBoard = None
			self.title = ""
			self.type = 0
			self.size = 0
			self.color = 0
			self.popup = None
	else:
		def __init__(self):
			#print "NEW MAKE_PRIVATE_SHOP_WINDOW ----------------------------------------------------------------"
			ui.ScriptWindow.__init__(self)
	
			self.__LoadWindow()
			self.itemStock = {}
			self.tooltipItem = None
			self.priceInputBoard = None
			self.title = ""

https://puu.sh/sgUww/d6da387d54.png
https://puu.sh/sgUwT/273201926e.png

---

Search:
			GetObject = self.GetChild
			self.nameLine = GetObject("NameLine")
			self.itemSlot = GetObject("ItemSlot")
			self.btnOk = GetObject("OkButton")
			self.btnClose = GetObject("CloseButton")
			self.titleBar = GetObject("TitleBar")

Change:
			GetObject = self.GetChild
			if app.ENABLE_OFFLINE_SHOP:
				self.Board = GetObject("board")
			self.nameLine = GetObject("NameLine")
			if app.ENABLE_OFFLINE_SHOP:
				for i in range(40, 90 + 10, 10):
					self.itemSlotList["ItemSlot_%d" % i] = GetObject("ItemSlot_%d" % i)
					self.itemSlotList["ItemSlot_%d" % i].Hide()
			else:
				self.itemSlot = GetObject("ItemSlot")
			self.btnOk = GetObject("OkButton")
			self.btnClose = GetObject("CloseButton")
			if app.ENABLE_OFFLINE_SHOP:
				self.nameSlot = GetObject("NameSlot")
			self.titleBar = GetObject("TitleBar")

https://puu.sh/sgUz5/2774faed00.png

---

Search:
		self.itemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.OnSelectEmptySlot))
		self.itemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.OnSelectItemSlot))
		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.OnOverInItem))
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))

Change:
		if app.ENABLE_OFFLINE_SHOP:
			# Store real positions
			self.realWidth, self.realHeight = self.GetWidth(), self.GetHeight()
			self.realBoardWidth, self.realBoardHeight = self.Board.GetWidth(), self.Board.GetHeight()
			self.realNameSlotX, self.realNameSlotY = self.nameSlot.GetWidth(), self.nameSlot.GetHeight()
			(self.realNameSlotPosX, self.realNameSlotPosY) = self.nameSlot.GetLocalPosition()
			self.realTitleBarX = self.titleBar.GetWidth()
			(self.okBtnRealX, self.okBtnRealY) = self.btnOk.GetLocalPosition()
			(self.closeBtnRealX, self.closeBtnRealY) = self.btnClose.GetLocalPosition()
		else:
			self.itemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.OnSelectEmptySlot))
			self.itemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.OnSelectItemSlot))
			self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.OnOverInItem))
			self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))

https://puu.sh/sgUAR/f1f03440c5.png

---

Search:
	def Destroy(self):
		self.ClearDictionary()

		self.nameLine = None
		self.itemSlot = None
		self.btnOk = None
		self.btnClose = None
		self.titleBar = None
		self.priceInputBoard = None

Change:
	def Destroy(self):
		self.ClearDictionary()

		self.nameLine = None
		if app.ENABLE_OFFLINE_SHOP:
			for i in range(40, 90 + 10, 10):
				if self.itemSlotList["ItemSlot_%d" % i]:
					del self.itemSlotList["ItemSlot_%d" % i]
			self.itemSlotList.clear()
			self.itemSlotList = None
		else:
			self.itemSlot = None

		self.btnOk = None
		self.btnClose = None
		self.titleBar = None
		if app.ENABLE_OFFLINE_SHOP:
			self.nameSlot = None
		self.priceInputBoard = None
		if app.ENABLE_OFFLINE_SHOP:
			self.popup = None

https://puu.sh/sgUEs/ddd78791cc.png
---

Search:
	def Open(self, title):

		self.title = title

		if len(title) > 25:
			title = title[:22] + "..."

		self.itemStock = {}
		shop.ClearPrivateShopStock()
		self.nameLine.SetText(title)
		self.SetCenterPosition()
		self.Refresh()
		self.Show()

		global g_isBuildingPrivateShop
		g_isBuildingPrivateShop = True

Change:
	if app.ENABLE_OFFLINE_SHOP:
		def Open(self, title, type, size, color):
	
			self.title = title
			self.type = type
			self.size = size
			self.color = color
	
			self.SetSize(self.realWidth, self.realHeight)	
			self.Board.SetSize(self.realBoardWidth, self.realBoardHeight)
			self.titleBar.SetWidth(self.realTitleBarX)
			self.btnOk.SetPosition(self.okBtnRealX, self.okBtnRealY)
			self.btnClose.SetPosition(self.closeBtnRealX, self.closeBtnRealY)
			self.nameSlot.SetPosition(self.realNameSlotPosX, self.realNameSlotPosY)
			self.nameSlot.SetSize(self.realNameSlotX, self.realNameSlotY)
	
			for i in range(40, 90 + 10, 10):
				if self.itemSlotList["ItemSlot_%d" % i].IsShow():
					self.itemSlotList["ItemSlot_%d" % i].Hide()
	
			gridSize = self.SizeToGridSize[self.size]
			self.itemSlotList["ItemSlot_%d" % gridSize].Show()
			self.itemSlotList["ItemSlot_%d" % gridSize].SetSelectEmptySlotEvent(ui.__mem_func__(self.OnSelectEmptySlot))
			self.itemSlotList["ItemSlot_%d" % gridSize].SetSelectItemSlotEvent(ui.__mem_func__(self.OnSelectItemSlot))
			self.itemSlotList["ItemSlot_%d" % gridSize].SetOverInItemEvent(ui.__mem_func__(self.OnOverInItem))
			self.itemSlotList["ItemSlot_%d" % gridSize].SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))	
	
			if len(title) > 25:
				title = title[:22] + "..."
	
			self.itemStock = {}
			shop.ClearPrivateShopStock()
			self.nameLine.SetText(title)
			self.SetCenterPosition()
			self.Refresh()
			self.Show()
	
			heightDifference = 70
			widthDifferenceBase = 32
			btnDifference = 20
			gridSizeToWindowPos = self.size - 1
	
			if gridSize == 50:
				self.SetSize(self.realWidth, self.realHeight + heightDifference)	
				self.Board.SetSize(self.realBoardWidth, self.realBoardHeight + heightDifference)	
				self.btnOk.SetPosition(self.okBtnRealX, self.okBtnRealY + heightDifference)
				self.btnClose.SetPosition(self.closeBtnRealX, self.closeBtnRealY + heightDifference)
	
			elif gridSize >= 60:
				self.SetSize(self.realWidth + widthDifferenceBase * gridSizeToWindowPos, self.realHeight + heightDifference)	
				self.Board.SetSize(self.realBoardWidth + widthDifferenceBase * gridSizeToWindowPos, self.realBoardHeight + heightDifference)
				self.nameSlot.SetSize(self.realNameSlotX + widthDifferenceBase * gridSizeToWindowPos, self.realNameSlotY)
				self.titleBar.SetWidth(self.realTitleBarX + widthDifferenceBase * gridSizeToWindowPos)
				self.btnOk.SetPosition(self.okBtnRealX + btnDifference * gridSizeToWindowPos, self.okBtnRealY + heightDifference)
				self.btnClose.SetPosition(self.closeBtnRealX + btnDifference * gridSizeToWindowPos, self.closeBtnRealY + heightDifference)
	
			global g_isBuildingPrivateShop
			g_isBuildingPrivateShop = True
	else:
		def Open(self, title):
			self.title = title
	
			if len(title) > 25:
				title = title[:22] + "..."
	
			self.itemStock = {}
			shop.ClearPrivateShopStock()
			self.nameLine.SetText(title)
			self.SetCenterPosition()
			self.Refresh()
			self.Show()
	
			global g_isBuildingPrivateShop
			g_isBuildingPrivateShop = True


https://puu.sh/sgUJL/d88fee48a4.png
https://puu.sh/sgUKq/44acc3b157.png

---

Search:
	def Close(self):
		global g_isBuildingPrivateShop
		g_isBuildingPrivateShop = False

		self.title = ""
		self.itemStock = {}
		shop.ClearPrivateShopStock()
		self.Hide()

Change:
	def Close(self):
		global g_isBuildingPrivateShop
		g_isBuildingPrivateShop = False

		self.title = ""
		if app.ENABLE_OFFLINE_SHOP:
			self.type = 0
			self.size = 0
			self.color = 0
		self.itemStock = {}
		shop.ClearPrivateShopStock()
		self.Hide()
		if app.ENABLE_OFFLINE_SHOP:
			self.wndInventory.RefreshBagSlotWindow()

https://puu.sh/sgUPy/8050cb5c06.png
---

Search:
	def Refresh(self):
		getitemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setitemVNum=self.itemSlot.SetItemSlot
		delItem=self.itemSlot.ClearSlot

		for i in xrange(shop.SHOP_SLOT_COUNT):

			if not self.itemStock.has_key(i):
				delItem(i)
				continue

			pos = self.itemStock[i]

			itemCount = getItemCount(*pos)
			if itemCount <= 1:
				itemCount = 0
			setitemVNum(i, getitemVNum(*pos), itemCount)

		self.itemSlot.RefreshSlot()

Change:
	def Refresh(self):
		getitemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		if app.ENABLE_OFFLINE_SHOP:
			gridSize = self.SizeToGridSize[self.size]
			setitemVNum=self.itemSlotList["ItemSlot_%d" % gridSize].SetItemSlot
			delItem=self.itemSlotList["ItemSlot_%d" % gridSize].ClearSlot
	
			for i in xrange(int(gridSize)):
				if not self.itemStock.has_key(i):
					delItem(i)
					continue
	
				pos = self.itemStock[i]
	
				itemCount = getItemCount(*pos)
				if itemCount <= 1:
					itemCount = 0
				setitemVNum(i, getitemVNum(*pos), itemCount)

		else:
			setitemVNum=self.itemSlot.SetItemSlot
			delItem=self.itemSlot.ClearSlot

			for i in xrange(shop.SHOP_SLOT_COUNT):

				if not self.itemStock.has_key(i):
					delItem(i)
					continue
	
				pos = self.itemStock[i]
	
				itemCount = getItemCount(*pos)
				if itemCount <= 1:
					itemCount = 0
				setitemVNum(i, getitemVNum(*pos), itemCount)

		if app.ENABLE_OFFLINE_SHOP:
			self.itemSlotList["ItemSlot_%d" % gridSize].RefreshSlot()
			self.wndInventory.RefreshBagSlotWindow()
		else:
			self.itemSlot.RefreshSlot()

https://puu.sh/sgURR/9d53600003.png
---

Search:
			if player.SLOT_TYPE_INVENTORY != attachedSlotType and player.SLOT_TYPE_DRAGON_SOUL_INVENTORY != attachedSlotType:
				return
			attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)

			itemVNum = player.GetItemIndex(attachedInvenType, attachedSlotPos)

Add it under:
			if app.ENABLE_OFFLINE_SHOP:
				itemCount = player.GetItemCount(attachedInvenType, attachedSlotPos)


Search:
			priceInputBoard = uiCommon.MoneyInputDialog()

Change:
			if app.ENABLE_OFFLINE_SHOP:
				if self.type:
					priceInputBoard = uiCommon.NewMoneyInputDialog()
				else:
					priceInputBoard = uiCommon.MoneyInputDialog()
			else:
				priceInputBoard = uiCommon.MoneyInputDialog()


https://puu.sh/sgUWF/f35e4c2772.png

---

Search:
			itemPrice=GetPrivateShopItemPrice(itemVNum)

			if itemPrice>0:
				priceInputBoard.SetValue(itemPrice)

Change:
			itemPrice=GetPrivateShopItemPrice(itemVNum)
			
			if app.ENABLE_OFFLINE_SHOP:
				if itemPrice>0:
					priceInputBoard.SetValue(itemPrice*itemCount)
			else:
				if itemPrice>0:
					priceInputBoard.SetValue(itemPrice)


Search:
			self.priceInputBoard.itemVNum = itemVNum

Add it under:
			if app.ENABLE_OFFLINE_SHOP:
				self.priceInputBoard.itemCount = itemCount

https://puu.sh/sgV0u/895acb5dd5.png

---

Search:
	def AcceptInputPrice(self):

Add it upper:
	if app.ENABLE_OFFLINE_SHOP:
		def PopupMsg(self, msg):
			self.popup = uiCommon.PopupDialog()
			self.popup.SetText(msg)
			self.popup.Open()


https://puu.sh/sgV29/e0527f07da.png

---

Search:
		text = self.priceInputBoard.GetText()

		if not text:
			return True

		if not text.isdigit():
			return True

		if int(text) <= 0:
			return True

Change:

		if app.ENABLE_OFFLINE_SHOP:
			if self.type:
				text = self.priceInputBoard.GetTextPrice1()
				textpricetwo = self.priceInputBoard.GetTextPrice2()
				textpricethree = self.priceInputBoard.GetTextPrice3()
				textpricefour = self.priceInputBoard.GetTextPrice4()
			else:
				text = self.priceInputBoard.GetText()

			if not text:
				self.PopupMsg("Please input price values")
				return True
	
			if not text.isdigit():
				self.PopupMsg("Please input only number to prices")
				return True
			if self.type:
				if not textpricetwo.isdigit() or not textpricethree.isdigit() or not textpricefour.isdigit():
					self.PopupMsg("Please input price values")
					return True
	
			if not self.type and int(text) <= 0:
				self.PopupMsg("Please input just only positive price")
				return True
			if self.type:
				if int(textpricetwo) < 0 or int(textpricethree) < 0 or int(textpricefour) < 0:
					self.PopupMsg("Please input just positive price")
					return True
	
				if int(text) == 0 and int(textpricetwo) == 0 and int(textpricethree) == 0 and int(textpricefour) == 0:
					self.PopupMsg("Please input price values")
					return True
	
				if self.priceInputBoard.itemVNum == 80007 and int(textpricethree) > 0:
					self.PopupMsg("You cannot sell gold bar with gold bar")
					return True
		else:
			text = self.priceInputBoard.GetText()
	
			if not text:
				return True
	
			if not text.isdigit():
				return True
	
			if int(text) <= 0:
				return True

https://puu.sh/sgV3S/b275d620cd.png
https://puu.sh/sgV4j/a9036e0a55.png

---

Search:
		price = int(self.priceInputBoard.GetText())

		if IsPrivateShopItemPriceList():
			SetPrivateShopItemPrice(self.priceInputBoard.itemVNum, price)

		shop.AddPrivateShopItemStock(attachedInvenType, sourceSlotPos, targetSlotPos, price)
		self.itemStock[targetSlotPos] = (attachedInvenType, sourceSlotPos)
		snd.PlaySound("sound/ui/drop.wav")

		self.Refresh()

		#####

		self.priceInputBoard = None
		return True

Change:
		if app.ENABLE_OFFLINE_SHOP:
			if self.type:
				price = int(self.priceInputBoard.GetTextPrice1())
				price_two = int(self.priceInputBoard.GetTextPrice2())
				price_three = int(self.priceInputBoard.GetTextPrice3())
				price_four = int(self.priceInputBoard.GetTextPrice4())
			else:
				price = int(self.priceInputBoard.GetText())
		else:
			price = int(self.priceInputBoard.GetText())
			
		if IsPrivateShopItemPriceList():
			SetPrivateShopItemPrice(self.priceInputBoard.itemVNum, price)
		
		if app.ENABLE_OFFLINE_SHOP:
			if self.type:
				if not constInfo.SHOP_ALLOW_COIN:
					price_two = 0
				if not constInfo.SHOP_ALLOW_GOLDBAR:
					price_three = 0
				if not constInfo.SHOP_ALLOW_WON:
					price_four = 0
	
				wonFlag = 0
				try: wonFlag = app.ENABLE_CHEQUE_SYSTEM
				except: pass
				if not wonFlag:
					price_four = 0
	
			if self.type:
				shop.AddPrivateShopItemStock(attachedInvenType, sourceSlotPos, targetSlotPos, price, price_two, price_three, price_four)
			else:
				shop.AddPrivateShopItemStock(attachedInvenType, sourceSlotPos, targetSlotPos, price)
		else:
			shop.AddPrivateShopItemStock(attachedInvenType, sourceSlotPos, targetSlotPos, price)

		self.itemStock[targetSlotPos] = (attachedInvenType, sourceSlotPos)
		snd.PlaySound("sound/ui/drop.wav")

		self.Refresh()

		#####
		if app.ENABLE_OFFLINE_SHOP:
			self.priceInputBoard.Close()
		self.priceInputBoard = None
		return True


https://puu.sh/sgV6o/8937fdd932.png
https://puu.sh/sgV75/f3faebf771.png

---

Search:
	def CancelInputPrice(self):
		self.priceInputBoard = None
		return True

Change:
	def CancelInputPrice(self):
		if app.ENABLE_OFFLINE_SHOP:
			if self.type and self.priceInputBoard:
				self.priceInputBoard.Close()
		self.priceInputBoard = None
		return True


Search:
	def OnOk(self):

		if not self.title:
			return

		if 0 == len(self.itemStock):
			return

		shop.BuildPrivateShop(self.title)
		self.Close()

Change:
	def OnOk(self):

		if not self.title:
			return

		if 0 == len(self.itemStock):
			return
		
		if app.ENABLE_OFFLINE_SHOP:
			shop.BuildPrivateShop(self.title, self.type, self.size, self.color)
		else:
			shop.BuildPrivateShop(self.title)
		self.Close()

https://puu.sh/sgVsc/25124a89cb.png



























