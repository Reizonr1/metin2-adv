class QuestionDialog(ui.ScriptWindow):
	def __init__(self):
		#içine-ekle#
		self.EscapeStat = 0
		
	#yeni-ekle#
	def EscapeKeyStat(self, gelen):
		self.EscapeStat = gelen
		
	#deðiþtir#
	def OnPressEscapeKey(self):
		if self.EscapeStat == 1:
			return TRUE
		self.Close()
		return TRUE