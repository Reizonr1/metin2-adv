Search:
import localeInfo

Add it under
import net

https://puu.sh/sgYHD/78e1ba8781.png

---

Search:
		self.inputDialog = None

Change:
		if app.ENABLE_OFFLINE_SHOP:
			self.shopInputDialog = None
		else:
			self.inputDialog = None

https://puu.sh/sgYKx/5dd41a3fad.png

---

Search:
		self.dlgPassword = uiSafebox.PasswordDialog()
		self.dlgPassword.Hide()

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			self.dlgOfflineShop = uiSafebox.OfflineShopUI()
			self.dlgOfflineShop.Close()


Search:
		self.privateShopBuilder = uiPrivateShopBuilder.PrivateShopBuilder()

Change:
		if app.ENABLE_OFFLINE_SHOP:
			self.privateShopBuilder = uiPrivateShopBuilder.PrivateShopBuilder(self.wndInventory)
		else:
			self.privateShopBuilder = uiPrivateShopBuilder.PrivateShopBuilder()


https://puu.sh/sgYOJ/b672abe13b.png

---

Search:
		if self.dlgPassword:
			self.dlgPassword.Destroy()

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			if self.dlgOfflineShop:
				self.dlgOfflineShop.Close()

https://puu.sh/sgYQt/9c5b72b1ef.png

---

Search:
		del self.dlgPassword

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			del self.dlgOfflineShop


Search:
		del self.inputDialog

Change:
		if app.ENABLE_OFFLINE_SHOP:
			del self.shopInputDialog
		else:
			del self.inputDialog

https://puu.sh/sgYUj/fafc4c1cbb.png

---

Search:
	def OpenShopDialog(self, vid):
		self.wndInventory.Show()
		self.wndInventory.SetTop()
		self.dlgShop.Open(vid)
		self.dlgShop.SetTop()

Change:
	if app.ENABLE_OFFLINE_SHOP:
		def OpenShopDialog(self, vid, owner_vid, grid_type):
			self.wndInventory.Show()
			self.wndInventory.SetTop()
			self.dlgShop.Open(vid, owner_vid, grid_type)
			self.dlgShop.SetTop()
	else:
		def OpenShopDialog(self, vid):
			self.wndInventory.Show()
			self.wndInventory.SetTop()
			self.dlgShop.Open(vid)
			self.dlgShop.SetTop()


https://puu.sh/sgYXT/7f19f53662.png

---

Search:
	def RefreshShopDialog(self):
		self.dlgShop.Refresh()

Add it under:
	if app.ENABLE_OFFLINE_SHOP:
		def RefreshShopDialogMoney(self):
			self.dlgShop.RefreshMoney()


https://puu.sh/sgYZI/4a814cf447.png


---

Search:
	def CommandCloseSafebox(self):
		self.wndSafebox.CommandCloseSafebox()
	
Add it under:
	if app.ENABLE_OFFLINE_SHOP:
		def AppendOfflineShopData(self, name, vid, mapIdx, x, y):
			self.dlgOfflineShop.AppendOfflineShop(name, vid, mapIdx, x, y)


https://puu.sh/sgZ2C/9cd0bbcb3d.png

---

Search:
	def BINARY_SetObserverMode(self, flag):
		self.wndGameButton.SetObserverMode(flag)

Add it under:
	if app.ENABLE_OFFLINE_SHOP:
		def BINARY_SetMoveShopMode(self, flag):
			self.wndGameButton.SetMoveShop(flag)
	
https://puu.sh/sgZ4J/e7dcad3381.png

---

Search:

	def OpenPrivateShopInputNameDialog(self):
		#if player.IsInSafeArea():
		#	chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CANNOT_OPEN_PRIVATE_SHOP_IN_SAFE_AREA)
		#	return

		inputDialog = uiCommon.InputDialog()
		inputDialog.SetTitle(localeInfo.PRIVATE_SHOP_INPUT_NAME_DIALOG_TITLE)
		inputDialog.SetMaxLength(32)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OpenPrivateShopBuilder))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.ClosePrivateShopInputNameDialog))
		inputDialog.Open()
		self.inputDialog = inputDialog

	def ClosePrivateShopInputNameDialog(self):
		self.inputDialog = None
		return True

	def OpenPrivateShopBuilder(self):

		if not self.inputDialog:
			return True

		if not len(self.inputDialog.GetText()):
			return True

		self.privateShopBuilder.Open(self.inputDialog.GetText())
		self.ClosePrivateShopInputNameDialog()
		return True

