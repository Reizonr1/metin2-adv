Search:
				self.AppendSellingPrice(player.GetISellItemPrice(window_type, slotIndex))

Change:
				if app.ENABLE_OFFLINE_SHOP:
					self.AppendSellingPrice(player.GetISellItemPrice(window_type, slotIndex), 0, 0, 0)
				else:
					self.AppendSellingPrice(player.GetISellItemPrice(window_type, slotIndex))

https://puu.sh/sgSd8/0363a4f739.png

---

Search:
	def SetShopItem(self, slotIndex):
		itemVnum = shop.GetItemID(slotIndex)
		if 0 == itemVnum:
			return

		price = shop.GetItemPrice(slotIndex)
		self.ClearToolTip()
		self.isShopItem = True

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(shop.GetItemMetinSocket(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(shop.GetItemAttribute(slotIndex, i))

		self.AddItemData(itemVnum, metinSlot, attrSlot)
		self.AppendPrice(price)

Change:
	if app.ENABLE_OFFLINE_SHOP:
		def SetShopItem(self, IsPc, slotIndex):
			itemVnum = shop.GetItemID(slotIndex)
			if 0 == itemVnum:
				return
	
			price = shop.GetItemPrice(slotIndex)
			if IsPc:
				price2 = shop.GetItemPrice2(slotIndex)
				price3 = shop.GetItemPrice3(slotIndex)
				price4 = shop.GetItemPrice4(slotIndex)
			else:
				price2 = 0
				price3 = 0
				price4 = 0
	
			self.ClearToolTip()
			self.isShopItem = True
	
			metinSlot = []
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				metinSlot.append(shop.GetItemMetinSocket(slotIndex, i))
			attrSlot = []
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				attrSlot.append(shop.GetItemAttribute(slotIndex, i))
	
			self.AddItemData(itemVnum, metinSlot, attrSlot)
			self.AppendPrice(IsPc, price, price2, price3, price4)
	else:
		def SetShopItem(self, slotIndex):
			itemVnum = shop.GetItemID(slotIndex)
			if 0 == itemVnum:
				return
	
			price = shop.GetItemPrice(slotIndex)
			self.ClearToolTip()
			self.isShopItem = True
	
			metinSlot = []
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				metinSlot.append(shop.GetItemMetinSocket(slotIndex, i))
			attrSlot = []
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				attrSlot.append(shop.GetItemAttribute(slotIndex, i))
	
			self.AddItemData(itemVnum, metinSlot, attrSlot)
			self.AppendPrice(price)

https://puu.sh/sgSfh/d8199c40ec.png

--

Search:
		self.AppendSellingPrice(shop.GetPrivateShopItemPrice(invenType, invenPos))

Change:
		if app.ENABLE_OFFLINE_SHOP:
			self.AppendSellingPrice(shop.GetPrivateShopItemPrice(invenType, invenPos), shop.GetPrivateShopItemPrice2(invenType, invenPos), shop.GetPrivateShopItemPrice3(invenType, invenPos), shop.GetPrivateShopItemPrice4(invenType, invenPos))
		else:
			self.AppendSellingPrice(shop.GetPrivateShopItemPrice(invenType, invenPos))

https://puu.sh/sgShm/be4e54dd32.png

---

Search:
	def AppendPrice(self, price):
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))

Change:
	if app.ENABLE_OFFLINE_SHOP:
		def AppendPrice(self, IsPc, price, price2, price3, price4):
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))
			if IsPc:
				if price2:
					self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToPriceString(price2, "Coin")), self.GetPriceColor(price))
					self.AppendSpace(1)
				if price3:
					self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToPriceString(price3, "Goldbar")), self.GetPriceColor(price))
					self.AppendSpace(1)
				if price4:
					self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToPriceString(price4, "Won")), self.GetPriceColor(price))
					self.AppendSpace(1)
	else:
		def AppendPrice(self, price):
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))

https://puu.sh/sgSjO/92e8569a32.png

---

Search:
	def AppendSellingPrice(self, price):
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
			self.AppendTextLine(localeInfo.TOOLTIP_ANTI_SELL, self.DISABLE_COLOR)
			self.AppendSpace(5)
		else:
			self.AppendTextLine(localeInfo.TOOLTIP_SELLPRICE % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))
			self.AppendSpace(5)

Change:
	if app.ENABLE_OFFLINE_SHOP:
		def AppendSellingPrice(self, price, price2, price3, price4):
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
				self.AppendTextLine(localeInfo.TOOLTIP_ANTI_SELL, self.DISABLE_COLOR)
				self.AppendSpace(5)
			else:
				if price:
					self.AppendTextLine(localeInfo.TOOLTIP_SELLPRICE % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))
					self.AppendSpace(1)
				if price2:
					self.AppendTextLine(localeInfo.TOOLTIP_SELLPRICE % (localeInfo.NumberToPriceString(price2, "Coin")), self.GetPriceColor(price))
					self.AppendSpace(1)
				if price3:
					self.AppendTextLine(localeInfo.TOOLTIP_SELLPRICE % (localeInfo.NumberToPriceString(price3, "Goldbar")), self.GetPriceColor(price))
					self.AppendSpace(1)
				if price4:
					self.AppendTextLine(localeInfo.TOOLTIP_SELLPRICE % (localeInfo.NumberToPriceString(price4, "Won")), self.GetPriceColor(price))
					self.AppendSpace(1)
				self.AppendSpace(4)
	else:
		def AppendSellingPrice(self, price):
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
				self.AppendTextLine(localeInfo.TOOLTIP_ANTI_SELL, self.DISABLE_COLOR)
				self.AppendSpace(5)
			else:
				self.AppendTextLine(localeInfo.TOOLTIP_SELLPRICE % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))
				self.AppendSpace(5)


https://puu.sh/sgT1S/0f6e5e8e3d.png

---






