#Arat
	def BINARY_Cube_UpdateInfo(self, gold, itemVnum, count):
		self.interface.UpdateCubeInfo(gold, itemVnum, count)
		
	#Altýna Ekle
	
	def oyuncu_black(self, black, sari, kirmizi, mavi):
		#blackdragonx61
		self.interface.wndMiniMap.online_cok_hojdir_ama_benane(black, sari, kirmizi, mavi)