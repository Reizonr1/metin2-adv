import ui, grp, nonplayer, math, constInfo, time, item, uiToolTip, uiCommon, event

class AchievementWindow(ui.ScriptWindow):
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = False
		self.__LoadWindow()
		
	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/Achievement.py")
		except:
			import exception
			exception.Abort("AchievementWindow.LoadWindow.LoadObject")
			
		self.categorys = [
			["Leveo", 1],
			["Mobs", 2],
			["Jefes", 3],
			["Metines", 4],
			["Tiempo de Juego", 5],
			["PVP", 6],
		]

		self.category = 0
		self.type = 0
		self.achievementsPos = 0
		self.progress = {}
		
		self.BindObjects()
		self.BindEvents()
		self.isLoaded = True
	
	def BindObjects(self):
		self.board = self.GetChild("board")
		self.elements = {
			'windows' : {'home' : self.GetChild("HomeWindow"), 'achievements' : self.GetChild("AchievementsWindow")},
			'objects' : {
				'shopButton' : self.GetChild("AchievementshopButton"),
				'leftArrow' : self.GetChild("LeftArrow"), 'rightArrow' : self.GetChild("RightArrow"),
				'home' : {
					'box_0' : AchievementBox(), 'box_1' : AchievementBox(), 'box_2' : AchievementBox(), 'box_3' : AchievementBox(),
					'last_box_0' : AchievementLastFinished(), 'last_box_1' : AchievementLastFinished(), 'last_box_2' : AchievementLastFinished(), 'last_box_3' : AchievementLastFinished(), 'last_box_4' : AchievementLastFinished(), 'last_box_5' : AchievementLastFinished(), 
					'last_window' : self.GetChild("bgLastAchievements"),
					'upArrow' : self.GetChild("UpArrow"), 'downArrow' : self.GetChild("DownArrow"),
					'upArrowLast' : self.GetChild("LastUpArrow"), 'downArrowLast' : self.GetChild("LastDownArrow"),
				},
				'achievements' : {
					'scrollbar' : self.GetChild("ScrollBar"),
					'box_0' : AchievementBox(), 'box_1' : AchievementBox(), 'box_2' : AchievementBox(), 'box_3' : AchievementBox(), 'box_4' : AchievementBox(),
					'btn_type_0' : self.GetChild("Type0Button"), 'btn_type_1' : self.GetChild("Type1Button"), 'btn_type_2' : self.GetChild("Type2Button"),
					'type_1' : [], 'type_2' : [],
				},
			}
		}
		self.arrows = {'categorys' : 0, 'global_achievements' : 0, 'last_achievements' : 0}
		
	def BindEvents(self):
		self.globalProgress = AchievementProgressBar()
		self.globalProgress.SetParent(self.board)
		self.globalProgress.SetSize(440, 30)
		self.globalProgress.SetPosition(0, 46)
		self.globalProgress.SetWindowHorizontalAlignCenter()
		self.globalProgress.SetText('Logros Terminados')
		self.globalProgress.SetProgress(10, 155)
		self.globalProgress.Show()
		
		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		self.shopButton = AchievementShopWindow()
		self.elements['objects']['shopButton'].SetEvent(ui.__mem_func__(self.shopButton.Open))
		
		self.elements['objects']['leftArrow'].SetEvent(ui.__mem_func__(self.__OnClickArrow), 'CATEGORY_LEFT')
		self.elements['objects']['rightArrow'].SetEvent(ui.__mem_func__(self.__OnClickArrow), 'CATEGORY_RIGHT')
		
		self.elements['objects']['home']['upArrow'].SetEvent(ui.__mem_func__(self.__OnClickArrow), 'GLOBAL_UP')
		self.elements['objects']['home']['downArrow'].SetEvent(ui.__mem_func__(self.__OnClickArrow), 'GLOBAL_DOWN')
		
		self.elements['objects']['home']['upArrowLast'].SetEvent(ui.__mem_func__(self.__OnClickArrow), 'LAST_UP')
		self.elements['objects']['home']['downArrowLast'].SetEvent(ui.__mem_func__(self.__OnClickArrow), 'LAST_DOWN')
		
		self.elements['objects']['achievements']['scrollbar'].SetScrollEvent(ui.__mem_func__(self.__OnScroll))
		
		self.elements['objects']['achievements']['box_0'].Open(self.elements['windows']['achievements'], -10, 40)
		self.elements['objects']['achievements']['box_1'].Open(self.elements['windows']['achievements'], -10, 40+40+20)
		self.elements['objects']['achievements']['box_2'].Open(self.elements['windows']['achievements'], -10, 40+(40+20)*2)
		self.elements['objects']['achievements']['box_3'].Open(self.elements['windows']['achievements'], -10, 40+(40+20)*3)
		self.elements['objects']['achievements']['box_4'].Open(self.elements['windows']['achievements'], -10, 40+(40+20)*4)
		
		self.elements['objects']['home']['box_0'].Open(self.elements['windows']['home'], -120, 40)
		self.elements['objects']['home']['box_1'].Open(self.elements['windows']['home'], -120, 40+58+14)
		self.elements['objects']['home']['box_2'].Open(self.elements['windows']['home'], -120, 40+(58+14)*2)
		self.elements['objects']['home']['box_3'].Open(self.elements['windows']['home'], -120, 40+(58+14)*3)
		
		self.elements['objects']['home']['last_box_0'].Open(self.elements['objects']['home']['last_window'], 0, 42)
		self.elements['objects']['home']['last_box_1'].Open(self.elements['objects']['home']['last_window'], 0, 42+30+7)
		self.elements['objects']['home']['last_box_2'].Open(self.elements['objects']['home']['last_window'], 0, 42+(30+7)*2)
		self.elements['objects']['home']['last_box_3'].Open(self.elements['objects']['home']['last_window'], 0, 42+(30+7)*3)
		self.elements['objects']['home']['last_box_4'].Open(self.elements['objects']['home']['last_window'], 0, 42+(30+7)*4)
		self.elements['objects']['home']['last_box_5'].Open(self.elements['objects']['home']['last_window'], 0, 42+(30+7)*5)
		
		for i in xrange(3):
			self.elements['objects']['achievements']['btn_type_%d' % i].SetEvent(ui.__mem_func__(self.SetType), i)

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def SetCategory(self, category):
		self.achievementsPos = 0
		self.category = category
		self.RefreshCategorys()
		if self.category == 0:
			self.elements['windows']['achievements'].Hide()
			self.elements['windows']['home'].Show()
			self.arrows['global_achievements'] = 0
			self.RefreshGlobalProgress()
			self.RefreshLastFinished()
		else:
			self.CreateTypes()
			self.elements['windows']['home'].Hide()
			self.elements['windows']['achievements'].Show()
			self.SetType(0)
			
	def CreateTypes(self):
		self.elements['objects']['achievements']['type_1'] = []
		self.elements['objects']['achievements']['type_2'] = []
		try:
			for i in xrange(len(constInfo.Achievements["achievements"][self.category])):
				if constInfo.Achievements["achievements"][self.category][i][0] < constInfo.Achievements["achievements"][self.category][i][1]:
					self.elements['objects']['achievements']['type_1'].append(constInfo.Achievements["achievements"][self.category][i])
				elif constInfo.Achievements["achievements"][self.category][i][0] >= constInfo.Achievements["achievements"][self.category][i][1]:
					self.elements['objects']['achievements']['type_2'].append(constInfo.Achievements["achievements"][self.category][i])
		except:
			pass

	def __OnClickArrow(self, arrow):
		if arrow == 'CATEGORY_LEFT':
			self.arrows['categorys'] -= 1
			self.RefreshCategorys()
		elif arrow == 'CATEGORY_RIGHT':
			self.arrows['categorys'] += 1
			self.RefreshCategorys()
		elif arrow == 'GLOBAL_UP':
			self.arrows['global_achievements'] -= 1
			self.RefreshGlobalProgress()
		elif arrow == 'GLOBAL_DOWN':
			self.arrows['global_achievements'] += 1
			self.RefreshGlobalProgress()
		elif arrow == 'LAST_UP':
			self.arrows['last_achievements'] -= 1
			self.RefreshLastFinished()
		elif arrow == 'LAST_DOWN':
			self.arrows['last_achievements'] += 1
			self.RefreshLastFinished()

	def SetType(self, type):
		for i in xrange(3):
			self.elements['objects']['achievements']['btn_type_%d' % i].SetUp()
		self.elements['objects']['achievements']['btn_type_%d' % type].Down()
		self.type = type
		self.achievementsPos = 0
		self.elements['objects']['achievements']['scrollbar'].SetPos(0)
		self.RefreshAchievements()
		
	def RefreshGlobalProgress(self):
		self.SetGlobalProgress()
		try:
			for i in xrange(4):
				self.elements['objects']['home']['box_%d' % i].Hide()
		except:
			pass
		try:
			for i in xrange(min(4, len(self.categorys))):
				curCategory = self.categorys[self.arrows['global_achievements'] + i][1]
				self.elements['objects']['home']['box_%d' % i].SetContent(0, self.progress['current_category_%d' % curCategory], self.progress['max_category_%d' % curCategory], 0)
				self.elements['objects']['home']['box_%d' % i].SetTitle(self.categorys[curCategory-1][0])
				self.elements['objects']['home']['box_%d' % i].Show()
		except:
			pass
		
		if (self.categorys > 4):
			if (self.arrows['global_achievements'] <= 0):
				self.elements['objects']['home']['downArrow'].Show()
				self.elements['objects']['home']['upArrow'].Hide()
			elif (self.arrows['global_achievements']+4 < len(self.categorys)):
				self.elements['objects']['home']['downArrow'].Show()
				self.elements['objects']['home']['upArrow'].Show()
			elif (self.arrows['global_achievements']+4 >= len(self.categorys)):
				self.elements['objects']['home']['downArrow'].Hide()
				self.elements['objects']['home']['upArrow'].Show()
		else:
			self.elements['objects']['home']['upArrow'].Hide()
			self.elements['objects']['home']['downArrow'].Hide()
			
	def RefreshLastFinished(self):
		for i in xrange(6):
			self.elements['objects']['home']['last_box_%d' % i].Hide()

		try:
			for i in xrange(min(6, len(constInfo.Achievements['last_achievements']))):
				curAchievement = constInfo.Achievements['last_achievements'][(len(constInfo.Achievements['last_achievements'])-1) - (self.arrows['last_achievements'] + i)]
				if curAchievement[0] == 2 or curAchievement[0] == 3 or curAchievement[0] == 4:
					self.elements['objects']['home']['last_box_%d' % i].SetText(self.GetDescByCat(curAchievement[0]) % (curAchievement[1], nonplayer.GetMonsterName(curAchievement[3])))
				else:
					self.elements['objects']['home']['last_box_%d' % i].SetText(self.GetDescByCat(curAchievement[0]) % curAchievement[1])
				self.elements['objects']['home']['last_box_%d' % i].SetPoints(curAchievement[2])
				self.elements['objects']['home']['last_box_%d' % i].Show()
		except:
			pass
			
		if (len(constInfo.Achievements['last_achievements']) > 6):
			if (self.arrows['last_achievements'] <= 0):
				self.elements['objects']['home']['downArrowLast'].Show()
				self.elements['objects']['home']['upArrowLast'].Hide()
			elif (self.arrows['last_achievements']+6 < len(constInfo.Achievements['last_achievements'])):
				self.elements['objects']['home']['downArrowLast'].Show()
				self.elements['objects']['home']['upArrowLast'].Show()
			elif (self.arrows['last_achievements']+6 >= len(constInfo.Achievements['last_achievements'])):
				self.elements['objects']['home']['downArrowLast'].Hide()
				self.elements['objects']['home']['upArrowLast'].Show()
		else:
			self.elements['objects']['home']['upArrowLast'].Hide()
			self.elements['objects']['home']['downArrowLast'].Hide()
		
	def RefreshCategorys(self):
		try:
			for i in xrange(5):
				self.elements['objects']['category_%d' % i].Hide()
		except:
			pass
		try:
			tmpCategorys = [["General", 0]]
			tmpCategorys += self.categorys
			for i in xrange(min(5, len(tmpCategorys))):
				scrolledId = i + self.arrows['categorys']
				self.elements['objects']['category_%d' % i] = self.CreateCategoryButton(self.board, 35+18+111*i, 94, tmpCategorys[scrolledId][0], self.SetCategory, tmpCategorys[scrolledId][1])
				self.elements['objects']['category_%d' % i].Show()
		except:
			pass
			
		if (len(tmpCategorys) > 5):
			if (self.arrows['categorys'] <= 0):
				self.elements['objects']['rightArrow'].Show()
				self.elements['objects']['leftArrow'].Hide()
			elif (self.arrows['categorys']+5 < len(tmpCategorys)):
				self.elements['objects']['leftArrow'].Show()
				self.elements['objects']['rightArrow'].Show()
			elif (self.arrows['categorys']+5 >= len(tmpCategorys)):
				self.elements['objects']['rightArrow'].Hide()
				self.elements['objects']['leftArrow'].Show()
		else:
			self.elements['objects']['leftArrow'].Hide()
			self.elements['objects']['rightArrow'].Hide()

	def RefreshAchievements(self):
		self.CreateTypes()
		for i in xrange(5):
			self.elements['objects']['achievements']['box_%d' % i].Hide()

		try:
			if self.type == 0:
				achievements = constInfo.Achievements["achievements"][self.category]
			elif self.type == 1:
				achievements = self.elements['objects']['achievements']['type_1']
			elif self.type == 2:
				achievements = self.elements['objects']['achievements']['type_2']
				
			for i in xrange(5):
				curAchievement = achievements[self.achievementsPos + i]
				self.elements['objects']['achievements']['box_%d' % i].SetContent(self.category, curAchievement[0], curAchievement[1], curAchievement[2], curAchievement[3])
				self.elements['objects']['achievements']['box_%d' % i].Show()
		except:
			self.elements['objects']['achievements']['scrollbar'].Hide()
			return
			
		if len(achievements) <= 5:
			self.elements['objects']['achievements']['scrollbar'].Hide()
		else:
			self.elements['objects']['achievements']['scrollbar'].SetMiddleBarSize(float(5)/float(len(achievements)))
			self.elements['objects']['achievements']['scrollbar'].Show()
			
	def __OnScroll(self):
		try:
			if self.type == 0:
				achievementslen = len(constInfo.Achievements["achievements"][self.category])
			elif self.type == 1:
				achievementslen = len(self.elements['objects']['achievements']['type_1'])
			elif self.type == 2:
				achievementslen = len(self.elements['objects']['achievements']['type_2'])
			self.achievementsPos = int(self.elements['objects']['achievements']['scrollbar'].GetPos() * (achievementslen-5))
		except:
			pass
		self.RefreshAchievements()
		
	def SetGlobalProgress(self):
		Finished,inProgress = 0,0
		for i in xrange(len(self.categorys)):
			self.progress['current_category_%d' % self.categorys[i][1]] = 0
			self.progress['max_category_%d' % self.categorys[i][1]] = 0
		for cat in constInfo.Achievements["achievements"]:
			for i in xrange(len(constInfo.Achievements["achievements"][cat])):
				inProgress += 1
				if constInfo.Achievements["achievements"][cat][i][0] >= constInfo.Achievements["achievements"][cat][i][1]:
					self.progress['current_category_%d' % cat] += 1
					Finished += 1
			self.progress['max_category_%d' % cat] = len(constInfo.Achievements["achievements"][cat])
		self.globalProgress.SetProgress(Finished, inProgress)
		
	def SetAchievementFinisehd(self, category, valueReached, points, mobVnum):
		firstLine = 'Has alcanzado un logro:'
		if category == 2 or category == 3 or category == 4:
			secondLine = self.GetDescByCat(category) % (valueReached, nonplayer.GetMonsterName(mobVnum))
		else:
			secondLine = self.GetDescByCat(category) % valueReached
		thirdLine = 'Puntos: %d' % points
		self.finishedAchievement = FinishedAchievementDialog()
		self.finishedAchievement.SetFirstLineText(firstLine)
		self.finishedAchievement.SetSecondLineText(secondLine)
		self.finishedAchievement.SetThirdLineText(thirdLine)
		self.finishedAchievement.Open(10)
		
	def GetDescByCat(self, category):
		return ('Subir al nivel %d','Matar a %dx %s','Matar a %dx %s','Romper %dx %s','Jugar %d minutos','Matar %dx jugadores')[category-1]
		
	def CreateCategoryButton(self, parent, x, y, text, func, arg):
		button = ui.Button()
		button.SetParent(parent)
		button.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		button.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		button.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		button.SetText(text)

		button.SetEvent(ui.__mem_func__(func), arg)
		button.SetPosition(x, y)
		button.Show()
		return button
		
	def Destroy(self):
		self.Close()
		self.ClearDictionary()
		
	def Open(self):
		if not self.isLoaded:
			self.__LoadWindow()
		
		self.SetCategory(0)
		self.SetCenterPosition()
		self.SetTop()
		self.Show()
		
	def Close(self):
		self.Hide()
		return TRUE
		
	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
		
	def OnPressExitKey(self):
		self.Close()
		return TRUE

