BOARD_WIDTH = 800
BOARD_HEIGHT = 520
ACHIEVEMENTS_PATH = "d:/ymir work/ui/achievementsystem/"

window = {
	"name" : "AchievementShopWindow",
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
			
			"title" : "Tienda de Logros",
			"children" :
			(
				{
					"name" : "bgTmpUserPanel",
					"type" : "thinboard",
					"horizontal_align" : "center",
					
					"x" : 0,
					"y" : 35,
					
					"width" : BOARD_WIDTH - 20,
					"height" : 50,
					
					"children" :
					(
						{
							"name" : "APSlot",
							"type" : "resizable_text_value",
							"vertical_align" : "center",
							"horizontal_align" : "center",
							
							"x" : 0,
							"y" : 0,
							
							"width" : 160,
							"height" : 22,
							
							"text" : "100.000 AP's",
							"all_lines" : 1,
							
							"children" :
							(
								{
									"name" : "AchievementIcon",
									"type" : "image",
									"vertical_align" : "center",
									
									"x" : -18,
									"y" : 0,
									
									"image" : ACHIEVEMENTS_PATH + "achievement_icon_amount.tga",
								},
							),
						},
					),
				},
				{
					"name" : "bgCategorys",
					"type" : "thinboard",
					
					"x" : 10,
					"y" : 35+50+5,
					
					"width" : 135,
					"height" : BOARD_HEIGHT - (35+50+5+10),
					
					"children" :
					(
						{
							"name" : "CategorysUpArrow",
							"type" : "button",
							"horizontal_align" : "center",
							
							"x" : 0,
							"y" : 8,
							
							"default_image" : ACHIEVEMENTS_PATH + "btn_arrowup_1.tga",
							"over_image" : ACHIEVEMENTS_PATH + "btn_arrowup_2.tga",
							"down_image" : ACHIEVEMENTS_PATH + "btn_arrowup_3.tga",
						},
						{
							"name" : "CategorysDownArrow",
							"type" : "button",
							"horizontal_align" : "center",
							"vertical_align" : "bottom",
							
							"x" : 0,
							"y" : 11+8,
							
							"default_image" : ACHIEVEMENTS_PATH + "btn_arrowdown_1.tga",
							"over_image" : ACHIEVEMENTS_PATH + "btn_arrowdown_2.tga",
							"down_image" : ACHIEVEMENTS_PATH + "btn_arrowdown_3.tga",
						},
					),
				},
				{
					"name" : "bgItems",
					"type" : "thinboard",
					
					"x" : 10+135+3,
					"y" : 35+50+5,
					
					"width" : BOARD_WIDTH - (10+135+3+10),
					"height" : BOARD_HEIGHT - (35+50+5+10),
					
					"children" :
					(
						{
							"name" : "PageNumber",
							"type" : "resizable_text_value",
							"vertical_align" : "bottom",
							
							"x" : (642-60)/2,
							"y" : 22+8,
							
							"width" : 60,
							"height" : 22,
							
							"text" : "10/100",
							"all_lines" : 1,
						},
						{
							"name" : "ItemsLeftArrow",
							"type" : "button",
							"vertical_align" : "bottom",
							"horizontal_align" : "center",
							
							"x" : -42,
							"y" : 11+17,
							
							"default_image" : ACHIEVEMENTS_PATH + "btn_arrowleft_1.tga",
							"over_image" : ACHIEVEMENTS_PATH + "btn_arrowleft_2.tga",
							"down_image" : ACHIEVEMENTS_PATH + "btn_arrowleft_3.tga",
						},
						{
							"name" : "ItemsRightArrow",
							"type" : "button",
							"vertical_align" : "bottom",
							"horizontal_align" : "center",
							
							"x" : 42,
							"y" : 11+17,
							
							"default_image" : ACHIEVEMENTS_PATH + "btn_arrowright_1.tga",
							"over_image" : ACHIEVEMENTS_PATH + "btn_arrowright_2.tga",
							"down_image" : ACHIEVEMENTS_PATH + "btn_arrowright_3.tga",
						},
					),
				},
			),
		},
	),
}
