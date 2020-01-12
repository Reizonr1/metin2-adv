#Find
			self.wndMoneySlot = self.GetChild("Money_Slot")

#Add
			if app.ADD_INVENTORY:
				self.engelblack = self.GetChild("engel_01_open")
				self.engelblackcl = self.GetChild("engel_01_close")
				self.engelblack2 = self.GetChild("engel_02_open")
				self.engelblack2cl = self.GetChild("engel_02_close")
				self.engelblack3 = self.GetChild("engel_03_open")
				self.engelblack3cl = self.GetChild("engel_03_close")
				self.engelblack4 = self.GetChild("engel_04_open")
				self.engelblack4cl = self.GetChild("engel_04_close")
				self.engelblack5 = self.GetChild("engel_05_open")
				self.engelblack5cl = self.GetChild("engel_05_close")
				self.engelblack6 = self.GetChild("engel_06_open")
				self.engelblack6cl = self.GetChild("engel_06_close")
				self.engelblack7 = self.GetChild("engel_07_open")
				self.engelblack7cl = self.GetChild("engel_07_close")
				self.engelblack8 = self.GetChild("engel_08_open")
				self.engelblack8cl = self.GetChild("engel_08_close")
				self.engelblack9 = self.GetChild("engel_09_open")
				self.engelblack9cl = self.GetChild("engel_09_close")

#Find
			if self.costumeButton and not app.ENABLE_COSTUME_SYSTEM:
				self.costumeButton.Hide()
				self.costumeButton.Destroy()
				self.costumeButton = 0

#Add
			if app.ADD_INVENTORY:
				self.engelblack.Hide()
				self.engelblackcl.Hide()
				self.engelblack2.Hide()
				self.engelblack2cl.Hide()
				self.engelblack3.Hide()
				self.engelblack3cl.Hide()
				self.engelblack4.Hide()
				self.engelblack4cl.Hide()
				self.engelblack5.Hide()
				self.engelblack5cl.Hide()
				self.engelblack6.Hide()
				self.engelblack6cl.Hide()
				self.engelblack7.Hide()
				self.engelblack7cl.Hide()
				self.engelblack8.Hide()
				self.engelblack8cl.Hide()
				self.engelblack9.Hide()
				self.engelblack9cl.Hide()

#Find
		self.dlgPickMoney = dlgPickMoney
		
#Add
		if app.ADD_INVENTORY:
			if self.engelblack:
				self.engelblack.SetEvent(ui.__mem_func__(self.en_ac))
			if self.engelblack2:
				self.engelblack2.SetEvent(ui.__mem_func__(self.en_ac))
			if self.engelblack3:
				self.engelblack3.SetEvent(ui.__mem_func__(self.en_ac))
			if self.engelblack4:
				self.engelblack4.SetEvent(ui.__mem_func__(self.en_ac))
			if self.engelblack5:
				self.engelblack5.SetEvent(ui.__mem_func__(self.en_ac))
			if self.engelblack6:
				self.engelblack6.SetEvent(ui.__mem_func__(self.en_ac))
			if self.engelblack7:
				self.engelblack7.SetEvent(ui.__mem_func__(self.en_ac))
			if self.engelblack8:
				self.engelblack8.SetEvent(ui.__mem_func__(self.en_ac))
			if self.engelblack9:
				self.engelblack9.SetEvent(ui.__mem_func__(self.en_ac))
				
#Find
		self.mallButton = None
		
#Add
		if app.ADD_INVENTORY:
			self.engelblack = None
			self.engelblackcl = None
			self.engelblack2 = None
			self.engelblack2cl = None
			self.engelblack3 = None
			self.engelblack3cl = None
			self.engelblack4 = None
			self.engelblack4cl = None
			self.engelblack5 = None
			self.engelblack5cl = None
			self.engelblack6 = None
			self.engelblack6cl = None
			self.engelblack7 = None
			self.engelblack7cl = None
			self.engelblack8 = None
			self.engelblack8cl = None
			self.engelblack9 = None
			self.engelblack9cl = None

#Find
	def SetInventoryPage(self, page):
	
