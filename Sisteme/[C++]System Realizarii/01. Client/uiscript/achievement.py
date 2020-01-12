import grp

BOARD_WIDTH = 660
BOARD_HEIGHT = 485
ACHIEVEMENTS_PATH = "d:/ymir work/ui/achievementsystem/"

window = {
	"name" : "AchievementWindow",
	"style" : ("movable", "float",),
	
	"x" : 0,
	"y" : 0,
	
	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,
	
	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),
			
			"x" : 0,
			"y" : 0,
			
			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
			
			"title" : "Sistema de Logros",
			"children" :
			(
				{
					"name" : "tmpBg",
					"type" : "thinboard",
					
					"x" : 10,
					"y" : 35,
					
					"width" : BOARD_WIDTH - 20,
					"height" : 95,
				},
				{
					"name" : "AchievementshopButton",
					"type" : "button",
					
					"x" : 30,
					"y" : 35+15,
					"tooltip_text" : "Tiendra de Logros",
					
					"default_image" : ACHIEVEMENTS_PATH + "shop_btn_1.tga",
					"over_image" : ACHIEVEMENTS_PATH + "shop_btn_2.tga",
					"down_image" : ACHIEVEMENTS_PATH + "shop_btn_3.tga",
				},
				{
					"name" : "LeftArrow",
					"type" : "button",
					
					"x" : 20,
					"y" : 94,
					
					"default_image" : ACHIEVEMENTS_PATH + "btn_arrowleft_1.tga",
					"over_image" : ACHIEVEMENTS_PATH + "btn_arrowleft_2.tga",
					"down_image" : ACHIEVEMENTS_PATH + "btn_arrowleft_3.tga",
				},
				{
					"name" : "RightArrow",
					"type" : "button",
					"horizontal_align" : "right",
					
					"x" : 14+20,
					"y" : 94,
					
					"default_image" : ACHIEVEMENTS_PATH + "btn_arrowright_1.tga",
					"over_image" : ACHIEVEMENTS_PATH + "btn_arrowright_2.tga",
					"down_image" : ACHIEVEMENTS_PATH + "btn_arrowright_3.tga",
				},
				{
					"name" : "HomeWindow",
					"style" : ("attach",),
					"horizontal_align" : "center",
					
					"x" : 0,
					"y" : 130,
					
					"width" : BOARD_WIDTH - 24,
					"height" : BOARD_HEIGHT - (130+10),
					
					"children" :
					(
						{
							"name" : "UpArrow",
							"type" : "button",
							
							"x" : 195,
							"y" : 10,
							
							"default_image" : ACHIEVEMENTS_PATH + "btn_arrowup_1.tga",
							"over_image" : ACHIEVEMENTS_PATH + "btn_arrowup_2.tga",
							"down_image" : ACHIEVEMENTS_PATH + "btn_arrowup_3.tga",
						},
						{
							"name" : "DownArrow",
							"type" : "button",
							"vertical_align" : "bottom",
							
							"x" : 195,
							"y" : 10+6,
							
							"default_image" : ACHIEVEMENTS_PATH + "btn_arrowdown_1.tga",
							"over_image" : ACHIEVEMENTS_PATH + "btn_arrowdown_2.tga",
							"down_image" : ACHIEVEMENTS_PATH + "btn_arrowdown_3.tga",
						},
						{
							"name" : "bgLastAchievements",
							"type" : "resizable_text_value",
							
							"x" : 400,
							"y" : 46,
							
							"width" : 215,
							"height" : 265,
							"without_background" : 1,
							"all_lines" : 1,
							
							"children" :
							(
								{
									"name" : "bgLastAchievements",
									"type" : "resizable_text_value",
									"horizontal_align" : "center",
									
									"x" : 0,
									"y" : -18,
									
									"width" : 140,
									"height" : 18,
									"text" : "Últimos logros completados",
									
									"line_top" : 1,
									"line_left" : 1,
									"line_right" : 1,
								},
								{
									"name" : "LastUpArrow",
									"type" : "button",
									"horizontal_align" : "center",
									
									"x" : 0,
									"y" : 4,
									
									"default_image" : ACHIEVEMENTS_PATH + "btn_arrowup_1.tga",
									"over_image" : ACHIEVEMENTS_PATH + "btn_arrowup_2.tga",
									"down_image" : ACHIEVEMENTS_PATH + "btn_arrowup_3.tga",
								},
								{
									"name" : "LastDownArrow",
									"type" : "button",
									"horizontal_align" : "center",
									
									"x" : 0,
									"y" : 265 - 18,
									
									"default_image" : ACHIEVEMENTS_PATH + "btn_arrowdown_1.tga",
									"over_image" : ACHIEVEMENTS_PATH + "btn_arrowdown_2.tga",
									"down_image" : ACHIEVEMENTS_PATH + "btn_arrowdown_3.tga",
								},
							),
						},
					),
				},
				{
					"name" : "AchievementsWindow",
					"style" : ("attach",),
					"horizontal_align" : "center",
					
					"x" : 0,
					"y" : 130,
					
					"width" : BOARD_WIDTH - 24,
					"height" : BOARD_HEIGHT - (130+10),
					
					"children" :
					(
						{
							"name" : "Type0Button",
							"type" : "radio_button",
							
							"x" : 75,
							"y" : 14,
							
							"text" : "Todos",
							
							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
						},
						{
							"name" : "Type1Button",
							"type" : "radio_button",
							
							"x" : 75+72+18,
							"y" : 14,
							
							"text" : "Incompletos",
							
							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
						},
						{
							"name" : "Type2Button",
							"type" : "radio_button",
							
							"x" : 75+(72+18)*2,
							"y" : 14,
							
							"text" : "Completados",
							
							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
						},
						{
							"name" : "ScrollBar",
							"type" : "scrollbar",
							"horizontal_align" : "center",
							
							"x" : 250,
							"y" : 40,
							
							"size" : 304,
						},
					),
				},
			),
		},
	),
}