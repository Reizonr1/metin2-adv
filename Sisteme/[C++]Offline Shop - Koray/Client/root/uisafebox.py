Search:
	def OnCloseMessageDialog(self):
		self.newPassword.SetText("")
		self.newPasswordCheck.SetText("")
		self.newPassword.SetFocus()
		self.dlgMessage.Hide()

Add it under:

if app.ENABLE_OFFLINE_SHOP:
	class OfflineShopListItem(ui.ListBoxEx.Item):
		def __init__(self, idx, text, vidOfShop, mapIndex, posX, posY):
			ui.ListBoxEx.Item.__init__(self)
			
			self.idx = idx
			self.vidOfShop = vidOfShop
			self.mapIndex = mapIndex
			self.posX = posX
			self.posY = posY
			self.text = text
	
			self.mapNameOld = str(background.GetMapName(long(self.posX), long(self.posY)))
			self.mapName = self.realMapName(self.mapNameOld)
	
			self.textLine = self.__CreateTextLine("%s" % (str(text)[:50]), (2, 5))
			self.textLineMap = self.__CreateTextLine("%s" % self.mapName, (150, 5))
			self.gotoShop = self.__CreateButton((280, 1), "Go", self.gotoShopFunc)
			self.warpShop = self.__CreateButton((340, 1), "Warp", self.warpShopFunc)
			self.closeShop = self.__CreateButton((400, 1), "Close", self.closeShopFunc)
			
		def __del__(self):
			self.idx = None
			self.vidOfShop = None
			self.mapIndex = None
			self.posX = None
			self.posY = None
			self.text = None
	
			if self.textLine and self.textLine.IsShow():
				self.textLine.Hide()
				self.textLine = None
			if self.gotoShop and self.gotoShop.IsShow():
				self.gotoShop.Hide()
				self.gotoShop = None
			if self.warpShop and self.warpShop.IsShow():
				self.warpShop.Hide()
				self.warpShop = None
			if self.closeShop and self.closeShop.IsShow():
				self.closeShop.Hide()
				self.closeShop = None
	
			ui.ListBoxEx.Item.__del__(self)
	
		def realMapName(self, oldName):
			mapNames = {"metin2_map_trent02": "Kizil Orman", "metin2_map_trent": "Orman", "metin2_map_WL_01": "Yilan Vadisi",
						 "metin2_map_nusluck01": "Devler Diyari", "metin2_map_devilscatacomb": "Seytan Katakombu", "metin2_map_duel": "VS Arenasi",
						 "metin2_map_a1": "Yongan Bolgesi(Shinsoo)", "metin2_map_b1 ": "Joan Bolgesi(Chunjo)", "metin2_map_c1": "Pyungmoo Bolgesi(Jinno)",
						 "metin2_map_a3": "Jayang Bolgesi(Shinsoo)", "metin2_map_b3 ": "Bokjung Bolgesi(Chunjo)", "metin2_map_c3": "Bakra Bolgesi(Jinno)",
						 "map_a2": "Seungryong Vadisi", "map_n_snowm_01 ": "Sohan Dagi", "metin2_map_n_desert_01": "Yongbi Colu",
						 "metin2_map_deviltower1": "Åeytan Kulesi", "metin2_map_guild_01 ": "Jungrang(Lonca BÃ¶lgesi)", "metin2_map_guild_02": "Waryong(Lonca BÃ¶lgesi)",
						 "metin2_map_guild_03": "Imha(Lonca BÃ¶lgesi)", "metin2_guild_village_01 ": "Miryan(Lonca SavaÅŸÄ±)", "metin2_guild_village_02": "Songpa(Lonca SavaÅŸÄ±)",
						 "metin2_guild_village_03": "Daeyami(Lonca SavaÅŸÄ±)", "metin2_map_milgyo ": "Hwang TapÄ±naÄŸÄ±", "metin2_map_monkeydungeon": "Maymun ZindanÄ±(Kolay)",
						 "metin2_map_monkeydungeon_02": "Maymun ZindanÄ±(Normal)", "metin2_map_monkeydungeon_03 ": "Maymun ZindanÄ±(Uzman)", "metin2_map_n_flame_01": "AteÅŸ DiyarÄ±",
						 "metin2_map_spiderdungeon": "Ã–rÃ¼mcek ZindanÄ± 1.Kat", "metin2_map_spiderdungeon_02 ": "Ã–rÃ¼mcek ZindanÄ± 2.Kat", "metin2_map_spiderdungeon_03": "Ã–rÃ¼mcek ZindanÄ± 3.Kat",
						 "metin2_map_skipia_dungeon_01": "SÃ¼rgÃ¼n MaÄŸarasÄ± 1.Kat", "metin2_map_skipia_dungeon_02 ": "SÃ¼rgÃ¼n MaÄŸarasÄ± 2.Kat"
			}
			if oldName in mapNames:
				return mapNames[oldName]
			return oldName
	
		def gotoShopFunc(self):
			net.SendChatPacket("/offlineshop_goto %s" % str(self.vidOfShop))
	
		def warpShopFunc(self):
			net.SendChatPacket("/offlineshop_warp %s" % str(self.vidOfShop))
	
		def closeShopFunc(self):
			net.SendChatPacket("/offlineshop_close %s" % str(self.vidOfShop))
		
	
		def SetSize(self, width, height):
			ui.ListBoxEx.Item.SetSize(self, 460, height + 7)
			
		def __CreateTextLine(self, text, pos):
			textLine=ui.TextLine()
			textLine.SetParent(self)
			textLine.SetPosition(pos[0], pos[1])
			textLine.SetText(text)
			textLine.Show()
			return textLine
			
		def __CreateButton(self, pos, buttonName, func):
			tmpButton = ui.Button()
			tmpButton.SetParent(self)
			tmpButton.SetPosition(pos[0], pos[1])
			
			tmpButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
			tmpButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
			tmpButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
	
			tmpButton.SetText(buttonName)
			tmpButton.SetEvent(func)
			tmpButton.Show()
			
			return tmpButton
	
	class OfflineShopUI(ui.BoardWithTitleBar):
		def __init__(self):
			ui.BoardWithTitleBar.__init__(self)
			self.LastIdx = 0
			self.BuildUI()
	
		def __del__(self):
			ui.BoardWithTitleBar.__del__(self)
	
		def BuildUI(self):
			posX = 500
			self.AddFlag('movable')
			self.AddFlag('float')
			self.SetSize(posX, 150)
			self.SetTitleName("Offline Shop Panel")
			self.SetCloseEvent(self.OpenWindow)
			self.SetCenterPosition()
			self.Show()
	
			self.bar = ui.Bar()
			self.bar.SetParent(self)
			self.bar.SetPosition(10, 35)
			self.bar.SetSize(posX - 20, 100)
			self.bar.SetColor(0x77000000)
			self.bar.Show()
	
			self.ListBox = ui.ListBoxEx()
			self.ListBox.SetParent(self.bar)
			self.ListBox.SetPosition(0, 0)
			self.ListBox.SetSize(posX, 100)
			self.ListBox.SetViewItemCount(5)
			self.ListBox.Show()
	
			self.scroll = ui.ScrollBar()
			self.scroll.SetParent(self.ListBox)
			self.scroll.SetPosition(posX-35, 0)
			self.scroll.SetScrollBarSize(200/2)
			self.scroll.Show()
			self.ListBox.SetScrollBar(self.scroll)
	
			self.refresh = ui.Button()
			self.refresh.SetParent(self)
			self.refresh.SetPosition(self.GetWidth() - 50, 8)
			self.refresh.SetUpVisual("d:/ymir work/ui/game/guild/Refresh_Button_01.sub")
			self.refresh.SetOverVisual("d:/ymir work/ui/game/guild/Refresh_Button_02.sub")
			self.refresh.SetDownVisual("d:/ymir work/ui/game/guild/Refresh_Button_03.sub")
			self.refresh.SetText("")
			self.refresh.SetEvent(self.Refresh)
			self.refresh.Show()
	
		def AppendOfflineShop(self, name, vid, mapIdx, x, y):
			if not self.IsShowWindow():
				self.LastIdx = 0
				self.ListBox.RemoveAllItems()
				self.ShowWindow()
	
			self.LastIdx += 1
			self.ListBox.AppendItem(OfflineShopListItem(self.LastIdx, name, vid, mapIdx, x, y))
			
		def Refresh(self):
			self.Close()
			net.SendChatPacket("/do_myshops")
	
		def IsShowWindow(self):
			return self.IsShow()
	
		def OpenWindow(self):
			if self.IsShow():
				self.Hide()
			else:
				self.Show()
	
		def ShowWindow(self):
			self.Show()
	
		def Close(self):
			self.Hide()
			return True
	
		def OnPressEscapeKey(self):
			self.Close()
			return True


