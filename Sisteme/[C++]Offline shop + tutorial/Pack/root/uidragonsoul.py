?mportlar��n aras��na alttakileri ekleyin ;

import uiPrivateShopBuilder
import uiOfflineShopBuilder

Alttaki kodu arat��n ;

			attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
			if player.SLOT_TYPE_PRIVATE_SHOP == attachedSlotType:
				mouseModule.mouseController.RunCallBack("INVENTORY")

Ustteki kodun alt��na , alttaki kodu ekleyin.

			elif (player.SLOT_TYPE_OFFLINE_SHOP == attachedSlotType):
				mouseModule.mouseController.RunCallBack("INVENTORY")

Alttaki kodu arat��n ;

	def UseItemSlot(self, slotIndex):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS():
			return
		slotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(player.DRAGON_SOUL_INVENTORY, slotIndex)
		try:
			# ��ȥ�� ��ȭâ�� ����������, ������ ��Ŭ�� �� �ڵ����� ��ȭâ���� ��.
			if self.wndDragonSoulRefine.IsShow():
				if uiPrivateShopBuilder.IsBuildingPrivateShop():
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
					return

Ustteki kodun alt��na , alttaki kodu ekleyin.

				if (uiOfflineShopBuilder.IsBuildingOfflineShop()):
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_OFFLINE_SHOP)
					return

Alttaki kodu arat��n ;

	def __SendMoveItemPacket(self, srcSlotWindow, srcSlotPos, dstSlotWindow, dstSlotPos, srcItemCount):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
			return

Ustteki kodun alt��na , alttaki kodu ekleyin.

		if (uiOfflineShopBuilder.IsBuildingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_OFFLINE_SHOP)
			return

Alttaki kodu arat��n ;

	def __UseEquipItem(self, slotIndex):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

Ustteki kodun alt��na , alttaki kodu ekleyin.

		if (uiOfflineShopBuilder.IsBuildingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_OFFLINE_SHOP)
			return

Alttaki kodu arat��n ;

				if uiPrivateShopBuilder.IsBuildingPrivateShop():
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
					return

Ustteki kodun alt��na , alttaki kodu ekleyin.

				if (uiOfflineShopBuilder.IsBuildingOfflineShop()):
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_OFFLINE_SHOP)
					return

Alttaki kodu arat��n ;

					if uiPrivateShopBuilder.IsBuildingPrivateShop():
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
						return

Ustteki kodun alt��na , alttaki kodu ekleyin.

					if (uiOfflineShopBuilder.IsBuildingOfflineShop()):	
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_OFFLINE_SHOP)
						return
