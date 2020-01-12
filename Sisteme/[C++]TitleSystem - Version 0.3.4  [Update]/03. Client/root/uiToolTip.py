#1.) Search function:

if item.ITEM_TYPE_WEAPON == itemType:

#2.) Add before:
		if app.ENABLE_TITLE_SYSTEM:
			if itemVnum in (constInfo.TITLE_SYSTEM_ITEM_1, constInfo.TITLE_SYSTEM_ITEM_2, constInfo.TITLE_SYSTEM_ITEM_3):
				potion_list = {
					constInfo.TITLE_SYSTEM_ITEM_1 : ["[i]", "This item is purchased from the shopping area.", "This potion is for the title: %s" % localeInfo.TITLE_17, "|cFF6af200"+localeInfo.TITLE_POTION_PRICE_COINS_COLOR_0],
					constInfo.TITLE_SYSTEM_ITEM_2 : ["[i]", "This item is purchased from the shopping area", "This potion is for the title: %s" % localeInfo.TITLE_18, "|cFF6af200"+localeInfo.TITLE_POTION_PRICE_COINS_COLOR_1],	
					constInfo.TITLE_SYSTEM_ITEM_3 : ["[i]", "This item is purchased from the shopping area.", "This potion is for the title: %s" % localeInfo.TITLE_19, "|cFF6af200"+localeInfo.TITLE_POTION_PRICE_COINS_COLOR_2]}							
					
				self.AppendSpace(5)	
				for i in xrange(len(potion_list[itemVnum])):
					self.AppendTextLine(potion_list[itemVnum][i], self.SPECIAL_POSITIVE_COLOR)					
""""""""""""""""""""""""""""""""""""""""""	