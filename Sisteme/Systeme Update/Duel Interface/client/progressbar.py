import ui
import grp
import app

class ProgressBar(ui.Window):
	BACKGROUND_COLOR = grp.GenerateColor(0.0, 0.0, 0.0, 1.0)
	DARK_COLOR 		 = grp.GenerateColor(0.4, 0.4, 0.4, 1.0)
	PROGRESS_COLOR   = grp.GenerateColor(1.0, 0.2, 0.2, 0.4)
	
	def __init__(self, layer = "UI"):
		ui.Window.__init__(self, layer)

		self.WIDTH 			= 0
		self.HEIGHT 		= 0		
		self.Percent    	= 100
		self.Time			= 0
		self.CallbackEvent  = None
		self.IsWorking		= FALSE
		self.LastValue		= 100
		
	def __del__(self):
		ui.Window.__del__(self)
		
	def Destroy(self):
		self.WIDTH 		= 0
		self.HEIGHT 	= 0		
		self.Percent    = 0

	def SetSize(self, WIDTH, HEIGHT):
		ui.Window.SetSize(self, WIDTH, HEIGHT)
		self.WIDTH  = WIDTH
		self.HEIGHT = HEIGHT

	def SetPercentage(self, CurrentPercent):
		if CurrentPercent <= 0:
			if not self.CallbackEvent == None:
				self.CallbackEvent()
			self.Percent = 0
		elif CurrentPercent < 0:
			self.Percent = 0
		else:
			self.Percent = CurrentPercent
			
	def SetWorking(self, IsWorking):
		self.IsWorking = IsWorking
		
	def SetCallbackEvent(self, Callback):
		self.CallbackEvent = Callback

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		
		widthRender  = self.WIDTH
		heightRender = self.HEIGHT
		
		grp.SetColor(self.BACKGROUND_COLOR)
		grp.RenderBar(xRender, yRender, widthRender, heightRender)
		grp.SetColor(self.DARK_COLOR)
		grp.RenderLine(xRender, yRender, widthRender, 0)
		grp.RenderLine(xRender, yRender, 0, heightRender)
		grp.RenderLine(xRender, yRender+heightRender, widthRender, 0)
		grp.RenderLine(xRender + widthRender, yRender, 0, heightRender)
		
		grp.SetColor(self.PROGRESS_COLOR)
		
		grp.RenderBar(xRender + 2, yRender + 2, (self.WIDTH - 3) * self.Percent / 100, heightRender - 3)
		
	def OnUpdate(self):
		if self.Time < app.GetTime() and self.IsWorking == TRUE:
			self.SetPercentage(self.Percent - 1)
			self.Time = app.GetTime() + 0.29
