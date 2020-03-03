## Search for:
			self.OwnerSlot.SetItemSlot(i, itemIndex, itemCount)

## Add under:
			if app.ENABLE_CHANGE_LOOK_SYSTEM:
				if exchange.GetItemLookVnumFromSelf(i):
					self.OwnerSlot.EnableSlotCoverImage(i)

## Search for:
			self.TargetSlot.SetItemSlot(i, itemIndex, itemCount)

## Add under:
			if app.ENABLE_CHANGE_LOOK_SYSTEM:
				if exchange.GetItemLookVnumFromTarget(i):
					self.TargetSlot.EnableSlotCoverImage(i)
