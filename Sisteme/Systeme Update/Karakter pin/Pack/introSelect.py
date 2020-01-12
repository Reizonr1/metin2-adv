Find - Bul:
class SelectCharacterWindow(ui.Window):

Add it upper - Üstüne ekle:
pin_sanal_klavye = 1

http://puu.sh/jS16p/534434a06c.png



Find - Bul:
self.flagDict = {}

Add it upper - Üstüne ekle:
self.PinBoard = None

http://puu.sh/jS1af/1e452b2325.png



Find - Bul:
if self.stream.isAutoSelect:
	chrSlot=self.stream.GetCharacterSlot()
	self.SelectSlot(chrSlot)
	self.StartGame()
	
Change - Değiştir:
if self.stream.isAutoSelect:
	chrSlot=self.stream.GetCharacterSlot()
	self.SelectSlot(chrSlot)
	self.GetKarakterPinBoard()
	#self.StartGame()
	
http://puu.sh/jS1em/b68b28bbb8.png



Find - Bul:
self.backGround = None

Add it under- Altına ekle:
self.PinBoard = None

http://puu.sh/jS1gE/f087f6d62d.png



Find - Bul:
self.btnStart.SetEvent(ui.__mem_func__(self.StartGame))

Change - Değiştir:
#self.btnStart.SetEvent(ui.__mem_func__(self.StartGame))
self.btnStart.SetEvent(ui.__mem_func__(self.GetKarakterPinBoard))

http://puu.sh/jS1kF/04cd77d6c3.png



Find - Bul:
def MakeCharacter(self, index, id, name, race, form, hair):
	if 0 == id:
		return

	chr.CreateInstance(index)
	chr.SelectInstance(index)
	chr.SetVirtualID(index)
	chr.SetNameString(name)

	chr.SetRace(race)
	chr.SetArmor(form)
	chr.SetHair(hair)

	chr.Refresh()
	chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
	chr.SetLoopMotion(chr.MOTION_INTRO_WAIT)

	chr.SetRotation(0.0)