class AchievementBox(ui.ScriptWindow):
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.data = [0,0]
		self.isLoaded = False
		
	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/achievement_box.py")
		except:
			import exception
			exception.Abort("AchievementBox.LoadWindow.LoadObject")
			
		try:
			self.board = self.GetChild("board")
			self.achievementTitle = self.GetChild("AchievementTitle")
			self.achievementTitle.Hide()
			self.achievementPoints = self.GetChild("AchievementPoints")
			
			self.achievementProgess = AchievementProgressBar()
			self.achievementProgess.SetParent(self)
			self.achievementProgess.SetSize(400, 25)
			self.achievementProgess.SetPosition(15, 18)
			self.achievementProgess.SetProgress(15, 50)
			self.achievementProgess.Show()
		except:
			import exception
			exception.Abort("AchievementBox.LoadWindow.LoadObject")

		self.isLoaded = True
		
	def SetContent(self, category, curValue, maxValue, points, mobVnum = 0):
		self.data = [curValue, maxValue]
		self.achievementProgess.SetProgress(curValue, maxValue)
		if points == 0:
			self.achievementPoints.Hide()
		else:
			self.achievementPoints.SetText('%d' % points)
			self.achievementPoints.Show()
		if category == 0:
			return
		if category == 2 or category == 3 or category == 4:
			self.achievementProgess.SetText(self.GetDescByCat(category) % (maxValue, nonplayer.GetMonsterName(mobVnum)))
		else:	
			self.achievementProgess.SetText(self.GetDescByCat(category) % maxValue)
			
	def SetTitle(self, title):
		self.achievementTitle.SetText(title)
		self.achievementTitle.Show()
		self.achievementProgess.SetSize(350, 20)
		self.achievementProgess.SetPosition(15, 23)
		self.achievementProgess.SetProgress(self.data[0], self.data[1])
		self.achievementProgess.SetProgressPosition(150)
		self.board.SetSize(380, 50)
		self.SetSize(380, 50)
		
	def GetDescByCat(self, category):
		return ('Subir al nivel %d','Matar a %dx %s','Matar a %dx %s','Romper %dx %s','Jugar %d minutos','Matar %dx jugadores')[category-1]
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Open(self, parent, x, y):
		if not self.isLoaded:
			self.LoadWindow()
			
		self.SetParent(parent)
		self.SetPosition(x, y)
		self.SetWindowHorizontalAlignCenter()
		self.Show()

