Alttaki kodu arat ;

	def __init__(self, *args, **kwargs):
		ToolTip.__init__(self, *args, **kwargs)
		self.itemVnum = 0
		self.isShopItem = False

Yukar©¥daki kodun alt©¥na ekle ;

		self.isOfflineShopItem = False

Alttaki kodu arat ;

	def ClearToolTip(self):

Yukar©¥daki kod blo?unu tamamen alttaki ile de?i?tir ;

	def ClearToolTip(self):
		self.isShopItem = False
		self.isOfflineShopItem = False
		self.toolTipWidth = self.TOOL_TIP_WIDTH
		ToolTip.ClearToolTip(self)

Alttaki kodu arat ;

	def SetInventoryItem(self, slotIndex, window_type = player.INVENTORY):

Yukar©¥daki kod blo?unu tamamen alttaki ile de?i?tir ;

	def SetInventoryItem(self, slotIndex, window_type = player.INVENTORY):
		itemVnum = player.GetItemIndex(window_type, slotIndex)
		if 0 == itemVnum:
			return

		self.ClearToolTip()
		if shop.IsOpen():
			if not shop.IsPrivateShop() or not shop.IsOfflineShop():
				item.SelectItem(itemVnum)
				self.AppendSellingPrice(player.GetISellItemPrice(window_type, slotIndex))

		metinSlot = [player.GetItemMetinSocket(window_type, slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		attrSlot = [player.GetItemAttribute(window_type, slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

		self.AddItemData(itemVnum, metinSlot, attrSlot)

Alttaki kodu arat ;

	def SetInventoryItem(self, slotIndex, window_type = player.INVENTORY):
		itemVnum = player.GetItemIndex(window_type, slotIndex)
		if 0 == itemVnum:
			return

		self.ClearToolTip()
		if shop.IsOpen():
			if not shop.IsPrivateShop() or not shop.IsOfflineShop():
				item.SelectItem(itemVnum)
				self.AppendSellingPrice(player.GetISellItemPrice(window_type, slotIndex))

		metinSlot = [player.GetItemMetinSocket(window_type, slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		attrSlot = [player.GetItemAttribute(window_type, slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

		self.AddItemData(itemVnum, metinSlot, attrSlot)

Yukar©¥daki kodun alt©¥na ekle ;

	def SetOfflineShopBuilderItem(self, invenType, invenPos, offlineShopIndex):
		itemVnum = player.GetItemIndex(invenType, invenPos)
		if (itemVnum == 0):
			return

		item.SelectItem(itemVnum)
		self.ClearToolTip()
		self.AppendSellingPrice(shop.GetOfflineShopItemPrice2(invenType, invenPos))

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(invenPos, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(player.GetItemAttribute(invenPos, i))
		
		self.AddItemData(itemVnum, metinSlot, attrSlot)
		
	def SetOfflineShopItem(self, slotIndex):
		itemVnum = shop.GetOfflineShopItemID(slotIndex)
		if (itemVnum == 0):
			return
			
		price = shop.GetOfflineShopItemPrice(slotIndex)
		self.ClearToolTip()
		self.isOfflineShopItem = True
		
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(shop.GetOfflineShopItemMetinSocket(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(shop.GetOfflineShopItemAttribute(slotIndex, i))
			
		self.AddItemData(itemVnum, metinSlot, attrSlot)
		self.AppendPrice(price)