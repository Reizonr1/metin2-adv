import gameInfo
import chat

	def RestartTown(self):
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"�temine VS an�nda, �ehirde yeniden ba�l�yamazs�n.")
			return
		net.SendChatPacket("/restart_town")
