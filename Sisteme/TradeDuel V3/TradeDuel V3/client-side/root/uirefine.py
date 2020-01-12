import gameInfo

class RefineDialog(ui.ScriptWindow):

	#deðiþtir#
	def Accept(self):
		if gameInfo.DUELLO_DURUM==1 or gameInfo.DUELLO_DURUM==4:
			self.Close()
			return
		net.SendItemUseToItemPacket(self.scrollItemPos, self.targetItemPos)
		self.Close()
		
class RefineDialogNew(ui.ScriptWindow):
	
	#deðiþtir#
	def Accept(self):
		if gameInfo.DUELLO_DURUM==1 or gameInfo.DUELLO_DURUM==4:
			self.CancelRefine()
			return
		net.SendRefinePacket(self.targetItemPos, self.type)
		self.Close()