https://puu.sh/sgU1v/a37fbbddf5.png
https://puu.sh/sgU1W/39868a3ff7.png

---

Search:
		self.GetChild("ExitButton").SetEvent(ui.__mem_func__(self.Close))

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			self.GetChild("CollectButton").SetEvent(ui.__mem_func__(self.OnCollect))
			self.GetChild("MyShopsButton").SetEvent(ui.__mem_func__(self.MyShops))

https://puu.sh/sgU4s/f56083455a.png

---

Search:
		#self.wndMoney = self.GetChild("Money")
		#self.wndMoneySlot = self.GetChild("Money_Slot")
		#self.wndMoneySlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog))

Change:
		if app.ENABLE_OFFLINE_SHOP:
			self.wndMoney = self.GetChild("Money")
			self.wndMoneySlot = self.GetChild("MoneySlot")
			self.wndMoneySlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog))

https://puu.sh/sgU6R/87a7e6d7a2.png

---

Search:
			self.dlgPickMoney.Open(curMoney)

Add it under:
			if app.ENABLE_OFFLINE_SHOP:
				self.dlgPickMoney.SetMax(11)

https://puu.sh/sgUa5/82a5420e58.png

---

Search:
			button.SetPosition(pos, 85)
			button.SetText(text)
			button.SetEvent(lambda arg=i: self.SelectPage(arg))
			button.Show()
			self.pageButtonList.append(button)

