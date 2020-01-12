	# COSTUME_SYSTEM
	def __Wear(self, type, vnum):
		if str(type) == "armor":
			if str(vnum) == "0":
				constInfo.COSTUME_ARMOR = 0
			else:
				constInfo.COSTUME_ARMOR = vnum
		elif str(type) == "hair":
			if str(vnum) == "0":
				constInfo.COSTUME_HAIR = 0
			else:
				constInfo.COSTUME_HAIR = vnum
			
	def __QuestDeclare(self, quest, id):
		if str(quest) == "armor":
			constInfo.COSTUME_ARMOR_QUEST = id
		elif str(quest) == "hair":
			constInfo.COSTUME_HAIR_QUEST = id
		
	# END_OF_COSTUME_SYSTEM
		

	def __ServerCommand_Build(self):
		serverCommandList={
			
			# COSTUME_SYSTEM
			"Wear"				: self.__Wear,
			"QuestDeclare"		: self.__QuestDeclare,
			# END_OF_COSTUME_SYSTEM