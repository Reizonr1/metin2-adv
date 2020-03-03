""""""
#1) Search:
	def __PlayMusic(self, flag, filename):
		flag = int(flag)
		if flag:
			snd.FadeOutAllMusic()
			musicInfo.SaveLastPlayFieldMusic()
			snd.FadeInMusic("BGM/" + filename)
		else:
			snd.FadeOutAllMusic()
			musicInfo.LoadLastPlayFieldMusic()
			snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)
#2) After make a new line and paste:
	if app.ENABLE_CHANGELOOK_SYSTEM:
		def ActChangeLook(self, iAct):
			if self.interface:
				self.interface.ActChangeLook(iAct)

		def AlertChangeLook(self):
			self.PopupMessage(localeInfo.CHANGE_LOOK_DEL_ITEM)
""""""