class AchievementProgressBar(ui.Window):

	BACKGROUND_COLOR = grp.GenerateColor(0.0, 0.0, 0.0, 1.0)
	DARK_COLOR = grp.GenerateColor(0.4, 0.4, 0.4, 1.0)
	
	PROGRESS_COLOR = grp.GenerateColor(1.0, 0.0, 0.0, 0.2)
	FINISHED_COLOR = grp.GenerateColor(0.0, 1.0, 0.0, 0.2)
	
	def __init__(self, layer = "UI"):
		ui.Window.__init__(self, layer)

		self.width = 0
		self.height = 0		
		self.progress = 0
		self.isFinished = False
		
		self.textLine = None
		self.textLineExtra = None
		
	def __del__(self):
		ui.Window.__del__(self)

	def SetSize(self, width, height):
		ui.Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def SetProgress(self, current, max):
		try:
			self.progress = min(math.ceil((float(current)/float(max))*100.00), 100)
		except:
			self.progress = 0
		if self.progress == 100:
			self.isFinished = True
		else:
			self.isFinished = False
		
		if not self.textLine:		
			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetOutline()
			textLine.Show()
			self.textLine = textLine
		
		if current > max:
			self.textLine.SetText('%d/%d' % (max, max))
		else:
			self.textLine.SetText('%d/%d' % (current, max))
		self.textLine.SetPosition(170, self.GetHeight()/2)
		self.textLine.SetHorizontalAlignCenter()
		self.textLine.SetWindowHorizontalAlignCenter()
		self.textLine.SetVerticalAlignCenter()
		
	def SetText(self, text):
		if not self.textLineExtra:		
			textLineExtra = ui.TextLine()
			textLineExtra.SetParent(self)
			textLineExtra.SetPosition(12, self.GetHeight()/2)
			textLineExtra.SetVerticalAlignCenter()
			textLineExtra.SetOutline()
			textLineExtra.Show()
			self.textLineExtra = textLineExtra
		
		self.textLineExtra.SetText('%s' % text)
		
	def SetProgressPosition(self, x):
		self.textLine.SetPosition(x, self.GetHeight()/2)

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		
		widthRender = self.width
		heightRender = self.height
		grp.SetColor(self.BACKGROUND_COLOR)
		grp.RenderBar(xRender, yRender, widthRender, heightRender)
		grp.SetColor(self.DARK_COLOR)
		grp.RenderLine(xRender, yRender, widthRender, 0)
		grp.RenderLine(xRender, yRender, 0, heightRender)
		grp.RenderLine(xRender, yRender+heightRender, widthRender+1, 0)
		grp.RenderLine(xRender+widthRender, yRender, 0, heightRender)

		if self.isFinished:
			grp.SetColor(self.FINISHED_COLOR)
		else:
			grp.SetColor(self.PROGRESS_COLOR)
		grp.RenderBar(xRender + 2, yRender + 2, (self.width - 3) * self.progress / 100, heightRender - 3)		

