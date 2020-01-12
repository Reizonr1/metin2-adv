[..]
class GameButtonWindow(ui.ScriptWindow):
	[..]
	def __LoadWindow(self, filename):
		[..]

		try:
			self.gameButtonDict={
				[..]
				"GIFT" : self.GetChild("GiftIcon"),
			}

		[..]


		
	def ShowGiftButton(self):
		self.gameButtonDict["GIFT"].Show()

	def HideGiftButton(self):
		self.gameButtonDict["GIFT"].Hide()



	
