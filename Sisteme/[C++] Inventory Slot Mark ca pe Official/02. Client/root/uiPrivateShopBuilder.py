# 1 Import app module with the imports at the top of the file:
# ********************************* BEGIN ********************************* #
import app
# ********************************** END ********************************** #

# 2.1 Search this in PrivateShopBuilder.__init__:
# ********************************* BEGIN ********************************* #
		self.title = ""
# ********************************** END ********************************** #

# 2.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.interface = None
			self.wndInventory = None
			self.lockedItems = {i:(-1,-1) for i in range(shop.SHOP_SLOT_COUNT)}
# ********************************** END ********************************** #

# 3.1 Search this in PrivateShopBuilder.Destroy:
# ********************************* BEGIN ********************************* #
		self.priceInputBoard = None
# ********************************** END ********************************** #

# 3.2 Add this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.interface = None
			self.wndInventory = None
			self.lockedItems = {i:(-1,-1) for i in range(shop.SHOP_SLOT_COUNT)}
# ********************************** END ********************************** #

# 4.1 Search this in PrivateShopBuilder.Open:
# ********************************* BEGIN ********************************* #
		self.Show()
# ********************************** END ********************************** #

# 4.2 Paste below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.lockedItems = {i:(-1,-1) for i in range(shop.SHOP_SLOT_COUNT)}
			self.interface.SetOnTopWindow(player.ON_TOP_WND_PRIVATE_SHOP)
			self.interface.RefreshMarkInventoryBag()
# ********************************** END ********************************** #

# 5.1 Search this in PrivateShopBuilder.Close:
# ********************************* BEGIN ********************************* #
		self.Hide()
# ********************************** END ********************************** #

# 5.2 Paste below:
# ********************************* BEGIN ********************************* #
		if self.priceInputBoard:
			self.priceInputBoard.Close()
			self.priceInputBoard = None

		if app.WJ_ENABLE_TRADABLE_ICON:
			for privatePos, (itemInvenPage, itemSlotPos) in self.lockedItems.items():
				if itemInvenPage == self.wndInventory.GetInventoryPageIndex():
					self.wndInventory.wndItem.SetCanMouseEventSlot(itemSlotPos)

			self.lockedItems = {i:(-1,-1) for i in range(shop.SHOP_SLOT_COUNT)}
			self.interface.SetOnTopWindow(player.ON_TOP_WND_NONE)
			self.interface.RefreshMarkInventoryBag()
# ********************************** END ********************************** #

# 6.1 Search this in PrivateShopBuilder.Refresh:
# ********************************* BEGIN ********************************* #
		self.itemSlot.RefreshSlot()
# ********************************** END ********************************** #

# 6.2 Add below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.RefreshLockedSlot()
# ********************************** END ********************************** #

# 7.1 Search this in PrivateShopBuilder.OnSelectEmptySlot:
# ********************************* BEGIN ********************************* #
			priceInputBoard = uiCommon.MoneyInputDialog()
# ********************************** END ********************************** #

# 7.2 Add this above:
# ********************************* BEGIN ********************************* #
			if app.WJ_ENABLE_TRADABLE_ICON and player.SLOT_TYPE_INVENTORY == attachedSlotType:
				self.CantTradableItem(selectedSlotPos, attachedSlotPos)
# ********************************** END ********************************** #

# 8.1 Search this in PrivateShopBuilder.OnSelectItemSlot:
# ********************************* BEGIN ********************************* #
			snd.PlaySound("sound/ui/drop.wav")
# ********************************** END ********************************** #

# 8.2 Add this below:
# ********************************* BEGIN ********************************* #
			if app.WJ_ENABLE_TRADABLE_ICON:
				(itemInvenPage, itemSlotPos) = self.lockedItems[selectedSlotPos]
				if itemInvenPage == self.wndInventory.GetInventoryPageIndex():
					self.wndInventory.wndItem.SetCanMouseEventSlot(itemSlotPos)

				self.lockedItems[selectedSlotPos] = (-1, -1)
# ********************************** END ********************************** #

# 9.1 Search this function in class PrivateShopBuilder:
# ********************************* BEGIN ********************************* #
	def CancelInputPrice(self):
# ********************************** END ********************************** #

# 9.2 Add replace the whole with this:
# ********************************* BEGIN ********************************* #
	def CancelInputPrice(self):
		if app.WJ_ENABLE_TRADABLE_ICON:
			itemInvenPage = self.priceInputBoard.sourceSlotPos / player.INVENTORY_PAGE_SIZE
			itemSlotPos = self.priceInputBoard.sourceSlotPos - (itemInvenPage * player.INVENTORY_PAGE_SIZE)
			if self.wndInventory.GetInventoryPageIndex() == itemInvenPage:
				self.wndInventory.wndItem.SetCanMouseEventSlot(itemSlotPos)

			self.lockedItems[self.priceInputBoard.targetSlotPos] = (-1, -1)

		if self.priceInputBoard:
			self.priceInputBoard.Close()
		self.priceInputBoard = None
		return 1
# ********************************** END ********************************** #

# 10.1 Search this function in class PrivateShopBuilder:
# ********************************* BEGIN ********************************* #
	def OnOverOutItem(self):
# ********************************** END ********************************** #

# 10.2 Paste these functions below the found function:
# ********************************* BEGIN ********************************* #
	if app.WJ_ENABLE_TRADABLE_ICON:
		def CantTradableItem(self, destSlotIndex, srcSlotIndex):
			itemInvenPage = srcSlotIndex / player.INVENTORY_PAGE_SIZE
			localSlotPos = srcSlotIndex - (itemInvenPage * player.INVENTORY_PAGE_SIZE)
			self.lockedItems[destSlotIndex] = (itemInvenPage, localSlotPos)
			if self.wndInventory.GetInventoryPageIndex() == itemInvenPage:
				self.wndInventory.wndItem.SetCantMouseEventSlot(localSlotPos)

		def RefreshLockedSlot(self):
			if self.wndInventory:
				for privatePos, (itemInvenPage, itemSlotPos) in self.lockedItems.items():
					if self.wndInventory.GetInventoryPageIndex() == itemInvenPage:
						self.wndInventory.wndItem.SetCantMouseEventSlot(itemSlotPos)

				self.wndInventory.wndItem.RefreshSlot()

		def BindInterface(self, interface):
			self.interface = interface

		def OnTop(self):
			if self.interface:
				self.interface.SetOnTopWindow(player.ON_TOP_WND_PRIVATE_SHOP)
				self.interface.RefreshMarkInventoryBag()

		def SetInven(self, wndInventory):
			from _weakref import proxy
			self.wndInventory = proxy(wndInventory)
# ********************************** END ********************************** #
