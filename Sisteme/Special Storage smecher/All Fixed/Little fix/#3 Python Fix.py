
This class full fix 

/BURHANBEY - DRACARYS\

uiinventory.py aç cauta

	class ExtendedInventoryWindow(ui.ScriptWindow):

schimba complet classı

if app.WJ_SPLIT_INVENTORY_SYSTEM:
	class ExtendedInventoryWindow(ui.ScriptWindow):
		tooltipItem = None
		interface = None
		dlgPickMoney = None
		dlgPickItem = None
		sellingSlotNumber = -1
		isLoaded = 0
		
		def __init__(self):
			ui.ScriptWindow.__init__(self)
			self.inventoryPageIndex = 0
			self.__LoadWindow()
			
		def __del__(self):
			ui.ScriptWindow.__del__(self)

		def Show(self):
			self.__LoadWindow()
			ui.ScriptWindow.Show(self)	
			
		def BindInterfaceClass(self, interface):
			self.interface = interface

		def __LoadWindow(self):
			if self.isLoaded == 1:
				return

			self.isLoaded = 1
			
			try:
				pyScrLoader = ui.PythonScriptLoader()
				pyScrLoader.LoadScriptFile(self, "UIScript/ExtendedInventoryWindow.py")
			except:
				import exception
				exception.Abort("ExtendedInventoryWindow.LoadWindow.LoadObject")	

			try:
				wndItem = self.GetChild("ItemSlot")
				self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
				self.titleName = self.GetChild("TitleName")
				self.SkillBookButton = self.GetChild("SkillBookButton")
				self.UpgradeItemsButton = self.GetChild("UpgradeItemsButton")
				self.stoneButton = self.GetChild("StoneButton")
				self.sandikButton = self.GetChild("SandikButton")
				self.inventoryTab = []
				self.inventoryTab.append(self.GetChild("Inventory_Tab_01"))
				self.inventoryTab.append(self.GetChild("Inventory_Tab_02"))
				self.inventoryTab.append(self.GetChild("Inventory_Tab_03"))	
			except:
				import exception
				exception.Abort("ExtendedInventoryWindow.LoadWindow.BindObject")

			## Item
			wndItem.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
			wndItem.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
			wndItem.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
			wndItem.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
			wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))	
			
			self.SkillBookButton.SetEvent(lambda arg=0: self.SetInventoryType(arg))
			self.UpgradeItemsButton.SetEvent(lambda arg=1: self.SetInventoryType(arg))
			self.stoneButton.SetEvent(lambda arg=2: self.SetInventoryType(arg))
			self.sandikButton.SetEvent(lambda arg=3: self.SetInventoryType(arg))
			self.SkillBookButton.Down()

			self.inventoryTab[0].SetEvent(lambda arg=0: self.SetInventoryPage(arg))
			self.inventoryTab[1].SetEvent(lambda arg=1: self.SetInventoryPage(arg))
			self.inventoryTab[2].SetEvent(lambda arg=2: self.SetInventoryPage(arg))
			self.inventoryTab[0].Down()
			
			## PickMoneyDialog
			dlgPickMoney = uiPickMoney.PickMoneyDialog2()
			dlgPickMoney.LoadDialog()
			dlgPickMoney.Hide()
			
			self.dlgPickMoney = dlgPickMoney

			self.wndItem = wndItem
			self.SetInventoryType(0)
			self.SetInventoryPage(0)
			
		def Destroy(self):
			self.ClearDictionary()
			self.dlgPickMoney.Destroy()
			self.dlgPickMoney = 0
			self.tooltipItem = None
			self.wndItem = 0
			self.interface = None
			self.inventoryTab = []
			
		def Hide(self):
			if None != self.tooltipItem:
				self.tooltipItem.HideToolTip()
			wndMgr.Hide(self.hWnd)
			
		def Close(self):
			self.Hide()


		def SetInventoryType(self, type):
			self.inventoryType = type
			if type == 0:
				self.SkillBookButton.Down()
				self.UpgradeItemsButton.SetUp()
				self.stoneButton.SetUp()
				self.sandikButton.SetUp()
				self.titleName.SetText(localeInfo.INVENTORY_SKILL_BOOK_TOOLTIP)
			elif type == 2:
				self.stoneButton.Down()
				self.sandikButton.SetUp()
				self.UpgradeItemsButton.SetUp()
				self.SkillBookButton.SetUp()
				self.titleName.SetText(localeInfo.INVENTORY_STONE_TOOLTIP)
			elif type == 3:
				self.sandikButton.Down()
				self.stoneButton.SetUp()
				self.UpgradeItemsButton.SetUp()
				self.SkillBookButton.SetUp()
				self.titleName.SetText(localeInfo.INVENTORY_SANDIK_TOOLTIP)
			else:
				self.UpgradeItemsButton.Down()
				self.SkillBookButton.SetUp()
				self.stoneButton.SetUp()
				self.sandikButton.SetUp()
				self.titleName.SetText(localeInfo.INVENTORY_UPGRADE_ITEM_TOOLTIP)
			self.RefreshBagSlotWindow()
			
		def SetInventoryPage(self, page):
			self.inventoryPageIndex = page
			for i in range(0,len(self.inventoryTab)):
				self.inventoryTab[i].SetUp()
			self.inventoryTab[page].Down()
			self.RefreshBagSlotWindow()

		def OnPickItem(self, count):
			itemSlotIndex = self.dlgPickMoney.itemGlobalSlotIndex
			selectedItemVNum = player.GetItemIndex(itemSlotIndex)
			if self.inventoryType == 0:
				mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_SKILL_BOOK_INVENTORY, itemSlotIndex, selectedItemVNum, count)
			elif self.inventoryType == 2:
				mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_STONE_INVENTORY, itemSlotIndex, selectedItemVNum, count)
			elif self.inventoryType == 3:
				mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_SANDIK_INVENTORY, itemSlotIndex, selectedItemVNum, count)
			else:
				mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY, itemSlotIndex, selectedItemVNum, count)

		def __InventoryLocalSlotPosToGlobalSlotPos(self, local):
			if self.inventoryType == 0:
				return self.inventoryPageIndex*player.SKILL_BOOK_INVENTORY_SLOT_COUNT + local + item.SKILL_BOOK_INVENTORY_SLOT_START
			elif self.inventoryType == 2:
				return self.inventoryPageIndex*player.STONE_INVENTORY_SLOT_COUNT + local + item.STONE_INVENTORY_SLOT_START
			elif self.inventoryType == 3:
				return self.inventoryPageIndex*player.SANDIK_INVENTORY_SLOT_COUNT + local + item.SANDIK_INVENTORY_SLOT_START
			else:
				return self.inventoryPageIndex*player.UPGRADE_ITEMS_INVENTORY_SLOT_COUNT + local + item.UPGRADE_ITEMS_INVENTORY_SLOT_START
				
		def GetInventoryPageIndex(self):
			return self.inventoryPageIndex
			
		def RefreshBagSlotWindow(self):
			getItemVNum=player.GetItemIndex
			getItemCount=player.GetItemCount
			setItemVNum=self.wndItem.SetItemSlot
			
			if self.inventoryType == 0:
				for i in xrange(player.SKILL_BOOK_INVENTORY_SLOT_COUNT):
					#slotNumber = item.SKILL_BOOK_INVENTORY_SLOT_START + i
					slotNumber = item.SKILL_BOOK_INVENTORY_SLOT_START + i
					if self.GetInventoryPageIndex() == 1:
						slotNumber += 45
					elif self.GetInventoryPageIndex() == 2:
						slotNumber += 90
					itemCount = getItemCount(slotNumber)
					if 0 == itemCount:
						self.wndItem.ClearSlot(i)
						continue
					elif 1 == itemCount:
						itemCount = 0
					itemVnum = getItemVNum(slotNumber)
					setItemVNum(i, itemVnum, itemCount)
			elif self.inventoryType == 2:
				for i in xrange(player.STONE_INVENTORY_SLOT_COUNT):
					slotNumber = item.STONE_INVENTORY_SLOT_START + i
					if self.GetInventoryPageIndex() == 1:
						slotNumber += 45
					elif self.GetInventoryPageIndex() == 2:
						slotNumber += 90
					itemCount = getItemCount(slotNumber)
					if 0 == itemCount:
						self.wndItem.ClearSlot(i)
						continue
					elif 1 == itemCount:
						itemCount = 0	
					itemVnum = getItemVNum(slotNumber)
					setItemVNum(i, itemVnum, itemCount)	
			elif self.inventoryType == 3:
				for i in xrange(player.SANDIK_INVENTORY_SLOT_COUNT):
					slotNumber = item.SANDIK_INVENTORY_SLOT_START + i
					if self.GetInventoryPageIndex() == 1:
						slotNumber += 45
					elif self.GetInventoryPageIndex() == 2:
						slotNumber += 90
					itemCount = getItemCount(slotNumber)
					if 0 == itemCount:
						self.wndItem.ClearSlot(i)
						continue
					elif 1 == itemCount:
						itemCount = 0	
					itemVnum = getItemVNum(slotNumber)
					setItemVNum(i, itemVnum, itemCount)
			else:
				for i in xrange(player.UPGRADE_ITEMS_INVENTORY_SLOT_COUNT):
					#slotNumber = item.UPGRADE_ITEMS_INVENTORY_SLOT_START + i
					slotNumber = item.UPGRADE_ITEMS_INVENTORY_SLOT_START + i
					if self.GetInventoryPageIndex() == 1:
						slotNumber += 45
					elif self.GetInventoryPageIndex() == 2:
						slotNumber += 90
					itemCount = getItemCount(slotNumber)
					if 0 == itemCount:
						self.wndItem.ClearSlot(i)
						continue
					elif 1 == itemCount:
						itemCount = 0	
					itemVnum = getItemVNum(slotNumber)
					setItemVNum(i, itemVnum, itemCount)
			self.wndItem.RefreshSlot()
			
		def RefreshItemSlot(self):
			self.RefreshBagSlotWindow()
			
		def RefreshStatus(self):
			pass
			
		def SetItemToolTip(self, tooltipItem):
			self.tooltipItem = tooltipItem
			
		def SelectEmptySlot(self, selectedSlotPos):
			if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
				return
			
			if self.inventoryType == 0:
				selectedSlotPos += item.SKILL_BOOK_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					selectedSlotPos += 45
				elif self.GetInventoryPageIndex() == 2:
					selectedSlotPos += 90
			elif self.inventoryType == 2:
				selectedSlotPos += item.STONE_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					selectedSlotPos += 45
				elif self.GetInventoryPageIndex() == 2:
					selectedSlotPos += 90
			elif self.inventoryType == 3:
				selectedSlotPos += item.SANDIK_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					selectedSlotPos += 45
				elif self.GetInventoryPageIndex() == 2:
					selectedSlotPos += 90
			else:
				selectedSlotPos += item.UPGRADE_ITEMS_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					selectedSlotPos += 45
				elif self.GetInventoryPageIndex() == 2:
					selectedSlotPos += 90
			
			if mouseModule.mouseController.isAttached():

				attachedSlotType = mouseModule.mouseController.GetAttachedType()
				attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
				attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()
				attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()

				if player.SLOT_TYPE_INVENTORY == attachedSlotType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == attachedSlotType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == attachedSlotType or player.SLOT_TYPE_STONE_INVENTORY == attachedSlotType or player.SLOT_TYPE_SANDIK_INVENTORY == attachedSlotType:
					itemCount = player.GetItemCount(attachedSlotPos)
					attachedCount = mouseModule.mouseController.GetAttachedItemCount()
					self.__SendMoveItemPacket(attachedSlotPos, selectedSlotPos, attachedCount)

					if item.IsRefineScroll(attachedItemIndex):
						self.wndItem.SetUseMode(False)

				elif player.SLOT_TYPE_PRIVATE_SHOP == attachedSlotType:
					mouseModule.mouseController.RunCallBack("INVENTORY")
					
				elif player.SLOT_TYPE_OFFLINE_SHOP == attachedSlotType:
					mouseModule.mouseController.RunCallBack("INVENTORY")

				elif player.SLOT_TYPE_SHOP == attachedSlotType:
					net.SendShopBuyPacket(attachedSlotPos)

				elif player.SLOT_TYPE_SAFEBOX == attachedSlotType:

					if player.ITEM_MONEY == attachedItemIndex:
						net.SendSafeboxWithdrawMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
						snd.PlaySound("sound/ui/money.wav")

					else:
						net.SendSafeboxCheckoutPacket(attachedSlotPos, selectedSlotPos)

				elif player.SLOT_TYPE_MALL == attachedSlotType:
					net.SendMallCheckoutPacket(attachedSlotPos, selectedSlotPos)

				mouseModule.mouseController.DeattachObject()
				
		def SelectItemSlot(self, itemSlotIndex):
			if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
				return
			if self.inventoryType == 0:
				itemSlotIndex += item.SKILL_BOOK_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					itemSlotIndex += 45
				elif self.GetInventoryPageIndex() == 2:
					itemSlotIndex += 90
			elif self.inventoryType == 2:
				itemSlotIndex += item.STONE_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					itemSlotIndex += 45
				elif self.GetInventoryPageIndex() == 2:
					itemSlotIndex += 90
			elif self.inventoryType == 3:
				itemSlotIndex += item.SANDIK_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					itemSlotIndex += 45
				elif self.GetInventoryPageIndex() == 2:
					itemSlotIndex += 90
			else:
				itemSlotIndex += item.UPGRADE_ITEMS_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					itemSlotIndex += 45
				elif self.GetInventoryPageIndex() == 2:
					itemSlotIndex += 90		

			if mouseModule.mouseController.isAttached():
				attachedSlotType = mouseModule.mouseController.GetAttachedType()
				attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
				attachedItemVID = mouseModule.mouseController.GetAttachedItemIndex()
				attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()
				
				if player.GetItemCount(itemSlotIndex) > attachedItemCount:
					return
				
				curCursorNum = app.GetCursor()
				if app.SELL == curCursorNum:
					self.__SellItem(itemSlotIndex)
			
				if player.SLOT_TYPE_INVENTORY == attachedSlotType or player.SLOT_TYPE_SKILL_BOOK_INVENTORY == attachedSlotType or player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY == attachedSlotType or player.SLOT_TYPE_STONE_INVENTORY == attachedSlotType or player.SLOT_TYPE_SANDIK_INVENTORY == attachedSlotType:
					self.__SendMoveItemPacket(attachedSlotPos, itemSlotIndex, attachedItemCount)
		
				mouseModule.mouseController.DeattachObject()
			else:

				curCursorNum = app.GetCursor()
				if app.SELL == curCursorNum:
					self.__SellItem(itemSlotIndex)
					
				elif app.BUY == curCursorNum:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_BUY_INFO)

				elif app.IsPressed(app.DIK_LALT):
					link = player.GetItemLink(itemSlotIndex)
					ime.PasteString(link)

				elif app.IsPressed(app.DIK_LSHIFT):
					itemCount = player.GetItemCount(itemSlotIndex)
					
					if itemCount > 1:
						self.dlgPickMoney.SetTitleName(localeInfo.PICK_ITEM_TITLE)
						self.dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickItem))
						self.dlgPickMoney.Open(itemCount)
						self.dlgPickMoney.itemGlobalSlotIndex = itemSlotIndex
					#else:
						#selectedItemVNum = player.GetItemIndex(itemSlotIndex)
						#mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum)

				elif app.IsPressed(app.DIK_LCONTROL):
					itemIndex = player.GetItemIndex(itemSlotIndex)

					if True == item.CanAddToQuickSlotItem(itemIndex):
						if self.inventoryType == 0:
							player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_SKILL_BOOK_INVENTORY, itemSlotIndex)
						elif self.inventoryType == 2:
							player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_STONE_INVENTORY, itemSlotIndex)
						elif self.inventoryType == 3:
							player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_SANDIK_INVENTORY, itemSlotIndex)
						else:
							player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY, itemSlotIndex)
					else:
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.QUICKSLOT_REGISTER_DISABLE_ITEM)

				else:
					selectedItemVNum = player.GetItemIndex(itemSlotIndex)
					itemCount = player.GetItemCount(itemSlotIndex)
					if self.inventoryType == 0:
						mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_SKILL_BOOK_INVENTORY, itemSlotIndex, selectedItemVNum, itemCount)
					elif self.inventoryType == 2:
						mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_STONE_INVENTORY, itemSlotIndex, selectedItemVNum, itemCount)
					elif self.inventoryType == 3:
						mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_SANDIK_INVENTORY, itemSlotIndex, selectedItemVNum, itemCount)
					else:
						mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_UPGRADE_ITEMS_INVENTORY, itemSlotIndex, selectedItemVNum, itemCount)

					self.wndItem.SetUseMode(True)

					snd.PlaySound("sound/ui/pick.wav")
					
		def __SellItem(self, itemSlotPos):
			if not player.IsEquipmentSlot(itemSlotPos):
				self.sellingSlotNumber = itemSlotPos
				itemIndex = player.GetItemIndex(itemSlotPos)
				itemCount = player.GetItemCount(itemSlotPos)
				
				
				self.sellingSlotitemIndex = itemIndex
				self.sellingSlotitemCount = itemCount

				item.SelectItem(itemIndex)
				## ?? ??? ?? ??? ??
				## 20140220
				if item.IsAntiFlag(item.ANTIFLAG_SELL):
					popup = uiCommon.PopupDialog()
					popup.SetText(localeInfo.SHOP_CANNOT_SELL_ITEM)
					popup.SetAcceptEvent(self.__OnClosePopupDialog)
					popup.Open()
					self.popup = popup
					return
				itemPrice = player.GetISellItemPrice(itemSlotPos)

				item.GetItemName(itemIndex)
				itemName = item.GetItemName()

				self.questionDialog = uiCommon.QuestionDialog()
				self.questionDialog.SetText(localeInfo.DO_YOU_SELL_ITEM(itemName, itemCount, itemPrice))
				self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.SellItem))
				self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
				self.questionDialog.Open()
				self.questionDialog.count = itemCount

				constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
				
		def SellItem(self):
			if self.sellingSlotitemIndex == player.GetItemIndex(self.sellingSlotNumber):
				if self.sellingSlotitemCount == player.GetItemCount(self.sellingSlotNumber):
					## ???? ??? ?? ?? ????? ?? type ??
					net.SendShopSellPacketNew(self.sellingSlotNumber, self.questionDialog.count, player.INVENTORY)
					snd.PlaySound("sound/ui/money.wav")
			self.OnCloseQuestionDialog()
			
		def OnCloseQuestionDialog(self):
			if not self.questionDialog:
				return
			
			self.questionDialog.Close()
			self.questionDialog = None
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
			
		def __OnClosePopupDialog(self):
			self.pop = None
			
		def OverOutItem(self):
			self.wndItem.SetUsableItem(False)
			if None != self.tooltipItem:
				self.tooltipItem.HideToolTip()

		def OverInItem(self, overSlotPos):
			if self.inventoryType == 0:
				overSlotPos += item.SKILL_BOOK_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					overSlotPos += 45
				elif self.GetInventoryPageIndex() == 2:
					overSlotPos += 90
			elif self.inventoryType == 2:
				overSlotPos += item.STONE_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					overSlotPos += 45
				elif self.GetInventoryPageIndex() == 2:
					overSlotPos += 90
			elif self.inventoryType == 3:
				overSlotPos += item.SANDIK_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					overSlotPos += 45
				elif self.GetInventoryPageIndex() == 2:
					overSlotPos += 90
			else:
				overSlotPos += item.UPGRADE_ITEMS_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					overSlotPos += 45
				elif self.GetInventoryPageIndex() == 2:
					overSlotPos += 90
			self.wndItem.SetUsableItem(False)
			self.ShowToolTip(overSlotPos)
			self.ShowToolTip(overSlotPosGlobal)

		def ShowToolTip(self, slotIndex):
			if None != self.tooltipItem:
				self.tooltipItem.SetInventoryItem(slotIndex)

		def OnPressEscapeKey(self):
			self.Close()
			return True	
			
		def UseItemSlot(self, slotIndex):
			if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS():
				return
				
			if self.inventoryType == 0:
				slotIndex += item.SKILL_BOOK_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					slotIndex += 45
				elif self.GetInventoryPageIndex() == 2:
					slotIndex += 90
			elif self.inventoryType == 2:
				slotIndex += item.STONE_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					slotIndex += 45
				elif self.GetInventoryPageIndex() == 2:
					slotIndex += 90
			elif self.inventoryType == 3:
				slotIndex += item.SANDIK_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					slotIndex += 45
				elif self.GetInventoryPageIndex() == 2:
					slotIndex += 90
			else:
				slotIndex += item.UPGRADE_ITEMS_INVENTORY_SLOT_START
				if self.GetInventoryPageIndex() == 1:
					slotIndex += 45
				elif self.GetInventoryPageIndex() == 2:
					slotIndex += 90
			self.__UseItem(slotIndex)
			mouseModule.mouseController.DeattachObject()
			self.OverOutItem()
			
		def __UseItem(self, slotIndex):
			ItemVNum = player.GetItemIndex(slotIndex)
			item.SelectItem(ItemVNum)
			if item.IsFlag(item.ITEM_FLAG_CONFIRM_WHEN_USE):
				self.questionDialog = uiCommon.QuestionDialog()
				self.questionDialog.SetText(localeInfo.INVENTORY_REALLY_USE_ITEM)
				self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnAccept))
				self.questionDialog.SetCancelEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnCancel))
				self.questionDialog.Open()
				self.questionDialog.slotIndex = slotIndex
			
				constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

			else:
				self.__SendUseItemPacket(slotIndex)
				#net.SendItemUsePacket(slotIndex)	
				
		def __UseItemQuestionDialog_OnCancel(self):
			self.OnCloseQuestionDialog()

		def __UseItemQuestionDialog_OnAccept(self):
			self.__SendUseItemPacket(self.questionDialog.slotIndex)
			self.OnCloseQuestionDialog()	
			
		def __SendUseItemPacket(self, slotPos):
			# ???? ?? ?? ?? ??? ?? ??
			if uiPrivateShopBuilder.IsBuildingPrivateShop():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
				return
				
			if (uiOfflineShopBuilder.IsBuildingOfflineShop()):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_OFFLINE_SHOP)
				return
					
			if (uiOfflineShop.IsEditingOfflineShop()):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_OFFLINE_SHOP)
				return
				
			net.SendItemUsePacket(slotPos)
		
		def __SendMoveItemPacket(self, srcSlotPos, dstSlotPos, srcItemCount):
			if uiPrivateShopBuilder.IsBuildingPrivateShop():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
				return

			if (uiOfflineShopBuilder.IsBuildingOfflineShop()):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_OFFLINE_SHOP)
				return

			if (uiOfflineShop.IsEditingOfflineShop()):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_OFFLINE_SHOP)
				return