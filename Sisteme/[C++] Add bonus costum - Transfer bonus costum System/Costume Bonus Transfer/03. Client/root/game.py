""""""
#1) Search: def BINARY_Cube_MaterialInfo(self, startIndex, listCount, listText):
#2) After their definition make a new line and paste:
	if app.ENABLE_ATTR_TRANSFER_SYSTEM:
		def BINARY_AttrTransfer_Open(self):
			self.interface.OpenAttrTransferWindow()

		def BINARY_AttrTransfer_Close(self):
			self.interface.CloseAttrTransferWindow()

		def BINARY_AttrTransfer_Success(self):
			self.interface.AttrTransferSuccess()
""""""

""""""
#1) Search: "MyShopPriceList"		: self.__PrivateShop_PriceList,
#2) Make a new line and paste:
			"AttrTransferMessage" : self.AttrTransferMessage,
""""""

""""""
#1) Search: def CommandCloseMall(self):
#2) Make a new line and paste:
	def AttrTransferMessage(self):
		snd.PlaySound("sound/ui/make_soket.wav")
		self.PopupMessage(localeInfo.COMB_ALERT)
""""""