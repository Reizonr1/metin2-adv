## Search for:
	SPECIAL_POSITIVE_COLOR2 = grp.GenerateColor(0.8824, 0.9804, 0.8824, 1.0)

## Add under:
	if app.ENABLE_CHANGE_LOOK_SYSTEM:
		CHANGELOOK_TITLE_COLOR = 0xff8BBDFF
		CHANGELOOK_ITEMNAME_COLOR = 0xffBCE55C

## Search for on def SetInventoryItem:
			self.AddItemData(itemVnum, metinSlot, attrSlot)

## Replace their function with this:
		if app.ENABLE_CHANGE_LOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, 0, player.INVENTORY, slotIndex)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)

## Search for on def SetShopItem:
			self.AddItemData(itemVnum, metinSlot, attrSlot)

## Replace their function with this:
		if app.ENABLE_CHANGE_LOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, 0, player.SHOP, slotIndex)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)

## Search for on def SetExchangeOwnerItem: <- Different
			self.AddItemData(itemVnum, metinSlot, attrSlot)

## Replace their function with this:
		if app.ENABLE_CHANGE_LOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, 0, player.TRADE_OWNER, slotIndex)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)

## Search for on def SetExchangeTargetItem: <- Different
			self.AddItemData(itemVnum, metinSlot, attrSlot)

## Replace their function with this:
		if app.ENABLE_CHANGE_LOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, 0, player.TRADE_TARGET, slotIndex)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)

## Search for on def SetPrivateShopBuilderItem:
			self.AddItemData(itemVnum, metinSlot, attrSlot)

## Replace their function with this:
		if app.ENABLE_CHANGE_LOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, 0, invenType, invenPos)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)

## Search for on def SetSafeBoxItem:
			self.AddItemData(itemVnum, metinSlot, attrSlot)

## Replace their function with this:
		if app.ENABLE_CHANGE_LOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, safebox.GetItemFlags(slotIndex), 0, player.SAFEBOX, slotIndex)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)

## Search for:
	def __AppendAttackSpeedInfo(self, item):

## Add before:
	if app.ENABLE_CHANGE_LOOK_SYSTEM:
		def SetChangeLookWindowItem(self, slotIndex):
			itemVnum = player.GetItemIndex(slotIndex)
			if 0 == itemVnum:
				return

			self.ClearToolTip()

			metinSlot = []
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				metinSlot.append(player.GetItemMetinSocket(slotIndex, i))

			attrSlot = []
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				attrSlot.append(player.GetItemAttribute(slotIndex, i))

			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, 0, player.INVENTORY, slotIndex)

		def AppendChangeLookInformation(self, window_type, slotIndex):
			table = {
				player.SAFEBOX : safebox.GetItemLook,
				# player.MALL : safebox.GetMallItemLook,
				player.INVENTORY : player.GetItemLook,
				player.TRADE_OWNER : exchange.GetItemLookVnumFromSelf,
				player.TRADE_TARGET : exchange.GetItemLookVnumFromTarget,
				player.SHOP : shop.GetItemLookVnum,
				player.GLASS : slotIndex,
			}

			if window_type in table:
				if window_type == player.GLASS:
					GetItemChangeLookVnum = table[window_type]
				else:
					GetItemChangeLookVnum = table[window_type](slotIndex)

				if GetItemChangeLookVnum > 0:
					self.AppendSpace(5)
					self.AppendTextLine("[ %s ]" % localeInfo.CHANGE_LOOK_TITLE , self.CHANGELOOK_TITLE_COLOR)

					item.SelectItem(GetItemChangeLookVnum)
					self.AppendTextLine("%s" % str(item.GetItemName()), self.CHANGELOOK_ITEMNAME_COLOR)

## Search for:
## If you don't have the same just search for def AddItemData and replace the line.
	def AddItemData(self, itemVnum, metinSlot, attrSlot = 0, flags = 0, unbindTime = 0):

## Replace their function with this:
	def AddItemData(self, itemVnum, metinSlot, attrSlot = 0, flags = 0, unbindTime = 0, window_type = player.INVENTORY, slotIndex = -1): ## ENABLE_CHANGE_LOOK_SYSTEM

## Search for:
				self.AppendWearableInformation()
				self.__AppendMetinSlotInfo(metinSlot)

		### Armor ###

## Add before self.AppendWearableInformation() this:
				if app.ENABLE_CHANGE_LOOK_SYSTEM:
					self.AppendChangeLookInformation(window_type, slotIndex)

## Search for:
			self.AppendWearableInformation()

			if itemSubType in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):
				self.__AppendAccessoryMetinSlotInfo(metinSlot, constInfo.GET_ACCESSORY_MATERIAL_VNUM(itemVnum, itemSubType))
			else:
				self.__AppendMetinSlotInfo(metinSlot)

## Add before self.AppendWearableInformation() this:
			if app.ENABLE_CHANGE_LOOK_SYSTEM and itemSubType == item.ARMOR_BODY:
				self.AppendChangeLookInformation(window_type, slotIndex)

## Search for:
			itemVnum = int(vnum, 16)

## Replace it with this:
			if app.ENABLE_CHANGE_LOOK_SYSTEM:
				itemVnum = str(vnum)
			else:
				itemVnum = int(vnum, 16)

## Search for:
			rests = tokens[6:]

## Add before:
			if app.ENABLE_CHANGE_LOOK_SYSTEM:
				abc = itemVnum.split("|")
				itemVnum = int(abc[0], 16)
				lookvnum = int(abc[1])

## Search for on class HyperlinkItemToolTip:
			self.AddItemData(itemVnum, metinSlot, attrSlot)

## Replace their function with this:
			if app.ENABLE_CHANGE_LOOK_SYSTEM:
				self.AddItemData(itemVnum, metinSlot, attrSlot, 0, 0, player.GLASS, lookvnum)
			else:
				self.AddItemData(itemVnum, metinSlot, attrSlot)
