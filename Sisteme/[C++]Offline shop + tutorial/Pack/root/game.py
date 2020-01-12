root > game.py acın ve importların arasına ekleyin ;

# OFFLINE_SHOP_PRICE_LIST
import uiOfflineShopBuilder
# END_OF_OFFLINE_SHOP_PRICE_LIST
import uiOfflineShop

Alttaki kodu aratın ;

		# PRIVATE_SHOP_PRICE_LIST
		uiPrivateShopBuilder.Clear()
		# END_OF_PRIVATE_SHOP_PRICE_LIST

Alttaki kodu ustteki kodun altına ekleyin.

		# OFFLINE_SHOP_PRICE_LIST
		uiOfflineShopBuilder.Clear()
		# END_OF_OFFLINE_SHOP_PRICE_LIST

Alttaki kodu aratın ;

	def	__PressJKey(self):

Kod blo?unu tamamen alttaki kod ile de?i?tirin ;

	def	__PressJKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			if player.IsMountingHorse():
				net.SendChatPacket("/unmount")
			else:
				#net.SendChatPacket("/user_horse_ride")
				if not uiPrivateShopBuilder.IsBuildingPrivateShop() or not uiOfflineShopBuilder.IsBuildingOfflineShop():
					for i in xrange(player.INVENTORY_PAGE_SIZE):
						if player.GetItemIndex(i) in (71114, 71116, 71118, 71120):
							net.SendItemUsePacket(i)
							break

Alttaki kodu aratın ;

	def SetShopSellingPrice(self, Price):
		pass

Alttaki kodu ustteki kodun altına ekleyin.

	## OfflineShop
	def StartOfflineShop(self, vid):
		self.interface.OpenOfflineShopDialog(vid)
		
	def EndOfflineShop(self):
		self.interface.CloseOfflineShopDialog()
		
	def RefreshOfflineShop(self):
		self.interface.RefreshOfflineShopDialog()

Alttaki kodu aratın ;

	def __DropMoney(self, attachedType, attachedMoney):
		# PRIVATESHOP_DISABLE_ITEM_DROP - 개인상점 열고 있는 동안 아이템 버림 방지
		if uiPrivateShopBuilder.IsBuildingPrivateShop():			
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return
		# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP

Alttaki kodu ustteki kodun altına ekleyin.

		# OFFLINESHOP_DISABLE_ITEM_DROP
		if (uiOfflineShopBuilder.IsBuildingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_OFFLINE_SHOP)
			return
		# END_OF_OFFLINESHOP_DISABLE_ITEM_DROP

		# OFFLINESHOP_DISABLE_ITEM_DROP2
		if (uiOfflineShop.IsEditingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_OFFLINE_SHOP)
			return
		# END_OF_OFFLINESHOP_DISABLE_ITEM_DROP2


Alttaki kodu aratın ;

	def __DropItem(self, attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount):
		# PRIVATESHOP_DISABLE_ITEM_DROP - 개인상점 열고 있는 동안 아이템 버림 방지
		if uiPrivateShopBuilder.IsBuildingPrivateShop():			
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return
		# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP

Alttaki kodu ustteki kodun altına ekleyin.

		# OFFLINESHOP_DISABLE_ITEM_DROP
		if (uiOfflineShopBuilder.IsBuildingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_OFFLINE_SHOP)
			return
		# END_OFF_OFFLINESHOP_DISABLE_ITEM_DROP
		
		# OFFLINESHOP_DISABLE_ITEM_DROP2
		if (uiOfflineShop.IsEditingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_OFFLINE_SHOP)
			return
		# END_OF_OFFLINESHOP_DISABLE_ITEM_DROP2

Alttaki kodu aratın ;

	def __SendDropItemPacket(self, itemVNum, itemCount, itemInvenType = player.INVENTORY):

Kod blo?unu tamamen alttaki kod ile de?i?tirin ;

	def __SendDropItemPacket(self, itemVNum, itemCount, itemInvenType = player.INVENTORY):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return
			
		if (uiOfflineShopBuilder.IsBuildingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_OFFLINE_SHOP)
			return
			
		if (uiOfflineShop.IsEditingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_OFFLINE_SHOP)
			return

		net.SendItemDropPacketNew(itemInvenType, itemVNum, itemCount)

Alttaki kodu aratın ;

			"OpenPrivateShop"		: self.__PrivateShop_Open,

Alttaki kodu ustteki kodun altına ekleyin.

			"OpenOfflineShop"		: self.__OfflineShop_Open,

Alttaki kodu aratın ;

	def BINARY_PrivateShop_Disappear(self, vid):
		if (chr.GetInstanceType(vid) == chr.INSTANCE_TYPE_PLAYER):
			self.interface.DisappearPrivateShop(vid)

Alttaki kodu ustteki kodun altına ekleyin.

	# OfflineShop
	def __OfflineShop_Open(self):
		self.interface.OpenOfflineShopInputNameDialog()
	
	def BINARY_OfflineShop_Appear(self, vid, text):	
		if (chr.GetInstanceType(vid) == chr.INSTANCE_TYPE_NPC):
			self.interface.AppearOfflineShop(vid, text)
		
	def BINARY_OfflineShop_Disappear(self, vid):	
		if (chr.GetInstanceType(vid) == chr.INSTANCE_TYPE_NPC):
			self.interface.DisappearOfflineShop(vid)





<---- GAME.PY ?LE ???M?Z B?TT? B?R SONRAK? DOSYA :) ---->



