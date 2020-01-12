##Ara:

		self.questShowingStartIndex = 0
		self.questScrollBar = None
		self.questSlot = None
		self.questNameList = None
		self.questLastTimeList = None
		self.questLastCountList = None
		
##Deðiþtir:

		#self.questShowingStartIndex = 0
		#self.questScrollBar = None
		#self.questSlot = None
		#self.questNameList = None
		#self.questLastTimeList = None
		#self.questLastCountList = None

##Ara:

		self.questShowingStartIndex = 0
		self.questScrollBar = self.GetChild("Quest_ScrollBar")
		self.questScrollBar.SetScrollEvent(ui.__mem_func__(self.OnQuestScroll))
		self.questSlot = self.GetChild("Quest_Slot")
		for i in xrange(quest.QUEST_MAX_NUM):
			self.questSlot.HideSlotBaseImage(i)
			self.questSlot.SetCoverButton(i,\
											"d:/ymir work/ui/game/quest/slot_button_01.sub",\
											"d:/ymir work/ui/game/quest/slot_button_02.sub",\
											"d:/ymir work/ui/game/quest/slot_button_03.sub",\
											"d:/ymir work/ui/game/quest/slot_button_03.sub", True)

		self.questNameList = []
		self.questLastTimeList = []
		self.questLastCountList = []
		for i in xrange(quest.QUEST_MAX_NUM):
			self.questNameList.append(self.GetChild("Quest_Name_0" + str(i)))
			self.questLastTimeList.append(self.GetChild("Quest_LastTime_0" + str(i)))
			self.questLastCountList.append(self.GetChild("Quest_LastCount_0" + str(i)))

##Depiþtir:

		#self.questShowingStartIndex = 0
		#self.questScrollBar = self.GetChild("Quest_ScrollBar")
		#self.questScrollBar.SetScrollEvent(ui.__mem_func__(self.OnQuestScroll))
		#self.questSlot = self.GetChild("Quest_Slot")
		#for i in xrange(quest.QUEST_MAX_NUM):
		#	self.questSlot.HideSlotBaseImage(i)
		#	self.questSlot.SetCoverButton(i,\
		#									"d:/ymir work/ui/game/quest/slot_button_01.sub",\
		#									"d:/ymir work/ui/game/quest/slot_button_02.sub",\
		#									"d:/ymir work/ui/game/quest/slot_button_03.sub",\
		#									"d:/ymir work/ui/game/quest/slot_button_03.sub", True)

		#self.questNameList = []
		#self.questLastTimeList = []
		#self.questLastCountList = []
		#for i in xrange(quest.QUEST_MAX_NUM):
		#	self.questNameList.append(self.GetChild("Quest_Name_0" + str(i)))
		#	self.questLastTimeList.append(self.GetChild("Quest_LastTime_0" + str(i)))
		#	self.questLastCountList.append(self.GetChild("Quest_LastCount_0" + str(i)))


##Ara:

	## Quest
	def __SelectQuest(self, slotIndex):
		questIndex = quest.GetQuestIndex(self.questShowingStartIndex+slotIndex)

		import event
		event.QuestButtonClick(-2147483648 + questIndex)
		
## Depiþtir:

	## Quest
	#def __SelectQuest(self, slotIndex):
		#questIndex = quest.GetQuestIndex(self.questShowingStartIndex+slotIndex)

		#import event
		#event.QuestButtonClick(-2147483648 + questIndex)
		
		
		
