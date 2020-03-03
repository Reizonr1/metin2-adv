""""""
#1) Search:
			setitemVNum(i, getitemVNum(*pos), itemCount)
#2) After make a new line and paste:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				itemTransmutedVnum = player.GetItemTransmutation(*pos)
				if itemTransmutedVnum:
					self.itemSlot.DisableCoverButton(i)
				else:
					self.itemSlot.EnableCoverButton(i)
""""""