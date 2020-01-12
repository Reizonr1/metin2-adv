# 1.1 Search this in ShopDialog.__init__:
# ********************************* BEGIN ********************************* #
		self.itemBuyQuestionDialog = None
# ********************************** END ********************************** #

# 1.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.interface = None
# ********************************** END ********************************** #

# 2.1 Search this in ShopDialog.Destroy:
# ********************************* BEGIN ********************************* #
		self.Close()
# ********************************** END ********************************** #

# 2.2 And replace it with this:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.Close(True)
			self.interface = None
		else:
			self.Close()
# ********************************** END ********************************** #

# 3.1 Search this function in class ShopDialog:
# ********************************* BEGIN ********************************* #
	def Close(self):
# ********************************** END ********************************** #

# 3.2 Add replace the whole with this:
# ********************************* BEGIN ********************************* #
	if app.WJ_ENABLE_TRADABLE_ICON:
		def Close(self, isDestroy=False):
			self.interface.SetOnTopWindow(player.ON_TOP_WND_NONE)
			if not isDestroy:
				self.interface.RefreshMarkInventoryBag()

			if self.itemBuyQuestionDialog:
				self.itemBuyQuestionDialog.Close()
				self.itemBuyQuestionDialog = None
				constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

			self.OnCloseQuestionDialog()
			shop.Close()
			net.SendShopEndPacket()
			self.CancelShopping()
			self.tooltipItem.HideToolTip()
			self.Hide()
	else:
		def Close(self):
			if self.itemBuyQuestionDialog:
				self.itemBuyQuestionDialog.Close()
				self.itemBuyQuestionDialog = None
				constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

			self.OnCloseQuestionDialog()
			shop.Close()
			net.SendShopEndPacket()
			self.CancelShopping()
			self.tooltipItem.HideToolTip()
			self.Hide()
# ********************************** END ********************************** #

# 4.1 Search this in ShopDialog.Open:
# ********************************* BEGIN ********************************* #
		(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()
# ********************************** END ********************************** #

# 4.2 Add this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			if not isPrivateShop:
				self.interface.SetOnTopWindow(player.ON_TOP_WND_SHOP)
				self.interface.RefreshMarkInventoryBag()
# ********************************** END ********************************** #

# 5.1 Search this function in class ShopDialog:
# ********************************* BEGIN ********************************* #
	def OnUpdate(self):
# ********************************** END ********************************** #

# 5.2 Paste these functions below the found function:
# ********************************* BEGIN ********************************* #
	if app.WJ_ENABLE_TRADABLE_ICON:
		def BindInterface(self, interface):
			self.interface = interface

		def OnTop(self):
			if not shop.IsPrivateShop():
				self.interface.SetOnTopWindow(player.ON_TOP_WND_SHOP)
				self.interface.RefreshMarkInventoryBag()
# ********************************** END ********************************** #
