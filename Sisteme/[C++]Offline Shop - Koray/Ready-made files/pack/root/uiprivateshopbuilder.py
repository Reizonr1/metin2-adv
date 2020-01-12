import ui
import snd
import shop
import mouseModule
import player
import chr
import net
import uiCommon
import localeInfo
import chat
import item
import systemSetting #김준호
import player #김준호
import constInfo
import app

g_isBuildingPrivateShop = False

g_itemPriceDict={}

g_privateShopAdvertisementBoardDict={}

def Clear():
	global g_itemPriceDict
	global g_isBuildingPrivateShop
	g_itemPriceDict={}
	g_isBuildingPrivateShop = False

def IsPrivateShopItemPriceList():
	global g_itemPriceDict
	if g_itemPriceDict:
		return True
	else:
		return False

def IsBuildingPrivateShop():
	global g_isBuildingPrivateShop
	if player.IsOpenPrivateShop() or g_isBuildingPrivateShop:
		return True
	else:
		return False

def SetPrivateShopItemPrice(itemVNum, itemPrice):
	global g_itemPriceDict
	g_itemPriceDict[int(itemVNum)]=itemPrice
	
def GetPrivateShopItemPrice(itemVNum):
	try:
		global g_itemPriceDict
		return g_itemPriceDict[itemVNum]
	except KeyError:
		return 0
		
def UpdateADBoard():	
	for key in g_privateShopAdvertisementBoardDict.keys():
		g_privateShopAdvertisementBoardDict[key].Show()
		
def DeleteADBoard(vid):
	if not g_privateShopAdvertisementBoardDict.has_key(vid):
		return
			
	del g_privateShopAdvertisementBoardDict[vid]
		

