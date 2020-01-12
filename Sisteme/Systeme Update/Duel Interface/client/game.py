*game.py

Add this import - Importlara ekleyin:
import uipvprequest



Find - Bul:
"MyShopPriceList"		: self.__PrivateShop_PriceList,

Add it upper - Üstüne ekle:
#VS GUI
"pvpchallenge"			: self.__PvPChallenge_Dialog,
#END VS GUI




Find - Bul:
def __LoginLover(self):

Add it upper - Üstüne ekle:
#VS GUI
def __PvPChallenge_Dialog(self, Name, Level, VID, Race):
	self.PvPChallengeDialog = uipvprequest.PVPRequestDialog()
	self.PvPChallengeDialog.LoadDialog()
	self.PvPChallengeDialog.OpenDialog(Name, Level, VID, Race)
		
		

Find - Bul:
self.playerGauge = None

Add it under- Altına ekle:
self.PvPChallengeDialog = None #VS GUI



Find - Bul:
self.affectShower = None

Add it under- Altına ekle:
self.PvPChallengeDialog = None #VS GUI