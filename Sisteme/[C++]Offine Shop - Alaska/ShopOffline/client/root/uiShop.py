import net
import player
import item
import snd
import shop
import net
import wndMgr
import app
import chat
import constInfo
import ui
import uiCommon
import mouseModule
import localeInfo
import chr

###################################################################################################
## Shop
class ShopDialog(ui.ScriptWindow):

	###Find this function and make changes like this
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		[..]
		self.vid = 0
		[..]
	
	def Destroy(self):
		[..]
		self.vid = 0
		[..]
	def Open(self, vid, type=0):
		self.vid=int(vid)
		isPrivateShop = False
		isMainPlayerPrivateShop = False
		myshop=False
		for i in xrange(len(constInfo.MyShops)):
			if int(constInfo.MyShops[i]["vid"]) == int(self.vid):
				myshop=True
				self.vid=int(constInfo.MyShops[i]["id"])
		chr.SelectInstance(self.vid)
		if chr.GetRace() == 30000 or not chr.IsNPC(self.vid):
			isPrivateShop = True
		if player.IsMainCharacterIndex(self.vid):
			myshop=True
			self.vid=""
		if myshop == True:
			isMainPlayerPrivateShop = True

			self.btnBuy.Hide()
			self.btnSell.Hide()
			self.btnClose.Show()

		else:

			isMainPlayerPrivateShop = False

			self.btnBuy.Show()
			self.btnSell.Show()
			self.btnClose.Hide()
		shop.Open(isPrivateShop, isMainPlayerPrivateShop)
		
		[..]


	def OnClosePrivateShop(self):
		net.SendChatPacket("/close_shop "+str(self.vid))
		self.OnCloseQuestionDialog()
		return True

	[..]