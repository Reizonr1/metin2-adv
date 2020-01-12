Search:
			if net.IsInsultIn(text):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHAT_INSULT_STRING)
				return

Add it under:
			if app.OFFLINE_MESSAGE:
				if text[0]=="#" and len(text)>1:
					if self.targetName==player.GetName():
						chat.AppendChat(chat.CHAT_TYPE_INFO, "You can not send offline message to yourself")
						return

					text = text.replace("#", "", 1) #remove offline message arg("#")
					text = text.replace(" ", "$") #replace spaces

					net.SendOfflineMessagePacket(self.targetName, text)

					text = text.replace("$", " ") # restore replace spaces

					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : #" + text)
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, "|cffff0000|H|hSended offline message|h|r: '%s' |cffff0000|H|hto|h|r: %s" % (text, self.targetName))
					self.chatLine.SetText("")
					return
