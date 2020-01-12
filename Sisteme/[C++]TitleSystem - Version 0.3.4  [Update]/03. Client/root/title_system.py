import net, item, wndMgr, uiCommon, ime, app, ui
import time, chat, playerSettingModule, localeInfo, player

No_Fog = 0
##############################################################################################################################
#####################################			TITLE SYSTEM BY VEGAS		 			 #####################################
##############################################################################################################################
Title_System2 = {
	"Title_Free_Num"  : {
		#-----------------------------------------------------------------------------------*****
		0 : localeInfo.TITLE_INDEX_0,
		1 : localeInfo.TITLE_INDEX_1,
		2 : localeInfo.TITLE_INDEX_2,
		3 : localeInfo.TITLE_INDEX_3,
		4 : localeInfo.TITLE_INDEX_4,
		5 : localeInfo.TITLE_INDEX_5,
		6 : localeInfo.TITLE_INDEX_6,
		7 : localeInfo.TITLE_INDEX_7,
		8 : localeInfo.TITLE_INDEX_8,
		9 : localeInfo.TITLE_INDEX_9,
		10 : localeInfo.TITLE_INDEX_10,
		11 : localeInfo.TITLE_INDEX_11,
		12 : localeInfo.TITLE_INDEX_12,
		13 : localeInfo.TITLE_INDEX_13,
		14 : localeInfo.TITLE_INDEX_14,
		15 : localeInfo.TITLE_INDEX_15,
		16 : localeInfo.TITLE_INDEX_16,
	},
	"prestige_targets_level"	   : {
		#-----------------------------------------------------------------------------------*****
		localeInfo.TITLE_INDEX_0	:	localeInfo.TITLE_TARGETS_LEVEL_0,
		localeInfo.TITLE_INDEX_1	:	localeInfo.TITLE_TARGETS_LEVEL_1,
		localeInfo.TITLE_INDEX_2	:	localeInfo.TITLE_TARGETS_LEVEL_2,
		localeInfo.TITLE_INDEX_3	:	localeInfo.TITLE_TARGETS_LEVEL_3,
		localeInfo.TITLE_INDEX_4	:	localeInfo.TITLE_TARGETS_LEVEL_4,
		localeInfo.TITLE_INDEX_5	:	localeInfo.TITLE_TARGETS_LEVEL_5,
		localeInfo.TITLE_INDEX_6	:	localeInfo.TITLE_TARGETS_LEVEL_6,
		localeInfo.TITLE_INDEX_7	:	localeInfo.TITLE_TARGETS_LEVEL_7,
		localeInfo.TITLE_INDEX_8	:	localeInfo.TITLE_TARGETS_LEVEL_8,
		localeInfo.TITLE_INDEX_9	:	localeInfo.TITLE_TARGETS_LEVEL_9,
		localeInfo.TITLE_INDEX_10	:	localeInfo.TITLE_TARGETS_LEVEL_10,
		localeInfo.TITLE_INDEX_11	:	localeInfo.TITLE_TARGETS_LEVEL_11,
		localeInfo.TITLE_INDEX_12	:	localeInfo.TITLE_TARGETS_LEVEL_12,
		localeInfo.TITLE_INDEX_13	:	localeInfo.TITLE_TARGETS_LEVEL_13,
		localeInfo.TITLE_INDEX_14	:	localeInfo.TITLE_TARGETS_LEVEL_14,
		localeInfo.TITLE_INDEX_15	:	localeInfo.TITLE_TARGETS_LEVEL_15,
		localeInfo.TITLE_INDEX_16	:	localeInfo.TITLE_TARGETS_LEVEL_16,
	},
	
	"prestige_targets_gold"	   : {
		#-----------------------------------------------------------------------------------*****
		localeInfo.TITLE_INDEX_0	:	localeInfo.TITLE_TARGETS_MONEY_0,
		localeInfo.TITLE_INDEX_1	:	localeInfo.TITLE_TARGETS_MONEY_1,
		localeInfo.TITLE_INDEX_2	:	localeInfo.TITLE_TARGETS_MONEY_2,
		localeInfo.TITLE_INDEX_3	:	localeInfo.TITLE_TARGETS_MONEY_3,
		localeInfo.TITLE_INDEX_4	:	localeInfo.TITLE_TARGETS_MONEY_4,
		localeInfo.TITLE_INDEX_5	:	localeInfo.TITLE_TARGETS_MONEY_5,
		localeInfo.TITLE_INDEX_6	:	localeInfo.TITLE_TARGETS_MONEY_6,
		localeInfo.TITLE_INDEX_7	:	localeInfo.TITLE_TARGETS_MONEY_7,
		localeInfo.TITLE_INDEX_8	:	localeInfo.TITLE_TARGETS_MONEY_8,
		localeInfo.TITLE_INDEX_9	:	localeInfo.TITLE_TARGETS_MONEY_9,
		localeInfo.TITLE_INDEX_10	:	localeInfo.TITLE_TARGETS_MONEY_10,
		localeInfo.TITLE_INDEX_11	:	localeInfo.TITLE_TARGETS_MONEY_11,
		localeInfo.TITLE_INDEX_12	:	localeInfo.TITLE_TARGETS_MONEY_12,
		localeInfo.TITLE_INDEX_13	:	localeInfo.TITLE_TARGETS_MONEY_13,
		localeInfo.TITLE_INDEX_14	:	localeInfo.TITLE_TARGETS_MONEY_14,
		localeInfo.TITLE_INDEX_15	:	localeInfo.TITLE_TARGETS_MONEY_15,
		localeInfo.TITLE_INDEX_16	:	localeInfo.TITLE_TARGETS_MONEY_16,
	},		
	
	"prestige_targets_minutes"	   : {
		#-----------------------------------------------------------------------------------*****
		localeInfo.TITLE_INDEX_0	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_0,
		localeInfo.TITLE_INDEX_1	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_1,
		localeInfo.TITLE_INDEX_2	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_2,
		localeInfo.TITLE_INDEX_3	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_3,
		localeInfo.TITLE_INDEX_4	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_4,
		localeInfo.TITLE_INDEX_5	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_5,
		localeInfo.TITLE_INDEX_6	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_6,
		localeInfo.TITLE_INDEX_7	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_7,
		localeInfo.TITLE_INDEX_8	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_8,
		localeInfo.TITLE_INDEX_9	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_9,
		localeInfo.TITLE_INDEX_10	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_10,
		localeInfo.TITLE_INDEX_11	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_11,
		localeInfo.TITLE_INDEX_12	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_12,
		localeInfo.TITLE_INDEX_13	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_13,
		localeInfo.TITLE_INDEX_14	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_14,
		localeInfo.TITLE_INDEX_15	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_15,
		localeInfo.TITLE_INDEX_16	:	localeInfo.TITLE_TARGETS_MINUTES_PLAYED_16,
	},	
	
	"prestige_targets_bonus"	   : {
		#-----------------------------------------------------------------------------------*****
		localeInfo.TITLE_INDEX_0	:	"",
		localeInfo.TITLE_INDEX_1	:	"",
		localeInfo.TITLE_INDEX_2	:	"",
		localeInfo.TITLE_INDEX_3	:	"",
		localeInfo.TITLE_INDEX_4	:	"",
		localeInfo.TITLE_INDEX_5	:	"",
		localeInfo.TITLE_INDEX_6	:	"",
		localeInfo.TITLE_INDEX_7	:	"",
		localeInfo.TITLE_INDEX_8	:	"", 
		localeInfo.TITLE_INDEX_9	:	"",
		localeInfo.TITLE_INDEX_10	:	"",
		localeInfo.TITLE_INDEX_11	:	"",
		localeInfo.TITLE_INDEX_12	:	"",
		localeInfo.TITLE_INDEX_13	:	"",
		localeInfo.TITLE_INDEX_14	:	"",
		localeInfo.TITLE_INDEX_15	:	"",
		localeInfo.TITLE_INDEX_16	:	"", 
	},		
	
	"Title_Name" : {
		#-----------------------------------------------------------------------------------*****
		localeInfo.TITLE_INDEX_0	:	(255,255,255),
		localeInfo.TITLE_INDEX_1	:	(18, 252, 18),
		localeInfo.TITLE_INDEX_2	:	(220, 185, 110),
		localeInfo.TITLE_INDEX_3	:	(72, 98, 0),
		localeInfo.TITLE_INDEX_4	:	(249, 141, 0),
		localeInfo.TITLE_INDEX_5	:	(255, 100, 100),
		localeInfo.TITLE_INDEX_6	:	(240, 13, 255),
		localeInfo.TITLE_INDEX_7	:	(184, 229, 227),
		localeInfo.TITLE_INDEX_8	:	(242, 19, 34),
		localeInfo.TITLE_INDEX_9	:	(217, 217, 217),
		localeInfo.TITLE_INDEX_10	:	(220, 185, 110),
		localeInfo.TITLE_INDEX_11	:	(185, 220, 110),
		localeInfo.TITLE_INDEX_12	:	(200, 155, 150),
		localeInfo.TITLE_INDEX_13	:	(255, 100, 100),
		localeInfo.TITLE_INDEX_14	:	(100, 220, 210),
		localeInfo.TITLE_INDEX_15	:	(20, 110, 40),
		localeInfo.TITLE_INDEX_16	:	(20, 190, 210),		
	},
}
premium_Title_System = {
	"Title_Premium_Num"  : {
		#-----------------------------------------------------------------------------------*****
		0 : localeInfo.TITLE_INDEX_17,
		1 : localeInfo.TITLE_INDEX_18,
		2 : localeInfo.TITLE_INDEX_19,		
		
	},
	"premium_prestige_targets_potion"	   : {
		#-----------------------------------------------------------------------------------*****
		localeInfo.TITLE_INDEX_17	:	localeInfo.TITLE_PREMIUM_INFO_OBJECT_0,
		localeInfo.TITLE_INDEX_18	:	localeInfo.TITLE_PREMIUM_INFO_OBJECT_1,
		localeInfo.TITLE_INDEX_19	:	localeInfo.TITLE_PREMIUM_INFO_OBJECT_2,
	},
	"premium_prestige_targets_bonus"	   : {
		#-----------------------------------------------------------------------------------*****
		localeInfo.TITLE_INDEX_17	:	localeInfo.TITLE_PREMIUM_INFO_BONUS_0,
		localeInfo.TITLE_INDEX_18	:	localeInfo.TITLE_PREMIUM_INFO_BONUS_1,
		localeInfo.TITLE_INDEX_19	:	localeInfo.TITLE_PREMIUM_INFO_BONUS_2,
	},	
	"Title_Premium_Name" : {
		#-----------------------------------------------------------------------------------*****
		localeInfo.TITLE_INDEX_17	:	(235, 252, 6),
		localeInfo.TITLE_INDEX_18	:	(255, 0, 145),
		localeInfo.TITLE_INDEX_19	:	(255, 255, 255),	
	},
}
store_premium_Title_System = {
	"Potion_Title_Num"  : {
		#-----------------------------------------------------------------------------------*****
		0 : localeInfo.TITLE_POTION_COLOR_0,
		1 : localeInfo.TITLE_POTION_COLOR_1,
		2 : localeInfo.TITLE_POTION_COLOR_2,		
		
	},
	"store_price"	   : {
		#-----------------------------------------------------------------------------------*****
		localeInfo.TITLE_POTION_COLOR_0	:	localeInfo.TITLE_POTION_PRICE_COINS_COLOR_0,
		localeInfo.TITLE_POTION_COLOR_1	:	localeInfo.TITLE_POTION_PRICE_COINS_COLOR_1,
		localeInfo.TITLE_POTION_COLOR_2	:	localeInfo.TITLE_POTION_PRICE_COINS_COLOR_2,
	},	
	"store_name_title"	   : {
		#-----------------------------------------------------------------------------------*****
		localeInfo.TITLE_POTION_COLOR_0	:	localeInfo.TITLE_17,
		localeInfo.TITLE_POTION_COLOR_1	:	localeInfo.TITLE_18,
		localeInfo.TITLE_POTION_COLOR_2	:	localeInfo.TITLE_19,
	},	
	"Potion_Title" : {
		#-----------------------------------------------------------------------------------*****
		localeInfo.TITLE_POTION_COLOR_0	:	(235, 252, 6),
		localeInfo.TITLE_POTION_COLOR_1	:	(255, 0, 145),
		localeInfo.TITLE_POTION_COLOR_2	:	(255, 255, 255),	
	},
}
##############################################################################################################################
#####################################			TITLE SYSTEM BY VEGAS		 			 #####################################
imagini_fete_vegas = {
	playerSettingModule.RACE_WARRIOR_M	: "d:/ymir work/TitleSystem/faces/warriorM.tga",
	playerSettingModule.RACE_WARRIOR_W	: "d:/ymir work/TitleSystem/faces/warriorF.tga",
	playerSettingModule.RACE_ASSASSIN_M	: "d:/ymir work/TitleSystem/faces/ninjaM.tga",
	playerSettingModule.RACE_ASSASSIN_W	: "d:/ymir work/TitleSystem/faces/ninjaF.tga",
	playerSettingModule.RACE_SURA_M		: "d:/ymir work/TitleSystem/faces/suraM.tga",
	playerSettingModule.RACE_SURA_W		: "d:/ymir work/TitleSystem/faces/suraF.tga",
	playerSettingModule.RACE_SHAMAN_M	: "d:/ymir work/TitleSystem/faces/shamanM.tga",
	playerSettingModule.RACE_SHAMAN_W	: "d:/ymir work/TitleSystem/faces/shamanF.tga",
}

