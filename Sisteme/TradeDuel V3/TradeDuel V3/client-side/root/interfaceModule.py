import gameInfo

class InterfaceModule(ui.ScriptWindow):	
	def OpenShopDialog(self, vid):
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			self.CloseShopDialog()
			return
		self.wndInventory.Show()
		self.wndInventory.SetTop()
		self.dlgShop.Open(vid)
		self.dlgShop.SetTop()