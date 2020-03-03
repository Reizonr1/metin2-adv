## Search for:
	def IsActivateSlot(self, slotNumber):
		return wndMgr.IsActivateSlot(self.hWnd, slotNumber)

## Add under:
	if app.ENABLE_CHANGE_LOOK_SYSTEM:
		def EnableSlotCoverImage(self, slotNumber):
			wndMgr.EnableSlotCoverImage(self.hWnd, slotNumber)

		def DisableSlotCoverImage(self, slotNumber):
			wndMgr.DisableSlotCoverImage(self.hWnd, slotNumber)

## Search for:
		def ActivateSlot(self, slotNumber):
			wndMgr.ActivateSlot(self.hWnd, slotNumber)

		def DeactivateSlot(self, slotNumber):
			wndMgr.DeactivateSlot(self.hWnd, slotNumber)

## Add under:			
	if app.ENABLE_CHANGE_LOOK_SYSTEM:
		def ActivateChangeLookSlot(self, slotNumber):
			wndMgr.ActivateChangeLookSlot(self.hWnd, slotNumber)

		def DeactivateChangeLookSlot(self, slotNumber):
			wndMgr.DeactivateChangeLookSlot(self.hWnd, slotNumber)
