import gameInfo


	def OnUpdate(self):
		if "OYUN_RAKIP" in gameInfo.DICE_SYSTEM.keys():
			net.SendExchangeExitPacket()