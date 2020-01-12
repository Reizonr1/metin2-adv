import gameInfo

class ShopDialog...

	def UnselectItemSlot(self, selectedSlotPos):
		if shop.IsPrivateShop():
			self.AskBuyItem(selectedSlotPos)
		else:
			if len(gameInfo.DICE_SYSTEM) > 0:
				return
			net.SendShopBuyPacket(selectedSlotPos)
			
	def OnUpdate(self):
		if len(gameInfo.DICE_SYSTEM) > 0:
			self.Close()

	#to-in#
	def AnswerBuyItem(self, flag):
		if flag:
			if len(gameInfo.DICE_SYSTEM) > 0:
				self.itemBuyQuestionDialog.Close()
				self.itemBuyQuestionDialog = None
				return