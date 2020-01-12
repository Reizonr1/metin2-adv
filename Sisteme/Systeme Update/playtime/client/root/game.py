*game.py

Find - Bul:
def BINARY_OnQuestConfirm(self, msg, timeout, pid)

Add it upper - Üstüne ekle:
	# LOGON
	def BINARY_InitPlayTime(self, play_time):
		if self.affectShower:
			self.affectShower.SetPlayTime(play_time)

	def BINARY_UpdatePlayTime(self, play_time):
		if self.affectShower:
			self.affectShower.OnUpdatePlayTime(play_time)
	# END LOGON
	

	
Find - Bul:
			"MyShopPriceList"		: self.__PrivateShop_PriceList,

Add it upper - Üstüne ekle:
			# LOGON
			"ClientLogonStart"		: self.BINARY_InitPlayTime,
			"ClientLogonUpdate"		: self.BINARY_UpdatePlayTime,
			# END LOGON