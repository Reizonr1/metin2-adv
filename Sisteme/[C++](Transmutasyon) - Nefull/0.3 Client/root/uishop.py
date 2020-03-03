## Search for:
			setItemID(i, getItemID(i), itemCount)

## Add under:
			if app.ENABLE_CHANGE_LOOK_SYSTEM:
				if shop.GetItemLookVnum(i):
					self.itemSlotWindow.EnableSlotCoverImage(i)
