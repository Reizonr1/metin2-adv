# 01. Cauta
		self.GetChild("cancel_button").SAFE_SetEvent(self.Close)

# 02. Adauga sub
		self.GetChild("Texturi").SAFE_SetEvent(self.ClickTexturi)

# 01. Cauta
	def __ClickExitButton(self):
		self.Close()
		net.ExitApplication()

# 02. Adauga sub
	def ClickTexturi(self):
		import skybox
		SkyBoxDialog = skybox.SkyboxSelect()
		SkyBoxDialog.Show()
		self.Close()