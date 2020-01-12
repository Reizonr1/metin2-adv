?mportlar©¥n aras©¥na alttakileri ekleyin.

import uiOfflineShop
import uiOfflineShopBuilder


Alttaki kodu arat ;

		self.wndMiniMap = None
		self.wndGuild = None
		self.wndGuildBuilding = None

Ustteki kodun alt©¥na alttaki kodlar©¥ ekle ;

		# OFFLINE_SHOP
		self.wndOfflineShopAdminPanel = None
		# END_OF_OFFLINE_SHOP

Alttaki kodu arat ;

		wndChatLog = uiChat.ChatLogWindow()
		wndChatLog.BindInterface(self)

Ustteki kodun alt©¥na alttaki kodlar©¥ ekle ;

		# OFFLINE_SHOP_ADMIN_PANEL
		wndOfflineShopAdminPanel = uiOfflineShop.OfflineShopAdminPanelWindow()
		wndOfflineShopAdminPanel.BindInterfaceClass(self)
		self.wndOfflineShopAdminPanel = wndOfflineShopAdminPanel
		# END_OF_OFFLINE_SHOP_ADMIN_PANEL

Alttaki kodu arat ;

	def __MakeDialogs(self):
		self.dlgExchange = uiExchange.ExchangeDialog()
		self.dlgExchange.LoadDialog()
		self.dlgExchange.SetCenterPosition()
		self.dlgExchange.Hide()

		self.dlgPointReset = uiPointReset.PointResetDialog()
		self.dlgPointReset.LoadDialog()
		self.dlgPointReset.Hide()

		self.dlgShop = uiShop.ShopDialog()
		self.dlgShop.LoadDialog()
		self.dlgShop.Hide()

Ustteki kodun alt©¥na alttaki kodlar©¥ ekle ;

		self.dlgOfflineShop = uiOfflineShop.OfflineShopDialog()
		self.dlgOfflineShop.LoadDialog()
		self.dlgOfflineShop.Hide()

		self.offlineShopBuilder = uiOfflineShopBuilder.OfflineShopBuilder()
		self.offlineShopBuilder.Hide()

Alttaki kodu arat ;

		self.privateShopBuilder.SetItemToolTip(self.tooltipItem)

Ustteki kodun alt©¥na alttaki kodlar©¥ ekle ;

		self.dlgOfflineShop.SetItemToolTip(self.tooltipItem)
		self.offlineShopBuilder.SetItemToolTip(self.tooltipItem)

Alttaki kodu arat ;

		# ACCESSORY_REFINE_ADD_METIN_STONE
		if self.wndItemSelect:
			self.wndItemSelect.Destroy()
		# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE

Ustteki kodun alt©¥na alttaki kodlar©¥ ekle ;

		if (self.dlgOfflineShop):
			self.dlgOfflineShop.Destroy()
			
		if (self.offlineShopBuilder):
			self.offlineShopBuilder.Destroy()
			
		# OFFLINE_SHOP_ADMIN_PANEL
		if (self.wndOfflineShopAdminPanel):
			self.wndOfflineShopAdminPanel.Destroy()
		# END_OF_OFFLINE_SHOP_ADMIN_PANEL

Alttaki kodu arat ;

		del self.tipBoard
		del self.bigBoard
		del self.wndItemSelect

Ustteki kodun alt©¥na alttaki kodlar©¥ ekle ;

		del self.dlgOfflineShop
		del self.wndOfflineShopAdminPanel

Alttaki kodu arat ;

		self.privateShopAdvertisementBoardDict = {}
		self.guildScoreBoardDict = {}
		self.equipmentDialogDict = {}

Ustteki kodun alt©¥na alttaki kodlar©¥ ekle ;

		self.offlineShopAdvertisementBoardDict = {}

Alttaki kodu arat ;

	def CloseShopDialog(self):
		self.dlgShop.Close()

	def RefreshShopDialog(self):
		self.dlgShop.Refresh()

Ustteki kodun alt©¥na alttaki kodlar©¥ ekle ;

	# OfflineShop
	def OpenOfflineShopDialog(self, vid):
		self.wndInventory.Show()
		self.wndInventory.SetTop()
		self.dlgOfflineShop.Open(vid)
		self.dlgOfflineShop.SetTop()
		
	def CloseOfflineShopDialog(self):	
		self.dlgOfflineShop.Close()
		
	def RefreshOfflineShopDialog(self):
		self.dlgOfflineShop.Refresh()

Alttaki kodu arat ;

	def CloseDragonSoulRefineWindow(self):
		if False == player.IsObserverMode():
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				if True == self.wndDragonSoulRefine.IsShow():
					self.wndDragonSoulRefine.Close()

Ustteki kodun alt©¥na alttaki kodlar©¥ ekle ;

	# Offline Shop Admin Panel
	def ToggleOfflineShopAdminPanelWindow(self):
		if (self.wndOfflineShopAdminPanel.IsShow() == True):
			self.wndOfflineShopAdminPanel.Close()
		else:
			self.wndOfflineShopAdminPanel.Show()

Alttaki kodu arat ;

	def DisappearPrivateShop(self, vid):

		if not self.privateShopAdvertisementBoardDict.has_key(vid):
			return

		del self.privateShopAdvertisementBoardDict[vid]
		uiPrivateShopBuilder.DeleteADBoard(vid)

Ustteki kodun alt©¥na alttaki kodlar©¥ ekle ;

	def OpenOfflineShopInputNameDialog(self):
		inputDialog = uiOfflineShop.OfflineShopInputDialog()
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OpenOfflineShopBuilder))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.CloseOfflineShopInputNameDialog))
		inputDialog.Open()
		self.inputDialog = inputDialog
		
	def CloseOfflineShopInputNameDialog(self):
		self.inputDialog = None
		return True
	
	def OpenOfflineShopBuilder(self):
		if (not self.inputDialog):
			return True
			
		if (not len(self.inputDialog.GetTitle())):
			return True
			
		if (self.inputDialog.GetTime() < 0 or self.inputDialog.GetTime() == 0):
			return True
			
		self.offlineShopBuilder.Open(self.inputDialog.GetTitle(), self.inputDialog.GetTime())
		self.CloseOfflineShopInputNameDialog()
		return True
	
	def AppearOfflineShop(self, vid, text):
		board = uiOfflineShopBuilder.OfflineShopAdvertisementBoard()
		board.Open(vid, text)
		
		self.offlineShopAdvertisementBoardDict[vid] = board
		
	def DisappearOfflineShop(self, vid):
		if (not self.offlineShopAdvertisementBoardDict.has_key(vid)):
			return
			
		del self.offlineShopAdvertisementBoardDict[vid]
		uiOfflineShopBuilder.DeleteADBoard(vid)

