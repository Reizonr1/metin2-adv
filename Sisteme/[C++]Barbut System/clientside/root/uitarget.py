import gameInfo
import localegame

BUTTON_NAME_LIST = {
	"Bahis",
}

	def __init__(self):
		self.bahisZAMAN = 0
		
		self.buttonDict["Bahis"].SetEvent(ui.__mem_func__(self.__OnBahis))
		
	def ShowDefaultButton(self):
		if(self.bahisZAMAN < app.GetTime()):
			self.showingButtonList.append(self.buttonDict["Bahis"])
			
	##ekle-yeni##
	def __OnBahis(self):
		if "ACIK" in gameInfo.DICE_SYSTEM.keys():
			chat.AppendChat(chat.CHAT_TYPE_INFO, str(localegame.DICE_SYSTEM_OYNAYAMAZSIN))
			return
			
		if not (self.bahisZAMAN < app.GetTime()):
			return
			
		if gameInfo.DICE_SYSTEM == 1: return
			
		self.bahisZAMAN = app.GetTime() + 10
		gameInfo.sendPacket("bahis_oyna#"+str(chr.GetNameByVID(self.vid)))
		
		
		
	def OnUpdate(self):
		if self.isShowButton:
		
			if(self.bahisZAMAN < app.GetTime()):
				self.bahisZAMAN = 0
				self.__ShowButton("Bahis")
				self.RefreshButton()
			else:
				self.__HideButton("Bahis")
				self.RefreshButton()