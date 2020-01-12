""""""
#1) Search: def SetInventoryItem(self, slotIndex, window_type = player.INVENTORY):
#2) After their definition make a new line and paste:
	if app.ENABLE_ATTR_TRANSFER_SYSTEM:
		def SetInventoryItemAttrTransfer(self, slotIndex_1, slotIndex_2, window_type = player.INVENTORY):
			itemVnum = player.GetItemIndex(window_type, slotIndex_1)
			itemVnum_2 = player.GetItemIndex(window_type, slotIndex_2)
			if itemVnum == 0 or itemVnum_2 == 0:
				return
			
			self.ClearToolTip()
			if shop.IsOpen():
				if not shop.IsPrivateShop():
					item.SelectItem(itemVnum)
					self.AppendSellingPrice(player.GetISellItemPrice(window_type, slotIndex_2))
			
			metinSlot = [player.GetItemMetinSocket(window_type, slotIndex_2, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			attrSlot = [player.GetItemAttribute(window_type, slotIndex_2, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
			self.AddItemDataAttrTransfer(itemVnum, itemVnum_2, metinSlot, attrSlot, 0, 0, window_type, slotIndex_2)

		def AddItemDataAttrTransfer(self, itemVnum, itemVnum_2, metinSlot, attrSlot = 0, flags = 0, unbindTime = 0, window_type = player.INVENTORY, slotIndex = -1):
			self.itemVnum = itemVnum
			item.SelectItem(itemVnum)
			itemType = item.GetItemType()
			itemSubType = item.GetItemSubType()
			itemDesc = item.GetItemDescription()
			itemSummary = item.GetItemSummary()
			
			self.__AdjustMaxWidth(attrSlot, itemDesc)
			self.__SetItemTitle(itemVnum, metinSlot, attrSlot)
			self.AppendDescription(itemDesc, 26)
			self.AppendDescription(itemSummary, 26, self.CONDITION_COLOR)
			self.__AppendLimitInformation()
			self.__AppendAffectInformation()
			
			item.SelectItem(itemVnum_2)
			self.__AppendAttributeInformation(attrSlot)
			
			item.SelectItem(itemVnum)
			self.AppendWearableInformation()
			bHasRealtimeFlag = 0
			for i in xrange(item.LIMIT_MAX_NUM):
				(limitType, limitValue) = item.GetLimit(i)
				if item.LIMIT_REAL_TIME == limitType:
					bHasRealtimeFlag = 1
			
			if 1 == bHasRealtimeFlag:
				self.AppendMallItemLastTime(metinSlot[0])
			
			self.ShowToolTip()
""""""