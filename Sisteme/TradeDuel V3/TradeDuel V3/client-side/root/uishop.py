import gameInfo

class ShopDialog...

	def UnselectItemSlot(self, selectedSlotPos):
		if shop.IsPrivateShop():
			self.AskBuyItem(selectedSlotPos)
		else:
			if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
				return
			net.SendShopBuyPacket(selectedSlotPos)
			
	def OnUpdate(self):
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			self.Close()

	#to-in#
	def AnswerBuyItem(self, flag):
		if flag:
			if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
				self.itemBuyQuestionDialog.Close()
				self.itemBuyQuestionDialog = None
				return