#1.) Search:
		self.__ServerCommand_Build()
		self.__ProcessPreservedServerCommand()
#2.) Add after:
		if app.ENABLE_FEATURES_OXEVENT:
			import uioxevent
			self.eventWindowLogin = uioxevent.OxEventManagerLogin()
			self.eventWindowManager = uioxevent.OxEventManager()
			self.eventWindow = uioxevent.OxEventWinners()
			
#1.) Search:
		if self.targetBoard:
			self.targetBoard.Destroy()
			self.targetBoard = None
#2.) Add after:
		if app.ENABLE_FEATURES_OXEVENT:
			if self.eventWindowLogin:
				self.eventWindowLogin.Hide()
				
			if self.eventWindowManager:
				self.eventWindowManager.Hide()
		
			if self.eventWindow:
				self.eventWindow.Hide()
				
#1.) Search:
		onPressKeyDict[app.DIK_F4]	= lambda : self.__PressQuickSlot(7)
#2.) Add after:
		if app.ENABLE_FEATURES_OXEVENT:
			onPressKeyDict[app.DIK_F12]	= lambda : self.RecvOxEventLogin()		
	
#1.) Search:
	def __PartyRequestDenied(self):
		self.PopupMessage(localeInfo.PARTY_REQUEST_DENIED)
#2.) Add after:
	if app.ENABLE_FEATURES_OXEVENT:
		def RecvOxEventLogin(self):
			if self.eventWindowLogin.IsShow():
				self.eventWindowLogin.Hide()
			else:
				self.eventWindowLogin.Show()

#1.) Search:
	def __LoverFar(self):
		if self.affectShower:
			self.affectShower.HideLoverState()
#2.) Add after:
	if app.ENABLE_FEATURES_OXEVENT:
		def BINARY_OxEvent_Append(self, event, participantsCount, observersCount):
			import oxevent
			tokens = int(event)

			if tokens == oxevent.APPEND_WINNERS:
				self.eventWindow.Append()

			elif tokens == oxevent.APPEND_REFRESH:
				self.eventWindowManager.RefreshCounter(participantsCount, observersCount)		

			elif tokens == oxevent.APPEND_WINDOW:
				self.eventWindowManager.Show()
				
#1.) Search:
	def __PressQuickSlot(self, localSlotIndex):
		player.RequestUseLocalQuickSlot(localSlotIndex)
#2.) Delete and replace with:
	if app.ENABLE_FEATURES_OXEVENT:
		def __PressQuickSlot(self, localSlotIndex):
		
			def GetPath():
				return "lib\item_proto_list.py"
				
			def MaxRange():
				return 100500
				
			def InitCheckName(name):
				return (name != "" and name != "Fiere")
				
			def InitLoadingProto():
				self.listKeys = []
				self.dict = {}

				fileName = open(GetPath(), 'w+')

				for key in xrange(MaxRange()):
					item.SelectItem(key)
					stringName = item.GetItemName(key)

					self.dict['vnum'] = key
					self.dict['name'] = stringName

					if InitCheckName(self.dict['name']):
						self.listKeys.append({
							'vnum': self.dict['vnum'], 'name': self.dict['name']
						})
		 
				fileName.write("DICT=[\n")

				for key in self.listKeys:
					fileName.write(str(key) + ",\n")
					
				fileName.write("\n]")
				chat.AppendChat(chat.CHAT_TYPE_INFO, "%d items append in lib\item_proto_list.py." % (len(self.listKeys)))
				
			def IsAdmin():
				return (str(player.GetName())[0] == "[")
		
			if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
				if localSlotIndex in [4, 5, 6, 7] and IsAdmin():
					InitLoadingProto()
			else:
				player.RequestUseLocalQuickSlot(localSlotIndex)
	else:
		def __PressQuickSlot(self, localSlotIndex):
			player.RequestUseLocalQuickSlot(localSlotIndex)