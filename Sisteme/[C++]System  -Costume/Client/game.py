Search for:
	serverCommandList={
down write:

			"costume"				: self.costume,
			"costume1"				: self.costume1,
			"costume"				: self.__costume_load,
			
in the end of game.py write:

	def __costume_load(self, value):
		constInfo.QUEST_INDEX_06 = int(value)
		
	def costume(self, qid):
		constInfo.costume = int(qid)
		
	def costume1(self, qid):
		constInfo.costume11 = int(qid)