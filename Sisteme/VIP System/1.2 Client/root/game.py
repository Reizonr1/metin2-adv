##1.0 suche:		
	self.serverCommander=stringCommander.Analyzer()
		for serverCommandItem in serverCommandList.items():
			self.serverCommander.SAFE_RegisterCallBack(
				serverCommandItem[0], serverCommandItem[1]
			)
##1.0 dahinter	
	if app.ENABLE_VIP_SYSTEM:
		self.serverCommander.SAFE_RegisterCallBack("VIP", self.vip)
	
##1.1 am ende der datei:
	if app.ENABLE_VIP_SYSTEM:
		def vip(self):
			net.SendChatPacket("/refresh_vip")