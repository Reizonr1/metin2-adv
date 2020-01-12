import gameInfo

class PrivateShopBuilder(ui.ScriptWindow):
	def Open(self, title):
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			self.Hide()
			return
			
	def OnOk(self):
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			self.Close()
			return