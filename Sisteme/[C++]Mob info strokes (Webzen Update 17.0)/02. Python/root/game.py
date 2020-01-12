#1.) Search for:
	def ChangeCurrentSkill(self, skillSlotNumber):
		self.interface.OnChangeCurrentSkill(skillSlotNumber)
#2.) Add after:
	if app.WJ_SHOW_STROKE_INFO:
		def RegisterStroke(self, targetVID, value):
			self.targetBoard.RegisterStroke(targetVID, value)