class AchievementLastFinished(ui.Window):

	BOARD_WIDTH = 175-38
	BOARD_HEIGHT = 30
	
	def __init__(self):
		ui.Window.__init__(self)
		
		bg = ui.ResizableTextValue()
		bg.SetParent(self)
		bg.SetPosition(0, 0)
		bg.SetSize(self.BOARD_WIDTH, self.BOARD_HEIGHT)
		bg.SetLine('top')
		bg.SetLine('bottom')
		bg.SetLine('left')
		bg.SetLine('right')
		bg.Show()
		self.Background = bg
		
		points_bg = ui.ResizableTextValue()
		points_bg.SetParent(self.Background)
		points_bg.SetPosition(self.BOARD_WIDTH, 0)
		points_bg.SetSize(38, self.BOARD_HEIGHT)
		points_bg.SetLine('top')
		points_bg.SetLine('bottom')
		points_bg.SetLine('left')
		points_bg.SetLine('right')
		points_bg.Show()
		self.Points = points_bg
		
		self.SetSize(self.BOARD_WIDTH+38, self.BOARD_HEIGHT)
		
	def SetText(self, text):
		tmpText = text
		if len(text) > 27:
			tmpText = '%s...' % text[:24]			
		self.Background.SetToolTipText(text)
		self.Background.SetText(tmpText)
		
	def SetPoints(self, points):			
		self.Points.SetText('+%d' % points)
		
	def __del__(self):
		ui.Window.__del__(self)
		
	def Open(self, parent, x, y):
		self.SetParent(parent)
		self.SetPosition(x, y)
		self.SetWindowHorizontalAlignCenter()
		self.Show()
	
