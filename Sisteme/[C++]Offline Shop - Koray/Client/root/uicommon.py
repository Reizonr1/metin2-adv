Search:
import uiScriptLocale

Add it under:
import dbg
import grp
import constInfo
import wndMgr

https://puu.sh/sgXAt/626758425b.png

--

Search:
		self.moneyText.SetText(self.moneyHeaderText + localeInfo.NumberToMoneyString(money))

Add it under:

if app.ENABLE_OFFLINE_SHOP:
	class ShopInputDialog(ui.ScriptWindow):
	
		def __init__(self):
			ui.ScriptWindow.__init__(self)
	
			self.colorTabIdx = -1
			self.sizeTabIdx = -1
			self.typeTabIdx = -1
			self.tabList = { }
			
			self.__CreateDialog()
	
		def __del__(self):
			ui.ScriptWindow.__del__(self)
	
		def __CreateDialog(self):
			try:
				pyScrLoader = ui.PythonScriptLoader()
				pyScrLoader.LoadScriptFile(self, "uiscript/shopinputdialog.py")
	
				getObject = self.GetChild
				self.board = getObject("Board")
				self.acceptButton = getObject("AcceptButton")
				self.cancelButton = getObject("CancelButton")
				self.inputSlot = getObject("InputSlot")
				self.inputValue = getObject("InputValue")
				
				self.colorDesc = getObject("ColorDesc")
				self.colorBG = getObject("ColorBG")
				for i in range(1, 7):
					self.tabList["colorTab%d" % i] = getObject("ColorTab%d" % i)
					self.tabList["colorTab%d" % i].SetEvent(ui.__mem_func__(self.CheckButtonStatus), i, "color")
					self.tabList["colorTab%d" % i].Hide()
	
					self.tabList["sizeTab%d" % i] = getObject("SizeTab%d" % i)
					self.tabList["sizeTab%d" % i].SetEvent(ui.__mem_func__(self.CheckButtonStatus), i, "size")
								
					self.tabList["typeTab%d" % i] = getObject("TypeTab%d" % i)
					self.tabList["typeTab%d" % i].SetEvent(ui.__mem_func__(self.CheckButtonStatus), i, "type")
				self.colorDesc.Hide()
				self.colorBG.Hide()
				
			except:
				import sys
				(type, msg, tb)=sys.exc_info()
				dbg.TraceError("ShopInputDialog.__CreateDialog - %s:%s" % (type, msg))
				app.Abort()
				return 0
				
		def CheckButtonStatus(self, idx, typ):
			if typ == "color":
				self.colorTabIdx = idx
			elif typ == "size":
				self.sizeTabIdx = idx		
			else:
				self.typeTabIdx = idx
			for i in range(1, 7):
				# Refresh buttons
				if not i == self.colorTabIdx and typ == "color":
					self.tabList["colorTab%d" % i].SetUp()
				if not i == self.sizeTabIdx and typ == "size":
					self.tabList["sizeTab%d" % i].SetUp()
				if not i == self.typeTabIdx and typ == "type":
					self.tabList["typeTab%d" % i].SetUp()
					
				# Show-Hide type buttons
				if not self.typeTabIdx == 1 and typ == "type":
					self.tabList["colorTab%d" % i].Show()
					if not self.colorDesc.IsShow():
						self.colorDesc.Show()
					if not self.colorBG.IsShow():
						self.colorBG.Show()
						
				elif self.typeTabIdx == 1 and typ == "type":
					self.tabList["colorTab%d" % i].Hide()
					if self.colorDesc.IsShow():
						self.colorDesc.Hide()
					if self.colorBG.IsShow():
						self.colorBG.Hide()
		
		def Open(self):
			self.inputValue.SetFocus()
			self.SetCenterPosition()
			self.SetTop()
			self.Show()
	
		def Close(self):
			self.ClearDictionary()
			self.board = None
			self.acceptButton = None
			self.cancelButton = None
			self.inputSlot = None
			self.inputValue = None
			
			self.colorTabIdx = 0
			self.typeTabIdx = 0
			self.tabList.clear()
			
			self.Hide()
	
		def SetTitle(self, name):
			self.board.SetTitleName(name)
	
		def SetNumberMode(self):
			self.inputValue.SetNumberMode()
	
		def SetSecretMode(self):
			self.inputValue.SetSecret()
	
		def SetFocus(self):
			self.inputValue.SetFocus()
	
		def SetMaxLength(self, length):
			width = length * 6 + 10
			self.inputValue.SetMax(length)
			self.SetSlotWidth(width)
			self.SetBoardWidth(max(width + 50, 160))
	
		def SetSlotWidth(self, width):
			self.inputSlot.SetSize(width, self.inputSlot.GetHeight())
			self.inputValue.SetSize(width, self.inputValue.GetHeight())
	
		def SetBoardWidth(self, width):
			self.board.SetSize(max(width + 50, 160), self.GetHeight())
			self.SetSize(max(width + 50, 160), self.GetHeight())
			self.UpdateRect()
	
		def SetAcceptEvent(self, event):
			self.acceptButton.SetEvent(event)
			self.inputValue.OnIMEReturn = event
	
		def SetCancelEvent(self, event):
			self.board.SetCloseEvent(event)
			self.cancelButton.SetEvent(event)
			self.inputValue.OnPressEscapeKey = event
	
		def GetText(self):
			return self.inputValue.GetText()
	
		def GetShopType(self):
			return self.typeTabIdx - 1
		
		def GetShopSize(self):
			return self.sizeTabIdx - 1
		
		def GetShopColor(self):
			return self.colorTabIdx - 1
	
	
	class NewMoneyInputDialog(ui.BoardWithTitleBar):
	
		def __init__(self):
			ui.BoardWithTitleBar.__init__(self)
	
			self.moneyHeaderText = localeInfo.MONEY_INPUT_DIALOG_SELLPRICE
			self.BuildUI()
			self.SetMaxLength(12)
	
		def __del__(self):
			ui.BoardWithTitleBar.__del__(self)
	
		def TabControl(self, parent, width, heigh, *tabv):
			self.tabs = []
			for arg in tabv:
				tab_item = {"TAB" : arg[0], "TAB_NAME" : arg[1]}
				self.tabs.append(tab_item)
	
			x = -70
			self.tabPageList = {}
			self.tabList = {}
			for tabs in self.tabs:
				x += 80
	
				Tab = ui.RadioButton()
				Tab.SetParent(parent)
				Tab.SetPosition(x, 30)
				Tab.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_01.sub")
				Tab.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_02.sub")
				Tab.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
				Tab.SetText(tabs["TAB_NAME"])
				Tab.SetEvent(lambda arg = tabs["TAB"]: self.TabEvent(arg))
				Tab.SetUp()
				Tab.Show()
	
				Page = ui.Box()
				Page.SetParent(parent)
				Page.SetPosition(8, 50)
				Page.SetSize(width-16, heigh-60)
				Page.SetColor(grp.GenerateColor(0.0, 0.0, 0.5, 0.3))
				Page.Show()
	
				self.tabList[tabs["TAB"]] = Tab
				self.tabPageList[tabs["TAB"]] = Page
	
			if self.tabs:
				self.SetState(self.tabs[0]["TAB"])
	
			return (self.tabPageList, self.tabList)
	
		def TabEvent(self, arg):
			self.SetState(arg)
	
		def SetState(self, stateKey):
			for tabs in self.tabs:
				self.tabList[tabs["TAB"]].SetUp()
				self.tabPageList[tabs["TAB"]].Hide()
	
			self.tabList[stateKey].Down()
			self.tabPageList[stateKey].Show()
	
		def TextLine(self, parent, text, x, y):
			tmpText = ui.TextLine()
	
			if parent:
				tmpText.SetParent(parent)
	
			tmpText.SetPosition(x, y)
			tmpText.SetText(text)
	
			tmpText.Show()
			return tmpText
	
		def SlotBar(self, parent, x, y, width, heigh):
			tmpSlotBar = ui.SlotBar()
	
			if parent:
				tmpSlotBar.SetParent(parent)
	
			tmpSlotBar.SetSize(width, heigh)
			tmpSlotBar.SetPosition(x, y)
	
			tmpSlotBar.Show()
			return tmpSlotBar
	
		def EditLine(self, parent, text, x, y, width, heigh, max):
			tmpEditLine = ui.EditLine()
	
			if parent:
				tmpEditLine.SetParent(parent)
	
			tmpEditLine.SetSize(width, heigh)
			tmpEditLine.SetPosition(x, y)
			tmpEditLine.SetMax(max)
			tmpEditLine.SetLimitWidth(width)
			tmpEditLine.SetMultiLine()
			tmpEditLine.SetText(text)
	
			tmpEditLine.Show()
			return tmpEditLine
	
		def BasicButton(self, parent, buttonName, x, y, func):
			tmpButton = ui.Button()
	
			if parent:
				tmpButton.SetParent(parent)
	
			tmpButton.SetPosition(x, y)
			tmpButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
			tmpButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
			tmpButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
	
			tmpButton.SetText(buttonName)
	
			tmpButton.SetEvent(func)
			tmpButton.Show()
			return tmpButton
	
	
		def BuildUI(self):
			self.AddFlag('movable')
			self.AddFlag('float')
			self.SetSize(335, 220)
			self.SetCenterPosition()
			self.SetTitleName("")
			self.SetCloseEvent(self.Close)
	
			self.infoboard = ui.ThinBoard()
			self.infoboard.SetParent(self)
			self.infoboard.SetSize(100, 210)
			self.infoboard.SetPosition(330, 4)
			self.infoboard.Show()
	
			self.tab_menu, self.tab_list = self.TabControl(self, 332, 220, ["tab1_yang", "Yang"], ["tab2_coin", "Coin"], ["tab3_goldbar", "Goldbar"], ["tab4_won", "Won"])
	
			#+Price1
			self.titleText1 = self.TextLine(self.tab_menu["tab1_yang"], "Price of Yang", 122, 10)
			self.InputSlot = self.SlotBar(self.tab_menu["tab1_yang"], 0, 60, 90, 18) #PARENT = BOARD
			self.InputSlot.SetWindowHorizontalAlignCenter()
	
			self.inputValueOne = self.EditLine(self.InputSlot, "", 3, 3, 90, 18, 10)
			self.inputValueOne.SetNumberMode()
			self.inputValueOne.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate)
	
			self.moneyText = self.TextLine(self.tab_menu["tab1_yang"], "999999999", 0, 90) #PARENT = BOARD
			self.moneyText.SetWindowHorizontalAlignCenter()
			self.moneyText.SetHorizontalAlignCenter()
			#-Price1
	
	
			#+Price2
			self.titleText2 = self.TextLine(self.tab_menu["tab2_coin"], "Price of Coin", 129, 10)
			self.InputSlot2 = self.SlotBar(self.tab_menu["tab2_coin"], 0, 60, 90, 18) #PARENT = BOARD
			self.InputSlot2.SetWindowHorizontalAlignCenter()
	
			self.inputValueTwo = self.EditLine(self.InputSlot2, "", 3, 3, 90, 18, 10)
			self.inputValueTwo.SetNumberMode()
			self.inputValueTwo.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdateTwo)
	
			self.moneyTwoText = self.TextLine(self.tab_menu["tab2_coin"], "999999999", 0, 90) #PARENT = BOARD
			self.moneyTwoText.SetWindowHorizontalAlignCenter()
			self.moneyTwoText.SetHorizontalAlignCenter()
			#-Price2
	
	
			#+Price3
			self.titleText3 = self.TextLine(self.tab_menu["tab3_goldbar"], "Price of 2KK Goldbar", 122, 10)
			self.InputSlot3 = self.SlotBar(self.tab_menu["tab3_goldbar"], 0, 60, 90, 18) #PARENT = BOARD
			self.InputSlot3.SetWindowHorizontalAlignCenter()
	
			self.inputValueThree = self.EditLine(self.InputSlot3, "", 3, 3, 90, 18, 10)
			self.inputValueThree.SetNumberMode()
			self.inputValueThree.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdateThree)
	
			self.moneyThreeText = self.TextLine(self.tab_menu["tab3_goldbar"], "999999999", 0, 90) #PARENT = BOARD
			self.moneyThreeText.SetWindowHorizontalAlignCenter()
			self.moneyThreeText.SetHorizontalAlignCenter()
			#-Price3
	
	
			#+Price4
			self.titleText4 = self.TextLine(self.tab_menu["tab4_won"], "Price of Won", 126, 10)
			self.InputSlot4 = self.SlotBar(self.tab_menu["tab4_won"], 0, 60, 90, 18) #PARENT = BOARD
			self.InputSlot4.SetWindowHorizontalAlignCenter()
	
			self.inputValueFour = self.EditLine(self.InputSlot4, "", 3, 3, 90, 18, 10)
			self.inputValueFour.SetNumberMode()
			self.inputValueFour.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdateFour)
	
			self.moneyFourText = self.TextLine(self.tab_menu["tab4_won"], "999999999", 0, 90) #PARENT = BOARD
			self.moneyFourText.SetWindowHorizontalAlignCenter()
			self.moneyFourText.SetHorizontalAlignCenter()
			#-Price4
	
			#+Info
			self.InfoYangTitle = self.TextLine(self.infoboard, "Yang price:", 10, 10)
			self.InfoYang = self.TextLine(self.infoboard, str(self.moneyText.GetText()), 10, 30)
	
			self.InfoEpTitle = self.TextLine(self.infoboard, "Coin price:", 10, 60)
			self.InfoEp = self.TextLine(self.infoboard, str(self.moneyText.GetText()), 10, 80)
	
			self.InfoGoldbarTitle = self.TextLine(self.infoboard, "Goldbar price:", 10, 110)
			self.InfoGoldbar = self.TextLine(self.infoboard, str(self.moneyText.GetText()), 10, 130)
	
			self.InfoExpTitle = self.TextLine(self.infoboard, "Won price:", 10, 160)
			self.InfoExp = self.TextLine(self.infoboard, str(self.moneyText.GetText()), 10, 180)
	
			#-Info
	
			self.acceptButton = self.BasicButton(self, uiScriptLocale.OK, - 61 - 5 + 30, 184, self.empty) #PARENT = BOARD
			self.acceptButton.SetWindowHorizontalAlignCenter()
			self.cancelButton = self.BasicButton(self, uiScriptLocale.CANCEL, 5 + 30, 184, self.Close) #PARENT = BOARD
			self.cancelButton.SetWindowHorizontalAlignCenter()
	
	
		def __OnValueUpdateFour(self):
			ui.EditLine.OnIMEUpdate(self.inputValueFour)
	
			text = self.inputValueFour.GetText()
	
			countexp = 0
			if text and text.isdigit():
				try:
					countexp = int(text)
				except ValueError:
					countexp = 1999999999
	
			if countexp > 999:
				countexp = 999
				self.inputValueFour.SetText(str(countexp))
	
			self.InfoExp.SetText(str(localeInfo.NumberToPriceString(countexp, "Won")))
	
			self.moneyFourText.SetText("Won price: " + localeInfo.NumberToPriceString(countexp, "Won"))
	
		def __OnValueUpdateThree(self):
			ui.EditLine.OnIMEUpdate(self.inputValueThree)
	
			text = self.inputValueThree.GetText()
	
			countbar = 0
			if text and text.isdigit():
				try:
					countbar = int(text)
				except ValueError:
					countbar = 1999999999
	
			if countbar > 199:
				countbar = 199
				self.inputValueThree.SetText(str(countbar))
	
			self.InfoGoldbar.SetText(str(localeInfo.NumberToPriceString(countbar, "Goldbar")))
	
			self.moneyThreeText.SetText("Goldbar price: " + localeInfo.NumberToPriceString(countbar, "Goldbar"))
	
		def __OnValueUpdateTwo(self):
			ui.EditLine.OnIMEUpdate(self.inputValueTwo)
	
			text = self.inputValueTwo.GetText()
	
			countep = 0
			if text and text.isdigit():
				try:
					countep = int(text)
				except ValueError:
					countep = 1999999999
	
			if countep > 10000:
				countep = 10000
				self.inputValueTwo.SetText(str(countep))
	
			self.InfoEp.SetText(str(localeInfo.NumberToPriceString(countep, "Coin")))
	
			self.moneyTwoText.SetText("Coin Price: " + localeInfo.NumberToPriceString(countep, "Coin"))
	
	
		def __OnValueUpdate(self):
			ui.EditLine.OnIMEUpdate(self.inputValueOne)
	
			text = self.inputValueOne.GetText()
	
			money = 0
			if text and text.isdigit():
				try:
					money = int(text)
				except ValueError:
					money = 199999999
	
			self.InfoYang.SetText(str(localeInfo.NumberToPriceString(money, "Yang")))
	
			self.moneyText.SetText(self.moneyHeaderText + localeInfo.NumberToMoneyString(money))
	
		def empty(self):
			pass
	
		def Open(self):
			self.inputValueFour.SetText("0")
			self.inputValueFour.SetFocus()
			self.inputValueThree.SetText("0")
			self.inputValueThree.SetFocus()
			self.inputValueTwo.SetText("0")
			self.inputValueTwo.SetFocus()
			self.inputValueOne.SetText("0")
			self.inputValueOne.SetFocus()
	
			self.__OnValueUpdate()
			self.__OnValueUpdateTwo()
			self.__OnValueUpdateThree()
			self.__OnValueUpdateFour()
			self.SetCenterPosition()
			self.SetTop()
			self.Show()
	
			wonFlag = 0
			try: wonFlag = app.ENABLE_CHEQUE_SYSTEM
			except: pass
			if not wonFlag or not constInfo.SHOP_ALLOW_WON:
				self.tab_list["tab4_won"].SetText("Disabled")
				self.tab_list["tab4_won"].Disable()
				self.tab_list["tab4_won"].SetUp()
				"""
				self.moneyFourText.SetText("Disabled this option")
				if self.inputValueFour.IsFocus():
					self.inputValueFour.KillFocus()
				self.inputValueFour.Hide()
				"""
			else:
				self.inputValueFour.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdateFour)
	
	
			if not constInfo.SHOP_ALLOW_GOLDBAR:
				self.tab_list["tab3_goldbar"].Disable()
				self.tab_list["tab3_goldbar"].SetUp()
				"""
				self.moneyThreeText.SetText("Disabled this option")
				if self.inputValueThree.IsFocus():
					self.inputValueThree.KillFocus()
				self.inputValueThree.Hide()
				"""
			else:
				self.inputValueThree.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdateThree)
	
	
			if not constInfo.SHOP_ALLOW_COIN:
				self.tab_list["tab2_coin"].Disable()
				self.tab_list["tab2_coin"].SetUp()
				"""
				self.moneyTwoText.SetText("Disabled this option")
				if self.inputValueTwo.IsFocus():
					self.inputValueTwo.KillFocus()
				self.inputValueTwo.Hide()
				"""
			else:
				self.inputValueTwo.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdateTwo)
	
	
		def Close(self):
			#self.ClearDictionary()
			self.acceptButton = None
			self.cancelButton = None
			self.inputValueOne = None
			self.inputValueTwo = None
			self.inputValueThree = None
			self.inputValueFour = None
			self.Hide()
	
		def SetTitle(self, name):
			self.SetTitleName(name)
	
		def SetFocus(self):
			self.inputValueOne.SetFocus()
	
		def SetFocusPriceTwo(self):
			self.inputValueTwo.SetFocus()
	
		def SetFocusPriceThree(self):
			self.inputValueThree.SetFocus()
	
		def SetFocusPriceFour(self):
			self.inputValueFour.SetFocus()
	
		def SetMaxLength(self, length):
			length = min(9, length)
			self.inputValueOne.SetMax(length)
			self.inputValueTwo.SetMax(length)
			self.inputValueThree.SetMax(length)
			self.inputValueFour.SetMax(length)
	
		def SetMoneyHeaderText(self, text):
			self.moneyHeaderText = text
	
		def SetAcceptEvent(self, event):
			self.acceptButton.SetEvent(event)
			self.inputValueOne.OnIMEReturn = event
			self.inputValueTwo.OnIMEReturn = event
			self.inputValueThree.OnIMEReturn = event
			self.inputValueFour.OnIMEReturn = event
	
		def SetCancelEvent(self, event):
			self.SetCloseEvent(event)
			self.cancelButton.SetEvent(event)
			self.inputValueOne.OnPressEscapeKey = event
			self.inputValueTwo.OnPressEscapeKey = event
			self.inputValueThree.OnPressEscapeKey = event
			self.inputValueFour.OnPressEscapeKey = event
	
		def SetValue(self, value):
			value=str(value)
			self.inputValueOne.SetText(value)
			self.__OnValueUpdate()
			ime.SetCursorPosition(len(value))
	
		def SetValueTwo(self, value):
			value=str(value)
			self.inputValueTwo.SetText(value)
			self.__OnValueUpdateTwo()
			ime.SetCursorPosition(len(value))
	
		def SetValueThree(self, value):
			value=str(value)
			self.inputValueThree.SetText(value)
			self.__OnValueUpdateThree()
			ime.SetCursorPosition(len(value))
	
		def SetValueFour(self, value):
			value=str(value)
			self.inputValueFour.SetText(value)
			self.__OnValueUpdateFour()
			ime.SetCursorPosition(len(value))
	
		def GetTextPrice1(self):
			return self.inputValueOne.GetText()
	
		def GetTextPrice2(self):
			if self.inputValueTwo.GetText() == "Disabled this option":
				return "0"
			return self.inputValueTwo.GetText()
	
		def GetTextPrice3(self):
			if self.inputValueThree.GetText() == "Disabled this option":
				return "0"
			return self.inputValueThree.GetText()
	
		def GetTextPrice4(self):
			if self.inputValueFour.GetText() == "Disabled this option":
				return "0"
			return self.inputValueFour.GetText()
	
		def OnPressEscapeKey(self):
			self.Close()
			return True




https://puu.sh/sgXCe/8ca117cf56.png
