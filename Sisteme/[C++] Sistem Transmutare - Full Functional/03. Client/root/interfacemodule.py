""""""
#1) Search:
IsQBHide = 0
#2) Before make a new line and paste:
if app.ENABLE_CHANGELOOK_SYSTEM:
	import uichangelook
""""""


""""""
#1) Search:
	def __MakeCubeWindow(self):
		self.wndCube = uiCube.CubeWindow()
		self.wndCube.LoadWindow()
		self.wndCube.Hide()
#2) Before make a new line and paste:
	if app.ENABLE_CHANGELOOK_SYSTEM:
		def __MakeChangeLookWindow(self):
			self.wndChangeLook = uichangelook.Window()
			self.wndChangeLook.LoadWindow()
			self.wndChangeLook.Hide()
			
			if self.wndInventory:
				self.wndInventory.SetChangeLookWindow(self.wndChangeLook)
""""""


""""""
#1) Search:
		self.__MakeCubeWindow()
#2) Before make a new line and paste:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.__MakeChangeLookWindow()
""""""


""""""
#1) Search:
		self.wndCube.SetItemToolTip(self.tooltipItem)
#2) Before make a new line and paste:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.wndChangeLook.SetItemToolTip(self.tooltipItem)
""""""


""""""
#1) Search:
		if self.wndCube:
			self.wndCube.Destroy()
#2) Before make a new line and paste:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			if self.wndChangeLook:
				self.wndChangeLook.Destroy()
""""""


""""""
#1) Search:
		del self.wndCube
#2) Before make a new line and paste:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			del self.wndChangeLook
""""""


""""""
#1) Search:
	def OpenCubeWindow(self):
		self.wndCube.Open()

		if False == self.wndInventory.IsShow():
			self.wndInventory.Show()
#2) Before make a new line and paste:
	if app.ENABLE_CHANGELOOK_SYSTEM:
		def ActChangeLook(self, iAct):
			if iAct == 1:
				if not self.wndChangeLook.IsOpened():
					self.wndChangeLook.Open()
				
				if not self.wndInventory.IsShow():
					self.wndInventory.Show()
				
				self.wndInventory.RefreshBagSlotWindow()
			elif iAct == 2:
				if self.wndChangeLook.IsOpened():
					self.wndChangeLook.Close()
				
				self.wndInventory.RefreshBagSlotWindow()
			elif iAct == 3 or iAct == 4:
				if self.wndChangeLook.IsOpened():
					self.wndChangeLook.Refresh()
				
				self.wndInventory.RefreshBagSlotWindow()
""""""