""""""
#1) Search: def RefreshBagSlotWindow(self):
#2) Delete their function and paste:
	def RefreshBagSlotWindow(self):
		is_activated = 0
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVNum=self.wndItem.SetItemSlot
		for i in xrange(player.INVENTORY_PAGE_SIZE*2):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)
			itemCount = getItemCount(slotNumber)
			if 0 == itemCount:
				self.wndItem.ClearSlot(i)
				continue
			elif 1 == itemCount:
				itemCount = 0
			
			itemVnum = getItemVNum(slotNumber)
			setItemVNum(i, itemVnum, itemCount)
			if constInfo.IS_AUTO_POTION(itemVnum):
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
				if slotNumber >= player.INVENTORY_PAGE_SIZE:
					slotNumber -= player.INVENTORY_PAGE_SIZE
				
				isActivated = 0 != metinSocket[0]
				if isActivated:
					self.wndItem.ActivateSlot(i)
					potionType = 0;
					if constInfo.IS_AUTO_POTION_HP(itemVnum):
						potionType = player.AUTO_POTION_TYPE_HP
					elif constInfo.IS_AUTO_POTION_SP(itemVnum):
						potionType = player.AUTO_POTION_TYPE_SP						
					
					usedAmount = int(metinSocket[1])
					totalAmount = int(metinSocket[2])					
					player.SetAutoPotionInfo(potionType, isActivated, (totalAmount - usedAmount), totalAmount, self.__InventoryLocalSlotPosToGlobalSlotPos(i))
				else:
					self.wndItem.DeactivateSlot(i)
			elif constInfo.IS_ACCE_ITEM(itemVnum, 1) == TRUE:
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
				isActivated = metinSocket[0]
				if isActivated == 1:
					player.SetAcceInfo(isActivated, i)
					self.wndItem.ActivateAcceSlot(i)
				else:
					self.wndItem.DeactivateAcceSlot(i)
		
		self.wndItem.RefreshSlot()
		if self.wndBelt:
			self.wndBelt.RefreshSlot()
""""""

""""""
#1) Search: def DetachMetinFromItem(self, scrollSlotPos, targetSlotPos):
#2) Delete their function and paste:
	def DetachMetinFromItem(self, scrollSlotPos, targetSlotPos):
		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)
		if constInfo.IS_ACCE_ITEM_DETACH(scrollIndex) == TRUE:
			item.SelectItem(targetIndex)
			if item.GetItemSubType() == item.COSTUME_TYPE_ACCE:
				if self.GetAcceAttribute(targetSlotPos) == 0:
					return
				
				self.questionDialog = uiCommon.QuestionDialog()
				self.questionDialog.SetText(localeInfo.ACCE_DO_YOU_REMOVE_ATTR)
				self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnDetachMetinFromItem))
				self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
				self.questionDialog.Open()
				self.questionDialog.sourcePos = scrollSlotPos
				self.questionDialog.targetPos = targetSlotPos
			else:
				return
		else:
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
""""""

""""""
#1) Search: def OnMoveWindow(self, x, y):
#2) After their functiobn make a new line and paste:
	def GetAcceAttribute(self, srcSlotPos):
		result = 0
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(player.GetItemAttribute(srcSlotPos, i))
			
		if 0 != attrSlot:
			for c in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				type = attrSlot[c][0]
				if type != 0:
					result = result + 1
		
		return result
""""""