class Title_System(ui.ScriptWindow):
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.Load()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
	
	def Load(self):
		money = player.GetElk()		
		race = net.GetMainActorRace()	
		faces = imagini_fete_vegas[race]	
		
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(621, 385)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetTitleName("System Professional Title's - by VegaS")
		self.Board.SetCloseEvent(self.Close)
		self.Board.Hide()

		self.design_bar = ui.ImageBox()
		self.design_bar.SetParent(self.Board)
		self.design_bar.SetPosition(-175,250)
		self.design_bar.LoadImage("d:/ymir work/TitleSystem/horizontal_bar/center.tga")
		self.design_bar.SetWindowHorizontalAlignCenter()
		self.design_bar.Show()		
		
		self.horizontalbar_info2 = ui.ImageBox()
		self.horizontalbar_info2.SetParent(self.Board)
		self.horizontalbar_info2.SetPosition(-175,300)
		self.horizontalbar_info2.LoadImage("d:/ymir work/TitleSystem/horizontal_bar/center.tga")
		self.horizontalbar_info2.SetWindowHorizontalAlignCenter()
		self.horizontalbar_info2.Show()			

		self.thinboard = ui.ThinBoard()
		self.thinboard.SetParent(self.Board)
		self.thinboard.AddFlag("float")
		self.thinboard.SetSize(370, 240)
		self.thinboard.SetPosition(620,85)
		self.thinboard.Show()
