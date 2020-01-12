from ui_wrapper import _ui
import dbg,net,player
import ui,constInfo

class IngameBank(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.Bar1T, self.Bar100M, self.Bar10M = 1000000000, 100000000, 10000000

		self.GUIFunc()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def GUIFunc(self):
		self.Board = _ui().BoardWithTitleBar(None, 1, 500, 150, 300, 200, "Ingame Bank", self.OpenWindow, False, True)
		self.Board.OnPressEscapeKey = ui.__mem_func__(self.Close)

		self.tab_menu = _ui().TabControl(self.Board, 300, 200, ["tab1_yangtobar", "Yang > Bar"], ["tab2_bartoyang", "Bar > Yang"])

		# Yang to bar tab ui init
		self.InputMoney = _ui().SlotBar(self.tab_menu["tab1_yangtobar"], 80, 15, 110, 68 - 50)
		self.EditMoney = _ui().EditLine(self.InputMoney, "", 3, 3, 90, 18, 10)
		self.EditMoney.SetNumberMode()
		self.EditMoney.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate)

		self.MoneyAmount = _ui().TextLine(self.tab_menu["tab1_yangtobar"], "0 Yang", 130, 100 - 50)
		self.MoneyAmount.SetHorizontalAlignCenter()


		self.ImageFirst = _ui().ExpandedImageBox(self.tab_menu["tab1_yangtobar"], "icon/item/80007.tga", 54, 133 - 50)
		self.ImageFirst.SetScale(float(0.5),float(0.5))

		self.FirstBarSlot = _ui().SlotBar(self.tab_menu["tab1_yangtobar"], 74, 133 - 50, 25, 15)
		self.FirstBarText = _ui().TextLine(self.FirstBarSlot, "0", 5, 1)

		self.ImageSecond = _ui().ExpandedImageBox(self.tab_menu["tab1_yangtobar"], "icon/item/80006.tga", 108, 133 - 50)
		self.ImageSecond.SetScale(float(0.5),float(0.5))

		self.SecondBarSlot = _ui().SlotBar(self.tab_menu["tab1_yangtobar"], 128, 133 - 50, 25, 15)
		self.SecondBarText = _ui().TextLine(self.SecondBarSlot, "0", 5, 1)

		self.ImageThird = _ui().ExpandedImageBox(self.tab_menu["tab1_yangtobar"], "icon/item/80005.tga", 160, 133 - 50)
		self.ImageThird.SetScale(float(0.5),float(0.5))

		self.ThirdBarSlot = _ui().SlotBar(self.tab_menu["tab1_yangtobar"], 180, 133 - 50, 25, 15)
		self.ThirdBarText = _ui().TextLine(self.ThirdBarSlot, "0", 5, 1)


		self.but1 = _ui().Button(self.tab_menu["tab1_yangtobar"], "Convert Yang > Bar", "", 50, 115, self.SendYangToBar, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')

		# bar to yang tab ui init
		self.InputMoney2 = _ui().SlotBar(self.tab_menu["tab2_bartoyang"], 80, 80, 110, 68 - 50)
		self.EditMoney2 = _ui().EditLine(self.InputMoney2, "", 3, 3, 90, 18, 10)
		self.EditMoney2.SetNumberMode()
		self.EditMoney2.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate2)


		self.MoneyAmount2 = _ui().TextLine(self.tab_menu["tab2_bartoyang"], "0 Yang", 130, 100 - 50)
		self.MoneyAmount2.SetHorizontalAlignCenter()


		self.ImageFirst2 = _ui().ExpandedImageBox(self.tab_menu["tab2_bartoyang"], "icon/item/80007.tga", 54, 133 - 115)
		self.ImageFirst2.SetScale(float(0.5),float(0.5))

		self.FirstBarSlot2 = _ui().SlotBar(self.tab_menu["tab2_bartoyang"], 74, 133 - 115, 25, 15)
		self.FirstBarText2 = _ui().TextLine(self.FirstBarSlot2, "0", 5, 1)

		self.ImageSecond2 = _ui().ExpandedImageBox(self.tab_menu["tab2_bartoyang"], "icon/item/80006.tga", 108, 133 - 115)
		self.ImageSecond2.SetScale(float(0.5),float(0.5))

		self.SecondBarSlot2 = _ui().SlotBar(self.tab_menu["tab2_bartoyang"], 128, 133 - 115, 25, 15)
		self.SecondBarText2 = _ui().TextLine(self.SecondBarSlot2, "0", 5, 1)

		self.ImageThird2 = _ui().ExpandedImageBox(self.tab_menu["tab2_bartoyang"], "icon/item/80005.tga", 160, 133 - 115)
		self.ImageThird2.SetScale(float(0.5),float(0.5))

		self.ThirdBarSlot2 = _ui().SlotBar(self.tab_menu["tab2_bartoyang"], 180, 133 - 115, 25, 15)
		self.ThirdBarText2 = _ui().TextLine(self.ThirdBarSlot2, "0", 5, 1)


		self.but2 = _ui().Button(self.tab_menu["tab2_bartoyang"], "Convert Bar > Yang", "", 50, 115, self.SendBarToYang, 'd:/ymir work/ui/public/xlarge_button_01.sub', 'd:/ymir work/ui/public/xlarge_button_02.sub', 'd:/ymir work/ui/public/xlarge_button_03.sub')


	# common
	def SplitNumber(self, n, type):
		if n <= 0 :
			return "0 " + str(type)

		return "%s %s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]), str(type))

	# yang to bar func
	def SendYangToBar(self):
		text = self.EditMoney.GetText()
		if not text:
			self.Notificaton = _ui().PopupNotification("Fill out yang section")
			return
		if int(text) > int(player.GetElk()):
			self.Notificaton = _ui().PopupNotification("Doesn't have enough yang")
			return
		if int(text) < self.Bar10M:
			self.Notificaton = _ui().PopupNotification("Yang amount is too low")
			return

		net.SendChatPacket("/ingame_bank 1 %s" % (text))

	def __OnValueUpdate(self):
		ui.EditLine.OnIMEUpdate(self.EditMoney)

		text = self.EditMoney.GetText()

		money_amount = 0
		if text and text.isdigit():
			try:
				money_amount = int(text)
			except ValueError:
				money_amount = 1999999999

		x1000, x100, x10 = 0,0,0
		converted_money = money_amount

		while converted_money >= int(self.Bar1T):
			x1000 += 1
			converted_money = converted_money  - int(self.Bar1T)
		while converted_money >= int(self.Bar100M):
			x100 += 1
			converted_money = converted_money  - int(self.Bar100M)
		while converted_money >= int(self.Bar10M):
			x10 += 1
			converted_money = converted_money  - int(self.Bar10M)

		self.FirstBarText.SetText(str(x1000)) # 1.000.000.000 Bar
		self.SecondBarText.SetText(str(x100)) # 100.000.000 Bar
		self.ThirdBarText.SetText(str(x10)) # 10.000.000 Bar

		self.MoneyAmount.SetText(self.SplitNumber(str(money_amount), "Yang"))

	# bar to yang func
	def SendBarToYang(self):
		text = self.EditMoney2.GetText()
		if not text:
			self.Notificaton = _ui().PopupNotification("Fill out yang section")
			return
		if int(text) < self.Bar10M:
			self.Notificaton = _ui().PopupNotification("Yang amount is too low")
			return

		if int(constInfo.bar_first_amount) < 0 and int(constInfo.bar_second_amount) < 0 and int(constInfo.bar_third_amount) < 0:
			self.Notificaton = _ui().PopupNotification("Your doesn't have bar")
			return

		mygold = player.GetElk()
		limit = 2000000000
		a1 = int(constInfo.bar_first_amount) * self.Bar10M
		b1 = int(constInfo.bar_second_amount) * self.Bar100M
		c1 = int(constInfo.bar_third_amount) * self.Bar1T

		if mygold + int(text) > limit or mygold + int(text) > limit or mygold + int(text) > limit:
			self.Notificaton = _ui().PopupNotification("Yang overflow!")
			return

		net.SendChatPacket("/ingame_bank 2 %s" % (text))

	def __OnValueUpdate2(self):
		ui.EditLine.OnIMEUpdate(self.EditMoney2)

		text = self.EditMoney2.GetText()

		money_amount = 0
		if text and text.isdigit():
			try:
				money_amount = int(text)
			except ValueError:
				money_amount = 1999999999

		x1000, x100, x10 = 0,0,0
		converted_money = money_amount

		while converted_money >= int(self.Bar1T):
			x1000 += 1
			converted_money = converted_money  - int(self.Bar1T)
		while converted_money >= int(self.Bar100M):
			x100 += 1
			converted_money = converted_money  - int(self.Bar100M)
		while converted_money >= int(self.Bar10M):
			x10 += 1
			converted_money = converted_money  - int(self.Bar10M)

		self.FirstBarText2.SetText(str(x1000)) # 1.000.000.000 Bar
		self.SecondBarText2.SetText(str(x100)) # 100.000.000 Bar
		self.ThirdBarText2.SetText(str(x10)) # 10.000.000 Bar

		self.MoneyAmount2.SetText(self.SplitNumber(str(money_amount), "Yang"))

	# gui funcs
	def OpenWindow(self):
		if self.Board.IsShow():
			self.Board.Hide()
		else:
			self.Board.Show()

	def Close(self):
		self.Board.Hide()

#IngameBank()
