""""""
#1) Search: self.currentCubeNPC = 0
#2) Make a new line and paste:
		self.acceInformation = {}
		self.currentAcceNPC = 0
""""""

""""""
#1) Search: BINARY_Cube_MaterialInfo
#2) Make a new line and paste:
	def BINARY_Acce_Open(self, npcVNUM):
		self.interface.OpenAcceWindow()

	def BINARY_Acce_Close(self):
		self.interface.CloseAcceWindow()

	def BINARY_Acce_UpdateInfo(self, gold, itemVnum, count, rItemVnum, rCount):
		self.interface.UpdateAcceInfo(gold, itemVnum, count, rItemVnum, rCount)

	def BINARY_Acce_Succeed(self, itemVnum, count):
		print "Making acce has succesfully!"
		self.interface.SucceedAcceWork(itemVnum, count)
		pass

	def BINARY_Acce_Failed(self):
		print "Making acce has failed!"
		self.interface.FailedAcceWork()
		pass

	def BINARY_Acce_Abs_Open(self, npcVNUM):
		self.interface.OpenAcceAbsWindow()

	def BINARY_Acce_Abs_Succeed(self):
		print "Acce absorption has succesfully!"
		self.interface.SucceedAcceAbsWork()
		pass
""""""

""""""
#1) Search: "MyShopPriceList"		: self.__PrivateShop_PriceList,
#2) Make a new line and paste:
			"AcceMessage" : self.AcceMessage,
			"AcceAbsMessage" : self.AcceAbsMessage,
""""""

""""""
#1) Search: def CommandCloseMall(self):
#2) Make a new line and paste:
	def AcceMessage(self):
		snd.PlaySound("sound/ui/make_soket.wav")
		self.PopupMessage(localeInfo.ACCE_DEL_SERVEITEM)

	def AcceAbsMessage(self):
		snd.PlaySound("sound/ui/make_soket.wav")
		self.PopupMessage(localeInfo.ACCE_DEL_ABSORDITEM)
""""""