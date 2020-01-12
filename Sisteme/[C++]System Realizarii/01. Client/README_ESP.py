### interfaceModule.py ###

# 1) Buscar: import uiScriptLocale
# 2) Hacer una nueva línea y debajo pegar esto:

import uiAchievements

# 1) Buscar:
"""
		self.dlgShop = uiShop.ShopDialog()
		self.dlgShop.LoadDialog()
		self.dlgShop.Hide()
"""
# en def __MakeDialogs(self):
# 2) Hacer una nueva línea y debajo pegar esto:

		self.wndAchievements = uiAchievements.AchievementWindow()
		self.wndAchievements.Hide()
		
# 1) Buscar:
"""
		if self.dlgShop:
			self.dlgShop.Destroy()
"""
# en def Close(self):
# 2) Hacer una nueva línea y debajo pegar esto:

		if self.wndAchievements:
			self.wndAchievements.Destroy()
			
# 1) Buscar: del self.wndItemSelect
# 2) Hacer una nueva línea y debajo pegar esto:

		del self.wndAchievements
		
############################
############################

### constInfo.py ###

# 1) Buscar: isItemDropQuestionDialog = 0
# 2) Hacer una nueva línea y debajo pegar esto:

Achievements = {
	'QID' : 0,
	'QCMD' : '',
	'achievements' : {},
	'last_achievements' : [],
	'achievementshop' : {'items': {}},
	'POINTS' : 0
}

############################
############################

### game.py ###

# 1) Buscar en el def __ServerCommand_Build
"""
			"mall"					: self.__InGameShop_Show,
"""
# 2) Hacer una nueva línea y debajo pegar esto:

			"ACHIEVEMENTS"			: self.ManagerAchievements,
			
# 1) Buscar:
"""
	def __InGameShop_Show(self, url):
		if constInfo.IN_GAME_SHOP_ENABLE:
			self.interface.OpenWebWindow(url
"""
# 2) Hacer una nueva línea y debajo pegar esto:

	def ManagerAchievements(self, cmd):
		cmd = cmd.split("#")
		if cmd[0] == 'QID':
			constInfo.Achievements['QID'] = int(cmd[1])
		elif cmd[0] == 'INPUT':
			constInfo.INPUT_IGNORE = int(cmd[1])
		elif cmd[0] == 'SEND':
			net.SendQuestInputStringPacket(constInfo.Achievements['QCMD'])
			constInfo.Achievements['QCMD'] = ''
		elif cmd[0] == 'SET_CATEGORY':
			constInfo.Achievements['achievements'][int(cmd[1])] = []
		elif cmd[0] == 'SET_ACHIEVEMENT':
			constInfo.Achievements['achievements'][int(cmd[1])].append([int(cmd[2]), int(cmd[3]), int(cmd[4]), int(cmd[5])])
		elif cmd[0] == 'UPDATE_ACHIEVEMENT':
			for i in xrange(len(constInfo.Achievements['achievements'][int(cmd[1])])):
				if int(cmd[1]) == 2 or int(cmd[1]) == 3 or int(cmd[1]) == 4:
					if constInfo.Achievements['achievements'][int(cmd[1])][i][3] == int(cmd[3]):
						constInfo.Achievements['achievements'][int(cmd[1])][i][0] = int(cmd[2])
				else:
					constInfo.Achievements['achievements'][int(cmd[1])][i][0] = int(cmd[2])
		elif cmd[0] == 'REFRESH_ACHIEVEMENTS':
			self.interface.wndAchievements.RefreshAchievements()
			self.interface.wndAchievements.RefreshGlobalProgress()
		elif cmd[0] == 'CLEAR_LAST_FINISHED':
			constInfo.Achievements['last_achievements'] = []
		elif cmd[0] == 'SET_FINISHED':
			self.interface.wndAchievements.SetAchievementFinisehd(int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))
		elif cmd[0] == 'SET_LAST_FINISHED':
			achievementInfo = cmd[1].split(',')
			constInfo.Achievements['last_achievements'].append([int(achievementInfo[0]), int(achievementInfo[1]), int(achievementInfo[2]), int(achievementInfo[3])])
		elif cmd[0] == 'REFRESH_LAST_FINISHED':
			self.interface.wndAchievements.RefreshLastFinished()
		elif cmd[0] == 'SET_AP':
			constInfo.Achievements['POINTS'] = int(cmd[1])
		elif cmd[0] == 'SET_ACHIEVEMENTSHOP_CATEGORY':
			constInfo.Achievements['achievementshop'][int(cmd[1])] = []
		elif cmd[0] == 'SET_ACHIEVEMENTSHOP_ITEM':
			constInfo.Achievements['achievementshop'][int(cmd[1])].append([int(cmd[2]), int(cmd[3]), int(cmd[4])])

############################
############################

### ui.py ###

