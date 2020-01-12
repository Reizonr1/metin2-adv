Search:
	def RemoveAllItems(self):
		self.selItem=None
		self.itemList=[]

		if self.scrollBar:
			self.scrollBar.SetPos(0)

Change:
	def RemoveAllItems(self):
		for i in self.itemList:
			if i.IsShow():
				i.Hide()
		self.selItem=None
		del self.itemList[:]
		self.itemList=[]

		if self.scrollBar:
			self.scrollBar.SetPos(0)

https://puu.sh/sgXUi/bb04ee9b66.png


Search:
	def SetCoverButton(self,\
						slotIndex,\
						upName="d:/ymir work/ui/public/slot_cover_button_01.sub",\
						overName="d:/ymir work/ui/public/slot_cover_button_02.sub",\
						downName="d:/ymir work/ui/public/slot_cover_button_03.sub",\
						disableName="d:/ymir work/ui/public/slot_cover_button_04.sub",\
						LeftButtonEnable = False,\
						RightButtonEnable = True):
		wndMgr.SetCoverButton(self.hWnd, slotIndex, upName, overName, downName, disableName, LeftButtonEnable, RightButtonEnable)
	
Add it under:
	if app.ENABLE_OFFLINE_SHOP:
		def DeleteCoverButton(self, slotIndex):
			wndMgr.DeleteCoverButton(self.hWnd, slotIndex)

		def HasCoverButton(self, slotIndex):
			return wndMgr.HasCoverButton(self.hWnd, slotIndex)


https://puu.sh/sgXLv/b497376af5.png
