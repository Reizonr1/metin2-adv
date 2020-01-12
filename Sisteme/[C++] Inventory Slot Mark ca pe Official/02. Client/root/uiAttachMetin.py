# 1 Import app module @1st:
# ********************************* BEGIN ********************************* #
import app
# ********************************** END ********************************** #

# 2.1 Search this function in class AttachMetinDialog:
# ********************************* BEGIN ********************************* #
		def __init__(self):
# ********************************** END ********************************** #

# 2.2 And replace the whole woth this:
# ********************************* BEGIN ********************************* #
	if app.WJ_ENABLE_TRADABLE_ICON:  
		def __init__(self, wndInventory):
			ui.ScriptWindow.__init__(self)
			self.__LoadScript()

			self.metinItemPos = 0
			self.targetItemPos = 0
			self.wndInventory = wndInventory
			self.lockedItems = {i:(-1,-1) for i in range(2)}
	else:
		def __init__(self):
			ui.ScriptWindow.__init__(self)
			self.__LoadScript()

			self.metinItemPos = 0
			self.targetItemPos = 0
# ********************************** END ********************************** #

# 3.1 Search this in AttachMetinDialog.Destroy:
# ********************************* BEGIN ********************************* #
		self.toolTip = 0
# ********************************** END ********************************** #

# 3.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:  
			self.wndInventory = 0
# ********************************** END ********************************** #

# 4.1 Search this in AttachMetinDialog.Open:
# ********************************* BEGIN ********************************* #
		self.Show()
# ********************************** END ********************************** #

# 4.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:  
			self.SetCantMouseEventSlot(0, self.metinItemPos)
			self.SetCantMouseEventSlot(1, self.targetItemPos)
# ********************************** END ********************************** #

# 5.1 Search this in AttachMetinDialog.Close:
# ********************************* BEGIN ********************************* #
		self.Hide()
# ********************************** END ********************************** #

# 5.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:  
			self.SetCanMouseEventSlot(0, self.metinItemPos)
			self.SetCanMouseEventSlot(1, self.targetItemPos)
# ********************************** END ********************************** #

# 6.1 Paste these functions below of this function AttachMetinDialog.Close:
# ********************************* BEGIN ********************************* #
	def Close(self):
# ********************************** END ********************************** #

# 6.2 Paste this below:
# ********************************* BEGIN ********************************* #
	if app.WJ_ENABLE_TRADABLE_ICON:  
		def SetCanMouseEventSlot(self, what, slotIndex):
			itemInvenPage = slotIndex / player.INVENTORY_PAGE_SIZE
			localSlotPos = slotIndex - (itemInvenPage * player.INVENTORY_PAGE_SIZE)
			self.lockedItems[what] = (-1, -1)

			if itemInvenPage == self.wndInventory.GetInventoryPageIndex():
				self.wndInventory.wndItem.SetCanMouseEventSlot(localSlotPos)

		def SetCantMouseEventSlot(self, what, slotIndex):
			itemInvenPage = slotIndex / player.INVENTORY_PAGE_SIZE
			localSlotPos = slotIndex - (itemInvenPage * player.INVENTORY_PAGE_SIZE)
			self.lockedItems[what] = (itemInvenPage, localSlotPos)

			if itemInvenPage == self.wndInventory.GetInventoryPageIndex():
				self.wndInventory.wndItem.SetCantMouseEventSlot(localSlotPos)

		def RefreshLockedSlot(self):
			if self.wndInventory:
				for what, (itemInvenPage, itemSlotPos) in self.lockedItems.items():
					if self.wndInventory.GetInventoryPageIndex() == itemInvenPage:
						self.wndInventory.wndItem.SetCantMouseEventSlot(itemSlotPos)

				self.wndInventory.wndItem.RefreshSlot()
# ********************************** END ********************************** #