# 1) Buscar:
"""
class NumberLine(window):
	...
"""
# debajo de toda la class
# 2) Hacer una nueva línea y debajo pegar esto:

class ResizableTextValue(Window):

	BACKGROUND_COLOR = grp.GenerateColor(0.0, 0.0, 0.0, 1.0)
	LINE_COLOR = grp.GenerateColor(0.4, 0.4, 0.4, 1.0)
	
	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		
		self.isBackground = TRUE
		self.LineText = None
		self.ToolTipText = None
		
		self.width = 0
		self.height = 0
		self.lines = []
		
	def __del__(self):
		Window.__del__(self)
		
	def SetSize(self, width, height):
		Window.SetSize(self, width, height)
		self.width = width
		self.height = height
		
	def SetToolTipText(self, tooltiptext, x = 0, y = 0):
		if not self.ToolTipText:		
			toolTip=createToolTipWindowDict["TEXT"]()
			toolTip.SetParent(self)
			toolTip.SetSize(0, 0)
			toolTip.SetHorizontalAlignCenter()
			toolTip.SetOutline()
			toolTip.Hide()
			toolTip.SetPosition(x + self.GetWidth()/2, y-20)
			self.ToolTipText=toolTip

		self.ToolTipText.SetText(tooltiptext)
		
	def SetText(self, text):
		if not self.LineText:
			textLine = TextLine()
			textLine.SetParent(self)
			textLine.SetPosition(self.GetWidth()/2, (self.GetHeight()/2)-1)
			textLine.SetVerticalAlignCenter()
			textLine.SetHorizontalAlignCenter()
			textLine.SetOutline()
			textLine.Show()
			self.LineText = textLine

		self.LineText.SetText(text)
		
	def SetTextColor(self, color):
		if not self.LineText:
			return
		self.LineText.SetPackedFontColor(color)
		
	def GetText(self):
		if not self.LineText:
			return
		return self.LineText.GetText()
		
	def SetLineColor(self, color):
		self.LINE_COLOR = color
		
	def SetLine(self, line_value):
		self.lines.append(line_value)
		
	def SetBackgroundColor(self, color):
		self.BACKGROUND_COLOR = color
		
	def SetNoBackground(self):
		self.isBackground = FALSE
	
	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		
		widthRender = self.width
		heightRender = self.height
		if self.isBackground:
			grp.SetColor(self.BACKGROUND_COLOR)
			grp.RenderBar(xRender, yRender, widthRender, heightRender)
		grp.SetColor(self.LINE_COLOR)
		if 'top' in self.lines:
			grp.RenderLine(xRender, yRender, widthRender, 0)
		if 'left' in self.lines:
			grp.RenderLine(xRender, yRender, 0, heightRender)
		if 'bottom' in self.lines:
			grp.RenderLine(xRender, yRender+heightRender, widthRender+1, 0)
		if 'right' in self.lines:	
			grp.RenderLine(xRender+widthRender, yRender, 0, heightRender)
			
# 1) Buscar:
"""
			elif Type == "listbox":
				parent.Children[Index] = ListBox()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBox(parent.Children[Index], ElementValue, parent)
"""
# 2) Hacer una nueva línea y debajo pegar esto:

			elif Type == "resizable_text_value":
				parent.Children[Index] = ResizableTextValue()
				parent.Children[Index].SetParent(parent)
				self.LoadElementResizableTextValue(parent.Children[Index], ElementValue, parent)
				
# 1) Buscar:
"""
	def LoadElementButton(self):
		...
"""
# debajo de toda la función
# 2) Hacer una nueva línea y debajo pegar esto:

	def LoadElementResizableTextValue(self, window, value, parentWindow):

		if value.has_key("width") and value.has_key("height"):
			window.SetSize(int(value["width"]), int(value["height"]))

		if TRUE == value.has_key("text"):
			window.SetText(value["text"])
			
		if value.has_key("line_color"):
			window.SetLineColor(value["line_color"])
			
		if value.has_key("color"):
			window.SetBackgroundColor(value["color"])
			
		if value.has_key("line_top"):
			window.SetLine('top')
		if value.has_key("line_bottom"):
			window.SetLine('bottom')
		if value.has_key("line_left"):
			window.SetLine('left')
		if value.has_key("line_right"):
			window.SetLine('right')
			
		if value.has_key('all_lines'):
			window.SetLine('top')
			window.SetLine('bottom')
			window.SetLine('left')
			window.SetLine('right')
			
		if value.has_key('without_background'):
			window.SetNoBackground()
			
		if value.has_key("text"):
			window.SetText(value["text"])

		self.LoadDefaultData(window, value, parentWindow)

		return TRUE

############################
############################

# 1) Para abrir la ventana del sistema de logros usar esta función:

def OpenAchievementsystemWindow(self):
	import uiAchievements
	self.achievement = uiAchievements.AchievementWindow()
	self.achievement.Open()
