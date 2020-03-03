""""""
#1) Search:
ITEM_FLAG_APPLICABLE = 1 << 14
#2) Before make a new line and paste:
if app.ENABLE_CHANGELOOK_SYSTEM:
	import changelook
""""""


""""""
#1) Search:
	def RefreshCostumeSlot(self):
#2) Inside this func search:
			self.wndEquip.SetItemSlot(slotNumber, getItemVNum(slotNumber), 0)
#3) After make a new line and paste:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				itemTransmutedVnum = player.GetItemTransmutation(slotNumber)
				if itemTransmutedVnum:
					self.wndEquip.DisableCoverButton(slotNumber)
				else:
					self.wndEquip.EnableCoverButton(slotNumber)
""""""


""""""
#1) Search:
		self.SetInventoryPage(0)
#2) Before make a new line and paste:
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.listAttachedCl = []
""""""


""""""
#1) Search:
	def RefreshBagSlotWindow(self):
#2) Inside this func search:
setItemVNum(i, itemVnum, itemCount)
#3) After make a new line and paste:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				itemTransmutedVnum = player.GetItemTransmutation(slotNumber)
				if itemTransmutedVnum:
					self.wndItem.DisableCoverButton(i)
				else:
					self.wndItem.EnableCoverButton(i)
""""""


""""""
#1) Search:
	def RefreshBagSlotWindow(self):
#2) Inside this func search:
		self.wndItem.RefreshSlot()
		if self.wndBelt:
			self.wndBelt.RefreshSlot()
#3) Before make a new line and paste:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				slotClNumberChecked = 0
				if not constInfo.IS_AUTO_POTION(itemVnum):
					if app.ENABLE_HIGHLIGHT_SYSTEM:
						if not slotNumber in self.listHighlightedSlot:
							self.wndItem.DeactivateSlot(i)
					else:
						self.wndItem.DeactivateSlot(i)
				
				for q in xrange(changelook.WINDOW_MAX_MATERIALS):
					(isHere, iCell) = changelook.GetAttachedItem(q)
					if isHere:
						if iCell == slotNumber:
							self.wndItem.ActivateSlot(i, (238.00 / 255.0), (11.00 / 255.0), (11.00 / 255.0), 1.0)
							if not slotNumber in self.listAttachedCl:
								self.listAttachedCl.append(slotNumber)
							
							slotClNumberChecked = 1
					else:
						if slotNumber in self.listAttachedCl and not slotClNumberChecked:
							self.wndItem.DeactivateSlot(i)
							self.listAttachedCl.remove(slotNumber)
""""""


""""""
#1) Search:
	def RefreshEquipSlotWindow(self):
#2) Inside this func search:
			setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)
		
		if app.ENABLE_NEW_EQUIPMENT_SYSTEM:
#3) Replace with:
			setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)
			if app.ENABLE_CHANGELOOK_SYSTEM:
				itemTransmutedVnum = player.GetItemTransmutation(slotNumber)
				if itemTransmutedVnum:
					self.wndEquip.DisableCoverButton(slotNumber)
				else:
					self.wndEquip.EnableCoverButton(slotNumber)
		
		if app.ENABLE_NEW_EQUIPMENT_SYSTEM:
""""""


""""""
#1) Search:
	def RefreshEquipSlotWindow(self):
#2) Inside this func search:
				setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)
		
		self.wndEquip.RefreshSlot()
#3) Replace with:
				setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)
				if app.ENABLE_CHANGELOOK_SYSTEM:
					itemTransmutedVnum = player.GetItemTransmutation(slotNumber)
					if itemTransmutedVnum:
						self.wndEquip.DisableCoverButton(slotNumber)
					else:
						self.wndEquip.EnableCoverButton(slotNumber)
		
		self.wndEquip.RefreshSlot()
""""""


""""""
#1) Search:
	def DetachMetinFromItem(self, scrollSlotPos, targetSlotPos):
		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)
		if not player.CanDetach(scrollIndex, targetSlotPos):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_METIN_INSEPARABLE_ITEM)
			return
		
		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.SetText(localeInfo.REFINE_DO_YOU_SEPARATE_METIN)
		self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnDetachMetinFromItem))
		self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		self.questionDialog.Open()
		self.questionDialog.sourcePos = scrollSlotPos
		self.questionDialog.targetPos = targetSlotPos