Add it under- Altına ekle:
	def GetKarakterPinBoard(self):
		self.KarakterPinBoard()
		
	def KarakterPinBoard(self):
		self.PinBoard = ui.Board()
		self.PinBoard.SetSize(400, 145)
		self.PinBoard.SetCenterPosition()
		self.PinBoard.AddFlag('movable')
		self.PinBoard.AddFlag('float')
		self.PinBoard.Show()
		self.KarakterPinElements = KarakterPinElements()

		self.baslik = self.KarakterPinElements.HorizontalBar(self.PinBoard, 7, 7, 385)
		self.baslik_text = self.KarakterPinElements.TextLine(self.PinBoard, 'Karakter pin Giris Sistemi', 130, 7, self.KarakterPinElements.RGB(255, 255, 255)) # Character pin login system

		self.pin_btns = {}
		self.pin_btns2 = {}
		self.btn_pos_x = [10, 95, 180, 260, 340]
		self.btn_pos_2_x = [10, 95, 180, 260, 340]
		for i in self.btn_pos_x:
			self.pin_btns["%s_btn" % self.btn_pos_x.index(i)] = self.KarakterPinElements.Button(self.PinBoard, str(self.btn_pos_x.index(i)), '', i, 150, lambda Index = self.btn_pos_x.index(i) : self.__KeyFunc(Index), 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
			self.pin_btns["%s_btn" % self.btn_pos_x.index(i)].Hide()
			self.pin_btns2["%s_btn" % self.btn_pos_x.index(i)] = self.KarakterPinElements.Button(self.PinBoard, str(self.btn_pos_x.index(i) + 5), '', i, 185, lambda Index2 = str(self.btn_pos_x.index(i) + 5) : self.__KeyFunc(Index2), 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
			self.pin_btns2["%s_btn" % self.btn_pos_x.index(i)].Hide()
		
		self.gerial = self.KarakterPinElements.Button(self.PinBoard, '<-', '', 330, 53, self.gerial_func, 'd:/ymir work/ui/public/xsmall_button_01.sub', 'd:/ymir work/ui/public/xsmall_button_02.sub', 'd:/ymir work/ui/public/xsmall_button_03.sub')
		
		self.pin_alt_btn = {}
		alt_btn_pos_x = [88, 224]
		alt_btns_dict = ["Tamam","Kapat"] # OK Close
		for i in alt_btn_pos_x:
			self.pin_alt_btn["%s_btn" % alt_btn_pos_x.index(i)] = self.KarakterPinElements.Button(self.PinBoard, alt_btns_dict[alt_btn_pos_x.index(i)], '', i, 84, lambda Index3 = alt_btn_pos_x.index(i) : self.__AltFunc(Index3), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		
		self.sanal_klavye_baslik = self.KarakterPinElements.HorizontalBar(self.PinBoard, 7, 120, 385)
		self.sanal_klavye_text = self.KarakterPinElements.TextLine(self.PinBoard, 'Sanal klavye:', 139, 119, self.KarakterPinElements.RGB(255, 255, 255))
		#virtual keyboard
		self.sanal_klavye_btn_minus = self.KarakterPinElements.Button(self.PinBoard, '', 'Sanal klavyeyi kapat', 211, 121, self.sanal_klavye_func, 'd:/ymir work/ui/game/windows/btn_minus_up.sub', 'd:/ymir work/ui/game/windows/btn_minus_over.sub', 'd:/ymir work/ui/game/windows/btn_minus_down.sub')
		#close virtual keyboard
		self.sanal_klavye_btn_plus = self.KarakterPinElements.Button(self.PinBoard, '', 'Sanal klavyeti ac', 211, 121, self.sanal_klavye_func, 'd:/ymir work/ui/game/windows/btn_plus_up.sub', 'd:/ymir work/ui/game/windows/btn_plus_over.sub', 'd:/ymir work/ui/game/windows/btn_plus_down.sub')
		#open virtual keyboard
		self.sanal_klavye_btn_minus.Hide()
		
		self.slotbar_pin, self.pin = self.KarakterPinElements.EditLine(self.PinBoard, '', 211, 54, 100, 15, 9)
		self.txt423 = self.KarakterPinElements.TextLine(self.PinBoard, 'Lutfen karakterinizin pin kodunu girin:', 17, 54, self.KarakterPinElements.RGB(255, 255, 255))
		#please enter your character pin
	
	def Popup(self, text):
		self.qqq = uiCommon.PopupDialog()
		self.qqq.SetText(text)
		self.qqq.Show()			
	
	def __KeyFunc(self, key):
		text = self.pin.GetText()
		if len(text) < 9:
			self.pin.SetText(text+str(key))
		else:
			self.Popup("Maksimum karakter girdiniz") # you have entered the maximum character
	
	def __AltFunc(self, key):
		if key:
			self.PinBoardOpenWindow()
			#self.ExitSelect()
		else:
			net.SendCharacterPinPacket(self.slot, int(self.pin.GetText()))
			self.PinBoardOpenWindow()
			self.StartGame()
	
	def sanal_klavye_func(self):
		global pin_sanal_klavye
		if not pin_sanal_klavye:
			self.sanal_klavye_btn_minus.Hide()
			for i in xrange(len(self.pin_btns)):
				self.pin_btns["%s_btn" % i].Hide()
				self.pin_btns2["%s_btn" % i].Hide()
			self.PinBoard.SetSize(400, 145)
			self.sanal_klavye_btn_plus.Show()
			pin_sanal_klavye = 1
		else:
			self.sanal_klavye_btn_plus.Hide()
			for i in xrange(len(self.pin_btns)):
				self.pin_btns["%s_btn" % i].Show()
				self.pin_btns2["%s_btn" % i].Show()
			self.PinBoard.SetSize(400, 230)		
			self.sanal_klavye_btn_minus.Show()
			pin_sanal_klavye = 0
	
	def gerial_func(self):
		text = self.pin.GetText()
		if text:
			self.pin.SetText(text[:-1])
	
	def PinBoardOpenWindow(self):
		if self.PinBoard.IsShow():
			self.PinBoard.Hide()
		else:
			self.PinBoard.Show()


http://puu.sh/jS1qz/711fdab257.png
http://puu.sh/jS1pA/4d8b2e9bbf.png


Find - Bul:
if 28 == key:
	id = net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_ID)
	if 0 == id:
		self.CreateCharacter()
	else:
		self.StartGame()

Change - Değiştir:
if 28 == key:
	id = net.GetAccountCharacterSlotDataInteger(self.slot, net.ACCOUNT_CHARACTER_SLOT_ID)
	if 0 == id:
		self.CreateCharacter()
	else:
		self.GetKarakterPinBoard()
		#self.StartGame()

http://puu.sh/jS1yU/2d572acc3f.png



Add in the bottom:
class KarakterPinElements:
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button

	def EditLine(self, parent, editlineText, x, y, width, heigh, max):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		Value = ui.EditLine()
		Value.SetParent(SlotBar)
		Value.SetSize(width, heigh)
		Value.SetPosition(1, 1)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetMultiLine()
		Value.SetNumberMode()
		Value.SetSecret()
		Value.SetText(editlineText)
		Value.Show()
		return SlotBar, Value

	def HorizontalBar(self, parent, x, y, width):
		horizontal = ui.HorizontalBar()
		if parent:
			horizontal.SetParent(parent)
		horizontal.SetPosition(x, y)
		horizontal.Create(width)
		horizontal.Show()
		return horizontal
		
	def TextLine(self, parent, textlineText, x, y, color):
		textline = ui.TextLine()
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.Show()
		return textline

	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)

http://puu.sh/jS1E5/3b263b113d.png