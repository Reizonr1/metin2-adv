## Search for:
		questionDialog = None

## Add before:
	if app.ENABLE_CHANGE_LOOK_SYSTEM:
		USE_TYPE_TUPLE = USE_TYPE_TUPLE + ("USE_RESET_LOOK_VNUM",)

## If you have def OnUpdate(self) add this inside it:
		self.RefreshBagSlotWindow()

		if app.ENABLE_CHANGE_LOOK_SYSTEM:
			for i in xrange(player.INVENTORY_PAGE_SIZE):
				if app.ENABLE_CHANGE_LOOK_SYSTEM:
					GlobalSlot = self.__InventoryLocalSlotPosToGlobalSlotPos(i)

					if player.GetItemLook(GlobalSlot):
						self.wndItem.EnableSlotCoverImage(i)
					else:
						self.wndItem.DisableSlotCoverImage(i)

					if player.FindActivedChangeLookSlot(0) == GlobalSlot or player.FindActivedChangeLookSlot(1) == GlobalSlot:
						self.wndItem.ActivateChangeLookSlot(i)
					else:
						self.wndItem.DeactivateChangeLookSlot(i)

## If you dont have def OnUpdate(self) paste this before RefreshBagSlotWindow event:
	if app.ENABLE_CHANGE_LOOK_SYSTEM:
		def OnUpdate(self):
			self.RefreshBagSlotWindow()

			for i in xrange(player.INVENTORY_PAGE_SIZE):
				GlobalSlot = self.__InventoryLocalSlotPosToGlobalSlotPos(i)

				if player.GetItemLook(GlobalSlot):
					self.wndItem.EnableSlotCoverImage(i)
				else:
					self.wndItem.DisableSlotCoverImage(i)

				if player.FindActivedChangeLookSlot(0) == GlobalSlot or player.FindActivedChangeLookSlot(1) == GlobalSlot:
					self.wndItem.ActivateChangeLookSlot(i)
				else:
					self.wndItem.DeactivateChangeLookSlot(i)

## Search for x2:
			setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)					

## Add under:
			if app.ENABLE_CHANGE_LOOK_SYSTEM:
				if player.GetItemLook(slotNumber):
					self.wndEquip.EnableSlotCoverImage(slotNumber)
				else:
					self.wndEquip.DisableSlotCoverImage(slotNumber)

## Search for:
	def SelectEmptySlot(self, selectedSlotPos):

## Add under:
		if app.ENABLE_CHANGE_LOOK_SYSTEM:
			if constInfo.BusySlots():
				return

## Search for:
			elif "USE_ADD_ACCESSORY_SOCKET" == useType:
				if self.__CanAddAccessorySocket(dstSlotPos):
					return True

## Add under:
			elif "USE_RESET_LOOK_VNUM" == useType:
				if not app.ENABLE_CHANGE_LOOK_SYSTEM:
					return False

				if self.__CanResetLookVnum(dstSlotPos):
					return True

## Search for:
	def ShowToolTip(self, slotIndex):

## Add before:
	if app.ENABLE_CHANGE_LOOK_SYSTEM:
		def __CanResetLookVnum(self, dstSlotPos):
			dstItemVNum = player.GetItemIndex(dstSlotPos)
			if dstItemVNum == 0:
				return False

			if player.GetItemLook(dstSlotPos):
				return True

			return False

## Search for:
	def UseItemSlot(self, slotIndex):

## Add under:
		if app.ENABLE_CHANGE_LOOK_SYSTEM:
			if constInfo.BusySlots():
				return
