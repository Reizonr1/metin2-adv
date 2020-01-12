##Search for:
	CHARACTER_SKILL_TAB = 2
##Down there put:
	class NewGoldChat(ui.Window):
		def __init__(self, parent = None, x = 0, y = 0):
			ui.Window.__init__(self)
			self.texts = {}
			self.parent = parent
			self.SpaceBet = 14
			self.maxY = 0
			self.x = x
			self.y = y
			self.ColorValue = 0xFFFFFFFF
			
			self.show = self.Button('Show Yang', x, y+3, self.showYang, 'sanyed_yang/btn_expand_normal.tga', 'sanyed_yang/btn_expand_over.tga', 'sanyed_yang/btn_expand_down.tga')
			self.hide = self.Button('Hide Yang', x, y+3, self.hideYang, 'sanyed_yang/btn_minimize_normal.tga', 'sanyed_yang/btn_minimize_over.tga', 'sanyed_yang/btn_minimize_down.tga')
			self.show.Hide()
			self.Show()

		def Button(self, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
			button = ui.Button()
			if self.parent != None:
				button.SetParent(self.parent)
			button.SetPosition(x, y)
			button.SetUpVisual(UpVisual)
			button.SetOverVisual(OverVisual)
			button.SetDownVisual(DownVisual)
			button.SetToolTipText(tooltipText)
			button.Show()
			button.SetEvent(func)
			return button

		def showYang(self):
			for i in xrange(len(self.texts)):
				self.texts[i].Show()
			self.hide.Show()
			self.show.Hide()
			self.Show()

		def hideYang(self):
			for i in xrange(len(self.texts)):
				self.texts[i].Hide()
			self.hide.Hide()
			self.show.Show()
			self.Hide()
			
		def GetMaxY(self):
			return self.maxY

		def AddGoldValue(self, text):
			for i in xrange(len(self.texts)):
				if len(self.texts) == 10 and i == 0:
					self.texts[i].Hide()
				x, y = self.texts[i].GetLocalPosition()
				self.texts[i].SetPosition(x, y-self.SpaceBet)

			i = 0
			if len(self.texts) == 10:
				for i in xrange(len(self.texts)-1):
					self.texts[i] = self.texts[i+1]
				i = 9
			else:
				i = len(self.texts)
			
			self.texts[i] = ui.TextLine("Tahoma:14")
			if self.parent != None:
				self.texts[i].SetParent(self.parent)
			self.texts[i].SetPosition(self.x, self.y)
			self.texts[i].SetPackedFontColor(self.ColorValue)
			self.texts[i].SetHorizontalAlignLeft()
			self.texts[i].SetOutline(TRUE)
			self.texts[i].SetText(text)
			if self.hide.IsShow():
				self.texts[i].Show()

			if self.hide.IsShow():
				x, y = self.texts[0].GetLocalPosition()
				x2, y2 = self.hide.GetLocalPosition()
				self.hide.SetPosition(x2, y-10)

		def ClearAll(self):
			self.Hide()
			self.texts = {}
			self.show.Hide()
			self.show = None
			self.hide.Hide()
			self.hide = None

		def OnRender(self):
			if len(self.texts) > 0 and self.hide.IsShow():
				x, y = self.hide.GetGlobalPosition()
				w, h = self.texts[0].GetTextSize()
				grp.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
				grp.RenderBar(x, y+h-6, 108, h*len(self.texts)+4)
				
##search for:
	def __MakeChatWindow(self):
##After this:
		self.wndChat.SetOpenChatLogEvent(ui.__mem_func__(self.ToggleChatLogWindow))
#add:
		if self.yangText:
			self.yangText.Hide()
		yangText = self.NewGoldChat(None, wndMgr.GetScreenWidth()/2 - wndChat.CHAT_WINDOW_WIDTH/2 + 600, wndMgr.GetScreenHeight() - wndChat.EDIT_LINE_HEIGHT - 37 + 9)
		self.yangText = yangText
##and after this function add:
	def OnPickMoneyNew(self, money):
		self.yangText.AddGoldValue("+%s"%(localeInfo.NumberToMoneyString(money)))
		
##search for:
	self.wndChat = None
##add down:
	self.yangText = None
##Search for:
		if self.wndChat:
			self.wndChat.Destroy()
##Add Down:
		if self.yangText:
			self.yangText.ClearAll()
##Search For:
		del self.wndChat
##Add Down:
		del self.yangText
##Search for:
		self.wndChat.Show()
##Add Down:
		self.yangText.Show()
##Search for:
		if self.wndChat:
			self.wndChat.Hide()
##Add Down:
		if self.yangText:
			self.yangText.Hide()
##Search for:
						self.wndChat,\
##Add Down:
						self.yangText,\