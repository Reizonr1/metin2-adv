Search:
		self.RefreshShowSalesText()

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			self.RefreshShowOfflineShop()

https://puu.sh/sgXdH/e64464db14.png

---

Search:
		self.showsalesTextButtonList = []

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			self.showOfflineShopButtonList = []

https://puu.sh/sgXfj/eba140c1ce.png

---

Search:
			self.showsalesTextButtonList.append(GetObject("salestext_off_button"))

Add it under:
			if app.ENABLE_OFFLINE_SHOP:
				self.showOfflineShopButtonList.append(GetObject("show_offline_shop_on"))
				self.showOfflineShopButtonList.append(GetObject("show_offline_shop_wome"))
				self.showOfflineShopButtonList.append(GetObject("show_offline_shop_off"))
			
https://puu.sh/sgXhf/17dd1208e5.png

---

Search:
		self.showsalesTextButtonList[0].SAFE_SetEvent(self.__OnClickSalesTextOnButton)
		self.showsalesTextButtonList[1].SAFE_SetEvent(self.__OnClickSalesTextOffButton)

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			self.showOfflineShopButtonList[0].SAFE_SetEvent(self.__OnClickOfflineShopOnButton)
			self.showOfflineShopButtonList[1].SAFE_SetEvent(self.__OnClickOfflineShopWoOnButton)
			self.showOfflineShopButtonList[2].SAFE_SetEvent(self.__OnClickOfflineShopOffButton)
		
https://puu.sh/sgXjb/15ac50d5df.png

--

Search:
	def __OnClickSalesTextOffButton(self):
		systemSetting.SetShowSalesTextFlag(False)
		self.RefreshShowSalesText()

Add it under:
	
	if app.ENABLE_OFFLINE_SHOP:
		def __OnClickOfflineShopOnButton(self):
			systemSetting.SetShowOfflineShop(1)
			self.RefreshShowOfflineShop()
			
		def __OnClickOfflineShopWoOnButton(self):
			systemSetting.SetShowOfflineShop(2)
			self.RefreshShowOfflineShop()
	
		def __OnClickOfflineShopOffButton(self):
			systemSetting.SetShowOfflineShop(0)
			self.RefreshShowOfflineShop()
	
https://puu.sh/sgXkV/009db621b4.png

---

Search:

	def RefreshShowSalesText(self):
		if systemSetting.IsShowSalesText():
			self.showsalesTextButtonList[0].Down()
			self.showsalesTextButtonList[1].SetUp()
		else:
			self.showsalesTextButtonList[0].SetUp()
			self.showsalesTextButtonList[1].Down()

Add it under:

	if app.ENABLE_OFFLINE_SHOP:
		def RefreshShowOfflineShop(self):
			if systemSetting.IsShowOfflineShop() == 1:
				self.showOfflineShopButtonList[0].Down()
				self.showOfflineShopButtonList[1].SetUp()
				self.showOfflineShopButtonList[2].SetUp()
			elif systemSetting.IsShowOfflineShop() == 2:
				self.showOfflineShopButtonList[0].SetUp()
				self.showOfflineShopButtonList[1].Down()
				self.showOfflineShopButtonList[2].SetUp()			
			else:
				self.showOfflineShopButtonList[0].SetUp()
				self.showOfflineShopButtonList[1].SetUp()
				self.showOfflineShopButtonList[2].Down()

				
https://puu.sh/sgXmN/9c1a0eb83b.png









