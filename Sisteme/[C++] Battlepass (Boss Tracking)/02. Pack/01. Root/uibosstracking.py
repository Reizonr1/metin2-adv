import net, item, wndMgr, uiCommon, ime, app, ui, time, chat, playerSettingModule, localeInfo, player, chr, snd, mouseModule, constInfo, uiScriptLocale, interfacemodule, event, dbg, chrmgr

def FormatTimeBevis(time):
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60) % 24
	return "%02d Saat %02d Dakika" % (hour, minute)

class BossTrackingSystemWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.Initialize()
		self.LoadWindow()

	def Initialize(self):
		self.updatetimer = 0
		self.newbtcadi1 = 0
		self.newbtcadi2 = 0
		self.newbtcadi3 = 0
		self.newbtcadi4 = 0
		self.newbtcadi5 = 0
		self.newbtcadi6 = 0

		self.newbtalevkral1 = 0
		self.newbtalevkral2 = 0
		self.newbtalevkral3 = 0
		self.newbtalevkral4 = 0
		self.newbtalevkral5 = 0
		self.newbtalevkral6 = 0

		self.newbtkorumcek1 = 0
		self.newbtkorumcek2 = 0
		self.newbtkorumcek3 = 0
		self.newbtkorumcek4 = 0
		self.newbtkorumcek5 = 0
		self.newbtkorumcek6 = 0

		self.newbtsarikaplan1 = 0
		self.newbtsarikaplan2 = 0
		self.newbtsarikaplan3 = 0
		self.newbtsarikaplan4 = 0
		self.newbtsarikaplan5 = 0
		self.newbtsarikaplan6 = 0

		self.newbtbuzkralice1 = 0
		self.newbtbuzkralice2 = 0
		self.newbtbuzkralice3 = 0
		self.newbtbuzkralice4 = 0
		self.newbtbuzkralice5 = 0
		self.newbtbuzkralice6 = 0

		self.newbtdokuzk1 = 0
		self.newbtdokuzk2 = 0
		self.newbtdokuzk3 = 0
		self.newbtdokuzk4 = 0
		self.newbtdokuzk5 = 0
		self.newbtdokuzk6 = 0

		self.newbtcolejder1 = 0
		self.newbtcolejder2 = 0
		self.newbtcolejder3 = 0
		self.newbtcolejder4 = 0
		self.newbtcolejder5 = 0
		self.newbtcolejder6 = 0

		self.newbtagac1 = 0
		self.newbtagac2 = 0
		self.newbtagac3 = 0
		self.newbtagac4 = 0
		self.newbtagac5 = 0
		self.newbtagac6 = 0

		self.newbtkomutan1 = 0
		self.newbtkomutan2 = 0
		self.newbtkomutan3 = 0
		self.newbtkomutan4 = 0
		self.newbtkomutan5 = 0
		self.newbtkomutan6 = 0

		self.newbtkaranlik1 = 0
		self.newbtkaranlik2 = 0
		self.newbtkaranlik3 = 0
		self.newbtkaranlik4 = 0
		self.newbtkaranlik5 = 0
		self.newbtkaranlik6 = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/bosstracking.py")
		except:
			import exception
			exception.Abort("BossTrackingSystemWindow.LoadWindow.LoadObject")
		try:
			self.titleBar = self.GetChild("titlebar")
			self.board = self.GetChild("board")
			self.title_name = self.GetChild("title_name")
			self.title_name_2 = self.GetChild("title_name_2")
			self.title_name_3 = self.GetChild("title_name_3")
			self.title_name_4 = self.GetChild("title_name_4")
			self.title_name_5 = self.GetChild("title_name_5")

			self.Channel1Time = self.GetChild("CH1Time")
			self.Channel2Time = self.GetChild("CH2Time")
			self.Channel3Time = self.GetChild("CH3Time")
			self.Channel4Time = self.GetChild("CH4Time")
			self.Channel5Time = self.GetChild("CH5Time")
			self.Channel6Time = self.GetChild("CH6Time")
			self.GetChild("btnMenuCadi").SAFE_SetEvent(self.__MenuFunction, 1)
			self.GetChild("btnMenuAlevKral").SAFE_SetEvent(self.__MenuFunction, 2)
			self.GetChild("btnMenuKOrumcek").SAFE_SetEvent(self.__MenuFunction, 3)
			self.GetChild("btnMenuKEjder").SAFE_SetEvent(self.__MenuFunction, 4)
			self.GetChild("btnMenuDokuzKuyruk").SAFE_SetEvent(self.__MenuFunction, 5)
			self.GetChild("btnMenuGeneral").SAFE_SetEvent(self.__MenuFunction, 6)
			self.GetChild("btnMenuOrumcekBarones").SAFE_SetEvent(self.__MenuFunction, 7)
			self.GetChild("btnMenuHayaletAgac").SAFE_SetEvent(self.__MenuFunction, 8)
			self.GetChild("btnMenuKomutan").SAFE_SetEvent(self.__MenuFunction, 9)
			self.GetChild("btnMenuKaranlikLider").SAFE_SetEvent(self.__MenuFunction, 10)
		except:
			import exception
			exception.Abort("BossTrackingSystemWindow.LoadWindow.BindObject")
			
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		
		self.title_name.SetText("Güçlü Buz Cadýsý")
		self.title_name_2.SetText("Seviye : 89")
		self.title_name_3.SetText("Bölge : Sürgün Maðarasý")
		self.title_name_4.SetText("Etkili Týlsým : Buz Týlsýmý")
		self.title_name_5.SetText("Yeniden Çýkýþ Süresi : 4saat")
		self.BossTrackingImage = ui.ExpandedImageBox()
		self.BossTrackingImage.SetParent(self.board)
		self.BossTrackingImage.LoadImage("d:/ymir work/patrontakip/slot_1.tga")
		self.BossTrackingImage.SetPosition(265-49, 95+194)
		self.BossTrackingImage.Show()
		constInfo.bosstracking = 1

	def __MenuFunction(self, value):
		if value == 1:
			self.title_name.SetText("Güçlü Buz Cadýsý")
			self.title_name_2.SetText("Seviye : 89")
			self.title_name_3.SetText("Bölge : Sürgün Maðarasý")
			self.title_name_4.SetText("Etkili Týlsým : Buz Týlsýmý")
			self.title_name_5.SetText("Yeniden Çýkýþ Süresi : 4saat")
			self.BossTrackingImage = ui.ExpandedImageBox()
			self.BossTrackingImage.SetParent(self.board)
			self.BossTrackingImage.LoadImage("d:/ymir work/patrontakip/slot_1.tga")
			self.BossTrackingImage.SetPosition(265-49, 95+194)
			self.BossTrackingImage.Show()
			constInfo.bosstracking = 1
		elif value == 2:
			self.title_name.SetText("Alev Kral")
			self.title_name_2.SetText("Seviye : 73")
			self.title_name_3.SetText("Bölge : Doyyumhwan")
			self.title_name_4.SetText("Etkili Týlsým : Ateþ Týlsýmý")
			self.title_name_5.SetText("Yeniden Çýkýþ Süresi : 2saat")
			self.BossTrackingImage = ui.ExpandedImageBox()
			self.BossTrackingImage.SetParent(self.board)
			self.BossTrackingImage.LoadImage("d:/ymir work/patrontakip/slot_2.tga")
			self.BossTrackingImage.SetPosition(265-49, 95+194)
			self.BossTrackingImage.Show()
			constInfo.bosstracking = 2
		elif value == 3:
			self.title_name.SetText("Kraliçe Örümcek")
			self.title_name_2.SetText("Seviye : 60")
			self.title_name_3.SetText("Bölge : Örümcek Zindaný")
			self.title_name_4.SetText("Etkili Týlsým : Rüzgar Týlsýmý")
			self.title_name_5.SetText("Yeniden Çýkýþ Süresi : 2saat")
			self.BossTrackingImage = ui.ExpandedImageBox()
			self.BossTrackingImage.SetParent(self.board)
			self.BossTrackingImage.LoadImage("d:/ymir work/patrontakip/slot_3.tga")
			self.BossTrackingImage.SetPosition(265-49, 95+194)
			self.BossTrackingImage.Show()
			constInfo.bosstracking = 3
		elif value == 4:
			self.title_name.SetText("Sarý Kaplan Hayaleti")
			self.title_name_2.SetText("Seviye : 75")
			self.title_name_3.SetText("Bölge : Hwang Tapýnaðý")
			self.title_name_4.SetText("Etkili Týlsým : Rüzgar Týlsýmý")
			self.title_name_5.SetText("Yeniden Çýkýþ Süresi : 2saat")
			self.BossTrackingImage = ui.ExpandedImageBox()
			self.BossTrackingImage.SetParent(self.board)
			self.BossTrackingImage.LoadImage("d:/ymir work/patrontakip/slot_4.tga")
			self.BossTrackingImage.SetPosition(265-49, 95+194)
			self.BossTrackingImage.Show()
			constInfo.bosstracking = 4
		elif value == 5:
			self.title_name.SetText("Ork Reisi")
			self.title_name_2.SetText("Seviye : 50")
			self.title_name_3.SetText("Bölge : Seungryong Vadisi")
			self.title_name_4.SetText("Etkili Týlsým : Bilinmiyor")
			self.title_name_5.SetText("Yeniden Çýkýþ Süresi : 20dakika")
			self.BossTrackingImage = ui.ExpandedImageBox()
			self.BossTrackingImage.SetParent(self.board)
			self.BossTrackingImage.LoadImage("d:/ymir work/patrontakip/slot_5.tga")
			self.BossTrackingImage.SetPosition(265-49, 95+194)
			self.BossTrackingImage.Show()
			constInfo.bosstracking = 5
		elif value == 6:
			self.title_name.SetText("Dokuz Kuyruk")
			self.title_name_2.SetText("Seviye : 67")
			self.title_name_3.SetText("Bölge : Sohan Daðý")
			self.title_name_4.SetText("Etkili Týlsým : Buz Týlsýmý")
			self.title_name_5.SetText("Yeniden Çýkýþ Süresi : 30dakika")
			self.BossTrackingImage = ui.ExpandedImageBox()
			self.BossTrackingImage.SetParent(self.board)
			self.BossTrackingImage.LoadImage("d:/ymir work/patrontakip/slot_6.tga")
			self.BossTrackingImage.SetPosition(265-49, 95+194)
			self.BossTrackingImage.Show()
			constInfo.bosstracking = 6
		elif value == 7:
			self.title_name.SetText("Dev Çöl Kaplumbaðasý")
			self.title_name_2.SetText("Seviye : 67")
			self.title_name_3.SetText("Bölge : Yongbi Çölü")
			self.title_name_4.SetText("Etkili Týlsým : Rüzgar Týlsýmý")
			self.title_name_5.SetText("Yeniden Çýkýþ Süresi : 20dakika")
			self.BossTrackingImage = ui.ExpandedImageBox()
			self.BossTrackingImage.SetParent(self.board)
			self.BossTrackingImage.LoadImage("d:/ymir work/patrontakip/slot_7.tga")
			self.BossTrackingImage.SetPosition(265-49, 95+194)
			self.BossTrackingImage.Show()
			constInfo.bosstracking = 7
		elif value == 8:
			self.title_name.SetText("Dev Hayalet Aðaç")
			self.title_name_2.SetText("Seviye : 86")
			self.title_name_3.SetText("Bölge : Kýzýl Orman")
			self.title_name_4.SetText("Etkili Týlsým : Toprak Týlsýmý")
			self.title_name_5.SetText("Yeniden Çýkýþ Süresi : 2,5saat")
			self.BossTrackingImage = ui.ExpandedImageBox()
			self.BossTrackingImage.SetParent(self.board)
			self.BossTrackingImage.LoadImage("d:/ymir work/patrontakip/slot_8.tga")
			self.BossTrackingImage.SetPosition(265-49, 95+194)
			self.BossTrackingImage.Show()
			constInfo.bosstracking = 8
		elif value == 9:
			self.title_name.SetText("Komutan")
			self.title_name_2.SetText("Seviye : 95")
			self.title_name_3.SetText("Bölge : Sürgün Maðarasý")
			self.title_name_4.SetText("Etkili Týlsým : Þimþek Týlsýmý")
			self.title_name_5.SetText("Yeniden Çýkýþ Süresi : 1saat")
			self.BossTrackingImage = ui.ExpandedImageBox()
			self.BossTrackingImage.SetParent(self.board)
			self.BossTrackingImage.LoadImage("d:/ymir work/patrontakip/slot_9.tga")
			self.BossTrackingImage.SetPosition(265-49, 95+194)
			self.BossTrackingImage.Show()
			constInfo.bosstracking = 9
		elif value == 10:
			self.title_name.SetText("Karanlýk Hayalet Lider")
			self.title_name_2.SetText("Seviye : 62")
			self.title_name_3.SetText("Bölge : Hwang Tapýnaðý")
			self.title_name_4.SetText("Etkili Týlsým : Rüzgar Týlsýmý")
			self.title_name_5.SetText("Yeniden Çýkýþ Süresi : 2saat")
			self.BossTrackingImage = ui.ExpandedImageBox()
			self.BossTrackingImage.SetParent(self.board)
			self.BossTrackingImage.LoadImage("d:/ymir work/patrontakip/slot_10.tga")
			self.BossTrackingImage.SetPosition(265-49, 95+194)
			self.BossTrackingImage.Show()
			constInfo.bosstracking = 10

	def Destroy(self):
		self.ClearDictionary()
		self.board = None

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()
		
	def GetMobInformation(self, btcadi1, btcadi2, btcadi3, btcadi4, btcadi5, btcadi6, btalevkral1, btalevkral2, btalevkral3, btalevkral4, btalevkral5, btalevkral6, btkorumcek1, btkorumcek2, btkorumcek3, btkorumcek4, btkorumcek5, btkorumcek6, btsarikaplan1, btsarikaplan2, btsarikaplan3, btsarikaplan4, btsarikaplan5, btsarikaplan6, btbuzkralice1, btbuzkralice2, btbuzkralice3, btbuzkralice4, btbuzkralice5, btbuzkralice6, btdokuzk1, btdokuzk2, btdokuzk3, btdokuzk4, btdokuzk5, btdokuzk6, btcolejder1, btcolejder2, btcolejder3, btcolejder4, btcolejder5, btcolejder6, btagac1, btagac2, btagac3, btagac4, btagac5, btagac6, btkomutan1, btkomutan2, btkomutan3, btkomutan4, btkomutan5, btkomutan6, btkaranlik1, btkaranlik2, btkaranlik3, btkaranlik4, btkaranlik5, btkaranlik6):
		self.newbtcadi1 = int(btcadi1)
		self.newbtcadi2 = int(btcadi2)
		self.newbtcadi3 = int(btcadi3)
		self.newbtcadi4 = int(btcadi4)
		self.newbtcadi5 = int(btcadi5)
		self.newbtcadi6 = int(btcadi6)
		
		self.newbtalevkral1 = int(btalevkral1)
		self.newbtalevkral2 = int(btalevkral2)
		self.newbtalevkral3 = int(btalevkral3)
		self.newbtalevkral4 = int(btalevkral4)
		self.newbtalevkral5 = int(btalevkral5)
		self.newbtalevkral6 = int(btalevkral6)
		
		self.newbtkorumcek1 = int(btkorumcek1)
		self.newbtkorumcek2 = int(btkorumcek2)
		self.newbtkorumcek3 = int(btkorumcek3)
		self.newbtkorumcek4 = int(btkorumcek4)
		self.newbtkorumcek5 = int(btkorumcek5)
		self.newbtkorumcek6 = int(btkorumcek6)
		
		self.newbtsarikaplan1 = int(btsarikaplan1)
		self.newbtsarikaplan2 = int(btsarikaplan2)
		self.newbtsarikaplan3 = int(btsarikaplan3)
		self.newbtsarikaplan4 = int(btsarikaplan4)
		self.newbtsarikaplan5 = int(btsarikaplan5)
		self.newbtsarikaplan6 = int(btsarikaplan6)
		
		self.newbtbuzkralice1 = int(btbuzkralice1)
		self.newbtbuzkralice2 = int(btbuzkralice2)
		self.newbtbuzkralice3 = int(btbuzkralice3)
		self.newbtbuzkralice4 = int(btbuzkralice4)
		self.newbtbuzkralice5 = int(btbuzkralice5)
		self.newbtbuzkralice6 = int(btbuzkralice6)
		
		self.newbtdokuzk1 = int(btdokuzk1)
		self.newbtdokuzk2 = int(btdokuzk2)
		self.newbtdokuzk3 = int(btdokuzk3)
		self.newbtdokuzk4 = int(btdokuzk4)
		self.newbtdokuzk5 = int(btdokuzk5)
		self.newbtdokuzk6 = int(btdokuzk6)

		self.newbtcolejder1 = int(btcolejder1)
		self.newbtcolejder2 = int(btcolejder2)
		self.newbtcolejder3 = int(btcolejder3)
		self.newbtcolejder4 = int(btcolejder4)
		self.newbtcolejder5 = int(btcolejder5)
		self.newbtcolejder6 = int(btcolejder6)

		self.newbtagac1 = int(btagac1)
		self.newbtagac2 = int(btagac2)
		self.newbtagac3 = int(btagac3)
		self.newbtagac4 = int(btagac4)
		self.newbtagac5 = int(btagac5)
		self.newbtagac6 = int(btagac6)

		self.newbtkomutan1 = int(btkomutan1)
		self.newbtkomutan2 = int(btkomutan2)
		self.newbtkomutan3 = int(btkomutan3)
		self.newbtkomutan4 = int(btkomutan4)
		self.newbtkomutan5 = int(btkomutan5)
		self.newbtkomutan6 = int(btkomutan6)

		self.newbtkaranlik1 = int(btkaranlik1)
		self.newbtkaranlik2 = int(btkaranlik2)
		self.newbtkaranlik3 = int(btkaranlik3)
		self.newbtkaranlik4 = int(btkaranlik4)
		self.newbtkaranlik5 = int(btkaranlik5)
		self.newbtkaranlik6 = int(btkaranlik6)


	def OnUpdate(self):
		self.updatetimer += 1
		if self.updatetimer == 500:
			net.SendChatPacket("/bosstrackingtest")
			self.updatetimer = 0

		if constInfo.bosstracking == 1:
			if int(self.newbtcadi1) == 0:
				self.Channel1Time.SetText("CH1: Yaþýyor")
			elif (int(self.newbtcadi1)-app.GetGlobalTimeStamp() < 0):
				self.Channel1Time.SetText("CH1: Yaþýyor")
			else:
				self.Channel1Time.SetText("CH1: " + str(FormatTimeBevis(int(self.newbtcadi1)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtcadi2) == 0:
				self.Channel2Time.SetText("CH2: Yaþýyor")
			elif (int(self.newbtcadi2)-app.GetGlobalTimeStamp() < 0):
				self.Channel2Time.SetText("CH2: Yaþýyor")
			else:
				self.Channel2Time.SetText("CH2: " + str(FormatTimeBevis(int(self.newbtcadi2)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtcadi3) == 0:
				self.Channel3Time.SetText("CH3: Yaþýyor")
			elif (int(self.newbtcadi3)-app.GetGlobalTimeStamp() < 0):
				self.Channel3Time.SetText("CH3: Yaþýyor")
			else:
				self.Channel3Time.SetText("CH3: " + str(FormatTimeBevis(int(self.newbtcadi3)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtcadi4) == 0:
				self.Channel4Time.SetText("CH4: Yaþýyor")
			elif (int(self.newbtcadi4)-app.GetGlobalTimeStamp() < 0):
				self.Channel4Time.SetText("CH4: Yaþýyor")
			else:
				self.Channel4Time.SetText("CH4: " + str(FormatTimeBevis(int(self.newbtcadi4)-app.GetGlobalTimeStamp())))
		
			if int(self.newbtcadi5) == 0:
				self.Channel5Time.SetText("CH5: Yaþýyor")
			elif (int(self.newbtcadi5)-app.GetGlobalTimeStamp() < 0):
				self.Channel5Time.SetText("CH5: Yaþýyor")
			else:
				self.Channel5Time.SetText("CH5: " + str(FormatTimeBevis(int(self.newbtcadi5)-app.GetGlobalTimeStamp())))
				
			if int(self.newbtcadi6) == 0:
				self.Channel6Time.SetText("CH6: Yaþýyor")
			elif (int(self.newbtcadi6)-app.GetGlobalTimeStamp() < 0):
				self.Channel6Time.SetText("CH6: Yaþýyor")
			else:
				self.Channel6Time.SetText("CH6: " + str(FormatTimeBevis(int(self.newbtcadi6)-app.GetGlobalTimeStamp())))
				
			#################################
		elif constInfo.bosstracking == 2:
			if int(self.newbtalevkral1) == 0:
				self.Channel1Time.SetText("CH1: Yaþýyor")
			elif (int(self.newbtalevkral1)-app.GetGlobalTimeStamp() < 0):
				self.Channel1Time.SetText("CH1: Yaþýyor")
			else:
				self.Channel1Time.SetText("CH1: " + str(FormatTimeBevis(int(self.newbtalevkral1)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtalevkral2) == 0:
				self.Channel2Time.SetText("CH2: Yaþýyor")
			elif (int(self.newbtalevkral2)-app.GetGlobalTimeStamp() < 0):
				self.Channel2Time.SetText("CH2: Yaþýyor")
			else:
				self.Channel2Time.SetText("CH2: " + str(FormatTimeBevis(int(self.newbtalevkral2)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtalevkral3) == 0:
				self.Channel3Time.SetText("CH3: Yaþýyor")
			elif (int(self.newbtalevkral3)-app.GetGlobalTimeStamp() < 0):
				self.Channel3Time.SetText("CH3: Yaþýyor")
			else:
				self.Channel3Time.SetText("CH3: " + str(FormatTimeBevis(int(self.newbtalevkral3)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtalevkral4) == 0:
				self.Channel4Time.SetText("CH4: Yaþýyor")
			elif (int(self.newbtalevkral4)-app.GetGlobalTimeStamp() < 0):
				self.Channel4Time.SetText("CH4: Yaþýyor")
			else:
				self.Channel4Time.SetText("CH4: " + str(FormatTimeBevis(int(self.newbtalevkral4)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtalevkral5) == 0:
				self.Channel5Time.SetText("CH5: Yaþýyor")
			elif (int(self.newbtalevkral5)-app.GetGlobalTimeStamp() < 0):
				self.Channel5Time.SetText("CH5: Yaþýyor")
			else:
				self.Channel5Time.SetText("CH5: " + str(FormatTimeBevis(int(self.newbtalevkral5)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtalevkral6) == 0:
				self.Channel6Time.SetText("CH6: Yaþýyor")
			elif (int(self.newbtalevkral6)-app.GetGlobalTimeStamp() < 0):
				self.Channel6Time.SetText("CH6: Yaþýyor")
			else:
				self.Channel6Time.SetText("CH6: " + str(FormatTimeBevis(int(self.newbtalevkral6)-app.GetGlobalTimeStamp())))
				
				#################################
				
		elif constInfo.bosstracking == 3:
			if int(self.newbtkorumcek1) == 0:
				self.Channel1Time.SetText("CH1: Yaþýyor")
			elif (int(self.newbtkorumcek1)-app.GetGlobalTimeStamp() < 0):
				self.Channel1Time.SetText("CH1: Yaþýyor")
			else:
				self.Channel1Time.SetText("CH1: " + str(FormatTimeBevis(int(self.newbtkorumcek1)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtkorumcek2) == 0:
				self.Channel2Time.SetText("CH2: Yaþýyor")
			elif (int(self.newbtkorumcek2)-app.GetGlobalTimeStamp() < 0):
				self.Channel2Time.SetText("CH2: Yaþýyor")
			else:
				self.Channel2Time.SetText("CH2: " + str(FormatTimeBevis(int(self.newbtkorumcek2)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtkorumcek3) == 0:
				self.Channel3Time.SetText("CH3: Yaþýyor")
			elif (int(self.newbtkorumcek3)-app.GetGlobalTimeStamp() < 0):
				self.Channel3Time.SetText("CH3: Yaþýyor")
			else:
				self.Channel3Time.SetText("CH3: " + str(FormatTimeBevis(int(self.newbtkorumcek3)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtkorumcek4) == 0:
				self.Channel4Time.SetText("CH4: Yaþýyor")
			elif (int(self.newbtkorumcek4)-app.GetGlobalTimeStamp() < 0):
				self.Channel4Time.SetText("CH4: Yaþýyor")
			else:
				self.Channel4Time.SetText("CH4: " + str(FormatTimeBevis(int(self.newbtkorumcek4)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtkorumcek5) == 0:
				self.Channel5Time.SetText("CH5: Yaþýyor")
			elif (int(self.newbtkorumcek5)-app.GetGlobalTimeStamp() < 0):
				self.Channel5Time.SetText("CH5: Yaþýyor")
			else:
				self.Channel5Time.SetText("CH5: " + str(FormatTimeBevis(int(self.newbtkorumcek5)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtkorumcek6) == 0:
				self.Channel6Time.SetText("CH6: Yaþýyor")
			elif (int(self.newbtkorumcek6)-app.GetGlobalTimeStamp() < 0):
				self.Channel6Time.SetText("CH6: Yaþýyor")
			else:
				self.Channel6Time.SetText("CH6: " + str(FormatTimeBevis(int(self.newbtkorumcek6)-app.GetGlobalTimeStamp())))
				
				#################################
		elif constInfo.bosstracking == 4:
			if int(self.newbtsarikaplan1) == 0:
				self.Channel1Time.SetText("CH1: Yaþýyor")
			elif (int(self.newbtsarikaplan1)-app.GetGlobalTimeStamp() < 0):
				self.Channel1Time.SetText("CH1: Yaþýyor")
			else:
				self.Channel1Time.SetText("CH1: " + str(FormatTimeBevis(int(self.newbtsarikaplan1)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtsarikaplan2) == 0:
				self.Channel2Time.SetText("CH2: Yaþýyor")
			elif (int(self.newbtsarikaplan2)-app.GetGlobalTimeStamp() < 0):
				self.Channel2Time.SetText("CH2: Yaþýyor")
			else:
				self.Channel2Time.SetText("CH2: " + str(FormatTimeBevis(int(self.newbtsarikaplan2)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtsarikaplan3) == 0:
				self.Channel3Time.SetText("CH3: Yaþýyor")
			elif (int(self.newbtsarikaplan3)-app.GetGlobalTimeStamp() < 0):
				self.Channel3Time.SetText("CH3: Yaþýyor")
			else:
				self.Channel3Time.SetText("CH3: " + str(FormatTimeBevis(int(self.newbtsarikaplan3)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtsarikaplan4) == 0:
				self.Channel4Time.SetText("CH4: Yaþýyor")
			elif (int(self.newbtsarikaplan4)-app.GetGlobalTimeStamp() < 0):
				self.Channel4Time.SetText("CH4: Yaþýyor")
			else:
				self.Channel4Time.SetText("CH4: " + str(FormatTimeBevis(int(self.newbtsarikaplan4)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtsarikaplan5) == 0:
				self.Channel5Time.SetText("CH5: Yaþýyor")
			elif (int(self.newbtsarikaplan5)-app.GetGlobalTimeStamp() < 0):
				self.Channel5Time.SetText("CH5: Yaþýyor")
			else:
				self.Channel5Time.SetText("CH5: " + str(FormatTimeBevis(int(self.newbtsarikaplan5)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtsarikaplan6) == 0:
				self.Channel6Time.SetText("CH6: Yaþýyor")
			elif (int(self.newbtsarikaplan6)-app.GetGlobalTimeStamp() < 0):
				self.Channel6Time.SetText("CH6: Yaþýyor")
			else:
				self.Channel6Time.SetText("CH6: " + str(FormatTimeBevis(int(self.newbtsarikaplan6)-app.GetGlobalTimeStamp())))
				
				#################################
				
		elif constInfo.bosstracking == 5:
			if int(self.newbtbuzkralice1) == 0:
				self.Channel1Time.SetText("CH1: Yaþýyor")
			elif (int(self.newbtbuzkralice1)-app.GetGlobalTimeStamp() < 0):
				self.Channel1Time.SetText("CH1: Yaþýyor")
			else:
				self.Channel1Time.SetText("CH1: " + str(FormatTimeBevis(int(self.newbtbuzkralice1)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtbuzkralice2) == 0:
				self.Channel2Time.SetText("CH2: Yaþýyor")
			elif (int(self.newbtbuzkralice2)-app.GetGlobalTimeStamp() < 0):
				self.Channel2Time.SetText("CH2: Yaþýyor")
			else:
				self.Channel2Time.SetText("CH2: " + str(FormatTimeBevis(int(self.newbtbuzkralice2)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtbuzkralice3) == 0:
				self.Channel3Time.SetText("CH3: Yaþýyor")
			elif (int(self.newbtbuzkralice3)-app.GetGlobalTimeStamp() < 0):
				self.Channel3Time.SetText("CH3: Yaþýyor")
			else:
				self.Channel3Time.SetText("CH3: " + str(FormatTimeBevis(int(self.newbtbuzkralice3)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtbuzkralice4) == 0:
				self.Channel4Time.SetText("CH4: Yaþýyor")
			elif (int(self.newbtbuzkralice4)-app.GetGlobalTimeStamp() < 0):
				self.Channel4Time.SetText("CH4: Yaþýyor")
			else:
				self.Channel4Time.SetText("CH4: " + str(FormatTimeBevis(int(self.newbtbuzkralice4)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtbuzkralice5) == 0:
				self.Channel5Time.SetText("CH5: Yaþýyor")
			elif (int(self.newbtbuzkralice5)-app.GetGlobalTimeStamp() < 0):
				self.Channel5Time.SetText("CH5: Yaþýyor")
			else:
				self.Channel5Time.SetText("CH5: " + str(FormatTimeBevis(int(self.newbtbuzkralice5)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtbuzkralice6) == 0:
				self.Channel6Time.SetText("CH6: Yaþýyor")
			elif (int(self.newbtbuzkralice6)-app.GetGlobalTimeStamp() < 0):
				self.Channel6Time.SetText("CH6: Yaþýyor")
			else:
				self.Channel6Time.SetText("CH6: " + str(FormatTimeBevis(int(self.newbtbuzkralice6)-app.GetGlobalTimeStamp())))
				
				#################################
				
		elif constInfo.bosstracking == 6:
			if int(self.newbtdokuzk1) == 0:
				self.Channel1Time.SetText("CH1: Yaþýyor")
			elif (int(self.newbtdokuzk1)-app.GetGlobalTimeStamp() < 0):
				self.Channel1Time.SetText("CH1: Yaþýyor")
			else:
				self.Channel1Time.SetText("CH1: " + str(FormatTimeBevis(int(self.newbtdokuzk1)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtdokuzk2) == 0:
				self.Channel2Time.SetText("CH2: Yaþýyor")
			elif (int(self.newbtdokuzk2)-app.GetGlobalTimeStamp() < 0):
				self.Channel2Time.SetText("CH2: Yaþýyor")
			else:
				self.Channel2Time.SetText("CH2: " + str(FormatTimeBevis(int(self.newbtdokuzk2)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtdokuzk3) == 0:
				self.Channel3Time.SetText("CH3: Yaþýyor")
			elif (int(self.newbtdokuzk3)-app.GetGlobalTimeStamp() < 0):
				self.Channel3Time.SetText("CH3: Yaþýyor")
			else:
				self.Channel3Time.SetText("CH3: " + str(FormatTimeBevis(int(self.newbtdokuzk3)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtdokuzk4) == 0:
				self.Channel4Time.SetText("CH4: Yaþýyor")
			elif (int(self.newbtdokuzk4)-app.GetGlobalTimeStamp() < 0):
				self.Channel4Time.SetText("CH4: Yaþýyor")
			else:
				self.Channel4Time.SetText("CH4: " + str(FormatTimeBevis(int(self.newbtdokuzk4)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtdokuzk5) == 0:
				self.Channel5Time.SetText("CH5: Yaþýyor")
			elif (int(self.newbtdokuzk5)-app.GetGlobalTimeStamp() < 0):
				self.Channel5Time.SetText("CH5: Yaþýyor")
			else:
				self.Channel5Time.SetText("CH5: " + str(FormatTimeBevis(int(self.newbtdokuzk5)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtdokuzk6) == 0:
				self.Channel6Time.SetText("CH6: Yaþýyor")
			elif (int(self.newbtdokuzk6)-app.GetGlobalTimeStamp() < 0):
				self.Channel6Time.SetText("CH6: Yaþýyor")
			else:
				self.Channel6Time.SetText("CH6: " + str(FormatTimeBevis(int(self.newbtdokuzk6)-app.GetGlobalTimeStamp())))
				
				#################################

		elif constInfo.bosstracking == 7:
			if int(self.newbtcolejder1) == 0:
				self.Channel1Time.SetText("CH1: Yaþýyor")
			elif (int(self.newbtcolejder1)-app.GetGlobalTimeStamp() < 0):
				self.Channel1Time.SetText("CH1: Yaþýyor")
			else:
				self.Channel1Time.SetText("CH1: " + str(FormatTimeBevis(int(self.newbtcolejder1)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtcolejder2) == 0:
				self.Channel2Time.SetText("CH2: Yaþýyor")
			elif (int(self.newbtcolejder2)-app.GetGlobalTimeStamp() < 0):
				self.Channel2Time.SetText("CH2: Yaþýyor")
			else:
				self.Channel2Time.SetText("CH2: " + str(FormatTimeBevis(int(self.newbtcolejder2)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtcolejder3) == 0:
				self.Channel3Time.SetText("CH3: Yaþýyor")
			elif (int(self.newbtcolejder3)-app.GetGlobalTimeStamp() < 0):
				self.Channel3Time.SetText("CH3: Yaþýyor")
			else:
				self.Channel3Time.SetText("CH3: " + str(FormatTimeBevis(int(self.newbtcolejder3)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtcolejder4) == 0:
				self.Channel4Time.SetText("CH4: Yaþýyor")
			elif (int(self.newbtcolejder4)-app.GetGlobalTimeStamp() < 0):
				self.Channel4Time.SetText("CH4: Yaþýyor")
			else:
				self.Channel4Time.SetText("CH4: " + str(FormatTimeBevis(int(self.newbtcolejder4)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtcolejder5) == 0:
				self.Channel5Time.SetText("CH5: Yaþýyor")
			elif (int(self.newbtcolejder5)-app.GetGlobalTimeStamp() < 0):
				self.Channel5Time.SetText("CH5: Yaþýyor")
			else:
				self.Channel5Time.SetText("CH5: " + str(FormatTimeBevis(int(self.newbtcolejder5)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtcolejder6) == 0:
				self.Channel6Time.SetText("CH6: Yaþýyor")
			elif (int(self.newbtcolejder6)-app.GetGlobalTimeStamp() < 0):
				self.Channel6Time.SetText("CH6: Yaþýyor")
			else:
				self.Channel6Time.SetText("CH6: " + str(FormatTimeBevis(int(self.newbtcolejder6)-app.GetGlobalTimeStamp())))
				
				#################################

		elif constInfo.bosstracking == 8:
			if int(self.newbtagac1) == 0:
				self.Channel1Time.SetText("CH1: Yaþýyor")
			elif (int(self.newbtagac1)-app.GetGlobalTimeStamp() < 0):
				self.Channel1Time.SetText("CH1: Yaþýyor")
			else:
				self.Channel1Time.SetText("CH1: " + str(FormatTimeBevis(int(self.newbtagac1)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtagac2) == 0:
				self.Channel2Time.SetText("CH2: Yaþýyor")
			elif (int(self.newbtagac2)-app.GetGlobalTimeStamp() < 0):
				self.Channel2Time.SetText("CH2: Yaþýyor")
			else:
				self.Channel2Time.SetText("CH2: " + str(FormatTimeBevis(int(self.newbtagac2)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtagac3) == 0:
				self.Channel3Time.SetText("CH3: Yaþýyor")
			elif (int(self.newbtagac3)-app.GetGlobalTimeStamp() < 0):
				self.Channel3Time.SetText("CH3: Yaþýyor")
			else:
				self.Channel3Time.SetText("CH3: " + str(FormatTimeBevis(int(self.newbtagac3)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtagac4) == 0:
				self.Channel4Time.SetText("CH4: Yaþýyor")
			elif (int(self.newbtagac4)-app.GetGlobalTimeStamp() < 0):
				self.Channel4Time.SetText("CH4: Yaþýyor")
			else:
				self.Channel4Time.SetText("CH4: " + str(FormatTimeBevis(int(self.newbtagac4)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtagac5) == 0:
				self.Channel5Time.SetText("CH5: Yaþýyor")
			elif (int(self.newbtagac5)-app.GetGlobalTimeStamp() < 0):
				self.Channel5Time.SetText("CH5: Yaþýyor")
			else:
				self.Channel5Time.SetText("CH5: " + str(FormatTimeBevis(int(self.newbtagac5)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtagac6) == 0:
				self.Channel6Time.SetText("CH6: Yaþýyor")
			elif (int(self.newbtagac6)-app.GetGlobalTimeStamp() < 0):
				self.Channel6Time.SetText("CH6: Yaþýyor")
			else:
				self.Channel6Time.SetText("CH6: " + str(FormatTimeBevis(int(self.newbtagac6)-app.GetGlobalTimeStamp())))
				
				#################################

		elif constInfo.bosstracking == 8:
			if int(self.newbtagac1) == 0:
				self.Channel1Time.SetText("CH1: Yaþýyor")
			elif (int(self.newbtagac1)-app.GetGlobalTimeStamp() < 0):
				self.Channel1Time.SetText("CH1: Yaþýyor")
			else:
				self.Channel1Time.SetText("CH1: " + str(FormatTimeBevis(int(self.newbtagac1)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtagac2) == 0:
				self.Channel2Time.SetText("CH2: Yaþýyor")
			elif (int(self.newbtagac2)-app.GetGlobalTimeStamp() < 0):
				self.Channel2Time.SetText("CH2: Yaþýyor")
			else:
				self.Channel2Time.SetText("CH2: " + str(FormatTimeBevis(int(self.newbtagac2)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtagac3) == 0:
				self.Channel3Time.SetText("CH3: Yaþýyor")
			elif (int(self.newbtagac3)-app.GetGlobalTimeStamp() < 0):
				self.Channel3Time.SetText("CH3: Yaþýyor")
			else:
				self.Channel3Time.SetText("CH3: " + str(FormatTimeBevis(int(self.newbtagac3)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtagac4) == 0:
				self.Channel4Time.SetText("CH4: Yaþýyor")
			elif (int(self.newbtagac4)-app.GetGlobalTimeStamp() < 0):
				self.Channel4Time.SetText("CH4: Yaþýyor")
			else:
				self.Channel4Time.SetText("CH4: " + str(FormatTimeBevis(int(self.newbtagac4)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtagac5) == 0:
				self.Channel5Time.SetText("CH5: Yaþýyor")
			elif (int(self.newbtagac5)-app.GetGlobalTimeStamp() < 0):
				self.Channel5Time.SetText("CH5: Yaþýyor")
			else:
				self.Channel5Time.SetText("CH5: " + str(FormatTimeBevis(int(self.newbtagac5)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtagac6) == 0:
				self.Channel6Time.SetText("CH6: Yaþýyor")
			elif (int(self.newbtagac6)-app.GetGlobalTimeStamp() < 0):
				self.Channel6Time.SetText("CH6: Yaþýyor")
			else:
				self.Channel6Time.SetText("CH6: " + str(FormatTimeBevis(int(self.newbtagac6)-app.GetGlobalTimeStamp())))
				
				#################################


		elif constInfo.bosstracking == 9:
			if int(self.newbtkomutan1) == 0:
				self.Channel1Time.SetText("CH1: Yaþýyor")
			elif (int(self.newbtkomutan1)-app.GetGlobalTimeStamp() < 0):
				self.Channel1Time.SetText("CH1: Yaþýyor")
			else:
				self.Channel1Time.SetText("CH1: " + str(FormatTimeBevis(int(self.newbtkomutan1)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtkomutan2) == 0:
				self.Channel2Time.SetText("CH2: Yaþýyor")
			elif (int(self.newbtkomutan2)-app.GetGlobalTimeStamp() < 0):
				self.Channel2Time.SetText("CH2: Yaþýyor")
			else:
				self.Channel2Time.SetText("CH2: " + str(FormatTimeBevis(int(self.newbtkomutan2)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtkomutan3) == 0:
				self.Channel3Time.SetText("CH3: Yaþýyor")
			elif (int(self.newbtkomutan3)-app.GetGlobalTimeStamp() < 0):
				self.Channel3Time.SetText("CH3: Yaþýyor")
			else:
				self.Channel3Time.SetText("CH3: " + str(FormatTimeBevis(int(self.newbtkomutan3)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtkomutan4) == 0:
				self.Channel4Time.SetText("CH4: Yaþýyor")
			elif (int(self.newbtkomutan4)-app.GetGlobalTimeStamp() < 0):
				self.Channel4Time.SetText("CH4: Yaþýyor")
			else:
				self.Channel4Time.SetText("CH4: " + str(FormatTimeBevis(int(self.newbtkomutan4)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtkomutan5) == 0:
				self.Channel5Time.SetText("CH5: Yaþýyor")
			elif (int(self.newbtkomutan5)-app.GetGlobalTimeStamp() < 0):
				self.Channel5Time.SetText("CH5: Yaþýyor")
			else:
				self.Channel5Time.SetText("CH5: " + str(FormatTimeBevis(int(self.newbtkomutan5)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtkomutan6) == 0:
				self.Channel6Time.SetText("CH6: Yaþýyor")
			elif (int(self.newbtkomutan6)-app.GetGlobalTimeStamp() < 0):
				self.Channel6Time.SetText("CH6: Yaþýyor")
			else:
				self.Channel6Time.SetText("CH6: " + str(FormatTimeBevis(int(self.newbtkomutan6)-app.GetGlobalTimeStamp())))
				
				#################################

		elif constInfo.bosstracking == 10:
			if int(self.newbtkaranlik1) == 0:
				self.Channel1Time.SetText("CH1: Yaþýyor")
			elif (int(self.newbtkaranlik1)-app.GetGlobalTimeStamp() < 0):
				self.Channel1Time.SetText("CH1: Yaþýyor")
			else:
				self.Channel1Time.SetText("CH1: " + str(FormatTimeBevis(int(self.newbtkaranlik1)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtkaranlik2) == 0:
				self.Channel2Time.SetText("CH2: Yaþýyor")
			elif (int(self.newbtkaranlik2)-app.GetGlobalTimeStamp() < 0):
				self.Channel2Time.SetText("CH2: Yaþýyor")
			else:
				self.Channel2Time.SetText("CH2: " + str(FormatTimeBevis(int(self.newbtkaranlik2)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtkaranlik3) == 0:
				self.Channel3Time.SetText("CH3: Yaþýyor")
			elif (int(self.newbtkaranlik3)-app.GetGlobalTimeStamp() < 0):
				self.Channel3Time.SetText("CH3: Yaþýyor")
			else:
				self.Channel3Time.SetText("CH3: " + str(FormatTimeBevis(int(self.newbtkaranlik3)-app.GetGlobalTimeStamp())))
	
			if int(self.newbtkaranlik4) == 0:
				self.Channel4Time.SetText("CH4: Yaþýyor")
			elif (int(self.newbtkaranlik4)-app.GetGlobalTimeStamp() < 0):
				self.Channel4Time.SetText("CH4: Yaþýyor")
			else:
				self.Channel4Time.SetText("CH4: " + str(FormatTimeBevis(int(self.newbtkaranlik4)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtkaranlik5) == 0:
				self.Channel5Time.SetText("CH5: Yaþýyor")
			elif (int(self.newbtkaranlik5)-app.GetGlobalTimeStamp() < 0):
				self.Channel5Time.SetText("CH5: Yaþýyor")
			else:
				self.Channel5Time.SetText("CH5: " + str(FormatTimeBevis(int(self.newbtkaranlik5)-app.GetGlobalTimeStamp())))
			
			if int(self.newbtkaranlik6) == 0:
				self.Channel6Time.SetText("CH6: Yaþýyor")
			elif (int(self.newbtkaranlik6)-app.GetGlobalTimeStamp() < 0):
				self.Channel6Time.SetText("CH6: Yaþýyor")
			else:
				self.Channel6Time.SetText("CH6: " + str(FormatTimeBevis(int(self.newbtkaranlik6)-app.GetGlobalTimeStamp())))
				
				#################################

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True
