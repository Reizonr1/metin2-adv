# 1.1 Search this in ExchangeDialog.__init__:
# ********************************* BEGIN ********************************* #
		self.yStart = 0
# ********************************** END ********************************** #

# 1.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.interface = 0
			self.wndInventory = 0
			self.lockedItems = {i:(-1,-1) for i in range(exchange.EXCHANGE_ITEM_MAX_NUM)}
# ********************************** END ********************************** #

# 2.1 Search this in ExchangeDialog.Destroy:
# ********************************* BEGIN ********************************* #
		self.tooltipItem = 0
# ********************************** END ********************************** #

# 2.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.interface = 0
			self.wndInventory = 0
			self.lockedItems = {i:(-1,-1) for i in range(exchange.EXCHANGE_ITEM_MAX_NUM)}
# ********************************** END ********************************** #

# 3.1 Search this in ExchangeDialog.OpenDialog:
# ********************************* BEGIN ********************************* #
		self.Show()
# ********************************** END ********************************** #

# 3.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.interface.SetOnTopWindow(player.ON_TOP_WND_EXCHANGE)
			self.interface.RefreshMarkInventoryBag()
# ********************************** END ********************************** #

# 4.1 Search this in ExchangeDialog.CloseDialog:
# ********************************* BEGIN ********************************* #
		self.Hide()
# ********************************** END ********************************** #

# 4.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			for exchangePos, (itemInvenPage, itemSlotPos) in self.lockedItems.items():
				if itemInvenPage == self.wndInventory.GetInventoryPageIndex():
					self.wndInventory.wndItem.SetCanMouseEventSlot(itemSlotPos)

			self.lockedItems = {i:(-1,-1) for i in range(exchange.EXCHANGE_ITEM_MAX_NUM)}
			self.interface.SetOnTopWindow(player.ON_TOP_WND_NONE)
			self.interface.RefreshMarkInventoryBag()
# ********************************** END ********************************** #

# 5.1 REMOVED!
# ********************************* BEGIN ********************************* #
# ********************************** END ********************************** #

# 5.2 REMOVED!
# ********************************* BEGIN ********************************* #
# ********************************** END ********************************** #

# 6.1 Search this in ExchangeDialog.Refresh:
# ********************************* BEGIN ********************************* #
		self.RefreshTargetSlot()
# ********************************** END ********************************** #

# 6.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.RefreshLockedSlot()
# ********************************** END ********************************** #

# 7.1 Search this in ExchangeDialog.OnTop:
# ********************************* BEGIN ********************************* #
		self.tooltipItem.SetTop()
# ********************************** END ********************************** #

# 7.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			if self.interface:
				self.interface.SetOnTopWindow(player.ON_TOP_WND_EXCHANGE)
				self.interface.RefreshMarkInventoryBag()
# ********************************** END ********************************** #

# 8.1 Search this function in class SafeboxWindow:
# ********************************* BEGIN ********************************* #
	def OnUpdate(self):
# ********************************** END ********************************** #

# 8.2 Paste these functions below the found function:
# ********************************* BEGIN ********************************* #
	if app.WJ_ENABLE_TRADABLE_ICON:
		def CantTradableItem(self, destSlotIndex, srcSlotIndex):
			if True == exchange.GetAcceptFromTarget():
				return

			itemInvenPage = srcSlotIndex / player.INVENTORY_PAGE_SIZE
			localSlotPos = srcSlotIndex - (itemInvenPage * player.INVENTORY_PAGE_SIZE)
			self.lockedItems[destSlotIndex] = (itemInvenPage, localSlotPos)

			if self.wndInventory.GetInventoryPageIndex() == itemInvenPage and self.IsShow():
				self.wndInventory.wndItem.SetCantMouseEventSlot(localSlotPos)

		def RefreshLockedSlot(self):
			if self.wndInventory:
				for exchangePos, (itemInvenPage, itemSlotPos) in self.lockedItems.items():
					if self.wndInventory.GetInventoryPageIndex() == itemInvenPage:
						self.wndInventory.wndItem.SetCantMouseEventSlot(itemSlotPos)

				self.wndInventory.wndItem.RefreshSlot()

		def BindInterface(self, interface):
			self.interface = interface

		def SetInven(self, wndInventory):
			from _weakref import proxy
			self.wndInventory = proxy(wndInventory)
# ********************************** END ********************************** #