Change:
			if app.ENABLE_OFFLINE_SHOP:
				button.SetPosition(pos, 100)
			else:
				button.SetPosition(pos, 85)
			button.SetText(text)
			button.SetEvent(lambda arg=i: self.SelectPage(arg))
			button.Show()
			self.pageButtonList.append(button)

https://puu.sh/sgUc8/f63968744b.png
---

Search:
		self.wndBoard.SetSize(self.BOX_WIDTH, wnd_height)
		self.SetSize(self.BOX_WIDTH, wnd_height)
		self.UpdateRect()

Change:
		if not app.ENABLE_OFFLINE_SHOP:
			self.wndBoard.SetSize(self.BOX_WIDTH, wnd_height)
			self.SetSize(self.BOX_WIDTH, wnd_height)
			self.UpdateRect()

https://puu.sh/sgUdp/3e9db54313.png
---

Search:
	def RefreshSafeboxMoney(self):
		pass
		#self.wndMoney.SetText(str(safebox.GetMoney()))

Change:
	def RefreshSafeboxMoney(self):
		if app.ENABLE_OFFLINE_SHOP:
			self.wndMoney.SetText(localeInfo.NumberToMoneyString(safebox.GetMoney()))

https://puu.sh/sgUeX/0ca61c937a.png

---

Search:
	def SelectEmptySlot(self, selectedSlotPos):

		selectedSlotPos = self.__LocalPosToGlobalPos(selectedSlotPos)

		if mouseModule.mouseController.isAttached():

			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()

			if player.SLOT_TYPE_SAFEBOX == attachedSlotType:

				net.SendSafeboxItemMovePacket(attachedSlotPos, selectedSlotPos, 0)
				#snd.PlaySound("sound/ui/drop.wav")
			else:
				attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
				if player.RESERVED_WINDOW == attachedInvenType:
					return

				if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
					net.SendSafeboxSaveMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")

				else:
					net.SendSafeboxCheckinPacket(attachedInvenType, attachedSlotPos, selectedSlotPos)
					#snd.PlaySound("sound/ui/drop.wav")

			mouseModule.mouseController.DeattachObject()

Change:
	def SelectEmptySlot(self, selectedSlotPos):

		selectedSlotPos = self.__LocalPosToGlobalPos(selectedSlotPos)

		if mouseModule.mouseController.isAttached():

			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			
			if app.ENABLE_OFFLINE_SHOP:
				if player.SLOT_TYPE_INVENTORY == attachedSlotType:
					if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
						net.SendSafeboxSaveMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
						snd.PlaySound("sound/ui/money.wav")
	
					else:
						net.SendSafeboxCheckinPacket(attachedSlotPos, selectedSlotPos)
						#snd.PlaySound("sound/ui/drop.wav")
						
				elif player.SLOT_TYPE_SAFEBOX == attachedSlotType:
	
					net.SendSafeboxItemMovePacket(attachedSlotPos, selectedSlotPos, 0)
					#snd.PlaySound("sound/ui/drop.wav")
			else:
				if player.SLOT_TYPE_SAFEBOX == attachedSlotType:
	
					net.SendSafeboxItemMovePacket(attachedSlotPos, selectedSlotPos, 0)
					#snd.PlaySound("sound/ui/drop.wav")
				else:
					attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
					if player.RESERVED_WINDOW == attachedInvenType:
						return
	
					if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
						net.SendSafeboxSaveMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
						snd.PlaySound("sound/ui/money.wav")
	
					else:
						net.SendSafeboxCheckinPacket(attachedInvenType, attachedSlotPos, selectedSlotPos)
						#snd.PlaySound("sound/ui/drop.wav")

			mouseModule.mouseController.DeattachObject()


https://puu.sh/sgUh5/29d137892b.png
https://puu.sh/sgUhI/0cc8a1cccb.png

--

Search:
	def OnChangePassword(self):
		self.dlgChangePassword.Open()

Add it under:
	if app.ENABLE_OFFLINE_SHOP:
		def OnCollect(self):
			net.SendChatPacket("/do_gather")
	
		def MyShops(self):
			net.SendChatPacket("/do_myshops")
	
https://puu.sh/sgUjE/aa5e3e8717.png

---

Search:
		self.wndBoard.SetSize(self.BOX_WIDTH, 82 + 32*size)
		self.SetSize(self.BOX_WIDTH, 85 + 32*size)
		self.UpdateRect()

Add it under:
		if not app.ENABLE_OFFLINE_SHOP:
			self.wndBoard.SetSize(self.BOX_WIDTH, 82 + 32*size)
			self.SetSize(self.BOX_WIDTH, 85 + 32*size)
			self.UpdateRect()


https://puu.sh/sgUli/9498d75669.png













