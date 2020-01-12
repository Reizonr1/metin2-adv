Search:
		if localeInfo.WHISPER_ERROR.has_key(mode):
			chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, localeInfo.WHISPER_ERROR[mode](name))

Change:
		if localeInfo.WHISPER_ERROR.has_key(mode):
			if app.OFFLINE_MESSAGE:
				chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, name + " now is offline. If you want send offline message, put # the beginning of the message. e.g: #Hello")
			else:
				chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, localeInfo.WHISPER_ERROR[mode](name))

---

Search:
			# PRIVATE_SHOP_PRICE_LIST
			"MyShopPriceList"		: self.__PrivateShop_PriceList,
			# END_OF_PRIVATE_SHOP_PRICE_LIST

Add it under:
			"OFFMSG"				: self.RecvOfflineMessage,

---

Search:
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

	# END_OF_WEDDING

Add it under:
	def RecvOfflineMessage(self, x):
		txt = str(x)
		nick = txt.split("_")[0]
		zamanex = txt.split("_")[1]
		mesaj = txt.split("_")[2]
		mesaj = mesaj.replace("$", " ")

		import datetime
		zaman = datetime.datetime.fromtimestamp(int(zamanex)).strftime('%d-%m-%Y %H:%M:%S')

		chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, nick, "|cffff0000|H|h[OFFMSG-%s]:|h|r %s" % (zaman, mesaj))
		self.interface.RecvWhisper(nick)