class FinishedAchievementDialog(ui.ScriptWindow):
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/Achievement_finished_dialog.py")

		except:
			import exception
			exception.Abort("FinishedAchievementDialog.LoadDialog.BindObject")
			
		try:
			self.firstLine = self.GetChild("FirstLine")
			self.secondLine = self.GetChild("SecondLine")
			self.thirdLine = self.GetChild("ThirdLine")
		except:
			import exception
			exception.Abort("FinishedAchievementDialog.LoadDialog.BindObject")
			
	def SetFirstLineText(self, text):
		self.firstLine.SetText(text)
		
	def SetSecondLineText(self, text):
		if len(text) > 22:
			text = '%s...' % text[:22]
		self.secondLine.SetText(text)
		
	def SetThirdLineText(self, text):
		self.thirdLine.SetText(text)

	def Open(self, waitTime):
		self.endTime = time.clock() + waitTime
		self.Show()		

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()
		
	def OnUpdate(self):
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
		
	def OnPressExitKey(self):
		self.Close()
		return TRUE
		
class AchievementShopWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = False
		
	def __LoadWindow(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/AchievementShop.py")

		except:
			import exception
			exception.Abort("AchievementShopWindow.LoadDialog.BindObject")
			
		self.categorys = [
			["Armas", 1],
			["Armaduras", 2],
			["Accesorios", 3],
		]
	
		self.arrows = {
			'items' : 1,
			'categorys' : 0,
		}
		
		self.category = 0
	
		self.BindObjects()
		self.BindEvents()
		self.isLoaded = True
		
	def BindObjects(self):
		self.board = self.GetChild("board")
		self.elements = {
			'items' : {
				'bg' : self.GetChild("bgItems"),
				'rightArrow' : self.GetChild("ItemsRightArrow"),
				'leftArrow' : self.GetChild("ItemsLeftArrow"),
				'pageNr' : self.GetChild("PageNumber"),
				'box_0' : ItemBox(),
				'box_1' : ItemBox(),
				'box_2' : ItemBox(),
				'box_3' : ItemBox(),
				'box_4' : ItemBox(),
				'box_5' : ItemBox(),
				'box_6' : ItemBox(),
				'box_7' : ItemBox(),
				'box_8' : ItemBox(),
			},
			'categorys' : {
				'bg' : self.GetChild("bgCategorys"),
				'upArrow' : self.GetChild("CategorysUpArrow"),
				'downArrow' : self.GetChild("CategorysDownArrow"),
			},
			'achievementPoints' : self.GetChild("APSlot"),
		}
		
	def BindEvents(self):
		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		
		self.elements['items']['box_0'].Open(self.elements['items']['bg'], 10, 18)
		self.elements['items']['box_1'].Open(self.elements['items']['bg'], 10+200+10, 18)
		self.elements['items']['box_2'].Open(self.elements['items']['bg'], 10+(200+10)*2, 18)
		self.elements['items']['box_3'].Open(self.elements['items']['bg'], 10, 18+122)
		self.elements['items']['box_4'].Open(self.elements['items']['bg'], 10+200+10, 18+122)
		self.elements['items']['box_5'].Open(self.elements['items']['bg'], 10+(200+10)*2, 18+122)
		self.elements['items']['box_6'].Open(self.elements['items']['bg'], 10, 18+122*2)
		self.elements['items']['box_7'].Open(self.elements['items']['bg'], 10+200+10, 18+122*2)
		self.elements['items']['box_8'].Open(self.elements['items']['bg'], 10+(200+10)*2, 18+122*2)
		
		self.elements['categorys']['upArrow'].SetEvent(ui.__mem_func__(self.__OnClickArrowButton), 'CATEGORY_UP')
		self.elements['categorys']['downArrow'].SetEvent(ui.__mem_func__(self.__OnClickArrowButton), 'CATEGORY_DOWN')
		self.elements['items']['rightArrow'].SetEvent(ui.__mem_func__(self.__OnClickArrowButton), 'ITEMS_RIGHT')
		self.elements['items']['leftArrow'].SetEvent(ui.__mem_func__(self.__OnClickArrowButton), 'ITEMS_LEFT')
		
	def __OnClickArrowButton(self, arrow):
		if arrow == 'CATEGORY_UP':
			self.arrows['categorys'] -= 1
			self.RefreshCategorys()
		elif arrow == 'CATEGORY_DOWN':
			self.arrows['categorys'] += 1
			self.RefreshCategorys()
		elif arrow == 'ITEMS_LEFT':
			self.arrows['items'] -= 1
			self.RefreshItems()
		elif arrow == 'ITEMS_RIGHT':
			self.arrows['items'] += 1
			self.RefreshItems()
		
	def RefreshCategorys(self):
		try:
			for i in xrange(12):
				self.elements['categorys']['category_%d' % i].Hide()
		except:
			pass
		try:
			for i in xrange(min(12, len(self.categorys))):
				scrolledId = i + self.arrows['categorys']
				self.elements['categorys']['category_%d' % i] = self.CreateCategoryButton(self.elements['categorys']['bg'], 0, 35+30*i, self.categorys[scrolledId][0], self.SetCategory, self.categorys[scrolledId][1])
				self.elements['categorys']['category_%d' % i].SetWindowHorizontalAlignCenter()
				self.elements['categorys']['category_%d' % i].Show()
		except:
			pass
			
		if (len(self.categorys) > 12):
			if (self.arrows['categorys'] <= 0):
				self.elements['categorys']['downArrow'].Show()
				self.elements['categorys']['upArrow'].Hide()
			elif (self.arrows['categorys']+12 < len(self.categorys)):
				self.elements['categorys']['upArrow'].Show()
				self.elements['categorys']['downArrow'].Show()
			elif (self.arrows['categorys']+12 >= len(self.categorys)):
				self.elements['categorys']['downArrow'].Hide()
				self.elements['categorys']['upArrow'].Show()
		else:
			self.elements['categorys']['upArrow'].Hide()
			self.elements['categorys']['downArrow'].Hide()
			
	def CreateCategoryButton(self, parent, x, y, text, func, arg):
		button = ui.Button()
		button.SetParent(parent)
		button.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		button.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		button.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		button.SetText(text)
		button.SetEvent(ui.__mem_func__(func), arg)
		button.SetPosition(x, y)
		button.Show()
		return button

	def SetCategory(self, cat):
		self.category = cat
		self.arrows['items'] = 1
		self.RefreshItems()
		
	def RefreshItems(self):
		currentPage = self.arrows['items']
		for i in xrange(9):
			self.elements['items']['box_%d' % i].Hide()

		try:
			for i in xrange(min(9, len(constInfo.Achievements['achievementshop'][self.category])-currentPage*9+9)):
				curItem = constInfo.Achievements['achievementshop'][self.category][i+(currentPage-1)*9]
				self.elements['items']['box_%d' % i].SetContent(curItem[0], curItem[1], curItem[2])
				self.elements['items']['box_%d' % i].Show()
		except:
			self.elements['items']['rightArrow'].Hide()
			self.elements['items']['leftArrow'].Hide()
			self.elements['items']['pageNr'].Hide()
			return
			
		maxPage = math.ceil(float(len(constInfo.Achievements['achievementshop'][self.category]))/float(9))
		if maxPage >= 1:
			self.elements['items']['pageNr'].SetText('%d/%d' % (currentPage, maxPage))
			self.elements['items']['pageNr'].Show()
		else:
			self.elements['items']['pageNr'].Hide()
		
		if currentPage * 9 >= len(constInfo.Achievements['achievementshop'][self.category]):
			self.elements['items']['rightArrow'].Hide()
		else:
			self.elements['items']['rightArrow'].Show()

		if currentPage > 1:
			self.elements['items']['leftArrow'].Show()
		else:
			self.elements['items']['leftArrow'].Hide()
	
	def OnUpdate(self):
		self.elements['achievementPoints'].SetText("%d AP's" % constInfo.Achievements['POINTS'])
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Close(self):
		self.Hide()
		
	def Open(self):
		if not self.isLoaded:
			self.__LoadWindow()

		self.SetCategory(1)
		self.RefreshCategorys()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

class ItemBox(ui.ScriptWindow):
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.id = 0
		self.data = [0, 0]
		self.isLoaded = False
		
	def __LoadWindow(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/AchievementShop_ItemBox.py")

		except:
			import exception
			exception.Abort("AchievementShop_ItemBox.LoadDialog.BindObject")
			
		self.itemName = self.GetChild("ItemName")
		self.itemIcon = self.GetChild("ItemIcon")
		self.itemPrice = self.GetChild("ItemPrice")
		self.itemAmount = self.GetChild("ItemAmount")
		self.buyButton = self.GetChild("BuyButton")
		self.toolTip = uiToolTip.ItemToolTip()
		self.toolTip.HideToolTip()
		
		self.itemIcon.SAFE_SetStringEvent("MOUSE_OVER_IN", self.toolTip.ShowToolTip)
		self.itemIcon.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.toolTip.HideToolTip)
		
		self.BuyQuestion = uiCommon.QuestionDialog()
		self.BuyQuestion.SetAcceptEvent(lambda arg = TRUE: self.AnswerBuyItem(arg))
		self.BuyQuestion.SetCancelEvent(lambda arg = FALSE: self.AnswerBuyItem(arg))
		
		self.buyButton.SetEvent(ui.__mem_func__(self.__OnClickBuyButton))
		self.isLoaded = True
		
	def SetContent(self, id, vnum, price):
		self.id = id
		self.data = [vnum, price]
		item.SelectItem(vnum)
		
		self.itemName.SetText(item.GetItemName())
		self.itemIcon.LoadImage(item.GetIconImageFileName())
		self.itemIcon.SetPosition(35, (46,32,25)[item.GetItemSize()[1]-1])
		self.itemIcon.SetScale(1, (1,1,0.8)[item.GetItemSize()[1]-1])
		self.itemPrice.SetText('Precio: %d %s' % (price, "AP's"))
		self.itemAmount.KillFocus()
		
		if item.IsFlag(4) == 1:
			self.GetChild("ItemAmountSlot").Show()
		else:
			self.GetChild("ItemAmountSlot").Hide()
		
		self.toolTip.ClearToolTip()
		self.toolTip.AddItemData(vnum, [0,0,0])
		self.toolTip.HideToolTip()
		
	def __OnClickBuyButton(self):
		self.itemAmount.KillFocus()
		amount = self.itemAmount.GetText()

		if amount == '1':
			self.BuyQuestion.SetText("Quieres comprar %s por %d %s?" % (self.itemName.GetText(), self.data[1], "AP's"))
		else:
			self.BuyQuestion.SetText("Quieres comprar %sx %s por %d %s?" % (amount, self.itemName.GetText(), self.data[1]*int(amount), "AP's"))
		self.BuyQuestion.Open()
		
	def AnswerBuyItem(self, arg):
		if arg:
			constInfo.Achievements['QCMD'] = 'BUY_ITEM#%d#%s' % (self.id, self.itemAmount.GetText())
			event.QuestButtonClick(constInfo.Achievements['QID'])
		self.BuyQuestion.Close()
		
	def OnUpdate(self):
		if not self.itemAmount.IsFocus() and (self.itemAmount.GetText() == '' or self.itemAmount.GetText() == '0'):
			self.itemAmount.SetText('1')
		if int(self.itemAmount.GetText()) > 200:
			self.itemAmount.SetText('200')
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self, parent, x, y):
		if not self.isLoaded:
			self.__LoadWindow()
			
		self.SetParent(parent)
		self.SetPosition(x, y)
		self.SetTop()
		self.Show()
		
