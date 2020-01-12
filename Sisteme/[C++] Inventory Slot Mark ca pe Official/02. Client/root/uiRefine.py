# 1. Make sure that app module is imported @ 1st, if not:
# ********************************* BEGIN ********************************* #
import app
# ********************************** END ********************************** #

# 2.1 Search this in RefineDialogNew.__init__:
# ********************************* BEGIN ********************************* #
		self.isLoaded = FALSE
# ********************************** END ********************************** #
# or Without case-sensitive False/false/0 

# 2.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.wndInventory = None
# ********************************** END ********************************** #

# 3.1 Search this in RefineDialogNew.__Initialize:
# ********************************* BEGIN ********************************* #
		self.type = 0
# ********************************** END ********************************** #

# 3.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.lockedItem = (-1,-1)
# ********************************** END ********************************** #

# 4.1 Search this in RefineDialogNew.Destroy:
# ********************************* BEGIN ********************************* #
		self.children = []
# ********************************** END ********************************** #

# 4.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.wndInventory = None
			self.lockedItem = (-1,-1)
# ********************************** END ********************************** #

# 5.1 Search this in RefineDialogNew.Open:
# ********************************* BEGIN ********************************* #
		self.toolTip.ClearToolTip()
# ********************************** END ********************************** #

# 5.2 Paste this above:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.SetCantMouseEventSlot(targetItemPos)
# ********************************** END ********************************** #

# 6.1 Search this function Close in class RefineDialogNew:
# ********************************* BEGIN ********************************* #
	def Close(self):
# ********************************** END ********************************** #

# 6.2 And replece it with this:
# ********************************* BEGIN ********************************* #
	def Close(self):
		if self.dlgQuestion:
			self.dlgQuestion.Close()

		self.dlgQuestion = None
		self.Hide()

		if app.WJ_ENABLE_TRADABLE_ICON:
			self.lockedItem = (-1, -1)
			self.SetCanMouseEventSlot(self.targetItemPos)
# ********************************** END ********************************** #

# 7.1 Search this functoin OnPressEscapeKey in class RefineDialogNew:
# ********************************* BEGIN ********************************* #
	def OnPressEscapeKey(self):
# ********************************** END ********************************** #

# 7.2 Paste these below that function:
# ********************************* BEGIN ********************************* #
	if app.WJ_ENABLE_TRADABLE_ICON:
		def SetCanMouseEventSlot(self, slotIndex):
			itemInvenPage = slotIndex / player.INVENTORY_PAGE_SIZE
			localSlotPos = slotIndex - (itemInvenPage * player.INVENTORY_PAGE_SIZE)
			self.lockedItem = (-1, -1)

			if itemInvenPage == self.wndInventory.GetInventoryPageIndex():
				self.wndInventory.wndItem.SetCanMouseEventSlot(localSlotPos)

		def SetCantMouseEventSlot(self, slotIndex):
			itemInvenPage = slotIndex / player.INVENTORY_PAGE_SIZE
			localSlotPos = slotIndex - (itemInvenPage * player.INVENTORY_PAGE_SIZE)
			self.lockedItem = (itemInvenPage, localSlotPos)

			if itemInvenPage == self.wndInventory.GetInventoryPageIndex():
				self.wndInventory.wndItem.SetCantMouseEventSlot(localSlotPos)

		def SetInven(self, wndInventory):
			from _weakref import proxy
			self.wndInventory = proxy(wndInventory)

		def RefreshLockedSlot(self):
			if self.wndInventory:
				itemInvenPage, itemSlotPos = self.lockedItem
				if self.wndInventory.GetInventoryPageIndex() == itemInvenPage:
					self.wndInventory.wndItem.SetCantMouseEventSlot(itemSlotPos)

				self.wndInventory.wndItem.RefreshSlot()
# ********************************** END ********************************** #
