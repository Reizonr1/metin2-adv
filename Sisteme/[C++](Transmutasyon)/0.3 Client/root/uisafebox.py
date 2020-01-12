## Search for:
			setItemID(i, getItemID(slotIndex), itemCount)

## Add under:
			if app.ENABLE_CHANGE_LOOK_SYSTEM:
				if safebox.GetItemLook(i):
					self.wndItem.EnableSlotCoverImage(i)