#Change like this
	def SetInventoryPage(self, page):
		if app.ADD_INVENTORY:
			constInfo.envanter = page
			if page == 2:#3 envanter
				if player.GetEnvanter() == 0:#Hepsi kapali
					self.engelblack.Show()#open
					self.engelblackcl.Hide()
					self.engelblack2.Hide()
					self.engelblack2cl.Show()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Show()
					self.engelblack4.Hide()
					self.engelblack4cl.Show()
					self.engelblack5.Hide()
					self.engelblack5cl.Show()
					self.engelblack6.Hide()
					self.engelblack6cl.Show()
					self.engelblack7.Hide()
					self.engelblack7cl.Show()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 1:# 1 tane acık
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()
					self.engelblack2.Show()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Show()
					self.engelblack4.Hide()
					self.engelblack4cl.Show()
					self.engelblack5.Hide()
					self.engelblack5cl.Show()
					self.engelblack6.Hide()
					self.engelblack6cl.Show()
					self.engelblack7.Hide()
					self.engelblack7cl.Show()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 2:# 2 tane acık
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Show()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()
					self.engelblack4cl.Show()
					self.engelblack5.Hide()
					self.engelblack5cl.Show()
					self.engelblack6.Hide()
					self.engelblack6cl.Show()
					self.engelblack7.Hide()
					self.engelblack7cl.Show()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 3:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Show()###
					self.engelblack4cl.Hide()
					self.engelblack5.Hide()
					self.engelblack5cl.Show()
					self.engelblack6.Hide()
					self.engelblack6cl.Show()
					self.engelblack7.Hide()
					self.engelblack7cl.Show()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 4:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()###
					self.engelblack4cl.Hide()
					self.engelblack5.Show()
					self.engelblack5cl.Hide()
					self.engelblack6.Hide()
					self.engelblack6cl.Show()
					self.engelblack7.Hide()
					self.engelblack7cl.Show()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 5:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()###
					self.engelblack4cl.Hide()
					self.engelblack5.Hide()
					self.engelblack5cl.Hide()
					self.engelblack6.Show()#open
					self.engelblack6cl.Hide()
					self.engelblack7.Hide()
					self.engelblack7cl.Show()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 6:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()###
					self.engelblack4cl.Hide()
					self.engelblack5.Hide()
					self.engelblack5cl.Hide()
					self.engelblack6.Hide()#open
					self.engelblack6cl.Hide()
					self.engelblack7.Show()
					self.engelblack7cl.Hide()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 7:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()###
					self.engelblack4cl.Hide()
					self.engelblack5.Hide()
					self.engelblack5cl.Hide()
					self.engelblack6.Hide()#open
					self.engelblack6cl.Hide()
					self.engelblack7.Hide()
					self.engelblack7cl.Hide()
					self.engelblack8.Show()
					self.engelblack8cl.Hide()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 8:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()###
					self.engelblack4cl.Hide()
					self.engelblack5.Hide()
					self.engelblack5cl.Hide()
					self.engelblack6.Hide()#open
					self.engelblack6cl.Hide()
					self.engelblack7.Hide()
					self.engelblack7cl.Hide()
					self.engelblack8.Hide()
					self.engelblack8cl.Hide()
					self.engelblack9.Show()
					self.engelblack9cl.Hide()
				elif player.GetEnvanter() == 9:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()###
					self.engelblack4cl.Hide()
					self.engelblack5.Hide()
					self.engelblack5cl.Hide()
					self.engelblack6.Hide()#open
					self.engelblack6cl.Hide()
					self.engelblack7.Hide()
					self.engelblack7cl.Hide()
					self.engelblack8.Hide()
					self.engelblack8cl.Hide()
					self.engelblack9.Hide()
					self.engelblack9cl.Hide()
				elif player.GetEnvanter() >= 10:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()###
					self.engelblack4cl.Hide()
					self.engelblack5.Hide()
					self.engelblack5cl.Hide()
					self.engelblack6.Hide()#open
					self.engelblack6cl.Hide()
					self.engelblack7.Hide()
					self.engelblack7cl.Hide()
					self.engelblack8.Hide()
					self.engelblack8cl.Hide()
					self.engelblack9.Hide()
					self.engelblack9cl.Hide()
			elif page == 3:
				if player.GetEnvanter() >= 0 and player.GetEnvanter() <= 8:
					self.engelblack.Hide()#open
					self.engelblackcl.Show()
					self.engelblack2.Hide()
					self.engelblack2cl.Show()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Show()
					self.engelblack4.Hide()
					self.engelblack4cl.Show()
					self.engelblack5.Hide()
					self.engelblack5cl.Show()
					self.engelblack6.Hide()
					self.engelblack6cl.Show()
					self.engelblack7.Hide()
					self.engelblack7cl.Show()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 9:#Hepsi kapali
					self.engelblack.Show()#open
					self.engelblackcl.Hide()
					self.engelblack2.Hide()
					self.engelblack2cl.Show()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Show()
					self.engelblack4.Hide()
					self.engelblack4cl.Show()
					self.engelblack5.Hide()
					self.engelblack5cl.Show()
					self.engelblack6.Hide()
					self.engelblack6cl.Show()
					self.engelblack7.Hide()
					self.engelblack7cl.Show()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 10:# 1 tane acık
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()
					self.engelblack2.Show()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Show()
					self.engelblack4.Hide()
					self.engelblack4cl.Show()
					self.engelblack5.Hide()
					self.engelblack5cl.Show()
					self.engelblack6.Hide()
					self.engelblack6cl.Show()
					self.engelblack7.Hide()
					self.engelblack7cl.Show()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 11:# 2 tane acık
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Show()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()
					self.engelblack4cl.Show()
					self.engelblack5.Hide()
					self.engelblack5cl.Show()
					self.engelblack6.Hide()
					self.engelblack6cl.Show()
					self.engelblack7.Hide()
					self.engelblack7cl.Show()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 12:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Show()###
					self.engelblack4cl.Hide()
					self.engelblack5.Hide()
					self.engelblack5cl.Show()
					self.engelblack6.Hide()
					self.engelblack6cl.Show()
					self.engelblack7.Hide()
					self.engelblack7cl.Show()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 13:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()###
					self.engelblack4cl.Hide()
					self.engelblack5.Show()
					self.engelblack5cl.Hide()
					self.engelblack6.Hide()
					self.engelblack6cl.Show()
					self.engelblack7.Hide()
					self.engelblack7cl.Show()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 14:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()###
					self.engelblack4cl.Hide()
					self.engelblack5.Hide()
					self.engelblack5cl.Hide()
					self.engelblack6.Show()#open
					self.engelblack6cl.Hide()
					self.engelblack7.Hide()
					self.engelblack7cl.Show()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 15:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()###
					self.engelblack4cl.Hide()
					self.engelblack5.Hide()
					self.engelblack5cl.Hide()
					self.engelblack6.Hide()#open
					self.engelblack6cl.Hide()
					self.engelblack7.Show()
					self.engelblack7cl.Hide()
					self.engelblack8.Hide()
					self.engelblack8cl.Show()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 16:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()###
					self.engelblack4cl.Hide()
					self.engelblack5.Hide()
					self.engelblack5cl.Hide()
					self.engelblack6.Hide()#open
					self.engelblack6cl.Hide()
					self.engelblack7.Hide()
					self.engelblack7cl.Hide()
					self.engelblack8.Show()
					self.engelblack8cl.Hide()
					self.engelblack9.Hide()
					self.engelblack9cl.Show()
				elif player.GetEnvanter() == 17:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()###
					self.engelblack4cl.Hide()
					self.engelblack5.Hide()
					self.engelblack5cl.Hide()
					self.engelblack6.Hide()#open
					self.engelblack6cl.Hide()
					self.engelblack7.Hide()
					self.engelblack7cl.Hide()
					self.engelblack8.Hide()
					self.engelblack8cl.Hide()
					self.engelblack9.Show()
					self.engelblack9cl.Hide()
				elif player.GetEnvanter() == 18:
					self.engelblack.Hide()#open
					self.engelblackcl.Hide()#open
					self.engelblack2.Hide()
					self.engelblack2cl.Hide()#close
					self.engelblack3.Hide()
					self.engelblack3cl.Hide()
					self.engelblack4.Hide()###
					self.engelblack4cl.Hide()
					self.engelblack5.Hide()
					self.engelblack5cl.Hide()
					self.engelblack6.Hide()#open
					self.engelblack6cl.Hide()
					self.engelblack7.Hide()
					self.engelblack7cl.Hide()
					self.engelblack8.Hide()
					self.engelblack8cl.Hide()
					self.engelblack9.Hide()
					self.engelblack9cl.Hide()
			else:
				self.engelblack.Hide()
				self.engelblackcl.Hide()
				self.engelblack2.Hide()
				self.engelblack2cl.Hide()
				self.engelblack3.Hide()
				self.engelblack3cl.Hide()
				self.engelblack4.Hide()
				self.engelblack4cl.Hide()
				self.engelblack5.Hide()
				self.engelblack5cl.Hide()
				self.engelblack6.Hide()
				self.engelblack6cl.Hide()
				self.engelblack7.Hide()
				self.engelblack7cl.Hide()
				self.engelblack8.Hide()
				self.engelblack8cl.Hide()
				self.engelblack9.Hide()
				self.engelblack9cl.Hide()
		self.inventoryPageIndex = page
		self.inventoryTab[(page+1)%4].SetUp()
		self.inventoryTab[(page+2)%4].SetUp()
		self.inventoryTab[(page+3)%4].SetUp()
		self.RefreshBagSlotWindow()
		
