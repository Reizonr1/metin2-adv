##Search for:
	def OnPickMoney(self, money):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GAME_PICK_MONEY % (money))
##replace with:
	def OnPickMoney(self, money):
		self.interface.OnPickMoneyNew(money)