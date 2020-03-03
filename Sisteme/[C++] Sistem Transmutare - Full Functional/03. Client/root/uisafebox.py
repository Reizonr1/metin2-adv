""""""
#1) Search:
	def RefreshSafebox(self):
#2) Inside this func search:
			setItemID(i, getItemID(slotIndex), itemCount)
#3) After make a new line and paste:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				itemTransmutedVnum = safebox.GetItemTransmutation(slotIndex)
				if itemTransmutedVnum:
					self.wndItem.DisableCoverButton(i)
				else:
					self.wndItem.EnableCoverButton(i)
""""""


""""""
#1) Search:
	def RefreshMall(self):
#2) Inside this func search:
			setItemID(i, itemID, itemCount)
#3) After make a new line and paste:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				itemTransmutedVnum = safebox.GetMallItemTransmutation(i)
				if itemTransmutedVnum:
					self.wndItem.DisableCoverButton(i)
				else:
					self.wndItem.EnableCoverButton(i)
""""""