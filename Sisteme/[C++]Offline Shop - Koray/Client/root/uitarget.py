Search:
	def Open(self, vid, name):

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			if chr.GetVirtualNumber(vid) >= 30005 and chr.GetVirtualNumber(vid) <= 30010 and chr.GetInstanceType(vid) != chr.INSTANCE_TYPE_PLAYER:
				try:
					name = str(name).rsplit("'", 1)[0] # rsplit is correct way but it's support 2.4+
				except:
					name = str(name).split("'")[0]

https://puu.sh/sgT5I/a8c9311d68.png

---

Search:
			if not player.IsSameEmpire(self.vid):
				self.__HideButton(localeInfo.TARGET_BUTTON_INVITE_PARTY)
				self.__HideButton(localeInfo.TARGET_BUTTON_FRIEND)
				self.__HideButton(localeInfo.TARGET_BUTTON_FIGHT)

Add it under:
		if app.ENABLE_OFFLINE_SHOP:
			if chr.GetVirtualNumber(self.vid) >= 30005 and chr.GetVirtualNumber(self.vid) <= 30010 and chr.GetInstanceType(self.vid) != chr.INSTANCE_TYPE_PLAYER:
				self.__HideButton(localeInfo.TARGET_BUTTON_EXCHANGE)
				self.__HideButton(localeInfo.TARGET_BUTTON_FIGHT)
				self.__HideButton(localeInfo.TARGET_BUTTON_EMOTION_ALLOW)
				self.__HideButton(localeInfo.TARGET_BUTTON_FRIEND)
				self.__HideButton(localeInfo.TARGET_BUTTON_INVITE_PARTY)
				self.__HideButton(localeInfo.TARGET_BUTTON_INVITE_GUILD)
				

https://puu.sh/sgT7t/1dc258a474.png

