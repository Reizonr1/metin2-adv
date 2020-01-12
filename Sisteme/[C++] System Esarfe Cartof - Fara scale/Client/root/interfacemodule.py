""""""
#1) Search: import locale
#2) Make a new line and paste:
	import uiAcce
""""""

""""""
#1) Search: def __MakeWebWindow(self):
#2) After their function make a new line and paste:
	def __MakeAcceWindow(self):
		self.wndAcce = uiAcce.AcceWindow()
		self.wndAcce.LoadWindow()
		self.wndAcce.Hide()
		self.wndAcceAbs = uiAcce.AcceAbsorbWindow()
		self.wndAcceAbs.LoadWindow()
		self.wndAcceAbs.Hide()
""""""

""""""
#1) Search: self.__MakeWebWindow()
#2) Make a new line and paste:
		self.__MakeAcceWindow()
""""""

""""""
#1) Search: self.wndSafebox.SetItemToolTip(self.tooltipItem)
#2) Make a new line and paste:
		self.wndAcce.SetItemToolTip(self.tooltipItem)
		self.wndAcceAbs.SetItemToolTip(self.tooltipItem)
""""""

""""""
#1) Search: self.wndHelp.Destroy()
#2) Make a new line and paste:
		if self.wndAcce:
			self.wndAcce.Destroy()

		if self.wndAcceAbs:
			self.wndAcceAbs.Destroy()
""""""

""""""
#1) Search: del self.wndHelp
#2) Make a new line and paste:
		del self.wndAcce
		del self.wndAcceAbs
""""""

""""""
#1) Search: def OpenWebWindow(self, url):
#2) Make a new line and paste:
	def OpenAcceWindow(self):
		self.wndAcce.Open()
		if self.wndInventory.IsShow() == FALSE:
			self.wndInventory.Show()

	def UpdateAcceInfo(self, gold, itemVnum, count, rItemVnum, rCount):
		self.wndAcce.UpdateInfo(gold, itemVnum, count, rItemVnum, rCount)

	def CloseAcceWindow(self):
		self.wndAcce.Close()

	def FailedAcceWork(self):
		self.wndAcce.Clear()

	def SucceedAcceWork(self, itemVnum, count):
		self.wndAcce.ClearSuccess()
		print "Making acce has succesfully! [%d:%d]" % (itemVnum, count)

	def OpenAcceAbsWindow(self):
		self.wndAcceAbs.Open()
		if self.wndInventory.IsShow() == FALSE:
			self.wndInventory.Show()

	def SucceedAcceAbsWork(self):
		self.wndAcceAbs.Clear()
""""""