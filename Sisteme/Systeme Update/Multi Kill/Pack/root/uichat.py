Search:
	def __SendChatPacket(self, text, type):

Add it under:
		if str(text) in ["(kill1)", "(kill2)", "(kill3)", "(kill4)", "(kill5)", "(kill6)"]:
			return