##Ara:

		questCount = quest.GetQuestCount()
		questRange = range(quest.QUEST_MAX_NUM)

		if questCount > quest.QUEST_MAX_NUM:
			self.questScrollBar.Show()
		else:
			self.questScrollBar.Hide()

		for i in questRange[:questCount]:
			(questName, questIcon, questCounterName, questCounterValue) = quest.GetQuestData(self.questShowingStartIndex+i)

			self.questNameList[i].SetText(questName)
			self.questNameList[i].Show()
			self.questLastCountList[i].Show()
			self.questLastTimeList[i].Show()

			if len(questCounterName) > 0:
				self.questLastCountList[i].SetText("%s : %d" % (questCounterName, questCounterValue))
			else:
				self.questLastCountList[i].SetText("")

			## Icon
			self.questSlot.SetSlot(i, i, 1, 1, questIcon)

		for i in questRange[questCount:]:
			self.questNameList[i].Hide()
			self.questLastTimeList[i].Hide()
			self.questLastCountList[i].Hide()
			self.questSlot.ClearSlot(i)
			self.questSlot.HideSlotBaseImage(i)

		self.__UpdateQuestClock()

	def __UpdateQuestClock(self):
		if "QUEST" == self.state:
			 QUEST_LIMIT_COUNT_BUG_FIX
			for i in xrange(min(quest.GetQuestCount(), quest.QUEST_MAX_NUM)):
			 END_OF_QUEST_LIMIT_COUNT_BUG_FIX
				(lastName, lastTime) = quest.GetQuestLastTime(i)

				clockText = localeInfo.QUEST_UNLIMITED_TIME
				if len(lastName) > 0:

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

				self.questLastTimeList[i].SetText(clockText)
				
##Deðiþtir:

		#questCount = quest.GetQuestCount()
		#questRange = range(quest.QUEST_MAX_NUM)

		#if questCount > quest.QUEST_MAX_NUM:
			#self.questScrollBar.Show()
		#else:
			#self.questScrollBar.Hide()

		#for i in questRange[:questCount]:
			#(questName, questIcon, questCounterName, questCounterValue) = quest.GetQuestData(self.questShowingStartIndex+i)

			#self.questNameList[i].SetText(questName)
			#self.questNameList[i].Show()
			#self.questLastCountList[i].Show()
			#self.questLastTimeList[i].Show()

			#if len(questCounterName) > 0:
				#self.questLastCountList[i].SetText("%s : %d" % (questCounterName, questCounterValue))
			#else:
				#self.questLastCountList[i].SetText("")

			## Icon
			#self.questSlot.SetSlot(i, i, 1, 1, questIcon)

		#for i in questRange[questCount:]:
			#self.questNameList[i].Hide()
			#self.questLastTimeList[i].Hide()
			#self.questLastCountList[i].Hide()
			#self.questSlot.ClearSlot(i)
			#self.questSlot.HideSlotBaseImage(i)

		#self.__UpdateQuestClock()

	#def __UpdateQuestClock(self):
		#if "QUEST" == self.state:
			# QUEST_LIMIT_COUNT_BUG_FIX
			#for i in xrange(min(quest.GetQuestCount(), quest.QUEST_MAX_NUM)):
			# END_OF_QUEST_LIMIT_COUNT_BUG_FIX
				#(lastName, lastTime) = quest.GetQuestLastTime(i)

				#clockText = localeInfo.QUEST_UNLIMITED_TIME
				#if len(lastName) > 0:

					#if lastTime <= 0:
						#clockText = localeInfo.QUEST_TIMEOVER

					#else:
						#questLastMinute = lastTime / 60
						#questLastSecond = lastTime % 60

						#clockText = lastName + " : "

						#if questLastMinute > 0:
							#clockText += str(questLastMinute) + localeInfo.QUEST_MIN
							#if questLastSecond > 0:
								#clockText += " "

						#if questLastSecond > 0:
							#clockText += str(questLastSecond) + localeInfo.QUEST_SEC

				#self.questLastTimeList[i].SetText(clockText)
				
#Ara:
	def OnUpdate(self):
		self.__UpdateQuestClock()

#Deðiþtir:

	def OnUpdate(self):
		self.questCategory.OnUpdate()
		#self.__UpdateQuestClock()
		
		
#Ara:

	def OnQuestScroll(self):
		questCount = quest.GetQuestCount()
		scrollLineCount = max(0, questCount - quest.QUEST_MAX_NUM)
		startIndex = int(scrollLineCount * self.questScrollBar.GetPos())

		if startIndex != self.questShowingStartIndex:
			self.questShowingStartIndex = startIndex
			self.RefreshQuest()
			
#Deðiþtir:

	#def OnQuestScroll(self):
		#questCount = quest.GetQuestCount()
		#scrollLineCount = max(0, questCount - quest.QUEST_MAX_NUM)
		#startIndex = int(scrollLineCount * self.questScrollBar.GetPos())

		#if startIndex != self.questShowingStartIndex:
			#self.questShowingStartIndex = startIndex
			#self.RefreshQuest()
