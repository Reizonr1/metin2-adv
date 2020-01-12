import gameInfo

class RefineDialog(ui.ScriptWindow):

	#de�i�tir#
	def Accept(self):
		if len(gameInfo.DICE_SYSTEM) > 0:
			self.Close()
			return
		net.SendItemUseToItemPacket(self.scrollItemPos, self.targetItemPos)
		self.Close()
		
class RefineDialogNew(ui.ScriptWindow):
	
	#de�i�tir#
	def Accept(self):
		if len(gameInfo.DICE_SYSTEM) > 0:
			self.Close()
			return
		net.SendRefinePacket(self.targetItemPos, self.type)
		self.Close()