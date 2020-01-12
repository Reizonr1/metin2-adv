# 1.1 Search this in SafeboxWindow.__init__:
# ********************************* BEGIN ********************************* #
		self.tooltipItem = None
# ********************************** END ********************************** #

# 1.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.interface = None
# ********************************** END ********************************** #

# 2.1 Search this in SafeboxWindow.Destroy:
# ********************************* BEGIN ********************************* #
		self.wndItem = None
# ********************************** END ********************************** #

# 2.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.interface = None
# ********************************** END ********************************** #

# 3.1 Search this in SafeboxWindow.ShowWindow:
# ********************************* BEGIN ********************************* #
		(self.xSafeBoxStart, self.ySafeBoxStart, z) = player.GetMainCharacterPosition()
# ********************************** END ********************************** #

# 3.2 Paste this above:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.interface.SetOnTopWindow(player.ON_TOP_WND_SAFEBOX)
			self.interface.RefreshMarkInventoryBag()
# ********************************** END ********************************** #

# 4.1 Search this in SafeboxWindow.Close:
# ********************************* BEGIN ********************************* #
		net.SendChatPacket("/safebox_close")
# ********************************** END ********************************** #

# 4.2 Paste this above:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.interface.SetOnTopWindow(player.ON_TOP_WND_NONE)
# ********************************** END ********************************** #

# 5.1 Search this in SafeboxWindow.CommandCloseSafebox:
# ********************************* BEGIN ********************************* #
		self.Hide()
# ********************************** END ********************************** #

# 5.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.interface.RefreshMarkInventoryBag()
# ********************************** END ********************************** #

# 5.1 Search this function in class SafeboxWindow:
# ********************************* BEGIN ********************************* #
	def OnUpdate(self):
# ********************************** END ********************************** #

# 6.2 Paste these functions below the found function:
# ********************************* BEGIN ********************************* #
	if app.WJ_ENABLE_TRADABLE_ICON:
		def BindInterface(self, interface):
			self.interface = interface

		def OnTop(self):
			self.interface.SetOnTopWindow(player.ON_TOP_WND_SAFEBOX)
			self.interface.RefreshMarkInventoryBag()
# ********************************** END ********************************** #

