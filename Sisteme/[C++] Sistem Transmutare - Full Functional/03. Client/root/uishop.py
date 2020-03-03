""""""
#1) Search:
			setItemID(i, getItemID(idx), itemCount)
#2) After make a new line and paste:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				itemTransmutedVnum = shop.GetItemTransmutation(idx)
				if itemTransmutedVnum:
					self.itemSlotWindow.DisableCoverButton(i)
				else:
					self.itemSlotWindow.EnableCoverButton(i)
""""""