##############################################################################################
		#-----------------------------------------------------------------------------------*
		# SHOPPING AREA #
		#-----------------------------------------------------------------------------------*
##############################################################################################		
		self.board2 = ui.BoardWithTitleBar()
		self.board2.SetSize(300, 235)
		self.board2.AddFlag("movable")
		self.board2.AddFlag("float")	
		self.board2.SetTitleName(localeInfo.TITLE_POTION_TITLE)		
		self.board2.Hide()			
			
		self.shop_thinboard_info_text = ui.ThinBoard()
		self.shop_thinboard_info_text.SetParent(self.board2)
		self.shop_thinboard_info_text.AddFlag("float")
		self.shop_thinboard_info_text.SetSize(383, 140)
		self.shop_thinboard_info_text.SetPosition(292,40)
		self.shop_thinboard_info_text.Show()	
		
		self.shop_slot_button_buy = ui.ThinBoard()
		self.shop_slot_button_buy.SetParent(self.board2)
		self.shop_slot_button_buy.AddFlag("movable")
		self.shop_slot_button_buy.AddFlag("float")
		self.shop_slot_button_buy.SetSize(200, 38)
		self.shop_slot_button_buy.SetPosition(50,185)
		self.shop_slot_button_buy.Show()	
		
		self.shop_slot_potion_1 = ui.ThinBoard()
		self.shop_slot_potion_1.SetParent(self.board2)
		self.shop_slot_potion_1.AddFlag("movable")
		self.shop_slot_potion_1.AddFlag("float")
		self.shop_slot_potion_1.SetSize(45, 45)
		self.shop_slot_potion_1.SetPosition(175,60)
		self.shop_slot_potion_1.Show()		

		self.shop_slot_potion_2 = ui.ThinBoard()
		self.shop_slot_potion_2.SetParent(self.board2)
		self.shop_slot_potion_2.AddFlag("movable")
		self.shop_slot_potion_2.AddFlag("float")
		self.shop_slot_potion_2.SetSize(45, 45)
		self.shop_slot_potion_2.SetPosition(230,60)
		self.shop_slot_potion_2.Show()	
		
		self.shop_slot_potion_3 = ui.ThinBoard()
		self.shop_slot_potion_3.SetParent(self.board2)
		self.shop_slot_potion_3.AddFlag("float")
		self.shop_slot_potion_3.SetSize(45, 45)
		self.shop_slot_potion_3.SetPosition(205,120)
		self.shop_slot_potion_3.Show()	

		self.shop_potion_1 = ui.ImageBox()
		self.shop_potion_1.SetParent(self.board2)
		self.shop_potion_1.SetPosition(180,67)
		self.shop_potion_1.Show()
		self.shop_potion_1.LoadImage("d:/ymir work/TitleSystem/potion/potion_prestige_1.tga")	

		self.shop_potion_2 = ui.ImageBox()
		self.shop_potion_2.SetParent(self.board2)
		self.shop_potion_2.SetPosition(235,67)
		self.shop_potion_2.Show()
		self.shop_potion_2.LoadImage("d:/ymir work/TitleSystem/potion/potion_prestige_2.tga")		

		self.shop_potion_3 = ui.ImageBox()
		self.shop_potion_3.SetParent(self.board2)
		self.shop_potion_3.SetPosition(210,127)
		self.shop_potion_3.Show()
		self.shop_potion_3.LoadImage("d:/ymir work/TitleSystem/potion/potion_prestige_3.tga")		

		self.shop_select_information = ui.TextLine()
		self.shop_select_information.SetFontName("Tahoma:15")
		self.shop_select_information.SetParent(self.board2)
		self.shop_select_information.SetPosition(-5,38)
		self.shop_select_information.SetWindowHorizontalAlignCenter()
		self.shop_select_information.SetHorizontalAlignCenter()
		self.shop_select_information.SetText(localeInfo.TITLE_POTION_SELECT)
		self.shop_select_information.SetPackedFontColor(0xfff8d090)
		self.shop_select_information.SetOutline()
		self.shop_select_information.Show()			
		
		self.shop_button_close = ui.Button()
		self.shop_button_close.SetParent(self.board2)
		self.shop_button_close.SetPosition(60,192)
		self.shop_button_close.SetUpVisual('d:/ymir work/ui/public/XLarge_Button_01.sub')
		self.shop_button_close.SetOverVisual('d:/ymir work/ui/public/XLarge_Button_02.sub')
		self.shop_button_close.SetDownVisual('d:/ymir work/ui/public/XLarge_Button_03.sub')
		self.shop_button_close.SetText(localeInfo.TITLE_POTION_)
		self.shop_button_close.SetEvent(ui.__mem_func__(self.BuyPrestige))
		self.shop_button_close.Show()
		
		self.fileListBox3 = ui.ListBoxEx()
		self.fileListBox3.SetParent(self.board2)
		self.fileListBox3.SetPosition(36, 70)
		self.fileListBox3.SetSelectEvent(lambda x=0: self.ReloadInfoPrestige3(x))
		self.fileListBox3.Show()	

		self.ScrollBar3 = ui.ThinScrollBar()
		self.ScrollBar3.SetParent(self.board2)
		self.ScrollBar3.SetPosition(12, 64)
		self.ScrollBar3.SetScrollBarSize(120)	
		self.ScrollBar3.Show()

		self.bar3 = ui.Bar()
		self.bar3.SetParent(self.fileListBox3)
		self.bar3.SetPosition(-26, -7)
		self.bar3.SetSize(154, 120)
		self.bar3.SetColor(0x77000000)
		self.bar3.Show()			
		
		self.shop_area_text = [[0,30,localeInfo.TITLE_POTION_TEXT_1],[0,50,localeInfo.TITLE_POTION_TEXT_2],[0,70,localeInfo.TITLE_POTION_TEXT_3],[0,90,localeInfo.TITLE_POTION_TEXT_4],[0,110,"-"]]
		self.text_shop = {}
		szText= 0
		for i in self.shop_area_text:
			self.text_shop["Text0"+str(szText)] = ui.TextLine()
			self.text_shop["Text0"+str(szText)].SetParent(self.shop_thinboard_info_text)
			self.text_shop["Text0"+str(szText)].SetPosition(i[0],i[1])
			self.text_shop["Text0"+str(szText)].SetWindowHorizontalAlignCenter()
			self.text_shop["Text0"+str(szText)].SetHorizontalAlignCenter()				
			if szText >= 5:
				break
			self.text_shop["Text0"+str(szText)].SetText(i[2])
			self.text_shop["Text0"+str(szText)].Show()
			
			szText+= 1			
