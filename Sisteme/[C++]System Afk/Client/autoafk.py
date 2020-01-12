from ui_wrapper import _ui
import ui, net, systemSetting, player

class AfkGui(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.GUIFunc()
		
	def __del__(self):
		ui.Window.__del__(self)
	
	def GUIFunc(self):
		self.Board = _ui().BoardWithTitleBar(None, 1, systemSetting.GetWidth() /2 -200, 50, 360, 140, "", self.OpenWindow) # parent moveable x y width heigh title event
		self.Text = _ui().TextLine(self.Board, "Suanda afk modundasin oyuna donmek icin asagidaki butona tikla", 25, 30)
		self.Image = _ui().ImageBox(self.Board, "sand.tga", 25, 50)
		self.Button = _ui().ResizeableButton(self.Board, 120, 65, 200, 40, "Oyuna devam et", "", self.DelAfk)
	
	def DelAfk(self):
		if player.IsOpenPrivateShop():
			self.Notification = _ui().Popup("Pazar acikken bu eylemi gerceklestiremezsin", None, None)
			return
		
		net.SendChatPacket("/remove_afk")
		self.OpenWindow()
	
	def OpenWindow(self):
		if self.Board.IsShow():
			self.Board.Hide()
		else:
			self.Board.Show()
	
	def Close(self):
		self.Board.Hide()
		
