Importlarýn arasýna ekle:
import autoafk
import time

Arat:
self.playerGauge = None

Altýna ekle:
self.AfkModeGui = autoafk.AfkGui()
self.AfkModeGui.Close()


Arat:
self.affectShower = None

Altýna ekle:
self.AfkModeGui = None


Arat:
def OnRecvWhisper(self, mode, name, line):

Altýna ekle:
if constInfo.AUTO_AFK_MODE:
	net.SendWhisperPacket(name, "Bilgisayar basinda degilim lutfen daha sonra yaziniz.")

http://puu.sh/koGSE/aff437cf7a.png


Arat:
def PartyHealReady(self):

Üstüne ekle:
	def __Start_Afk_Loop(self):
		constInfo.AUTO_AFK_MODE = 1
		self.PopupMessage("%s'de afk moduna gectin" % (str(time.strftime("%H.%M.%S - %d.%m.%y"))))
		self.AfkModeGui.OpenWindow()
		
	def __End_Afk_Loop(self):
		constInfo.AUTO_AFK_MODE = 0
		
		
http://puu.sh/koGUh/1f793453ab.png



Arat:
"MyShopPriceList"		: self.__PrivateShop_PriceList,

Üstüne ekle:
"set_afk"				: self.__Start_Afk_Loop,
"del_afk"				: self.__End_Afk_Loop,


http://puu.sh/koGWd/3a52a8ec09.png