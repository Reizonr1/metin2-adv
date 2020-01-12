Searh:
			# PRIVATE_SHOP_PRICE_LIST
			"MyShopPriceList"		: self.__PrivateShop_PriceList,
			# END_OF_PRIVATE_SHOP_PRICE_LIST

Add it under:
			"1x_kill"			: self.__KillEffect,
			"2x_kill"			: self.__DoubleEffect,
			"3x_kill"			: self.__TripleEffect,
			"4x_kill"			: self.__QuadraEffect,
			"5x_kill"			: self.__PentaEffect,
			"6x_kill"			: self.__HexaEffect,


---

Search:
	# ITEM_MALL
	def AskMallPassword(self):
		self.interface.AskMallPassword()

	def __ItemMall_Open(self):
		self.interface.OpenItemMall();

	def CommandCloseMall(self):
		self.interface.CommandCloseMall()
	# END_OF_ITEM_MALL

Add it under:
	def __KillEffect(self):
		snd.PlaySound("BGM//kill//onekill.mp3")
		net.SendChatPacket("(kill1)")

	def __DoubleEffect(self):
		snd.PlaySound("BGM//kill//doublekill.mp3")
		net.SendChatPacket("(kill2)")

	def __TripleEffect(self):
		snd.PlaySound("BGM//kill//triplekill.mp3")
		net.SendChatPacket("(kill3)")

	def __QuadraEffect(self):
		snd.PlaySound("BGM//kill//quadra.mp3")
		net.SendChatPacket("(kill4)")

	def __PentaEffect(self):
		snd.PlaySound("BGM//kill//pentakill.mp3")
		net.SendChatPacket("(kill5)")

	def __HexaEffect(self):
		snd.PlaySound("BGM//kill//hexakill.mp3")
		net.SendChatPacket("(kill6)")
