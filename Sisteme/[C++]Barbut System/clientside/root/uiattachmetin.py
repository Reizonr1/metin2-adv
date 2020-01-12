import gameInfo

class AttachMetinDialog(ui.ScriptWindow):

	def Accept(self):
		if len(gameInfo.DICE_SYSTEM) > 0:
			self.Close()
			return
			
		net.SendItemUseToItemPacket(self.metinItemPos, self.targetItemPos)
		snd.PlaySound("sound/ui/metinstone_insert.wav")
		self.Close()