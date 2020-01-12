""""""
#1) Search: import localeInfo
#2) Make a new line and paste:
if app.ENABLE_ATTR_TRANSFER_SYSTEM:
	import uiAttrTransfer
""""""

""""""
#1) Search: def __MakeWebWindow(self):
#2) After their function make a new line and paste:
	if app.ENABLE_ATTR_TRANSFER_SYSTEM:
		def __MakeAttrTransferWindow(self):
			self.wndAttrTransfer = uiAttrTransfer.TransferWindow()
			self.wndAttrTransfer.LoadWindow()
			self.wndAttrTransfer.Hide()
""""""

""""""
#1) Search: self.__MakeWebWindow()
#2) Make a new line and paste:
		if app.ENABLE_ATTR_TRANSFER_SYSTEM:
			self.__MakeAttrTransferWindow()
""""""

""""""
#1) Search: self.wndSafebox.SetItemToolTip(self.tooltipItem)
#2) Make a new line and paste:
		if app.ENABLE_ATTR_TRANSFER_SYSTEM:
			self.wndAttrTransfer.SetItemToolTip(self.tooltipItem)
""""""

""""""
#1) Search: self.wndHelp.Destroy()
#2) Make a new line and paste:
		if app.ENABLE_ATTR_TRANSFER_SYSTEM:
			if self.wndAttrTransfer:
				self.wndAttrTransfer.Destroy()
""""""

""""""
#1) Search: del self.wndHelp
#2) Make a new line and paste:
		if app.ENABLE_ATTR_TRANSFER_SYSTEM:
			del self.wndAttrTransfer
""""""

""""""
#1) Search: def OpenWebWindow(self, url):
#2) Make a new line and paste:
	if app.ENABLE_ATTR_TRANSFER_SYSTEM:
		def OpenAttrTransferWindow(self):
			self.wndAttrTransfer.Open()
			if self.wndInventory.IsShow() == FALSE:
				self.wndInventory.Show()

		def CloseAttrTransferWindow(self):
			self.wndAttrTransfer.Close()

		def AttrTransferSuccess(self):
			self.wndAttrTransfer.Success()
""""""