class PrivateShopAdvertisementBoard(ui.ThinBoard):
	def __init__(self):
		ui.ThinBoard.__init__(self, "UI_BOTTOM")
		if app.ENABLE_OFFLINE_SHOP:
			self.shopAdvertismentBoardSeen = []
		self.vid = None
		self.__MakeTextLine()

	def __del__(self):
		ui.ThinBoard.__del__(self)

	def __MakeTextLine(self):
		self.textLine = ui.TextLine()
		self.textLine.SetParent(self)
		self.textLine.SetWindowHorizontalAlignCenter()
		self.textLine.SetWindowVerticalAlignCenter()
		self.textLine.SetHorizontalAlignCenter()
		self.textLine.SetVerticalAlignCenter()
		self.textLine.Show()

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
		self.Show() 
				
		g_privateShopAdvertisementBoardDict[vid] = self
		
	def OnMouseLeftButtonUp(self):
		if not self.vid:
			return
		net.SendOnClickPacket(self.vid)
		if app.ENABLE_OFFLINE_SHOP:
			if self.vid != player.GetMainCharacterIndex():
				self.textLine.SetPackedFontColor(0xFF00C8FF)
				self.shopAdvertismentBoardSeen.append(self.vid)
		return True
		
	def OnUpdate(self):
		if not self.vid:
			return

		if systemSetting.IsShowSalesText():
			self.Show()
			x, y = chr.GetProjectPosition(self.vid, 220)
			self.SetPosition(x - self.GetWidth()/2, y - self.GetHeight()/2)
		
		else:
			for key in g_privateShopAdvertisementBoardDict.keys():
				if  player.GetMainCharacterIndex() == key:  #상점풍선을 안보이게 감추는 경우에도, 플레이어 자신의 상점 풍선은 보이도록 함. by 김준호
					g_privateShopAdvertisementBoardDict[key].Show() 	
					x, y = chr.GetProjectPosition(player.GetMainCharacterIndex(), 220)
					g_privateShopAdvertisementBoardDict[key].SetPosition(x - self.GetWidth()/2, y - self.GetHeight()/2)
				else:
					g_privateShopAdvertisementBoardDict[key].Hide()

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

	def __del__(self):
		#print "------------------------------------------------------------- DELETE MAKE_PRIVATE_SHOP_WINDOW"
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PrivateShopBuilder.py")
		except:
			import exception
			exception.Abort("PrivateShopBuilderWindow.LoadWindow.LoadObject")

		try:
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
		except:
			import exception
			exception.Abort("PrivateShopBuilderWindow.LoadWindow.BindObject")

		self.btnOk.SetEvent(ui.__mem_func__(self.OnOk))
		self.btnClose.SetEvent(ui.__mem_func__(self.OnClose))
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.OnClose))

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

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

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

	def OnSelectEmptySlot(self, selectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			mouseModule.mouseController.DeattachObject()

			if player.SLOT_TYPE_INVENTORY != attachedSlotType and player.SLOT_TYPE_DRAGON_SOUL_INVENTORY != attachedSlotType:
				return
			attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
				
			itemVNum = player.GetItemIndex(attachedInvenType, attachedSlotPos)
			item.SelectItem(itemVNum)
			if app.ENABLE_OFFLINE_SHOP:
				itemCount = player.GetItemCount(attachedInvenType, attachedSlotPos)

			if item.IsAntiFlag(item.ANTIFLAG_GIVE) or item.IsAntiFlag(item.ANTIFLAG_MYSHOP):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.PRIVATE_SHOP_CANNOT_SELL_ITEM)
				return

			if app.ENABLE_OFFLINE_SHOP:
				if self.type:
					priceInputBoard = uiCommon.NewMoneyInputDialog()
				else:
					priceInputBoard = uiCommon.MoneyInputDialog()
			else:
				priceInputBoard = uiCommon.MoneyInputDialog()
			priceInputBoard.SetTitle(localeInfo.PRIVATE_SHOP_INPUT_PRICE_DIALOG_TITLE)
			priceInputBoard.SetAcceptEvent(ui.__mem_func__(self.AcceptInputPrice))
			priceInputBoard.SetCancelEvent(ui.__mem_func__(self.CancelInputPrice))
			priceInputBoard.Open()

			itemPrice=GetPrivateShopItemPrice(itemVNum)
			
			if app.ENABLE_OFFLINE_SHOP:
				if itemPrice>0:
					priceInputBoard.SetValue(itemPrice*itemCount)
			else:
				if itemPrice>0:
					priceInputBoard.SetValue(itemPrice)
			
			self.priceInputBoard = priceInputBoard
			self.priceInputBoard.itemVNum = itemVNum
			if app.ENABLE_OFFLINE_SHOP:
				self.priceInputBoard.itemCount = itemCount
			self.priceInputBoard.sourceWindowType = attachedInvenType
			self.priceInputBoard.sourceSlotPos = attachedSlotPos
			self.priceInputBoard.targetSlotPos = selectedSlotPos

	def OnSelectItemSlot(self, selectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			snd.PlaySound("sound/ui/loginfail.wav")
			mouseModule.mouseController.DeattachObject()

		else:
			if not selectedSlotPos in self.itemStock:
				return

			invenType, invenPos = self.itemStock[selectedSlotPos]
			shop.DelPrivateShopItemStock(invenType, invenPos)
			snd.PlaySound("sound/ui/drop.wav")

			del self.itemStock[selectedSlotPos]

			self.Refresh()

	if app.ENABLE_OFFLINE_SHOP:
		def PopupMsg(self, msg):
			self.popup = uiCommon.PopupDialog()
			self.popup.SetText(msg)
			self.popup.Open()

	def AcceptInputPrice(self):

		if not self.priceInputBoard:
			return True

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

		attachedInvenType = self.priceInputBoard.sourceWindowType
		sourceSlotPos = self.priceInputBoard.sourceSlotPos
		targetSlotPos = self.priceInputBoard.targetSlotPos

		for privatePos, (itemWindowType, itemSlotIndex) in self.itemStock.items():
			if itemWindowType == attachedInvenType and itemSlotIndex == sourceSlotPos:
				shop.DelPrivateShopItemStock(itemWindowType, itemSlotIndex)
				del self.itemStock[privatePos]

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
		
	def CancelInputPrice(self):
		if app.ENABLE_OFFLINE_SHOP:
			if self.type and self.priceInputBoard:
				self.priceInputBoard.Close()
		self.priceInputBoard = None
		return True

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


	def OnClose(self):
		self.Close()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnOverInItem(self, slotIndex):

		if self.tooltipItem:
			if self.itemStock.has_key(slotIndex):
				self.tooltipItem.SetPrivateShopBuilderItem(*self.itemStock[slotIndex] + (slotIndex,))

	def OnOverOutItem(self):

		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
