#Search:

def chop(n):
	return round(n - 0.5, 1)

#Add After:

	
def pointop(n):
	t = int(n)
	if t / 10 < 1:
		return "0."+n
	else:		
		return n[0:len(n)-1]+"."+n[len(n)-1:]

#Search:
	def AddItemData(self, itemVnum, metinSlot, attrSlot = 0, flags = 0, unbindTime = 0):

#Before ADD:
		
	def check_sigillo(self, item_vnum):
		for x in range(55701,55705):
			if x == item_vnum:
				return TRUE	
		if item_vnum == 55801:
			return TRUE
		return FALSE
		
#Search:
		### Hair Preview Image ###
		if self.__IsHair(itemVnum):	
			self.__AppendHairIcon(itemVnum)

		### Description ###
		self.AppendDescription(itemDesc, 26)
		self.AppendDescription(itemSummary, 26, self.CONDITION_COLOR)

#ADD After:

		
		if self.check_sigillo(itemVnum) or itemVnum == 55002:
			if attrSlot[0][1] != 0:
				self.AppendSpace(5)
				self.AppendTextLine("Level: "+str(metinSlot[1]), self.NORMAL_COLOR)
				self.AppendTextLine("Hp: +"+pointop(str(attrSlot[0][1]))+"%", self.SPECIAL_POSITIVE_COLOR)
				self.AppendTextLine("Def: +"+pointop(str(attrSlot[1][1]))+"%", self.SPECIAL_POSITIVE_COLOR)
				self.AppendTextLine("Sp: +"+pointop(str(attrSlot[2][1]))+"%", self.SPECIAL_POSITIVE_COLOR)
				self.AppendSpace(5)
				if itemVnum != 55002:
					days = (int(attrSlot[3][1])/60)/24
					hours = (int(attrSlot[3][1]) - (days*60*24)) / 60
					mins = int(attrSlot[3][1]) - (days*60*24) - (hours*60)
					self.AppendTextLine("Durata: %d Zile %d Ore %d Minute" % (days, hours, mins), self.SPECIAL_POSITIVE_COLOR)
