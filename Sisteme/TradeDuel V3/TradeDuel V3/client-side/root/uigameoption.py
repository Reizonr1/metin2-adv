import gameInfo

	def __OnClickPvPModeFreeButton(self):
	
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			self.pvpModeButtonDict[player.PK_MODE_FREE].SetUp()
			chat.AppendChat(chat.CHAT_TYPE_INFO,"�temine ws varken serbest modunu kullanamazs�n.")
			return
			
	def __OnClickPvPModeGuildButton(self):

		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			self.pvpModeButtonDict[player.PK_MODE_GUILD].SetUp()
			chat.AppendChat(chat.CHAT_TYPE_INFO,"�temine ws varken lonca modunu kullanamazs�n.")
			return