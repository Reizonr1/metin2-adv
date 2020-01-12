Search:
	def StartShop(self, vid):
		self.interface.OpenShopDialog(vid)

Change:
	if app.ENABLE_OFFLINE_SHOP:
		def StartShop(self, vid, owner_vid, grid_type):
			self.interface.OpenShopDialog(vid, owner_vid, grid_type)
	else:
		def StartShop(self, vid):
			self.interface.OpenShopDialog(vid)


https://puu.sh/sgYiM/eab1650247.png

---

Search:
	def RefreshShop(self):
		self.interface.RefreshShopDialog()

Add it under:
	if app.ENABLE_OFFLINE_SHOP:
		def RefreshShopMoney(self):
			self.interface.RefreshShopDialogMoney()


https://puu.sh/sgYkW/749894fe15.png

---

Search:
	def RefreshSafeboxMoney(self):
		self.interface.RefreshSafeboxMoney()

Add it under:
	if app.ENABLE_OFFLINE_SHOP:
		def AppendOfflineShopInfo(self, name, vid, mapIdx, x, y):
			self.interface.AppendOfflineShopData(name, vid, mapIdx, x, y)

https://puu.sh/sgYph/ce6c618b68.png
---

Search:
		self.interface.BUILD_OnUpdate()

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			self.interface.OFFSHOP_OnUpdate()


https://puu.sh/sgYr0/a0668996d8.png

---

Search:
	def __GuildWar_OnDecline(self):

		guildName = self.guildWarQuestionDialog.GetGuildName()

		net.SendChatPacket("/nowar " + guildName)
		self.__GuildWar_CloseAskDialog()

		return 1

Add it under:
	if app.ENABLE_OFFLINE_SHOP:
		def BINARY_SetOfflineShopMoveMode(self, isEnable):
			self.interface.BINARY_SetMoveShopMode(isEnable)
	
https://puu.sh/sgYtn/23f5a05558.png

---

Search:
		self.serverCommander=stringCommander.Analyzer()
		for serverCommandItem in serverCommandList.items():
			self.serverCommander.SAFE_RegisterCallBack(
				serverCommandItem[0], serverCommandItem[1]
			)

Add it upper:
		if app.ENABLE_OFFLINE_SHOP:
			serverCommandList.update({"offlineshop_info" : self.AppendOfflineShopInfo })

https://puu.sh/sgYv3/3ff8e62bde.png

---

Search:
	def __PrivateShop_Open(self):
		self.interface.OpenPrivateShopInputNameDialog()

	def BINARY_PrivateShop_Appear(self, vid, text):
		self.interface.AppearPrivateShop(vid, text)

Change:
	if app.ENABLE_OFFLINE_SHOP:
		def __PrivateShop_Open(self, hasCoin, hasGoldbar, hasWon):
			self.interface.OpenPrivateShopInputNameDialog(hasCoin, hasGoldbar, hasWon)
	else:
		def __PrivateShop_Open(self):
			self.interface.OpenPrivateShopInputNameDialog()

	def BINARY_PrivateShop_Appear(self, vid, text):
		if app.ENABLE_OFFLINE_SHOP:
			fmName = "%s's Offline shop" % player.GetName()
			if (systemSetting.IsShowOfflineShop() != 1 and not player.IsMainCharacterIndex(vid)) and (systemSetting.IsShowOfflineShop() == 2 and chr.GetNameByVID(vid) != fmName):
				return
			if chr.GetVirtualNumber(vid) < 30000:
				return
		self.interface.AppearPrivateShop(vid, text)


https://puu.sh/sgYwQ/a547e96a3e.png