Change:
	if app.ENABLE_OFFLINE_SHOP:
		def OpenPrivateShopInputNameDialog(self, hasCoin, hasGoldbar, hasWon):
			#if player.IsInSafeArea():
			#	chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CANNOT_OPEN_PRIVATE_SHOP_IN_SAFE_AREA)
			#	return
	
			constInfo.SHOP_ALLOW_COIN = hasCoin
			constInfo.SHOP_ALLOW_GOLDBAR = hasGoldbar
			constInfo.SHOP_ALLOW_WON = hasWon
	
			shopInputDialog = uiCommon.ShopInputDialog()
			shopInputDialog.SetTitle(localeInfo.PRIVATE_SHOP_INPUT_NAME_DIALOG_TITLE)
			shopInputDialog.SetMaxLength(32)
			shopInputDialog.SetAcceptEvent(ui.__mem_func__(self.OpenPrivateShopBuilder))
			shopInputDialog.SetCancelEvent(ui.__mem_func__(self.ClosePrivateShopInputNameDialog))
			shopInputDialog.Open()
			self.shopInputDialog = shopInputDialog
	
		def ClosePrivateShopInputNameDialog(self):
			self.shopInputDialog = None
			return True
	
		def OpenPrivateShopBuilder(self):
			if not self.shopInputDialog:
				return True
	
			shopPriceList = [0, 10000, 20000, 30000, 40000, 80000]
			shopType = self.shopInputDialog.GetShopType()
			shopSize = self.shopInputDialog.GetShopSize()
			shopColor = self.shopInputDialog.GetShopColor()
			
			if not len(self.shopInputDialog.GetText()):
				chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Enter the shop name")
				return True
			
			if shopSize < 0 or shopSize > 5:
				chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Select any shop size")
				return True	
	
			if shopType < 0 or shopType > 5:
				chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Select any shop type")
				return True
			
			if not shopType == 0 and (shopColor < 0 or shopColor > 5):
				chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Select any shop color")
				return True		
	
			if player.GetElk() < shopPriceList[shopType]:
				chat.AppendChat(chat.CHAT_TYPE_NOTICE, "You have not enough yang")
				return True
	
	
			self.privateShopBuilder.Open(self.shopInputDialog.GetText(), shopType, shopSize, shopColor)
			self.ClosePrivateShopInputNameDialog()
			return True
	else:
		def OpenPrivateShopInputNameDialog(self):
			#if player.IsInSafeArea():
			#	chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CANNOT_OPEN_PRIVATE_SHOP_IN_SAFE_AREA)
			#	return
	
			inputDialog = uiCommon.InputDialog()
			inputDialog.SetTitle(localeInfo.PRIVATE_SHOP_INPUT_NAME_DIALOG_TITLE)
			inputDialog.SetMaxLength(32)
			inputDialog.SetAcceptEvent(ui.__mem_func__(self.OpenPrivateShopBuilder))
			inputDialog.SetCancelEvent(ui.__mem_func__(self.ClosePrivateShopInputNameDialog))
			inputDialog.Open()
			self.inputDialog = inputDialog
	
		def ClosePrivateShopInputNameDialog(self):
			self.inputDialog = None
			return True
	
		def OpenPrivateShopBuilder(self):
	
			if not self.inputDialog:
				return True
	
			if not len(self.inputDialog.GetText()):
				return True
	
			self.privateShopBuilder.Open(self.inputDialog.GetText())
			self.ClosePrivateShopInputNameDialog()
			return True

https://puu.sh/sgZ9V/c95424f680.png
https://puu.sh/sgZaN/51a99e2840.png



---

Search:
	def BUILD_OnUpdate(self):
		if not self.wndGuildBuilding:
			return

		if self.wndGuildBuilding.IsPositioningMode():
			import background
			x, y, z = background.GetPickingPoint()
			self.wndGuildBuilding.SetBuildingPosition(x, y, z)


Add it under:
	if app.ENABLE_OFFLINE_SHOP:
		def OFFSHOP_OnUpdate(self):
			if constInfo.SHOP_MOVE_FLAG:
				import background, chr, player
				x, y, z = background.GetPickingPoint()
				net.offshopx = int(x)
				net.offshopy = int(y)
				chr.SelectInstance(constInfo.SHOP_LAST_VID)
				if 0 != z:
					chr.SetPixelPosition(int(x), int(y), int(z))
				else:
					chr.SetPixelPosition(int(x), int(y))
				
		def OFFSHOP_BreakMouse(self):
			import chr
			constInfo.SHOP_MOVE_FLAG = 0
			newposx = net.offshopx / 100
			newposy = net.offshopy / 100
			net.SendChatPacket("/do_moveshop %s %s" % (str(newposx), str(newposy)))
			net.offshopx = 0
			net.offshopy = 0
			net.SetShopMoveMode(0)



https://puu.sh/sgZfD/57d99e06a9.png
https://puu.sh/sgZe2/a4cf4c8165.png


Search:
	def BUILD_OnMouseLeftButtonUp(self):

Add it under:
		if app.ENABLE_OFFLINE_SHOP and constInfo.SHOP_MOVE_FLAG:
			self.OFFSHOP_BreakMouse()
			return True

https://puu.sh/sgZhu/f095027c15.png
			








