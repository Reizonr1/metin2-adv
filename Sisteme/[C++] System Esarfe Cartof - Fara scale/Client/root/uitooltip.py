""""""
#1) Search: def __AppendAttributeInformation(self, attrSlot):
#2) After their function make a new line and paste:
	def __AppendAcceAttributeInformation(self, attrSlot):
		if 0 != attrSlot:
			hasAttack = 0
			hasMagicAttack = 0
			minPower = 0
			maxPower = 0
			minMagicAttackPower = 0
			maxMagicAttackPower = 0
			
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				if i <= 6:
					continue
				else:
					type = attrSlot[i][0]
					value = attrSlot[i][1]
					if 0 == value:
						continue
					
					if type == 53 and i == 8:
						hasAttack = 1
						minPower = value
					elif type == 53 and i == 9:
						hasAttack = 1
						maxPower = value
					elif type == 55 and i == 10:
						hasMagicAttack = 1
						minMagicAttackPower = value
					elif type == 55 and i == 11:
						hasMagicAttack = 1
						maxMagicAttackPower = value
			
			if hasAttack == 1:
				self.__AppendAttackAccePowerInfo(minPower, maxPower)
			
			if hasMagicAttack == 1:
				self.__AppendMagicAttackAcceInfo(minMagicAttackPower, maxMagicAttackPower)
			
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				if i <= 6 or i >= 8 and i <= 11:
					continue
				else:
					type = attrSlot[i][0]
					value = attrSlot[i][1]
					if 0 == value:
						continue
					
					affectString = self.__GetAffectString(type, value)
					if affectString:
						affectColor = self.__GetAttributeColor(i, value)
						self.AppendTextLine(affectString, affectColor)
			
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				if i >= 7:
					continue
				else:
					type = attrSlot[i][0]
					value = attrSlot[i][1]
					if 0 == value:
						continue
					
					affectString = self.__GetAffectString(type, value)
					if affectString:
						affectColor = self.__GetAttributeColor(i, value)
						self.AppendTextLine(affectString, affectColor)

	def __AppendAttackAccePowerInfo(self, minPower, maxPower):
		minPower_final = minPower
		maxPower_final = maxPower
		if maxPower > minPower:
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_POWER % (minPower_final, maxPower_final), self.POSITIVE_COLOR)
		else:
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_POWER_ONE_ARG % (minPower_final), self.POSITIVE_COLOR)

	def __AppendMagicAttackAcceInfo(self, minMagicAttackPower, maxMagicAttackPower):
		minMagicAttackPower_final = minMagicAttackPower
		maxMagicAttackPower_final = maxMagicAttackPower
		if minMagicAttackPower_final > 0 or maxMagicAttackPower_final > 0:
			if maxMagicAttackPower_final > minMagicAttackPower_final:
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_ATT_POWER % (minMagicAttackPower_final, maxMagicAttackPower_final), self.POSITIVE_COLOR)
			else:
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_ATT_POWER_ONE_ARG % (minMagicAttackPower_final), self.POSITIVE_COLOR)
""""""

""""""
#1) Search: def __GetAttributeColor(self, index, value):
#2) Delete their function and paste:
	def __GetAttributeColor(self, index, value):
		if value > 0:
			if index >= 5 and index <= 6:
				return self.SPECIAL_POSITIVE_COLOR2
			elif index >= 7:
				return self.POSITIVE_COLOR
			else:
				return self.SPECIAL_POSITIVE_COLOR
		elif value == 0:
			return self.NORMAL_COLOR
		else:
			return self.NEGATIVE_COLOR
""""""

""""""
#1) Search: isCostumeBody = 0
#2) Make a new line and paste:
isCostumeAcce = 0
""""""

""""""
#1) Search: isCostumeBody = item.COSTUME_TYPE_BODY == itemSubType
#2) Make a new line and paste:
isCostumeAcce = item.COSTUME_TYPE_ACCE == itemSubType
""""""

""""""
#1) Search: elif 0 != isCostumeItem:
#2) Delete their function and paste:
		elif 0 != isCostumeItem:
			self.__AppendLimitInformation()
			self.__AppendAffectInformation()
			if isCostumeAcce != 0:
				self.__AppendAcceAttributeInformation(attrSlot)
			else:
				self.__AppendAttributeInformation(attrSlot)
			
			self.AppendWearableInformation()
			bHasRealtimeFlag = 0
			for i in xrange(item.LIMIT_MAX_NUM):
				(limitType, limitValue) = item.GetLimit(i)
				if item.LIMIT_REAL_TIME == limitType:
					bHasRealtimeFlag = 1
			
			if 1 == bHasRealtimeFlag:
				self.AppendMallItemLastTime(metinSlot[0])
			
			if isCostumeAcce != 0:
				if metinSlot != 0:
					absChance = int(metinSlot[1])
					if absChance > 0:
						self.AppendSpace(5)
						self.AppendTextLine(localeInfo.ACCE_ABSORB_CHANCE % (absChance), self.CONDITION_COLOR)
""""""