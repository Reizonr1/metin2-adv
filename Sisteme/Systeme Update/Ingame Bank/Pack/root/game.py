Search:
	def RefreshStatus(self):
		self.CheckGameButton()

		if self.interface:
			self.interface.RefreshStatus()

		if self.playerGauge:
			self.playerGauge.RefreshGauge()

Add it under:
	def RefreshBarAmount(self):
		if self.interface:
			self.interface.RefreshBarAmount()


---

Search:
			# PRIVATE_SHOP_PRICE_LIST
			"MyShopPriceList"		: self.__PrivateShop_PriceList,
			# END_OF_PRIVATE_SHOP_PRICE_LIST

Add it under:
			"RecvBarCount"			: self.RecvBarCount,


---

Search:
	def __PlayMusic(self, flag, filename):
		flag = int(flag)
		if flag:
			snd.FadeOutAllMusic()
			musicInfo.SaveLastPlayFieldMusic()
			snd.FadeInMusic("BGM/" + filename)
		else:
			snd.FadeOutAllMusic()
			musicInfo.LoadLastPlayFieldMusic()
			snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)

	# END_OF_WEDDING

Add it under:
	def RecvBarCount(self, first, second, third):
		constInfo.bar_first_amount = str(first)
		constInfo.bar_second_amount = str(second)
		constInfo.bar_third_amount = str(third)

		self.RefreshBarAmount()