##############################################################################################
		#-----------------------------------------------------------------------------------*
		# END SHOPPING AREA #
		#-----------------------------------------------------------------------------------*
##############################################################################################	
		self.thinboard2 = ui.ThinBoard()
		self.thinboard2.SetParent(self.Board)
		self.thinboard2.AddFlag("float")
		self.thinboard2.SetSize(615, 34)
		self.thinboard2.SetPosition(3,340)
		self.thinboard2.Show()

		self.slot_level = ui.ImageBox()
		self.slot_level.SetParent(self.Board)
		self.slot_level.SetPosition(120,150)
		self.slot_level.Show()
		self.slot_level.LoadImage("d:/ymir work/TitleSystem/chenare/chenar_bun.png")			
		
		self.chenar_prestige = ui.ImageBox()
		self.chenar_prestige.SetParent(self.Board)
		self.chenar_prestige.SetPosition(120,180)
		self.chenar_prestige.Show()
		self.chenar_prestige.LoadImage("d:/ymir work/TitleSystem/chenare/chenar_bun.png")	

		self.chenar_total_yang = ui.ImageBox()
		self.chenar_total_yang.SetParent(self.Board)
		self.chenar_total_yang.SetPosition(120,210)
		self.chenar_total_yang.Show()
		self.chenar_total_yang.LoadImage("d:/ymir work/TitleSystem/chenare/chenar_bun.png")

		self.chenar_prestige2 = ui.ImageBox()
		self.chenar_prestige2.SetParent(self.Board)
		self.chenar_prestige2.SetPosition(120,240)
		self.chenar_prestige2.Show()
		self.chenar_prestige2.LoadImage("d:/ymir work/TitleSystem/chenare/chenar_bun.png")			
		
		self.blue_legion1 = ui.TextLine()
		self.blue_legion1.SetParent(self.chenar_prestige)
		self.blue_legion1.SetPosition(-100,0)
		self.blue_legion1.SetText(localeInfo.TITLE_CURRENT_NAME)
		self.blue_legion1.SetPackedFontColor(0xffe0f283)
		self.blue_legion1.Show()	
		
		self.blue_legion212 = ui.TextLine()
		self.blue_legion212.SetParent(self.chenar_total_yang)
		self.blue_legion212.SetPosition(65,5)
		self.blue_legion212.SetText(localeInfo.NumberToMoneyString(money))
		self.blue_legion212.SetHorizontalAlignCenter()
		self.blue_legion212.Show()
		
		self.blue_legion2123 = ui.TextLine()
		self.blue_legion2123.SetParent(self.chenar_prestige2)
		self.blue_legion2123.SetPosition(65,5)
		self.blue_legion2123.SetText(str(player.GetPlayTime()) + "222")
		self.blue_legion2123.SetHorizontalAlignCenter()
		self.blue_legion2123.Show()		
		
		self.blue_legion21 = ui.TextLine()
		self.blue_legion21.SetParent(self.blue_legion212)
		self.blue_legion21.SetPosition(-165,0)
		self.blue_legion21.SetText(localeInfo.TITLE_TOTAL_AMOUNT)
		self.blue_legion21.SetPackedFontColor(0xffe0f283)
		self.blue_legion21.Show()
		
		self.text_minutes = ui.TextLine()
		self.text_minutes.SetParent(self.blue_legion2123)
		self.text_minutes.SetPosition(-165,0)
		self.text_minutes.SetText(localeInfo.TITLE_MINUTES_PLAYED)
		self.text_minutes.SetPackedFontColor(0xffe0f283)
		self.text_minutes.Show()	

		self.text_level = ui.TextLine()
		self.text_level.SetParent(self.slot_level)
		self.text_level.SetPosition(-100,0)
		self.text_level.SetText("Level character:")
		self.text_level.SetPackedFontColor(0xffe0f283)
		self.text_level.Show()		

		self.check_race = ui.ImageBox()
		self.check_race.SetParent(self.Board)
		self.check_race.SetPosition(15, 40)
		self.check_race.Show()		
		
		self.image_race = ui.ImageBox()
		self.image_race.SetParent(self.check_race)
		self.image_race.SetPosition(68, 0)
		self.image_race.LoadImage(faces)
		self.image_race.Show()	
		
		self.level = ui.TextLine()
		self.level.SetParent(self.slot_level)
		self.level.SetPosition(0,5)
		self.level.SetWindowHorizontalAlignCenter()
		self.level.SetHorizontalAlignCenter()
		self.level.SetText(str(player.GetStatus(player.LEVEL)))
		self.level.Show()	
		
		self.pos_prestige = [[0,30,localeInfo.TITLE_SELECT_INFO],[0,70,localeInfo.TITLE_UNBLOCK],[0,100,localeInfo.TITLE_LIST_NAME],[0,130,localeInfo.TITLE_INFO_ACTIVATE],[0,150,"-"],[0,165,"-"],[0,180,"-"],[0,210,"-"]]
		self.text_thinboard = {}
		o = 0
		for i in self.pos_prestige:
			self.text_thinboard["Text0"+str(o)] = ui.TextLine()
			self.text_thinboard["Text0"+str(o)].SetParent(self.thinboard)
			self.text_thinboard["Text0"+str(o)].SetPosition(i[0],i[1])
			self.text_thinboard["Text0"+str(o)].SetWindowHorizontalAlignCenter()
			self.text_thinboard["Text0"+str(o)].SetHorizontalAlignCenter()
			self.text_thinboard["Text0"+str(o)].SetHorizontalAlignCenter()	
			self.text_thinboard["Text0"+str(o)].SetHorizontalAlignCenter()	
			self.text_thinboard["Text0"+str(o)].SetHorizontalAlignCenter()				
			if o >= 8:
				break
			self.text_thinboard["Text0"+str(o)].SetText(i[2])
			self.text_thinboard["Text0"+str(o)].Show()
			
			o+= 1	
		
		self.information_welcome = ui.TextLine()
		self.information_welcome.SetFontName("Tahoma:15")
		self.information_welcome.SetParent(self.Board)
		self.information_welcome.SetPosition(-150,85)
		self.information_welcome.SetWindowHorizontalAlignCenter()
		self.information_welcome.SetHorizontalAlignCenter()
		self.information_welcome.SetText(localeInfo.TITLE_WELCOME + player.GetName())
		self.information_welcome.SetPackedFontColor(0xfff8d090)
		self.information_welcome.SetOutline()
		#self.information_welcome.Show()
		
		self.information_premium = ui.TextLine()
		self.information_premium.SetFontName("Tahoma:15")
		self.information_premium.SetParent(self.Board)
		self.information_premium.SetPosition(210,45)
		self.information_premium.SetWindowHorizontalAlignCenter()
		self.information_premium.SetHorizontalAlignCenter()
		self.information_premium.SetText(localeInfo.TITLE_PREMIUM)
		self.information_premium.SetPackedFontColor(0xfff8d090)
		self.information_premium.SetOutline()
		self.information_premium.Show()				
		
		self.information_free = ui.TextLine()
		self.information_free.SetFontName("Tahoma:15")
		self.information_free.SetParent(self.Board)
		self.information_free.SetPosition(35,45)
		self.information_free.SetWindowHorizontalAlignCenter()
		self.information_free.SetHorizontalAlignCenter()
		self.information_free.SetText(localeInfo.TITLE_FREE)
		self.information_free.SetPackedFontColor(0xfff8d090)
		self.information_free.SetOutline()
		self.information_free.Show()	

		self.premium_button2 = ui.Button()
		self.premium_button2.SetParent(self.Board)
		self.premium_button2.SetPosition(50,288)
		self.premium_button2.SetUpVisual('d:/ymir work/ui/public/XLarge_Button_01.sub')
		self.premium_button2.SetOverVisual('d:/ymir work/ui/public/XLarge_Button_02.sub')
		self.premium_button2.SetDownVisual('d:/ymir work/ui/public/XLarge_Button_03.sub')
		self.premium_button2.SetText(localeInfo.TITLE_SHOPPING_AREA)
		self.premium_button2.SetEvent(ui.__mem_func__(self.OpenItemShopTitle))
		self.premium_button2.Show()	

		self.button_close = ui.Button()
		self.button_close.SetParent(self.thinboard2)
		self.button_close.SetPosition(424,3)
		self.button_close.SetUpVisual('d:/ymir work/ui/public/XLarge_Button_01.sub')
		self.button_close.SetOverVisual('d:/ymir work/ui/public/XLarge_Button_02.sub')
		self.button_close.SetDownVisual('d:/ymir work/ui/public/XLarge_Button_03.sub')
		self.button_close.SetText(localeInfo.TITLE_CHANGE_TITLE_PREMIUM)
		self.button_close.SetEvent(ui.__mem_func__(self.__ChangeTitlePremium))
		self.button_close.Show()			
		
		self.premium_button3 = ui.Button()
		self.premium_button3.SetParent(self.thinboard2)
		self.premium_button3.SetPosition(10,3)
		self.premium_button3.SetUpVisual('d:/ymir work/ui/public/XLarge_Button_01.sub')
		self.premium_button3.SetOverVisual('d:/ymir work/ui/public/XLarge_Button_02.sub')
		self.premium_button3.SetDownVisual('d:/ymir work/ui/public/XLarge_Button_03.sub')
		self.premium_button3.SetText(localeInfo.TITLE_TRANSFORM_PREMIUM)
		self.premium_button3.SetEvent(ui.__mem_func__(self.__TransformBox))
		self.premium_button3.Show()	

		self.accept_title_prestige = ui.Button()
		self.accept_title_prestige.SetParent(self.thinboard2)
		self.accept_title_prestige.SetPosition(220,3)
		self.accept_title_prestige.SetUpVisual('d:/ymir work/ui/public/XLarge_Button_01.sub')
		self.accept_title_prestige.SetOverVisual('d:/ymir work/ui/public/XLarge_Button_02.sub')
		self.accept_title_prestige.SetDownVisual('d:/ymir work/ui/public/XLarge_Button_03.sub')
		self.accept_title_prestige.SetEvent(ui.__mem_func__(self.__ChangeTitleFree))
		self.accept_title_prestige.SetText(localeInfo.TITLE_CHANGE_FREE)
		self.accept_title_prestige.Show()
