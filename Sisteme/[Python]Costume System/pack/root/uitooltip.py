def SetInventoryItem(self, slotIndex):
		COSTUME_START_INDEX = 109
		if slotIndex == COSTUME_START_INDEX + 0:
			itemVnum = int(constInfo.COSTUME_ARMOR)
		elif slotIndex == COSTUME_START_INDEX + 1:
			itemVnum = int(constInfo.COSTUME_HAIR)
		else:
			itemVnum = player.GetItemIndex(slotIndex)
	
		if 0 == itemVnum:
			return

		self.ClearToolTip()
		if shop.IsOpen():
			if not shop.IsPrivateShop():
				item.SelectItem(itemVnum)
				self.AppendSellingPrice(player.GetISellItemPrice(slotIndex))

		metinSlot = [player.GetItemMetinSocket(slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		attrSlot = [player.GetItemAttribute(slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

		#print itemVnum, metinSlot, attrSlot
		self.AddItemData(itemVnum, metinSlot, attrSlot)