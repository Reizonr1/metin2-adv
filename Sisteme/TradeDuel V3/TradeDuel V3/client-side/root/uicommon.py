class QuestionDialog(ui.ScriptWindow):
	def __init__(self):
		#i�ine-ekle#
		self.EscapeStat = 0
		
	#yeni-ekle#
	def EscapeKeyStat(self, gelen):
		self.EscapeStat = gelen
		
	#de�i�tir#
	def OnPressEscapeKey(self):
		if self.EscapeStat == 1:
			return TRUE
		self.Close()
		return TRUE