#Find
	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

#Add
	if app.ADD_INVENTORY:
		def genislet(self):
			if uiPrivateShopBuilder.IsBuildingPrivateShop():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.ENVANTER_UYARI)
				return
			net.Envanter_genislet()
			self.OnCloseQuestionDialog()
			
#Find
	def __UseItem(self, slotIndex):
		ItemVNum = player.GetItemIndex(slotIndex)
		item.SelectItem(ItemVNum)
		
#Add
		if app.ADD_INVENTORY:
			if ItemVNum == 72320:
				if player.GetEnvanter() < 4:
					envanter = 2
					self.questionDialog = uiCommon.QuestionDialog()
					self.questionDialog.SetText(localeInfo.ENVANTER_GENIS_1 % envanter)
					self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.genislet))
					self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
					self.questionDialog.Open()
					self.questionDialog.slotIndex = slotIndex
				elif player.GetEnvanter() == 4 or player.GetEnvanter() == 5:
					envanter = 3
					self.questionDialog = uiCommon.QuestionDialog()
					self.questionDialog.SetText(localeInfo.ENVANTER_GENIS_1 % envanter)
					self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.genislet))
					self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
					self.questionDialog.Open()
					self.questionDialog.slotIndex = slotIndex
				elif player.GetEnvanter() == 6 or player.GetEnvanter() == 7 or player.GetEnvanter() == 8:
					envanter = 4
					self.questionDialog = uiCommon.QuestionDialog()
					self.questionDialog.SetText(localeInfo.ENVANTER_GENIS_1 % envanter)
					self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.genislet))
					self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
					self.questionDialog.Open()
					self.questionDialog.slotIndex = slotIndex
				elif player.GetEnvanter() == 9 or player.GetEnvanter() == 10 or player.GetEnvanter() == 11:
					envanter = 5
					self.questionDialog = uiCommon.QuestionDialog()
					self.questionDialog.SetText(localeInfo.ENVANTER_GENIS_1 % envanter)
					self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.genislet))
					self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
					self.questionDialog.Open()
					self.questionDialog.slotIndex = slotIndex
				elif player.GetEnvanter() == 12 or player.GetEnvanter() == 13 or player.GetEnvanter() == 14:
					envanter = 6
					self.questionDialog = uiCommon.QuestionDialog()
					self.questionDialog.SetText(localeInfo.ENVANTER_GENIS_1 % envanter)
					self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.genislet))
					self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
					self.questionDialog.Open()
					self.questionDialog.slotIndex = slotIndex
				elif player.GetEnvanter() == 15 or player.GetEnvanter() == 16 or player.GetEnvanter() == 17:
					envanter = 7
					self.questionDialog = uiCommon.QuestionDialog()
					self.questionDialog.SetText(localeInfo.ENVANTER_GENIS_1 % envanter)
					self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.genislet))
					self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
					self.questionDialog.Open()
					self.questionDialog.slotIndex = slotIndex
				else:
					self.wndPopupDialog = uiCommon.PopupDialog()
					self.wndPopupDialog.SetText(localeInfo.ENVANTER_ZATEN_GENIS_3)
					self.wndPopupDialog.Open()