############################################################################3
		self.fileListBox = ui.ListBoxEx()
		self.fileListBox.SetParent(self.Board)
		self.fileListBox.SetPosition(295, 75)
		self.fileListBox.SetSelectEvent(lambda x=0: self.ReloadInfoPrestige(x))
		self.fileListBox.Show()	
		
		self.fileListBox_premium = ui.ListBoxEx()
		self.fileListBox_premium.SetParent(self.Board)
		self.fileListBox_premium.SetPosition(475, 75)
		self.fileListBox_premium.SetSelectEvent(lambda x=0: self.__UpdateTitlePremium(x))
		self.fileListBox_premium.Show()			
		
		self.ScrollBar = ui.ScrollBar()
		self.ScrollBar.SetParent(self.Board)
		self.ScrollBar.SetPosition(258, 70)
		self.ScrollBar.SetScrollBarSize(265)
		
		self.ScrollBar_premium = ui.ScrollBar()
		self.ScrollBar_premium.SetParent(self.Board)
		self.ScrollBar_premium.SetPosition(590, 71)
		self.ScrollBar_premium.SetScrollBarSize(265)	
		
		self.background = ui.Bar()
		self.background.SetParent(self.fileListBox)
		self.background.SetPosition(-37, -3)
		self.background.SetSize(174, 265)
		self.background.SetColor(0x77000000)
		self.background.Show()
		
		self.background_premium = ui.Bar()
		self.background_premium.SetParent(self.fileListBox_premium)
		self.background_premium.SetPosition(-30, -3)
		self.background_premium.SetSize(154, 265)
		self.background_premium.SetColor(0x77000000)
		self.background_premium.Show()		
		
		self.fileListBox.SetScrollBar(self.ScrollBar)
		self.fileListBox_premium.SetScrollBar(self.ScrollBar_premium)
		self.ScrollBar.Show()
		self.ScrollBar_premium.Show()		
		
		self.__AppendFileList()
		self.__AppendFileList2()	
		self.__StartInterfaceShop()		
		self.__AppendPrestige()
		
	def __AppendPrestige(self):	
		point, grade = player.GetPrestigeData()
		
		self.blue_legion = ui.TextLine()
		self.blue_legion.SetParent(self.chenar_prestige)
		self.blue_legion.SetPosition(65,5)
		self.blue_legion.SetText(localeInfo.TITLEPRESTIGE_NAME_LIST[grade])
		self.blue_legion.SetHorizontalAlignCenter()
		self.blue_legion.Show()		
