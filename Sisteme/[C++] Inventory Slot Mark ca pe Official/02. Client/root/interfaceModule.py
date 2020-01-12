# 1.1 Search this in Interface.__init__:
# ********************************* BEGIN ********************************* #
		self.windowOpenPosition = 0
# ********************************** END ********************************** #

# 1.2 Add this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.onTopWindow = player.ON_TOP_WND_NONE
# ********************************** END ********************************** #

# 2.1 Search this in Interface.__MakeWindows:
# ********************************* BEGIN ********************************* #
		wndSafebox = uiSafebox.SafeboxWindow()
# ********************************** END ********************************** #

# 2.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			wndSafebox.BindInterface(self)
# ********************************** END ********************************** #

# 3.1 Search this in Interface.__MakeDialogs:
# ********************************* BEGIN ********************************* #
		self.dlgExchange = uiExchange.ExchangeDialog()
# ********************************** END ********************************** #

# 3.2 Add this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.dlgExchange.BindInterface(self)
			self.dlgExchange.SetInven(self.wndInventory)
			self.wndInventory.BindWindow(self.dlgExchange)
# ********************************** END ********************************** #

# 4.1 Search this in Interface.__MakeDialogs:
# ********************************* BEGIN ********************************* #
		self.dlgShop = uiShop.ShopDialog()
# ********************************** END ********************************** #

# 4.2 Add this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.dlgShop.BindInterface(self)
# ********************************** END ********************************** #

# 5.1 Search this in Interface.__MakeDialogs:
# ********************************* BEGIN ********************************* #
		self.privateShopBuilder = uiPrivateShopBuilder.PrivateShopBuilder()
# ********************************** END ********************************** #

# 5.2 Add this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.privateShopBuilder.BindInterface(self)
			self.privateShopBuilder.SetInven(self.wndInventory)
			self.wndInventory.BindWindow(self.privateShopBuilder)
# ********************************** END ********************************** #

# 6. Paste this functions below the "Interface.RefreshExchange":
# ********************************* BEGIN ********************************* #
	if app.WJ_ENABLE_TRADABLE_ICON:
		def CantTradableItemExchange(self, dstSlotIndex, srcSlotIndex):
			self.dlgExchange.CantTradableItem(dstSlotIndex, srcSlotIndex)
# ********************************** END ********************************** #

# 7. Add these functions below the "Interface.EmptyFunc":
# ********************************* BEGIN ********************************* #
	def GetInventoryPageIndex(self):
		if self.wndInventory:
			return self.wndInventory.GetInventoryPageIndex()
		else:
			return -1

	if app.WJ_ENABLE_TRADABLE_ICON:
		def SetOnTopWindow(self, onTopWnd):
			self.onTopWindow = onTopWnd

		def GetOnTopWindow(self):
			return self.onTopWindow

		def RefreshMarkInventoryBag(self):
			self.wndInventory.RefreshMarkSlots()
# ********************************** END ********************************** #

# 8.1 Search this in Interface.__MakeDialogs:
# ********************************* BEGIN ********************************* #
		self.dlgRefineNew = uiRefine.RefineDialogNew()
# ********************************** END ********************************** #

# 8.2 Add this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.dlgRefineNew.SetInven(self.wndInventory)
			self.wndInventory.BindWindow(self.dlgRefineNew)
# ********************************** END ********************************** #

