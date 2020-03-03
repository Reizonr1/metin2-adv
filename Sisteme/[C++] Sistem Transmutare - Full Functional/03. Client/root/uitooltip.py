""""""
#1) Search:
	def SetInventoryItem(self, slotIndex, window_type = player.INVENTORY):
#2) Inside this func search:
		self.AddItemData(itemVnum, metinSlot, attrSlot)
#3) Replace with:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.INVENTORY, slotIndex)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)
""""""


""""""
#1) Search:
	def SetShopItem(self, slotIndex):
#2) Inside this func search:
		self.AddItemData(itemVnum, metinSlot, attrSlot)
#3) Replace with:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			transmutation = shop.GetItemTransmutation(slotIndex)
			if not transmutation:
				self.AddItemData(itemVnum, metinSlot, attrSlot)
			else:
				self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.INVENTORY, -1, transmutation)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)
""""""


""""""
#1) Search:
	def SetShopItemBySecondaryCoin(self, slotIndex):
#2) Inside this func search:
		self.AddItemData(itemVnum, metinSlot, attrSlot)
#3) Replace with:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			transmutation = shop.GetItemTransmutation(slotIndex)
			if not transmutation:
				self.AddItemData(itemVnum, metinSlot, attrSlot)
			else:
				self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.INVENTORY, -1, transmutation)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)
""""""


""""""
#1) Search:
	def SetExchangeOwnerItem(self, slotIndex):
#2) Inside this func search:
		self.AddItemData(itemVnum, metinSlot, attrSlot)
#3) Replace with:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			transmutation = exchange.GetItemTransmutation(slotIndex, True)
			if not transmutation:
				self.AddItemData(itemVnum, metinSlot, attrSlot)
			else:
				self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.INVENTORY, -1, transmutation)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)
""""""


""""""
#1) Search:
	def SetExchangeTargetItem(self, slotIndex):
#2) Inside this func search:
		self.AddItemData(itemVnum, metinSlot, attrSlot)
#3) Replace with:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			transmutation = exchange.GetItemTransmutation(slotIndex, False)
			if not transmutation:
				self.AddItemData(itemVnum, metinSlot, attrSlot)
			else:
				self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.INVENTORY, -1, transmutation)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)
""""""


""""""
#1) Search:
	def SetPrivateShopBuilderItem(self, invenType, invenPos, privateShopSlotIndex):
#2) Inside this func search:
		self.AddItemData(itemVnum, metinSlot, attrSlot, 0)
#3) Replace with:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, invenType, invenPos)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0)
""""""


""""""
#1) Search:
	def SetSafeBoxItem(self, slotIndex):
#2) Inside this func search:
			self.AddItemData(itemVnum, metinSlot, attrSlot, safebox.GetItemFlags(slotIndex))
#3) Replace with:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, safebox.GetItemFlags(slotIndex), player.SAFEBOX, slotIndex)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot, safebox.GetItemFlags(slotIndex))
""""""


""""""
#1) Search:
	def SetMallItem(self, slotIndex):
#2) Inside this func search:
		self.AddItemData(itemVnum, metinSlot, attrSlot)
#3) Replace with:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.MALL, slotIndex)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)
""""""


""""""
#1) Search:
	def AddItemData(self, itemVnum, metinSlot, attrSlot = 0, flags = 0, window_type = player.INVENTORY, slotIndex = -1):
#2) Replace with:
	def AddItemData(self, itemVnum, metinSlot, attrSlot = 0, flags = 0, window_type = player.INVENTORY, slotIndex = -1, transmutation = -1):
""""""


""""""
#1) Search:
		if item.ITEM_TYPE_WEAPON == itemType:
#2) Inside this statement search:
			self.__AppendAttributeInformation(attrSlot)
#3) After make a new line and paste:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				self.AppendTransmutation(window_type, slotIndex, transmutation)
""""""


""""""
#1) Search:
		elif item.ITEM_TYPE_ARMOR == itemType:
#2) Inside this statement search:
			self.__AppendAttributeInformation(attrSlot)
#3) After make a new line and paste:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				self.AppendTransmutation(window_type, slotIndex, transmutation)
""""""


""""""
#1) Search:
		elif 0 != isCostumeItem:
#2) Inside this statement search:
			self.AppendWearableInformation()
#3) Before make a new line and paste:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				self.AppendTransmutation(window_type, slotIndex, transmutation)
""""""


""""""
#1) Search:
class HyperlinkItemToolTip(ItemToolTip):
#2) Before make a new line and paste:
	if app.ENABLE_CHANGELOOK_SYSTEM:
		def AppendTransmutation(self, window_type, slotIndex, transmutation):
			itemVnum = 0
			if transmutation == -1:
				if window_type == player.INVENTORY:
					itemVnum = player.GetItemTransmutation(window_type, slotIndex)
				elif window_type == player.SAFEBOX:
					itemVnum = safebox.GetItemTransmutation(slotIndex)
				elif window_type == player.MALL:
					itemVnum = safebox.GetItemMallTransmutation(slotIndex)
			else:
				itemVnum = transmutation
			
			if not itemVnum:
				return
			
			item.SelectItem(itemVnum)
			itemName = item.GetItemName()
			if not itemName or itemName == "":
				return
			
			self.AppendSpace(5)
			title = "[ " + localeInfo.CHANGE_LOOK_TITLE + " ]"
			self.AppendTextLine(title, self.NORMAL_COLOR)
			textLine = self.AppendTextLine(itemName, self.CONDITION_COLOR, True)
			textLine.SetFeather()
""""""


""""""
#1) Search:
	def SetHyperlinkItem(self, tokens):
#2) Inside this func search:
		minTokenCount = 3 + player.METIN_SOCKET_MAX_NUM
#2) After make a new line and paste:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			minTokenCount += 1
""""""


""""""
#1) Search:
	def SetHyperlinkItem(self, tokens):
#2) Inside this func search:
			rests = tokens[6:]
#3) After make a new line and paste:
			transmutation = 0
			if app.ENABLE_CHANGELOOK_SYSTEM:
				rests = tokens[7:]
				cnv = [int(cnv, 16) for cnv in tokens[6:7]]
				transmutation = int(cnv[0])
""""""


""""""
#1) Search:
	def SetHyperlinkItem(self, tokens):
#2) Inside this func search:
			self.AddItemData(itemVnum, metinSlot, attrSlot)
#3) Replace with:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				if not transmutation:
					self.AddItemData(itemVnum, metinSlot, attrSlot)
				else:
					self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.INVENTORY, -1, transmutation)
			else:
				self.AddItemData(itemVnum, metinSlot, attrSlot)
""""""