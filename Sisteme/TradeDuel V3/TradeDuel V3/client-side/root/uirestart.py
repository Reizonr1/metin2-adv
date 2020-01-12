import gameInfo
import chat

	def RestartTown(self):
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Ýtemine VS anýnda, þehirde yeniden baþlýyamazsýn.")
			return
		net.SendChatPacket("/restart_town")
