Search:
			self.blockButtonList.append(GetObject("block_party_request_button"))
Add it under:
			self.blockButtonList.append(GetObject("emotionblock_on_button"))

---

Search:
		self.blockButtonList[6].SetToggleUpEvent(self.__OnClickBlockEquipButton)

Add it under:
		self.blockButtonList[7].SetToggleUpEvent(self.__OnClickBlockEmotionButton)

---

Search:
		self.blockButtonList[6].SetToggleDownEvent(self.__OnClickBlockEquipButton)

Add it under:
		self.blockButtonList[7].SetToggleDownEvent(self.__OnClickBlockEmotionButton)

		
---

Search:
	def __OnClickBlockEquipButton(self):
		self.RefreshBlock()
		net.SendChatPacket("/setblockmode " + str(constInfo.BLOCKMODE ^ player.BLOCK_EQUIP_VIEW))

Add it under:
	def __OnClickBlockEmotionButton(self):
		self.RefreshBlock()
		net.SendChatPacket("/setblockmode " + str(constInfo.BLOCKMODE ^ player.BLOCK_EMOTION_REQUEST))