#2) Replace with:
	def DetachMetinFromItem(self, scrollSlotPos, targetSlotPos):
		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)
		if app.ENABLE_CHANGELOOK_SYSTEM:
			if not player.CanDetach(scrollIndex, targetSlotPos):
				item.SelectItem(scrollIndex)
				if item.GetValue(0) == changelook.CLEAN_ATTR_VALUE0:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHANGE_LOOK_FAILURE_CLEAN)
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_METIN_INSEPARABLE_ITEM)
				
				return
		else:
			if not player.CanDetach(scrollIndex, targetSlotPos):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_METIN_INSEPARABLE_ITEM)
				return
		
		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.SetText(localeInfo.REFINE_DO_YOU_SEPARATE_METIN)
		if app.ENABLE_CHANGELOOK_SYSTEM:
			item.SelectItem(targetIndex)
			if item.GetItemType() == item.ITEM_TYPE_WEAPON or item.GetItemType() == item.ITEM_TYPE_ARMOR or item.GetItemType() == item.ITEM_TYPE_COSTUME:
				item.SelectItem(scrollIndex)
				if item.GetValue(0) == changelook.CLEAN_ATTR_VALUE0:
					self.questionDialog.SetText(localeInfo.CHANGE_LOOK_DO_YOU_CLEAN)
		
		self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnDetachMetinFromItem))
		self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		self.questionDialog.Open()
		self.questionDialog.sourcePos = scrollSlotPos
		self.questionDialog.targetPos = targetSlotPos
""""""


""""""
#1) Search (DO THIS STEP JUST IF YOU GOT MY HIGHLIGHT SYSTEM):
	def OverInItem(self, overSlotPos):
		if app.ENABLE_HIGHLIGHT_SYSTEM:
			stat = 0
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(overSlotPos)
			itemVnum = player.GetItemIndex(slotNumber)
			if constInfo.IS_AUTO_POTION(itemVnum):
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
				if slotNumber >= player.INVENTORY_PAGE_SIZE:
					slotNumber -= player.INVENTORY_PAGE_SIZE
				
				isActivated = 0 != metinSocket[0]
				if isActivated:
					stat = 1
			
			if not stat:
				if slotNumber in self.listHighlightedSlot:
					self.wndItem.DeactivateSlot(overSlotPos)
					try:
							self.listHighlightedSlot.remove(slotNumber)
					except:
						pass
#2) Replace with:
	def OverInItem(self, overSlotPos):
		if app.ENABLE_HIGHLIGHT_SYSTEM:
			stat = 0
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(overSlotPos)
			itemVnum = player.GetItemIndex(slotNumber)
			if constInfo.IS_AUTO_POTION(itemVnum):
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
				if slotNumber >= player.INVENTORY_PAGE_SIZE:
					slotNumber -= player.INVENTORY_PAGE_SIZE
				
				isActivated = 0 != metinSocket[0]
				if isActivated:
					stat = 1
			
			if not stat:
				if slotNumber in self.listHighlightedSlot:
					self.wndItem.DeactivateSlot(overSlotPos)
					try:
						if app.ENABLE_CHANGELOOK_SYSTEM:
							if not slotNumber in self.listAttachedCl:
								self.listHighlightedSlot.remove(slotNumber)
						else:
							self.listHighlightedSlot.remove(slotNumber)
					except:
						pass
""""""


""""""
#1) Search:
	def UseItemSlot(self, slotIndex):
		if constInfo.GET_ITEM_DROP_QUESTION_DIALOG_STATUS():
			return
		
		slotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(slotIndex)
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			if self.wndDragonSoulRefine.IsShow():
				self.wndDragonSoulRefine.AutoSetItem((player.INVENTORY, slotIndex), 1)
				return
		
		self.__UseItem(slotIndex)
		mouseModule.mouseController.DeattachObject()
		self.OverOutItem()
#2) Replace with:
	def UseItemSlot(self, slotIndex):
		if constInfo.GET_ITEM_DROP_QUESTION_DIALOG_STATUS():
			return
		
		slotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(slotIndex)
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			if self.wndDragonSoulRefine.IsShow():
				self.wndDragonSoulRefine.AutoSetItem((player.INVENTORY, slotIndex), 1)
				return
		
		if app.ENABLE_CHANGELOOK_SYSTEM:
			if self.isShowChangeLookWindow():
				changelook.Add(player.INVENTORY, slotIndex, 255)
				return
		
		self.__UseItem(slotIndex)
		mouseModule.mouseController.DeattachObject()
		self.OverOutItem()
""""""


""""""
#1) Search:
	def SetDragonSoulRefineWindow(self, wndDragonSoulRefine):
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoulRefine = wndDragonSoulRefine
#2) After make a new line and paste:
	if app.ENABLE_CHANGELOOK_SYSTEM:
		def SetChangeLookWindow(self, wndChangeLook):
			self.wndChangeLook = wndChangeLook

		def isShowChangeLookWindow(self):
			if self.wndChangeLook:
				if self.wndChangeLook.IsShow():
					return 1
			
			return 0
""""""