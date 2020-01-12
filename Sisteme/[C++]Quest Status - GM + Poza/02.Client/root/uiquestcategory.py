import ui
import quest
import localeInfo
import grp
import event

class QuestCategoryWindow(ui.Window):

	MAX_CATEGORY = 6
	MAX_QUEST = 7
	MAX_CATEGORY_SIZE = 304

	class QuestList(ui.Window):
		def __init__(self, parent):
			ui.Window.__init__(self)

			self.__questList = {}
			self.__parentWnd = parent
			self.__startIndex = 0

		def __del__(self):
			del self.__questList
			del self.__parentWnd
			del self.__startIndex
			ui.Window.__del__(self)

		def Open(self):
			count = self.GetCount()
			if count > QuestCategoryWindow.MAX_QUEST:
				count = QuestCategoryWindow.MAX_QUEST

			for i in xrange(count):
				self.__questList[i].Show()
			self.RefreshQuest()

		def Close(self):
			for i in xrange(len(self.__questList)):
				self.__questList[i].Hide()

		def AppendItem(self, questName, questIndex):
			for i in xrange(len(self.__questList)):
				if self.__questList[i].text.GetText() == questName and self.__questList[i].questIndex == questIndex:
					return

			bar = ui.Bar()
			bar.SetParent(self.__parentWnd)
			bar.SetSize(100, 10)
			bar.SetColor(grp.GenerateColor(1.0, 1.0, 1.0, 0.0))
			bar.OnMouseLeftButtonDown = lambda x=len(self.__questList), arg=questIndex: self.__SelectQuest(x, arg)
			bar.Hide()

			bar.btn = ui.Button()
			bar.btn.SetParent(bar)
			bar.btn.SetUpVisual("Other/questcategory/quest_checkbox.tga")
			bar.btn.SetOverVisual("Other/questcategory/quest_checkbox.tga")
			bar.btn.SetDownVisual("Other/questcategory/quest_checkbox.tga")
			bar.btn.SetPosition(0, 0)
			bar.btn.Show()

			bar.checked = ui.ImageBox()
			bar.checked.SetParent(bar.btn)
			bar.checked.LoadImage("Other/questcategory/quest_checked.tga")
			bar.checked.SetPosition(0,-2)
			bar.checked.Hide()

			bar.text = ui.TextLine()
			bar.text.SetParent(bar)
			bar.text.SetText(questName)
			bar.text.SetPosition(15, -2)
			bar.text.SetWindowHorizontalAlignLeft()
			bar.text.SetHorizontalAlignLeft()
			bar.text.Show()

			bar.text.clock = ui.TextLine()
			bar.text.clock.SetParent(bar.text)
			bar.text.clock.SetText(localeInfo.QUEST_UNLIMITED_TIME)
			bar.text.clock.SetPosition(5,10)
			bar.text.clock.SetWindowHorizontalAlignLeft()
			bar.text.clock.SetHorizontalAlignLeft()
			bar.text.clock.Show()

			bar.text.counter = ui.TextLine()
			bar.text.counter.SetParent(bar.text)
			bar.text.counter.SetText("")
			bar.text.counter.SetPosition(5,20)
			bar.text.counter.SetWindowHorizontalAlignLeft()
			bar.text.counter.SetHorizontalAlignLeft()
			bar.text.counter.Show()

			bar.questIndex = questIndex

			self.__questList[len(self.__questList)] = bar

		def SetPosition(self, x, y):
			for i in xrange(len(self.__questList)):
				self.__questList[i].SetPosition(x, y + i*30)

		def GetCount(self):
			return len(self.__questList)

		def GetHeight(self):
			return self.GetCount() * 30

		def SetClockText(self, questIdx, text):
			self.__questList[questIdx].text.clock.SetText(text)

		def SetCounterText(self, questIdx, text):
			self.__questList[questIdx].text.counter.SetText(text)

		def __SelectQuest(self, qIdx, questIndex):
			self.__questList[qIdx].checked.Show()
			event.QuestButtonClick(questIndex)

		def RefreshQuest(self):
			questCount = self.GetCount()

			for i in xrange(questCount):
				(questName, questIcon, questCounterName, questCounterValue) = quest.GetQuestData(i)

				if i >= questCount or i >= QuestCategoryWindow.MAX_QUEST:
					break

				if questCounterName != "":
					self.SetCounterText(i, "%s : %d" % (questCounterName, questCounterValue))
				else:
					self.SetCounterText(i, "")

				self.RefreshClock()

		def RefreshClock(self):
			for i in xrange(self.GetCount()):
				try:
					(lastName, lastTime) = quest.GetQuestLastTime(i)

					clockText = ""
					if len(lastName) > 0:
						clockText = localeInfo.QUEST_UNLIMITED_TIME
						if lastTime <= 0:
							clockText = localeInfo.QUEST_TIMEOVER
						else:
							questLastMinute = lastTime / 60
							questLastSecond = lastTime % 60

							clockText = lastName + " : "

							if questLastMinute > 0:
								clockText += str(questLastMinute) + localeInfo.QUEST_MIN
								if questLastSecond > 0:
									clockText += " "

							if questLastSecond > 0:
								clockText += str(questLastSecond) + localeInfo.QUEST_SEC

					if len(clockText) > 0:
						self.SetClockText(i, clockText)
					else:
						self.SetClockText(i, localeInfo.QUEST_UNLIMITED_TIME)
				except:
					pass

	def __init__(self, parent):
		ui.Window.__init__(self)
		self.SetParent(parent)
		self.__questCategorySlot = []
		self.__questList = {}

		self.__MakeCategorySlot(parent)

	def __del__(self):
		del self.__questCategorySlot
		del self.__questList
		ui.Window.__del__(self)

	def __MakeCategorySlot(self, parent):
		for i in xrange(self.MAX_CATEGORY):
			self.__questCategorySlot.append(ui.Button())
			self.__questCategorySlot[i].SetParent(parent)
			self.__questCategorySlot[i].SetPosition(7, 5 + i*20)
			self.__questCategorySlot[i].SetSize(253, 23)
			self.__questCategorySlot[i].SetUpVisual("Other/questcategory/quest_category.tga")
			self.__questCategorySlot[i].SetOverVisual("Other/questcategory/quest_category.tga")
			self.__questCategorySlot[i].SetDownVisual("Other/questcategory/quest_category.tga")
			self.__questCategorySlot[i].SetTextAlignLeft("%s (0)" % getattr(localeInfo, "QUESTCATEGORY_%d" % i))
			self.__questCategorySlot[i].SetTextColor(0xFFFFE3AD)
			self.__questCategorySlot[i].SAFE_SetEvent(self.__OnClickQuestCategory, i)
			self.__questCategorySlot[i].Show()
			self.__questCategorySlot[i].openImage = ui.Button()
			self.__questCategorySlot[i].openImage.SetParent(self.__questCategorySlot[i])
			self.__questCategorySlot[i].openImage.SetUpVisual("Other/questcategory/quest_category_open.tga")
			self.__questCategorySlot[i].openImage.SetOverVisual("Other/questcategory/quest_category_open.tga")
			self.__questCategorySlot[i].openImage.SetDownVisual("Other/questcategory/quest_category_close.tga")
			self.__questCategorySlot[i].openImage.SetPosition(10,5)
			self.__questCategorySlot[i].openImage.SAFE_SetEvent(self.__OnClickQuestCategory, i)
			self.__questCategorySlot[i].openImage.Show()

			self.__questList[i] = self.QuestList(parent)
			self.__questList[i].Close()

	def __IsCategoryOpen(self, categoryIndex):
		return self.__questCategorySlot[categoryIndex].openImage.IsDown()

	def __CloseCategories(self):
		for i in xrange(self.MAX_CATEGORY):
			self.__questList[i].Close()
			self.__questCategorySlot[i].openImage.SetUp()
			self.__questCategorySlot[i].SetPosition(7, 5 + i*20)

	def __GetOpenedCategories(self):
		indexes = []
		for i in xrange(self.MAX_CATEGORY):
			if self.__IsCategoryOpen(i):
				indexes.append(i)
		return indexes

	def __ArrangeQuestListPosition(self):
		for i in xrange(self.MAX_CATEGORY):
			(x,y) = self.__questCategorySlot[i].GetLocalPosition()
			self.__questList[i].SetPosition(20, y + 20)

	def __OnClickQuestCategory(self, categoryIndex):
		isAlreadyOpen = self.__IsCategoryOpen(categoryIndex)
		self.__CloseCategories()

		if isAlreadyOpen:
			return

		self.__questCategorySlot[categoryIndex].openImage.Down()
		(x,y) = self.__questCategorySlot[categoryIndex].GetLocalPosition()
		self.__questList[categoryIndex].SetPosition(20, y + 20)
		self.__questList[categoryIndex].Open()

		btnCount = self.__questList[categoryIndex].GetCount()

		if btnCount <= 0:
			return

		listHeight = self.__questList[categoryIndex].GetHeight() * len(self.__GetOpenedCategories())
		for i in xrange(categoryIndex+1, self.MAX_CATEGORY):
			slotY = listHeight + (5 + i*20)
			self.__questCategorySlot[i].SetPosition(7, slotY)
			self.__questList[i].SetPosition(20, slotY + 20)

	def RecvQuest(self, func, index, name):
		try:
			category = int(name[0])
			name = name[1:]
		except:
			category = 0

		if func:
			func(index, name, "file", localeInfo.GetLetterImageName())

		self.__questList[category].AppendItem(name, index)
		self.__questCategorySlot[category].SetTextAlignLeft("%s (%d)" % (getattr(localeInfo, "QUESTCATEGORY_%d" % category), self.__questList[category].GetCount()))

	def OnUpdate(self):
		for i in xrange(self.MAX_CATEGORY):
			self.__questList[i].RefreshClock()
