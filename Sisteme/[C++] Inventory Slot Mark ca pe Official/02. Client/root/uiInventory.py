# 1.1 Search this in InventoryWindow.__init__:
# ********************************* BEGIN ********************************* #
	dlgPickMoney = None
# ********************************** END ********************************** #

# 1.2 Paste this below:
# ********************************* BEGIN ********************************* #
	interface = None
	if app.WJ_ENABLE_TRADABLE_ICON:
		bindWnds = []
# ********************************** END ********************************** #

# 2.1 Search this function in class InventoryWindow:
# ********************************* BEGIN ********************************* #
	def BindInterfaceClass(self, interface):
# ********************************** END ********************************** #

# 2.2 Paste this function below:
# ********************************* BEGIN ********************************* #
	if app.WJ_ENABLE_TRADABLE_ICON:
		def BindWindow(self, wnd):
			self.bindWnds.append(wnd)
# ********************************** END ********************************** #

# 3.1 Search this in InventoryWindow.Destroy:
# ********************************* BEGIN ********************************* #
		self.interface = None
# ********************************** END ********************************** #

# 3.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.bindWnds = []
# ********************************** END ********************************** #

# 4.1 Search this function in class InventoryWindow:
# ********************************* BEGIN ********************************* #
	def __InventoryLocalSlotPosToGlobalSlotPos(self, local):
# ********************************** END ********************************** #

# 4.2 Paste these function below:
# ********************************* BEGIN ********************************* #
	def GetInventoryPageIndex(self):
		return self.inventoryPageIndex

	if app.WJ_ENABLE_TRADABLE_ICON:
		def RefreshMarkSlots(self, localIndex=None):
			if not self.interface:
				return

			onTopWnd = self.interface.GetOnTopWindow()
			if localIndex:
				slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(localIndex)
				if onTopWnd == player.ON_TOP_WND_NONE:
					self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif onTopWnd == player.ON_TOP_WND_SHOP:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SELL):
						self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif onTopWnd == player.ON_TOP_WND_EXCHANGE:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_GIVE):
						self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif onTopWnd == player.ON_TOP_WND_PRIVATE_SHOP:
					if player.IsAntiFlagBySlot(slotNumber, item.ITEM_ANTIFLAG_MYSHOP):
						self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif onTopWnd == player.ON_TOP_WND_SAFEBOX:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SAFEBOX):
						self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				return

			for i in xrange(player.INVENTORY_PAGE_SIZE):
				slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)

				if onTopWnd == player.ON_TOP_WND_NONE:
					self.wndItem.SetUsableSlotOnTopWnd(i)

				elif onTopWnd == player.ON_TOP_WND_SHOP:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SELL):
						self.wndItem.SetUnusableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)

				elif onTopWnd == player.ON_TOP_WND_EXCHANGE:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_GIVE):
						self.wndItem.SetUnusableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)

				elif onTopWnd == player.ON_TOP_WND_PRIVATE_SHOP:
					if player.IsAntiFlagBySlot(slotNumber, item.ITEM_ANTIFLAG_MYSHOP):
						self.wndItem.SetUnusableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)

				elif onTopWnd == player.ON_TOP_WND_SAFEBOX:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SAFEBOX):
						self.wndItem.SetUnusableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)
# ********************************** END ********************************** #

# 5.1 Search this in InventoryWindow.RefreshBagSlotWindow:
# ********************************* BEGIN ********************************* #
			if constInfo.IS_AUTO_POTION(itemVnum):
# ********************************** END ********************************** #

# 5.2 Paste this below of the whole if-statement<!>:
# ********************************* BEGIN ********************************* #
			if app.WJ_ENABLE_TRADABLE_ICON:
				self.RefreshMarkSlots(i)
# ********************************** END ********************************** #

# 6.1 Search this in InventoryWindow.RefreshBagSlotWindow:
# ********************************* BEGIN ********************************* #
		if self.wndBelt:
			self.wndBelt.RefreshSlot()
# ********************************** END ********************************** #

# 6.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			map(lambda wnd:wnd.RefreshLockedSlot(), self.bindWnds)
# ********************************** END ********************************** #

# 7.1 Search this in InventoryWindow.OnTop:
# ********************************* BEGIN ********************************* #
		if None != self.tooltipItem:
			self.tooltipItem.SetTop()
# ********************************** END ********************************** #

# 7.2 Paste this below:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:
			map(lambda wnd:wnd.RefreshLockedSlot(), self.bindWnds)
			self.RefreshMarkSlots()
# ********************************** END ********************************** #

# 8.1 Search this in InventoryWindow.__LoadWindow:
# ********************************* BEGIN ********************************* #
		self.attachMetinDialog = uiAttachMetin.AttachMetinDialog()
# ********************************** END ********************************** #

# 8.2 And replace it with this:
# ********************************* BEGIN ********************************* #
		if app.WJ_ENABLE_TRADABLE_ICON:  
			self.attachMetinDialog = uiAttachMetin.AttachMetinDialog(self)
			self.BindWindow(self.attachMetinDialog)
		else:
			self.attachMetinDialog = uiAttachMetin.AttachMetinDialog()
# ********************************** END ********************************** #