##############################################################################################
		#-----------------------------------------------------------------------------------*
		# FREEE TITLE #
		#-----------------------------------------------------------------------------------*
##############################################################################################
	def __StartInterfaceShop(self):
		for i in xrange(len(store_premium_Title_System["Potion_Title"])):
			premium_title2 = store_premium_Title_System["Potion_Title_Num"][i]
			if premium_title2.find("_"):
				premium_title2 = premium_title2.replace("_", " ")
			self.fileListBox3.AppendItem(TitleWindow_3(premium_title2))			
		
	def __AppendFileList(self):
		for i in xrange(len(Title_System2["Title_Name"])):
			object = Title_System2["Title_Free_Num"][i]
			if object.find("_"):
				object = object.replace("_", " ")
			self.fileListBox.AppendItem(TitleWindow_1(object))				

	def __ChangeTitleFree(self):
		list_name_prestige = self.fileListBox.GetSelectedItem()
		
		if list_name_prestige:
			title_prestige = list_name_prestige.GetText()	
			self.questionDialog_free = uiCommon.QuestionDialog()
			self.questionDialog_free.SetText(localeInfo.TITLE_QUESTIONDIALOG_CHANGE)
			self.questionDialog_free.SetAcceptEvent(ui.__mem_func__(self.__AcceptTitleFreePrestige))
			self.questionDialog_free.SetCancelEvent(ui.__mem_func__(self.__CancelTitleBoard2))
			self.questionDialog_free.Open()	
		else:
			self.__RemoveSelect()
			self.NonSelectBox()				

	def __CancelTitleBoard2(self):
		if self.questionDialog_free:
			self.questionDialog_free.Close()

		self.questionDialog_free = None			

	def ReloadInfoPrestige(self,x):
		list_name_prestige = self.fileListBox.GetSelectedItem()
		if list_name_prestige:
			title_prestige = list_name_prestige.GetText()
			if title_prestige.find(" "):
				title_prestige = title_prestige.replace(" ", "_")
				
			tColorList = Title_System2["Title_Name"][title_prestige]
			vegas_target_1 = Title_System2["prestige_targets_level"][title_prestige]
			vegas_target_2 = Title_System2["prestige_targets_gold"][title_prestige]
			vegas_target_3 = Title_System2["prestige_targets_minutes"][title_prestige]		
			vegas_target_4 = Title_System2["prestige_targets_bonus"][title_prestige]				
			titleColor = ui.GenerateColor(tColorList[0], tColorList[1], tColorList[2])

			title_prestige = title_prestige.replace("_", " ")
			self.text_thinboard["Text00"].SetText(localeInfo.TITLE_REQUEST_INFO)
			
			self.text_thinboard["Text02"].SetText(title_prestige)
			self.text_thinboard["Text02"].SetPackedFontColor(titleColor)
			
			self.text_thinboard["Text04"].SetText(vegas_target_1)
			self.text_thinboard["Text04"].SetPackedFontColor(0xffff7400)
			
			self.text_thinboard["Text05"].SetText(vegas_target_2)
			self.text_thinboard["Text05"].SetPackedFontColor(0xff00ff38)
			
			self.text_thinboard["Text06"].SetText(vegas_target_3)			
			self.text_thinboard["Text06"].SetPackedFontColor(0xfff8d090)
			
			self.text_thinboard["Text07"].SetFontName("Tahoma:15")
			self.text_thinboard["Text07"].SetText(vegas_target_4)			

	def __ClearFileList(self):
		self.fileListBox.RemoveAllItems()		
		self.fileListBox_premium.RemoveAllItems()		
	
	def __RemoveSelect(self):
		self.__ClearFileList()	
		self.__AppendFileList()
		self.__AppendFileList2()

	def NonSelectBox(self):		
		self.prestige_vegas = uiCommon.PopupDialog()
		self.prestige_vegas.SetWidth(550)
		self.prestige_vegas.SetText(localeInfo.TITLE_WARNING_DIALOG)
		self.prestige_vegas.Show()
		
##############################################################################################
		#-----------------------------------------------------------------------------------*
		# PREMIUM TITLE #
		#-----------------------------------------------------------------------------------*
