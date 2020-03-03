""""""
#1) Search: import localeInfo
#2) Make a new line and paste:
if app.ENABLE_NEW_ENCHANT_ATTR:
	import uiAttrDialog
""""""

""""""
#1) Search: def __MakeWebWindow(self):
#2) After their function make a new line and paste:
	if app.ENABLE_NEW_ENCHANT_ATTR:
		def __MakeEnchantAttrWindow(self):
			self.wndEnchantAttr = uiAttrDialog.AttrDialogWindow()
			self.wndEnchantAttr.LoadWindow()
			self.wndEnchantAttr.Hide()
""""""

""""""
#1) Search: self.__MakeWebWindow()
#2) Make a new line and paste:
		if app.ENABLE_NEW_ENCHANT_ATTR:
			self.__MakeEnchantAttrWindow()
""""""

""""""
#1) Search: self.wndSafebox.SetItemToolTip(self.tooltipItem)
#2) Make a new line and paste:
		if app.ENABLE_NEW_ENCHANT_ATTR:
			self.wndEnchantAttr.SetItemToolTip(self.tooltipItem)
""""""

""""""
#1) Search: self.wndHelp.Destroy()
#2) Make a new line and paste:
		if app.ENABLE_NEW_ENCHANT_ATTR:
			if self.wndEnchantAttr:
				self.wndEnchantAttr.Destroy()
""""""

""""""
#1) Search: del self.wndHelp
#2) Make a new line and paste:
		if app.ENABLE_NEW_ENCHANT_ATTR:
			del self.wndEnchantAttr
""""""

""""""
#1) Search: def OpenWebWindow(self, url):
#2) Before this make a new line and paste:
	if app.ENABLE_NEW_ENCHANT_ATTR:
		def OpenEnchantAttrWindow(self, cell, new_attrSlot = 0):
			self.wndEnchantAttr.Open(cell, new_attrSlot)
""""""