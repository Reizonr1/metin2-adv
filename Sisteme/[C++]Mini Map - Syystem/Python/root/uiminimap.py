#arat
			self.serverInfo = self.GetChild("ServerInfo")
#Altýna Ekle
	
			self.mali	= self.GetChild("Toplam")
			self.sari	= self.GetChild("sari")
			self.kirmizi	= self.GetChild("kirmizi")
			self.mavi	= self.GetChild("mavi")
#Arat
			
	def UpdateObserverCount(self, observerCount):
		if observerCount>0:
			self.observerCount.Show()
		elif observerCount<=0:
			self.observerCount.Hide()

		self.observerCount.SetText(localeInfo.MINIMAP_OBSERVER_COUNT % observerCount)

#Altýna Ekle

	def online_cok_hojdir_ama_benane(self, black, sari, kirmizi, mavi):	 	
		#blackdragonx61
		self.mali.Show()
		self.sari.Show()
		self.kirmizi.Show()
		self.mavi.Show()
		self.mali.SetText(localeInfo.BLACK_ONLINE + str(black))#Toplam
		self.sari.SetText(localeInfo.BLACK_SARI + str(sari))
		self.kirmizi.SetText(localeInfo.BLACK_KIRMIZI + str(kirmizi))
		self.mavi.SetText("|cff00ccffMavi Bayrak:|h|r" + str(mavi))