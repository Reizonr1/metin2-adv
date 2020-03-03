""""""
#1) Search:
			self.OwnerSlot.SetItemSlot(i, itemIndex, itemCount)
#2) After make a new line and paste:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				itemTransmutedVnum = exchange.GetItemTransmutation(i, True)
				if itemTransmutedVnum:
					self.OwnerSlot.DisableCoverButton(i)
				else:
					self.OwnerSlot.EnableCoverButton(i)
""""""


""""""
#1) Search:
			self.TargetSlot.SetItemSlot(i, itemIndex, itemCount)
#2) After make a new line and paste:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				itemTransmutedVnum = exchange.GetItemTransmutation(i, False)
				if itemTransmutedVnum:
					self.TargetSlot.DisableCoverButton(i)
				else:
					self.TargetSlot.EnableCoverButton(i)
""""""