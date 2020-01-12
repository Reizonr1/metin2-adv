import localegame
import gameInfo
import event
import chat
import uiCommon

class TargetBoard(ui.ThinBoard):
	
	BUTTON_NAME_LIST = ( 
		"Eþya ile Düello",
		"Ý.Düello Kabul Et",
	)

	
	self.buttonDict["Eþya ile Düello"].SAFE_SetEvent(self.__OnEsyaDuello)
	self.buttonDict["Ý.Düello Kabul Et"].SAFE_SetEvent(self.__OnEsyaDuello)

	## Fonksiyonun içine eklenecek!!! ##
	def RefreshButton(self):
			#40K ÝSE LOCALEINFO!!!!
			
		if player.IsPartyMember(self.vid):
			self.__HideButton("Eþya ile Düello")
			self.__HideButton("Ý.Düello Kabul Et")
			
			if player.IsSameEmpire(self.vid):
				if gameInfo.DUELLO_DURUM == 3 and "#"+str(chr.GetNameByVID(self.vid))+"#" in gameInfo.DUELLO_YOLLAYANLAR:
					self.__HideButton("Eþya ile Düello")
					self.__HideButton(locale.TARGET_BUTTON_ACCEPT_FIGHT)
					self.__ShowButton("Ý.Düello Kabul Et")
				elif gameInfo.DUELLO_DURUM == 5 and "#"+str(chr.GetNameByVID(self.vid))+"#" in gameInfo.DUELLO_YOLLAYANLAR:
					self.__HideButton("Eþya ile Düello")
					self.__HideButton(locale.TARGET_BUTTON_ACCEPT_FIGHT)
					self.__ShowButton("Ý.Düello Kabul Et")
				elif gameInfo.DUELLO_DURUM == 1:
					self.__HideButton("Eþya ile Düello")
					self.__HideButton("Ý.Düello Kabul Et")
				elif "#"+str(chr.GetNameByVID(self.vid))+"#" in gameInfo.DUELLO_YOLLANANLAR or gameInfo.DUELLO_DURUM == 4:
					self.__HideButton("Eþya ile Düello")
					self.__HideButton(locale.TARGET_BUTTON_ACCEPT_FIGHT)
					self.__HideButton("Ý.Düello Kabul Et")

		#if gameInfo.DUELLO_DURUM == 0:
		#	self.__ShowButton("Eþya ile Düello")
		#else:
		#	self.__HideButton("Eþya ile Düello")

	def ShowDefaultButton(self):
		self.showingButtonList.append(self.buttonDict["Eþya ile Düello"])


	## Fonksiyonu deðiþtir!!! ##
	def OnPVP(self):
		if gameInfo.DUELLO_DURUM == 1:
			self.Chat("<Düello> : Þuan'da zaten düellodasýn.")
			return

		if gameInfo.DUELLO_DURUM == 4:
			self.Chat("<Düello> : Þuan'da panel ekranýnda iken bu seçeneði kullanamassýn.")
			return

		net.SendChatPacket("/pvp %d" % (self.vid))

		
	## Fonksiyonu boþ yere ekle!!! ##
	def __OnEsyaDuello(self):
		if player.IsChallengeInstance(self.vid) and gameInfo.DUELLO_DURUM == 0:
			race = net.GetMainActorRace()
			if not guild.IsGuildEnable():
				net.SendWhisperPacket(chr.GetNameByVID(self.vid), "##xsbyfatihbab34-axsadsahdgsadsadassadjadada##"+str(player.GetStatus(player.LEVEL))+"#Lonca yok.#"+str(race)+"#")
			else:
				net.SendWhisperPacket(chr.GetNameByVID(self.vid), "##xsbyfatihbab34-axsadsahdgsadsadassadjadada##"+str(player.GetStatus(player.LEVEL))+"#"+str(player.GetGuildName())+"#"+str(race)+"#")
			gameInfo.DUELLO_YOLLANANLAR.append("#"+str(chr.GetNameByVID(self.vid))+"#")
			gameInfo.DUELLO_VID = self.vid
			
		elif player.IsRevengeInstance(self.vid) and gameInfo.DUELLO_DURUM == 0:
			#net.SendWhisperPacket(chr.GetNameByVID(self.vid), "##xsbyfatihbab34-axsadsahdgsadsadassadjadada##")
			race = net.GetMainActorRace()
			if not guild.IsGuildEnable():
				net.SendWhisperPacket(chr.GetNameByVID(self.vid), "##xsbyfatihbab34-axsadsahdgsadsadassadjadada##"+str(player.GetStatus(player.LEVEL))+"#Lonca yok.#"+str(race)+"#")
			else:
				net.SendWhisperPacket(chr.GetNameByVID(self.vid), "##xsbyfatihbab34-axsadsahdgsadsadassadjadada##"+str(player.GetStatus(player.LEVEL))+"#"+str(player.GetGuildName())+"#"+str(race)+"#")
			gameInfo.DUELLO_YOLLANANLAR.append("#"+str(chr.GetNameByVID(self.vid))+"#")
			gameInfo.DUELLO_VID = self.vid
			
		elif gameInfo.DUELLO_DURUM == 0: ## duello teklif ##
			race = net.GetMainActorRace()
			if not guild.IsGuildEnable():
				net.SendWhisperPacket(chr.GetNameByVID(self.vid), "##xsbyfatihbab34axsadsahdgsadsadassadjadada##"+str(player.GetStatus(player.LEVEL))+"#Lonca yok.#"+str(race)+"#")
			else:
				net.SendWhisperPacket(chr.GetNameByVID(self.vid), "##xsbyfatihbab34axsadsahdgsadsadassadjadada##"+str(player.GetStatus(player.LEVEL))+"#"+str(player.GetGuildName())+"#"+str(race)+"#")
			net.SendChatPacket("/pvp %d" % (self.vid))
			gameInfo.DUELLO_YOLLANANLAR.append("#"+str(chr.GetNameByVID(self.vid))+"#")
			gameInfo.DUELLO_VID = self.vid
		elif gameInfo.DUELLO_DURUM == 3: ## duello kabul ##
			race = net.GetMainActorRace()
			if not guild.IsGuildEnable():
				net.SendWhisperPacket(chr.GetNameByVID(self.vid), "#xsbyfatihbab34sdajdsadnsadmnasdmnaswmqwmnmdsnaddasawq#"+str(player.GetStatus(player.LEVEL))+"#Lonca yok.#"+str(race)+"#")
			else:
				net.SendWhisperPacket(chr.GetNameByVID(self.vid), "#xsbyfatihbab34sdajdsadnsadmnasdmnaswmqwmnmdsnaddasawq#"+str(player.GetStatus(player.LEVEL))+"#"+str(player.GetGuildName())+"#"+str(race)+"#")
			gameInfo.DUELLO_VID = self.vid
			
		elif gameInfo.DUELLO_DURUM == 5: 
			race = net.GetMainActorRace()
			if not guild.IsGuildEnable():
				net.SendWhisperPacket(chr.GetNameByVID(self.vid), "#xsbyfatihbab34-sdajdsadnsadmnasdmnaswmqwmnmdsnaddasawq#"+str(player.GetStatus(player.LEVEL))+"#Lonca yok.#"+str(race)+"#")
			else:
				net.SendWhisperPacket(chr.GetNameByVID(self.vid), "#xsbyfatihbab34-sdajdsadnsadmnasdmnaswmqwmnmdsnaddasawq#"+str(player.GetStatus(player.LEVEL))+"#"+str(player.GetGuildName())+"#"+str(race)+"#")
			gameInfo.DUELLO_VID = self.vid
			
		elif gameInfo.DUELLO_DURUM == 1:
			self.Chat(str(localegame.DUELLO_YAPAMAZSIN))
	
	def Chat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, str(text))
		
		
	## OnUpdate sorunu varsa;
	def OnUpdate(self):
		if self.isShowButton:
		
			if not player.IsMainCharacterIndex(self.vid):
				self.RefreshButton()