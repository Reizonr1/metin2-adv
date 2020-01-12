#Adauga
import uibosstracking

#Cauta
		self.playerGauge = uiPlayerGauge.PlayerGauge(self)
		self.playerGauge.Hide()

#Adauga
		self.bosstracking = uibosstracking.BossTrackingSystemWindow()
		self.bosstracking.Hide()

#Cauta
		if self.console:
			self.console.BindGameClass(0)
			self.console.Close()
			self.console=None

#Adauga
		if self.bosstracking:
			self.bosstracking.Destroy()
			self.bosstracking = None

# Adauga mai jos
	def BossTracking(self):
		import constInfo
		constInfo.BOSS_TRACKING = 1

	def GetBossTrackingInformation(self, btcadi1, btcadi2, btcadi3, btcadi4, btcadi5, btcadi6, btalevkral1, btalevkral2, btalevkral3, btalevkral4, btalevkral5, btalevkral6, btkorumcek1, btkorumcek2, btkorumcek3, btkorumcek4, btkorumcek5, btkorumcek6, btsarikaplan1, btsarikaplan2, btsarikaplan3, btsarikaplan4, btsarikaplan5, btsarikaplan6, btbuzkralice1, btbuzkralice2, btbuzkralice3, btbuzkralice4, btbuzkralice5, btbuzkralice6, btdokuzk1, btdokuzk2, btdokuzk3, btdokuzk4, btdokuzk5, btdokuzk6, btcolejder1, btcolejder2, btcolejder3, btcolejder4, btcolejder5, btcolejder6, btagac1, btagac2, btagac3, btagac4, btagac5, btagac6, btkomutan1, btkomutan2, btkomutan3, btkomutan4, btkomutan5, btkomutan6, btkaranlik1, btkaranlik2, btkaranlik3, btkaranlik4, btkaranlik5, btkaranlik6):
		self.bosstracking.GetMobInformation(btcadi1, btcadi2, btcadi3, btcadi4, btcadi5, btcadi6, btalevkral1, btalevkral2, btalevkral3, btalevkral4, btalevkral5, btalevkral6, btkorumcek1, btkorumcek2, btkorumcek3, btkorumcek4, btkorumcek5, btkorumcek6, btsarikaplan1, btsarikaplan2, btsarikaplan3, btsarikaplan4, btsarikaplan5, btsarikaplan6, btbuzkralice1, btbuzkralice2, btbuzkralice3, btbuzkralice4, btbuzkralice5, btbuzkralice6, btdokuzk1, btdokuzk2, btdokuzk3, btdokuzk4, btdokuzk5, btdokuzk6, btcolejder1, btcolejder2, btcolejder3, btcolejder4, btcolejder5, btcolejder6, btagac1, btagac2, btagac3, btagac4, btagac5, btagac6, btkomutan1, btkomutan2, btkomutan3, btkomutan4, btkomutan5, btkomutan6, btkaranlik1, btkaranlik2, btkaranlik3, btkaranlik4, btkaranlik5, btkaranlik6)

	def BossTrackingUpdate(self):
		net.SendChatPacket("/bosstrackingtest")

	def BossTrackingSystemShow(self):
		self.bosstracking.Show()
		net.SendChatPacket("/bosstrackingtest")

#Cauta
		onPressKeyDict[app.DIK_F4]	= lambda : self.__PressQuickSlot(7)

#Adauga
		onPressKeyDict[app.DIK_F6]	= lambda : self.BossTracking()

#Cauta
		if self.isShowDebugInfo:
			self.UpdateDebugInfo()

		if self.enableXMasBoom:
			self.__XMasBoom_Update()

#Adauga
		if 1== constInfo.BOSS_TRACKING:
			constInfo.BOSS_TRACKING = 0
			self.BossTrackingSystemShow()

#Cauta
			"WarUC"					: self.__GuildWar_UpdateMemberCount,
			"test_server"			: self.__EnableTestServerFlag,
			"mall"			: self.__InGameShop_Show,

#Adauga
			"BossTracking"		: self.GetBossTrackingInformation,
			"BossTrackingUpdatePacket" : self.BossTrackingUpdate,