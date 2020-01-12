#Search:
	SPECIAL_POSITIVE_COLOR2 = grp.GenerateColor(0.8824, 0.9804, 0.8824, 1.0)
#Add after:	
	ITEM_BUFF_LEVEL_COLOR = 0xffffd300
	ITEM_BUFF_TYPE_COLOR = 0xfffc9c3a
	ITEM_BUFF_RATE_COLOR = 0xff40e0d0
	ITEM_BUFF_DURATION_COLOR = 0xffadff00
	ITEM_BUFF_USAGE_COLOR = 0xffffffff	
#Search:
			elif itemVnum in WARP_SCROLLS:
				if 0 != metinSlot:
					xPos = int(metinSlot[0])
					yPos = int(metinSlot[1])

					if xPos != 0 and yPos != 0:
						(mapName, xBase, yBase) = background.GlobalPositionToMapInfo(xPos, yPos)
						
						localeMapName=localeInfo.MINIMAP_ZONE_NAME_DICT.get(mapName, "")

						self.AppendSpace(5)

						if localeMapName!="":						
							self.AppendTextLine(localeInfo.TOOLTIP_MEMORIZED_POSITION % (localeMapName, int(xPos-xBase)/100, int(yPos-yBase)/100), self.NORMAL_COLOR)
						else:
							self.AppendTextLine(localeInfo.TOOLTIP_MEMORIZED_POSITION_ERROR % (int(xPos)/100, int(yPos)/100), self.NORMAL_COLOR)
							dbg.TraceError("NOT_EXIST_IN_MINIMAP_ZONE_NAME_DICT: %s" % mapName)
#Add after:
			if 79000 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [MASTER]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Resist Damage Buff" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 24" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 164" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(80 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
	
					
			if 79001 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [GRAND]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Resist Damage Buff" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 29" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 224" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(60 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
					
			if 79002 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [PERFECT]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Resist Damage Buff" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 35" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 310" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(50 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
	
			if 79003 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [MASTER]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Dragon's Strength(Critical Buff)" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 24" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 110" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(80 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
	
					
			if 79004 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [GRAND]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Dragon's Strength(Critical Buff)" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 29" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 142" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(60 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
					
			if 79005 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [PERFECT]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Dragon's Strength(Critical Buff)" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 35" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 185" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(50 - useCount), self.ITEM_BUFF_USAGE_COLOR)					

			if 79006 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [MASTER]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Reflection" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 21" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 160" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(80 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
	
					
			if 79007 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [GRAND]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Reflection" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 31" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 224" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(60 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
					
			if 79008 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [PERFECT]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Reflection" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 45" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 310" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(50 - useCount), self.ITEM_BUFF_USAGE_COLOR)										