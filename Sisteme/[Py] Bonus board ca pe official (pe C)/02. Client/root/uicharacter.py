# Search import chr add after

import uiCharacterDetails

# Search def __init__(self): add after

		self.chDetailsWnd = None
		self.isOpenedDetailsWnd = False		

# Search def Show(self): add before

	def OnTop(self):
		if self.chDetailsWnd:
			self.chDetailsWnd.SetTop()

	def Hide(self):
		if self.chDetailsWnd:
			self.isOpenedDetailsWnd = self.chDetailsWnd.IsShow()
			self.chDetailsWnd.Close()
		wndMgr.Hide(self.hWnd)

# Search ui.ScriptWindow.Show(self) add before

		self.__InitCharacterDetailsUIButton()
		if self.chDetailsWnd and self.isOpenedDetailsWnd:
			self.chDetailsWnd.Show()

# Search def __SetSkillSlotEvent(self): add before

		self.MainBoard = self.GetChild("board")
		self.ExpandBtn = ui.MakeButton(self.MainBoard, 240, 120, "", "d:/ymir work/ui/game/belt_inventory/", "btn_minimize_normal.tga", "btn_minimize_over.tga", "btn_minimize_down.tga")
		self.ExpandBtn.SetEvent(ui.__mem_func__(self.__ClickExpandButton))
		self.MinimizeBtn = ui.MakeButton(self.MainBoard, 240, 120, "", "d:/ymir work/ui/game/belt_inventory/", "btn_expand_normal.tga", "btn_expand_over.tga", "btn_expand_down.tga")
		self.MinimizeBtn.SetEvent(ui.__mem_func__(self.__ClickMinimizeButton))

	def __InitCharacterDetailsUIButton(self):
		self.ExpandBtn.Show()
		self.MinimizeBtn.Hide()

	def __ClickExpandButton(self):
		if not self.chDetailsWnd:
			self.chDetailsWnd = uiCharacterDetails.CharacterDetailsUI(self)
			self.chDetailsWnd.Show()
		else:
			self.chDetailsWnd.Show()

		self.ExpandBtn.Hide()
		self.MinimizeBtn.Show()

	def __ClickMinimizeButton(self):
		self.chDetailsWnd.Hide()
		self.MinimizeBtn.Hide()
		self.ExpandBtn.Show()

	def OnMoveWindow(self, x, y):
		if self.chDetailsWnd:
			self.chDetailsWnd.AdjustPosition(x, y)

# Search titleBarValue.SetCloseEvent(ui.__mem_func__(self.Hide)) and replace with

			titleBarValue.SetCloseEvent(ui.__mem_func__(self.Close))

# Search def Close(self): and replace with

	def Close(self):
		if 0 != self.toolTipSkill:
			self.toolTipSkill.Hide()

		if self.chDetailsWnd and self.chDetailsWnd.IsShow():
			self.chDetailsWnd.Hide()

		self.Hide()

# Search def __RefreshStatusPlusButtonList(self): add before

		if self.chDetailsWnd and self.chDetailsWnd.IsShow():
			self.chDetailsWnd.RefreshLabel()