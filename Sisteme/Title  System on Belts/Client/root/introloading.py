""""""
#1) Search: chrmgr.RegisterTitleName(i, localeInfo.TITLE_NAME_LIST[i])
#2) After this make a new line and paste:
		if app.ENABLE_TITLE_SYSTEM:
			for i in xrange(len(localeInfo.TITLE_SYSTEM_LIST)):
				chrmgr.RegistersTitleName(i + 1, localeInfo.TITLE_SYSTEM_LIST[i])
""""""


""""""
#1) Search: count += 1
#2) Be sure before the line searched is: chrmgr.RegisterTitleColor(count, rgb[0], rgb[1], rgb[2])
#3) After this make a new line and paste:
		if app.ENABLE_TITLE_SYSTEM:
			TITLE_SYSTEM_COLOR_DICT = (
										colorInfo.TITILE_NAME_1,
										colorInfo.TITILE_NAME_2,
										colorInfo.TITILE_NAME_3,
										colorInfo.TITILE_NAME_4,
										colorInfo.TITILE_NAME_5,
										colorInfo.TITILE_NAME_6,
										colorInfo.TITILE_NAME_7,
										colorInfo.TITILE_NAME_8,
										colorInfo.TITILE_NAME_9,
										colorInfo.TITILE_NAME_10,
										colorInfo.TITILE_NAME_11,
										colorInfo.TITILE_NAME_12,
										colorInfo.TITILE_NAME_13,
										colorInfo.TITILE_NAME_14,
										colorInfo.TITILE_NAME_15,
										colorInfo.TITILE_NAME_16,
										colorInfo.TITILE_NAME_17,
										colorInfo.TITILE_NAME_18,
										colorInfo.TITILE_NAME_19,
										colorInfo.TITILE_NAME_20,
			)
			
			count = 1
			for rgb in TITLE_SYSTEM_COLOR_DICT:
				chrmgr.RegistersTitleColor(count, rgb[0], rgb[1], rgb[2])
				count += 1
""""""