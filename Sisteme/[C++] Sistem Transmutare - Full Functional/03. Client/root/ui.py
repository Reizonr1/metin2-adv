""""""
#1) Search:
		def ActivateSlot(self, slotNumber):
			wndMgr.ActivateSlot(self.hWnd, slotNumber)

		def DeactivateSlot(self, slotNumber):
			wndMgr.DeactivateSlot(self.hWnd, slotNumber)
#2) Replace with:
	if app.ENABLE_CHANGELOOK_SYSTEM:
		def ActivateSlot(self, slotNumber, r = 1.0, g = 1.0, b = 1.0, a = 1.0):
			wndMgr.ActivateEffect(self.hWnd, slotNumber, r, g, b, a)

		def DeactivateSlot(self, slotNumber):
			wndMgr.DeactivateEffect(self.hWnd, slotNumber)

		def ActivateSlotOld(self, slotNumber):
			wndMgr.ActivateSlot(self.hWnd, slotNumber)

		def DeactivateSlotOld(self, slotNumber):
			wndMgr.DeactivateSlot(self.hWnd, slotNumber)
	else:
		def ActivateSlot(self, slotNumber):
			wndMgr.ActivateSlot(self.hWnd, slotNumber)

		def DeactivateSlot(self, slotNumber):
			wndMgr.DeactivateSlot(self.hWnd, slotNumber)
""""""


""""""
#1) Search:
		wndMgr.SetSlotID(self.hWnd, renderingSlotNumber, id)
#2) After make a new line and paste:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			wndMgr.SetCoverButton(self.hWnd, renderingSlotNumber, "d:/ymir work/ui/game/quest/slot_button_00.sub", "d:/ymir work/ui/game/quest/slot_button_00.sub", "d:/ymir work/ui/game/quest/slot_button_00.sub", "icon/item/ingame_convert_mark.tga", False, False)
""""""