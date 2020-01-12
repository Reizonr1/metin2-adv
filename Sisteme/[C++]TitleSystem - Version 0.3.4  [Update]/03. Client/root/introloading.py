# 1) Search: 
		count = 0
		for rgb in TITLE_COLOR_DICT:
			chrmgr.RegisterTitleColor(count, rgb[0], rgb[1], rgb[2])
			count += 1
# 2) After their function make a new line and paste:
		# NEW TITLE SYSTEM - VEGAS
		if app.ENABLE_TITLE_SYSTEM:
			TITLEPRESTIGE_COLOR_DICT = ( colorInfo.TITLE_PRESTIGE_COLOR_1,
									colorInfo.TITLE_PRESTIGE_COLOR_2,
									colorInfo.TITLE_PRESTIGE_COLOR_3,
									colorInfo.TITLE_PRESTIGE_COLOR_4,		
									colorInfo.TITLE_PRESTIGE_COLOR_5,
									colorInfo.TITLE_PRESTIGE_COLOR_6,
									colorInfo.TITLE_PRESTIGE_COLOR_7,
									colorInfo.TITLE_PRESTIGE_COLOR_8,
									colorInfo.TITLE_PRESTIGE_COLOR_9,
									colorInfo.TITLE_PRESTIGE_COLOR_10,
									colorInfo.TITLE_PRESTIGE_COLOR_11,
									colorInfo.TITLE_PRESTIGE_COLOR_12,
									colorInfo.TITLE_PRESTIGE_COLOR_13,
									colorInfo.TITLE_PRESTIGE_COLOR_14,
									colorInfo.TITLE_PRESTIGE_COLOR_15,
									colorInfo.TITLE_PRESTIGE_COLOR_16,
									colorInfo.TITLE_PRESTIGE_COLOR_17,
									colorInfo.TITLE_PRESTIGE_COLOR_18,
									colorInfo.TITLE_PRESTIGE_COLOR_19,
									colorInfo.TITLE_PRESTIGE_COLOR_0,)
			count_prestige_vegas = 0
			for rgb in TITLEPRESTIGE_COLOR_DICT:
				chrmgr.RegisterTitlePrestigeColor(count_prestige_vegas, rgb[0], rgb[1], rgb[2])
				count_prestige_vegas += 1
			
# 1) Search: 		self.__RegisterTitleName()
# 2) After their function make a new line and paste:
		if app.ENABLE_TITLE_SYSTEM:	
			self.__RegisterTitlePrestigeName()			
""""""""""""""""""""""""""""""""""""""""""		
# 1) Search:	def __RegisterTitleName(self):
# 2) After their function make a new line and paste:
	if app.ENABLE_TITLE_SYSTEM:			
		def __RegisterTitlePrestigeName(self):
			for i in xrange(len(localeInfo.TITLEPRESTIGE_NAME_LIST)):
				chrmgr.RegisterTitlePrestigeName(i, localeInfo.TITLEPRESTIGE_NAME_LIST[i])				
""""""""""""""""""""""""""""""""""""""""""