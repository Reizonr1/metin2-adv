	if app.WJ_ENABLE_TRADABLE_ICON:
		def RefreshMarkSlots(self, localIndex=None):
			if not self.interface:
				return
			if not self.wndItem:
				return

			onTopWnd = self.interface.GetOnTopWindow()
			if localIndex:
				slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(localIndex)
				if onTopWnd == player.ON_TOP_WND_NONE:
					self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif onTopWnd == player.ON_TOP_WND_SHOP:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SELL) or app.ENABLE_SEALBIND_SYSTEM and player.IsSealedItemBySlot(player.INVENTORY, slotNumber):
						self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif onTopWnd == player.ON_TOP_WND_EXCHANGE:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_GIVE) or app.ENABLE_SEALBIND_SYSTEM and player.IsSealedItemBySlot(player.INVENTORY, slotNumber):
						self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif onTopWnd == player.ON_TOP_WND_PRIVATE_SHOP:
					if player.IsAntiFlagBySlot(slotNumber, item.ITEM_ANTIFLAG_MYSHOP) or app.ENABLE_SEALBIND_SYSTEM and player.IsSealedItemBySlot(player.INVENTORY, slotNumber):
						self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif onTopWnd == player.ON_TOP_WND_SAFEBOX:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SAFEBOX):
						self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif app.ENABLE_ACCE_COSTUME_SYSTEM and onTopWnd == player.ON_TOP_WND_ACCE_COMBINE:
					if not (player.GetItemTypeBySlot(player.INVENTORY, slotNumber) == item.ITEM_TYPE_COSTUME and player.GetItemSubTypeBySlot(player.INVENTORY, slotNumber) == item.COSTUME_TYPE_ACCE):
						if app.ENABLE_SEALBIND_SYSTEM and player.IsSealedItemBySlot(player.INVENTORY, slotNumber):
							self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
						else:
							self.wndItem.SetUsableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif app.ENABLE_ACCE_COSTUME_SYSTEM and onTopWnd == player.ON_TOP_WND_ACCE_ABSORB:
					if not (player.GetItemTypeBySlot(player.INVENTORY, slotNumber) == item.ITEM_TYPE_WEAPON and player.GetItemSubTypeBySlot(player.INVENTORY, slotNumber) != item.WEAPON_ARROW or (app.ENABLE_QUIVER_SYSTEM and player.GetItemTypeBySlot(player.INVENTORY, slotNumber) == item.ITEM_TYPE_WEAPON and player.GetItemSubTypeBySlot(player.INVENTORY, slotNumber) == item.WEAPON_QUIVER) or (player.GetItemTypeBySlot(player.INVENTORY, slotNumber) == item.ITEM_TYPE_COSTUME and player.GetItemSubTypeBySlot(player.INVENTORY, slotNumber) == item.COSTUME_TYPE_ACCE) or (player.GetItemTypeBySlot(player.INVENTORY, slotNumber) == item.ITEM_TYPE_ARMOR and player.GetItemSubTypeBySlot(player.INVENTORY, slotNumber) == item.ARMOR_BODY)):
						if app.ENABLE_SEALBIND_SYSTEM and player.IsSealedItemBySlot(player.INVENTORY, slotNumber):
							self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
						else:
							self.wndItem.SetUsableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				#elif app.ENABLE_ACCE_COSTUME_SYSTEM and onTopWnd == player.ON_TOP_WND_ACCE_RESTORE:
				#	if ():
				#		self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
				#	else:
				#		self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				return

			for i in xrange(player.INVENTORY_PAGE_SIZE):
				slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)

				if onTopWnd == player.ON_TOP_WND_NONE:
					self.wndItem.SetUsableSlotOnTopWnd(i)

				elif onTopWnd == player.ON_TOP_WND_SHOP:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SELL) or app.ENABLE_SEALBIND_SYSTEM and player.IsSealedItemBySlot(player.INVENTORY, slotNumber):
						self.wndItem.SetUnusableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)

				elif onTopWnd == player.ON_TOP_WND_EXCHANGE:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_GIVE) or app.ENABLE_SEALBIND_SYSTEM and player.IsSealedItemBySlot(player.INVENTORY, slotNumber):
						self.wndItem.SetUnusableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)

				elif onTopWnd == player.ON_TOP_WND_PRIVATE_SHOP:
					if player.IsAntiFlagBySlot(slotNumber, item.ITEM_ANTIFLAG_MYSHOP) or app.ENABLE_SEALBIND_SYSTEM and player.IsSealedItemBySlot(player.INVENTORY, slotNumber):
						self.wndItem.SetUnusableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)

				elif onTopWnd == player.ON_TOP_WND_SAFEBOX:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SAFEBOX):
						self.wndItem.SetUnusableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)

				elif app.ENABLE_ACCE_COSTUME_SYSTEM and onTopWnd == player.ON_TOP_WND_ACCE_COMBINE:
					if not (player.GetItemTypeBySlot(player.INVENTORY, slotNumber) == item.ITEM_TYPE_COSTUME and player.GetItemSubTypeBySlot(player.INVENTORY, slotNumber) == item.COSTUME_TYPE_ACCE):
						if app.ENABLE_SEALBIND_SYSTEM and player.IsSealedItemBySlot(player.INVENTORY, slotNumber):
							self.wndItem.SetUnusableSlotOnTopWnd(i)
						else:
							self.wndItem.SetUsableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)

				elif app.ENABLE_ACCE_COSTUME_SYSTEM and onTopWnd == player.ON_TOP_WND_ACCE_ABSORB:
					if not (player.GetItemTypeBySlot(player.INVENTORY, slotNumber) == item.ITEM_TYPE_WEAPON and player.GetItemSubTypeBySlot(player.INVENTORY, slotNumber) != item.WEAPON_ARROW or (app.ENABLE_QUIVER_SYSTEM and player.GetItemTypeBySlot(player.INVENTORY, slotNumber) == item.ITEM_TYPE_WEAPON and player.GetItemSubTypeBySlot(player.INVENTORY, slotNumber) == item.WEAPON_QUIVER) or (player.GetItemTypeBySlot(player.INVENTORY, slotNumber) == item.ITEM_TYPE_COSTUME and player.GetItemSubTypeBySlot(player.INVENTORY, slotNumber) == item.COSTUME_TYPE_ACCE) or (player.GetItemTypeBySlot(player.INVENTORY, slotNumber) == item.ITEM_TYPE_ARMOR and player.GetItemSubTypeBySlot(player.INVENTORY, slotNumber) == item.ARMOR_BODY)):
						if app.ENABLE_SEALBIND_SYSTEM and player.IsSealedItemBySlot(player.INVENTORY, slotNumber):
							self.wndItem.SetUnusableSlotOnTopWnd(i)
						else:
							self.wndItem.SetUsableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)

				#elif app.ENABLE_ACCE_COSTUME_SYSTEM and onTopWnd == player.ON_TOP_WND_ACCE_RESTORE:
				#	if ():
				#		self.wndItem.SetUnusableSlotOnTopWnd(i)
				#	else:
				#		self.wndItem.SetUsableSlotOnTopWnd(i)
