#1.) Search for:
import localeInfo
#2.) Add after:
if app.WJ_SHOW_STROKE_INFO:
	DICT_MOB_STROKE_INFO = {}
	
#1.) Search for:
	def __init__(self):
		ui.ThinBoard.__init__(self)
#2.) Add after:
		if app.WJ_SHOW_STROKE_INFO:
			strokeInfo = ui.TextLine()
			strokeInfo.SetDefaultFontName()
			strokeInfo.SetParent(self)
			strokeInfo.SetOutline()
			strokeInfo.SetFontColor(255, 045, 0)
			strokeInfo.SetPosition(10, 45)
			strokeInfo.Hide()
			
#1.) Search for:
		self.closeButton = closeButton
#2.) Add after:
		if app.WJ_SHOW_STROKE_INFO:
			self.strokeInfo = strokeInfo

#1.) Search for:
		self.closeButton = None
#2.) Add after:
		if app.WJ_SHOW_STROKE_INFO:
			self.strokeInfo = None

#1.) Search for:
		self.hpGauge.Hide()
#2.) Add after:
		if app.WJ_SHOW_STROKE_INFO:
			self.strokeInfo.Hide()

#1.) Search in def SetHP(self, hpPercentage):
		self.hpGauge.SetPercentage(hpPercentage, 100)
#2.) Add before:
		if app.WJ_SHOW_STROKE_INFO:
			self.GetStrokeByVid(self.GetTargetVID())
			
#1.) Search for:
	def GetTargetName(self):
		return self.nameString
#2.) Add after:
	if app.WJ_SHOW_STROKE_INFO:
		def RegisterStroke(self, targetVID, value):
			DICT_MOB_STROKE_INFO.update({targetVID : value})
			
		def GetStrokeByVid(self, targetVID):
			if targetVID in DICT_MOB_STROKE_INFO:
				self.strokeInfo.SetText(localeInfo.MOB_INFORMATION_STROKE % (DICT_MOB_STROKE_INFO[targetVID]))
				self.strokeInfo.Show()