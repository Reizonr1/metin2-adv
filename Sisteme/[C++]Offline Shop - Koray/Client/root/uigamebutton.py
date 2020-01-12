Search:
import ui

Add it under:
import constInfo

https://puu.sh/sgXrW/fe9c3db94a.png

---

Search:
			self.gameButtonDict["EXIT_OBSERVER"].SetEvent(ui.__mem_func__(self.__OnClickExitObserver))

Add it under:
			if app.ENABLE_OFFLINE_SHOP:
				self.gameButtonDict.update({"EXIT_MOVESHOP"	: self.GetChild("ExitMoveShop")})

			self.gameButtonDict["EXIT_OBSERVER"].SetEvent(ui.__mem_func__(self.__OnClickExitObserver))
			if app.ENABLE_OFFLINE_SHOP:
				self.gameButtonDict["EXIT_MOVESHOP"].SetEvent(ui.__mem_func__(self.__OnClickExitMoveShop))

https://puu.sh/sgXuv/68a98e9b73.png

---

Search:
	def __OnClickExitObserver(self):
		net.SendChatPacket("/observer_exit")

Add it under:
	if app.ENABLE_OFFLINE_SHOP:
		def __OnClickExitMoveShop(self):
			net.offshopx = 0
			net.offshopy = 0
			net.SetShopMoveMode(0)
			constInfo.SHOP_MOVE_FLAG = 0
			net.SendChatPacket("/reloadpos")


Search:
	def SetObserverMode(self, isEnable):
		if isEnable:
			self.gameButtonDict["EXIT_OBSERVER"].Show()
		else:
			self.gameButtonDict["EXIT_OBSERVER"].Hide()

Add it under:
	if app.ENABLE_OFFLINE_SHOP:
		def SetMoveShop(self, isEnable):
			if isEnable:
				self.gameButtonDict["EXIT_MOVESHOP"].Show()
			else:
				self.gameButtonDict["EXIT_MOVESHOP"].Hide()		
	

https://puu.sh/sgXy8/0f5f0ff341.png