##############################################################################################	
	
	def __AppendFileList2(self):
		for i in xrange(len(premium_Title_System["Title_Premium_Name"])):
			premium_title = premium_Title_System["Title_Premium_Num"][i]
			if premium_title.find("_"):
				premium_title = premium_title.replace("_", " ")
			self.fileListBox_premium.AppendItem(TitleWindow_2(premium_title))

	def __ChangeTitlePremium(self):
		list_name_premium_prestige = self.fileListBox_premium.GetSelectedItem()
		
		if list_name_premium_prestige:
			title_premium_prestige = list_name_premium_prestige.GetText()	
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.TITLE_QUESTIONDIALOG_CHANGE)
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__AcceptTitlePremium))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.__CancelTitlePremium))
			self.questionDialog.Open()	
		else:
			self.__RemoveSelect()
			self.NonSelectBox()	
			
	def __AcceptTitlePremium(self):	
		list_name_premium_prestige = self.fileListBox_premium.GetSelectedItem()	
		
		if list_name_premium_prestige:
			title_premium_prestige = list_name_premium_prestige.GetText()
			if title_premium_prestige == localeInfo.TITLE_17:
				net.SendChatPacket("/prestige_title_name prestige_17")
			if title_premium_prestige == localeInfo.TITLE_18:
				net.SendChatPacket("/prestige_title_name prestige_18")
			if title_premium_prestige == localeInfo.TITLE_19:
				net.SendChatPacket("/prestige_title_name prestige_19")
		if self.questionDialog:
			self.questionDialog.Close()
			self.questionDialog = None	

	def __CancelTitlePremium(self):
		if self.questionDialog:
			self.questionDialog.Close()

		self.questionDialog = None				

	def __UpdateTitlePremium(self,x):
		list_name_prestige = self.fileListBox_premium.GetSelectedItem()
		title_prestige = list_name_prestige.GetText()
		
		if list_name_prestige:
			title_prestige = list_name_prestige.GetText()
			if title_prestige.find(" "):
				title_prestige = title_prestige.replace(" ", "_")
				
				
			tColorList = premium_Title_System["Title_Premium_Name"][title_prestige]
			premium_vegas_target_1 = premium_Title_System["premium_prestige_targets_potion"][title_prestige]		
			premium_vegas_target_4 = premium_Title_System["premium_prestige_targets_bonus"][title_prestige]				
			titleColor = ui.GenerateColor(tColorList[0], tColorList[1], tColorList[2])

			title_prestige = title_prestige.replace("_", " ")
			self.text_thinboard["Text00"].SetText(localeInfo.TITLE_NEED_ACTIVATE_INFO)
			
			self.text_thinboard["Text02"].SetText(title_prestige)
			self.text_thinboard["Text02"].SetPackedFontColor(titleColor)

			self.text_thinboard["Text04"].SetFontName("Tahoma:13")
			self.text_thinboard["Text04"].SetText(premium_vegas_target_1)
			self.text_thinboard["Text04"].SetPackedFontColor(0xff82ff21)
			
			self.text_thinboard["Text05"].SetText(localeInfo.TITLE_BUY_POTIONS_INFO)
			self.text_thinboard["Text05"].SetPackedFontColor(0xff21fff9)
			
			self.text_thinboard["Text06"].SetText("")			
			self.text_thinboard["Text06"].SetPackedFontColor(0xfff8d090)	


			self.text_thinboard["Text07"].SetFontName("Tahoma:17")
			self.text_thinboard["Text07"].SetText(premium_vegas_target_4)
			self.text_thinboard["Text07"].SetPackedFontColor(0xffff8100)					
			
##############################################################################################
		#-----------------------------------------------------------------------------------*
		# TRANSFORM TITLE #
		#-----------------------------------------------------------------------------------*
##############################################################################################				
	def __TransformBox(self):
		self.dialogQuestion_transform = uiCommon.QuestionDialog()
		self.dialogQuestion_transform.SetText(localeInfo.TITLE_TRANSFORM_DIALOGQUESTION)
		self.dialogQuestion_transform.SetAcceptEvent(ui.__mem_func__(self.__TransformTitle))
		self.dialogQuestion_transform.SetCancelEvent(ui.__mem_func__(self.__CancelTransformTitle))
		self.dialogQuestion_transform.Open()		

	def __TransformTitle(self):
		net.SendChatPacket("/prestige_title_name vegas_transform_title")	
		if self.dialogQuestion_transform:
			self.dialogQuestion_transform.Close()
			self.dialogQuestion_transform = None		

	def __CancelTransformTitle(self):
		if self.dialogQuestion_transform:
			self.dialogQuestion_transform.Close()

		self.dialogQuestion_transform = None									
			
	def __AcceptTitleFreePrestige(self):			
		list_name_prestige = self.fileListBox.GetSelectedItem()

		if list_name_prestige:
			title_prestige = list_name_prestige.GetText()
			if title_prestige == localeInfo.TITLE_0:
				net.SendChatPacket("/prestige_title_name prestige_0")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_1:
				net.SendChatPacket("/prestige_title_name prestige_1")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_2:
				net.SendChatPacket("/prestige_title_name prestige_2")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_3:
				net.SendChatPacket("/prestige_title_name prestige_3")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_4:
				net.SendChatPacket("/prestige_title_name prestige_4")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_5:
				net.SendChatPacket("/prestige_title_name prestige_5")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_6:
				net.SendChatPacket("/prestige_title_name prestige_6")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_7:
				net.SendChatPacket("/prestige_title_name prestige_7")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_8:
				net.SendChatPacket("/prestige_title_name prestige_8")	
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_9:
				net.SendChatPacket("/prestige_title_name prestige_9")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_10:
				net.SendChatPacket("/prestige_title_name prestige_10")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_11:
				net.SendChatPacket("/prestige_title_name prestige_11")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_12:
				net.SendChatPacket("/prestige_title_name prestige_12")	
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_13:
				net.SendChatPacket("/prestige_title_name prestige_13")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_14:
				net.SendChatPacket("/prestige_title_name prestige_14")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_15:
				net.SendChatPacket("/prestige_title_name prestige_15")
				self.__RemoveSelect()					
			if title_prestige == localeInfo.TITLE_16:
				net.SendChatPacket("/prestige_title_name prestige_16")	
				self.__RemoveSelect()	
		if self.questionDialog_free:
			self.questionDialog_free.Close()

		self.questionDialog_free = None						
			
##############################################################################################
		#-----------------------------------------------------------------------------------*
		# SHOPPING AREA #
		#-----------------------------------------------------------------------------------*
