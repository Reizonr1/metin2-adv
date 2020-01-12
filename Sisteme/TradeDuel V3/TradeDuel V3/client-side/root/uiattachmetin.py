import gameInfo

class AttachMetinDialog(ui.ScriptWindow):

	def Accept(self):
		if gameInfo.DUELLO_DURUM == 1 or gameInfo.DUELLO_DURUM == 4:
			self.Close()
			return
			
		net.SendItemUseToItemPacket(self.metinItemPos, self.targetItemPos)
		snd.PlaySound("sound/ui/metinstone_insert.wav")
		self.Close()