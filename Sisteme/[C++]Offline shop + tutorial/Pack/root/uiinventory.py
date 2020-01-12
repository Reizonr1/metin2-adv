?mportlar©¥n aras©¥na ekleyin ;

import uiOfflineShopBuilder
import uiOfflineShop

A??a?©¥daki kodu arat©¥n ;

			self.costumeButton = self.GetChild2("CostumeButton")

Yukardaki kodun alt©¥na a??a?©¥daki kodu ekleyin ;

			self.offlineShopButton = self.GetChild2("OfflineShopButton")

A??a?©¥daki kodu arat©¥n ;

		# Costume Button
		if self.costumeButton:
			self.costumeButton.SetEvent(ui.__mem_func__(self.ClickCostumeButton))

Yukardaki kodun alt©¥na a??a?©¥daki kodu ekleyin ;

		# Offline Shop Button
		if (self.offlineShopButton):
			self.offlineShopButton.SetEvent(ui.__mem_func__(self.ClickOfflineShopButton))

A??a?©¥daki kodu arat©¥n ;

	def ClickDSSButton(self):
		print "click_dss_button"
		self.interface.ToggleDragonSoulWindow()

Yukardaki kodun alt©¥na a??a?©¥daki kodu ekleyin ;

	# Offline Shop Button
	def ClickOfflineShopButton(self):
		print "click_offline_shop_button"
		self.interface.ToggleOfflineShopAdminPanelWindow()

A??a?©¥daki kodu arat©¥n ;

			elif player.SLOT_TYPE_PRIVATE_SHOP == attachedSlotType:
				mouseModule.mouseController.RunCallBack("INVENTORY")

Yukardaki kodun alt©¥na a??a?©¥daki kodu ekleyin ;

			elif player.SLOT_TYPE_OFFLINE_SHOP == attachedSlotType:
				mouseModule.mouseController.RunCallBack("INVENTORY")

A??a?©¥daki kodu arat©¥n ;

		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

Yukardaki kodun alt©¥na a??a?©¥daki kodu ekleyin ;

		if (uiOfflineShopBuilder.IsBuildingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_OFFLINE_SHOP)
			return
			
		if (uiOfflineShop.IsEditingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_OFFLINE_SHOP)
			return

A??a?©¥daki kodu arat©¥n ;

		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

Yukardaki kodun alt©¥na a??a?©¥daki kodu ekleyin ;

		if (uiOfflineShopBuilder.IsBuildingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_OFFLINE_SHOP)
			return

		if (uiOfflineShop.IsEditingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_OFFLINE_SHOP)
			return

A??a?©¥daki kodu arat©¥n ;

		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
			return

Yukardaki kodun alt©¥na a??a?©¥daki kodu ekleyin ;

		if (uiOfflineShopBuilder.IsBuildingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_OFFLINE_SHOP)
			return

		if (uiOfflineShop.IsEditingOfflineShop()):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_OFFLINE_SHOP)
			return