##############################################################################################		

	def OpenItemShopTitle(self):
		if self.board2.IsShow():
			self.board2.Hide()
		else:
			self.board2.Show()
			self.board2.SetTop()	
		
	def BuyPrestige(self):
		list_name_prestige = self.fileListBox3.GetSelectedItem()
		
		if list_name_prestige:
			title_prestige = list_name_prestige.GetText()	
			self.dialogQuestion_buyPotion = uiCommon.QuestionDialog()
			self.dialogQuestion_buyPotion.SetText(localeInfo.TITLE_QUESTIONDIALOG_POTION)
			self.dialogQuestion_buyPotion.SetAcceptEvent(ui.__mem_func__(self.__AcceptTitleStorePrestige))
			self.dialogQuestion_buyPotion.SetCancelEvent(ui.__mem_func__(self.__CancelTitleBoard3))
			self.dialogQuestion_buyPotion.Open()	
		else:
			self.__RemoveSelect()
			self.prestige_vegas = uiCommon.PopupDialog()
			self.prestige_vegas.SetWidth(550)
			self.prestige_vegas.SetText(localeInfo.TITLE_QUESTWARNING_POTION)
			self.prestige_vegas.Show()

	def __CancelTitleBoard3(self):
		if self.dialogQuestion_buyPotion:
			self.dialogQuestion_buyPotion.Close()

		self.dialogQuestion_buyPotion = None	

	def __AcceptTitleStorePrestige(self):	
		store_premium = self.fileListBox3.GetSelectedItem()	
		
		if store_premium:
			store_premium_text = store_premium.GetText()
			if store_premium_text == localeInfo.TITLE_POTION_NAME_0:
				net.SendChatPacket("/prestige_title_name buy_prestige_1")
			if store_premium_text == localeInfo.TITLE_POTION_NAME_1:
				net.SendChatPacket("/prestige_title_name buy_prestige_2")
			if store_premium_text == localeInfo.TITLE_POTION_NAME_2:
				net.SendChatPacket("/prestige_title_name buy_prestige_3")
		if self.dialogQuestion_buyPotion:
			self.dialogQuestion_buyPotion.Close()
			self.dialogQuestion_buyPotion = None	

	def ReloadInfoPrestige3(self,x):
		list_name_prestige2 = self.fileListBox3.GetSelectedItem()
		store_title_prestige = list_name_prestige2.GetText()
		
		if list_name_prestige2:
			store_title_prestige = list_name_prestige2.GetText()
			if store_title_prestige.find(" "):
				store_title_prestige = store_title_prestige.replace(" ", "_")
				
			tColorList = store_premium_Title_System["Potion_Title"][store_title_prestige]
			premium_vegas_target_1 = store_premium_Title_System["store_price"][store_title_prestige]	
			premium_vegas_target_2 = store_premium_Title_System["store_name_title"][store_title_prestige]					
			titleColor = ui.GenerateColor(tColorList[0], tColorList[1], tColorList[2])

			store_title_prestige = store_title_prestige.replace("_", " ")
			self.text_shop["Text00"].SetText(localeInfo.TITLE_POTION_INFO)
			
			self.text_shop["Text02"].SetText(premium_vegas_target_2)
			self.text_shop["Text02"].SetPackedFontColor(titleColor)
			
			self.text_shop["Text04"].SetFontName("Tahoma:15")			
			self.text_shop["Text04"].SetText(premium_vegas_target_1)
			self.text_shop["Text04"].SetPackedFontColor(0xfff96ff00)				
##############################################################################################
		#-----------------------------------------------------------------------------------*
		# END SHOPPING AREA #
		#-----------------------------------------------------------------------------------*
##############################################################################################	

	def Show(self):
		if self.board2.IsShow():
			self.board2.Hide()
		else:
			self.Board.Show()
			self.ScrollBar.Show()
			self.fileListBox.Show()
			self.ScrollBar_premium.Show()
			self.fileListBox_premium.Show()
	
	def Close(self):
		self.Board.Hide()
		self.board2.Hide()
		self.ScrollBar.Hide()
		self.fileListBox.Hide()
		self.ScrollBar_premium.Hide()
		self.fileListBox_premium.Hide()
		
	def OpenWindow(self):
		if self.Board.IsShow():
			self.Board.Hide()
			self.board2.Hide()
			self.ScrollBar.Hide()
			self.fileListBox.Hide()
			self.ScrollBar_premium.Hide()
			self.fileListBox_premium.Hide()
		else:
			self.Board.Show()
			self.ScrollBar.Show()
			self.fileListBox.Show()
			self.ScrollBar_premium.Show()
			self.fileListBox_premium.Show()
			
	def OnUpdate(self):
		prestige_money = player.GetElk()
		prestige_point, prestige_grade = player.GetPrestigeData()
		
		self.blue_legion.SetText(localeInfo.TITLEPRESTIGE_NAME_LIST[prestige_grade])		
		self.blue_legion212.SetText(localeInfo.NumberToMoneyString(prestige_money))
		self.blue_legion2123.SetText(str(player.GetPlayTime()) + "")
		self.level.SetText(str(player.GetStatus(player.LEVEL)))	
		
class TitleWindow_3(ui.ListBoxEx.Item):
	def __init__(self, fileName):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=fileName
		self.textLine=self.__CreateTextLine(fileName[:40])          

	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)

	def GetText(self):
		return self.text

	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 125+ 4, 17)

	def __CreateTextLine(self, fileName):
		if fileName.find("["):
			fileName = fileName.replace("_", " ")
		if fileName.find("]"):
			fileName = fileName.replace("_", " ")		
		if fileName.find(" "):
			fileName = fileName.replace(" ", "_")
		premium_tColorList = store_premium_Title_System["Potion_Title"][fileName]
		premium_titleColor = ui.GenerateColor(premium_tColorList[0], premium_tColorList[1], premium_tColorList[2])	
		
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 0)
		if fileName.find("_"):
			fileName = fileName.replace("_", " ")		
		textLine.SetText(fileName)
		textLine.SetPackedFontColor(premium_titleColor)
		textLine.Show()
		return textLine		
		
class TitleWindow_2(ui.ListBoxEx.Item):
	def __init__(self, fileName):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=fileName
		self.textLine=self.__CreateTextLine(fileName[:40])          

	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)

	def GetText(self):
		return self.text

	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 125+ 4, 17)

	def __CreateTextLine(self, fileName):
		if fileName.find("["):
			fileName = fileName.replace("_", " ")
		if fileName.find("]"):
			fileName = fileName.replace("_", " ")		
		if fileName.find(" "):
			fileName = fileName.replace(" ", "_")
		premium_tColorList = premium_Title_System["Title_Premium_Name"][fileName]
		premium_titleColor = ui.GenerateColor(premium_tColorList[0], premium_tColorList[1], premium_tColorList[2])	
		
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 0)
		if fileName.find("_"):
			fileName = fileName.replace("_", " ")		
		textLine.SetText(fileName)
		textLine.SetPackedFontColor(premium_titleColor)
		textLine.Show()
		return textLine
		
class TitleWindow_1(ui.ListBoxEx.Item):
	def __init__(self, fileName):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=fileName
		self.textLine=self.__CreateTextLine(fileName[:40])          

	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)

	def GetText(self):
		return self.text

	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 125+ 4, 17)

	def __CreateTextLine(self, fileName):
		if fileName.find("["):
			fileName = fileName.replace("_", " ")
		if fileName.find("]"):
			fileName = fileName.replace("_", " ")		
		if fileName.find(" "):
			fileName = fileName.replace(" ", "_")
		tColorList = Title_System2["Title_Name"][fileName]
		titleColor = ui.GenerateColor(tColorList[0], tColorList[1], tColorList[2])	
		
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 0)
		if fileName.find("_"):
			fileName = fileName.replace("_", " ")		
		textLine.SetText(fileName)
		textLine.SetPackedFontColor(titleColor)
		textLine.Show()
		return textLine