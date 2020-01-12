## 1. In function:
	def __UseItem(self, slotIndex):
## 1. Before:
		else:
			self.__SendUseItemPacket(slotIndex)
## 1. Add:
		elif app.ENABLE_SHOW_CHEST_DROP:
			if player.GetItemTypeBySlot(slotIndex) == item.ITEM_TYPE_GIFTBOX:
				if self.interface:
					if self.interface.dlgChestDrop:
						if not self.interface.dlgChestDrop.IsShow():
							self.interface.dlgChestDrop.Open(slotIndex)
							if not constInfo.CHEST_DROP_INFO_DATA.has_key(ItemVNum):
								net.SendChestDropInfo(slotIndex)