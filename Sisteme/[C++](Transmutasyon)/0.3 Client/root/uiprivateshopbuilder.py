## Search for:
			setitemVNum(i, getitemVNum(*pos), itemCount)

## Add under:
			if app.ENABLE_CHANGE_LOOK_SYSTEM:
				if player.GetItemLook(*pos):
					self.itemSlot.EnableSlotCoverImage(i)
