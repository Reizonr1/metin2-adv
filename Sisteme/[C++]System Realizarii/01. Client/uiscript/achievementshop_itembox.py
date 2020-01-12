BOARD_WIDTH = 200
BOARD_HEIGHT = 105

window = {
	"name" : "AchievementShopItemBox",
	
	"x" : 0,
	"y" : 0,
	
	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,
	
	"children" :
	(
		{
			"name" : "board",
			"type" : "resizable_text_value",
			"style" : ("attach",),
			
			"x" : 0,
			"y" : 0,
			
			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
			
			"all_lines" : 1,
			
			"children" :
			(
				{
					"name" : "ItemName",
					"type" : "resizable_text_value",
					"horizontal_align" : "right",
					
					"x" : 170,
					"y" : 0,
					
					"width" : 170,
					"height" : 18,
					
					"text" : "Nombre del Item",
					"all_lines" : 1,
				},
				{
					"name" : "ItemIcon",
					"type" : "expanded_image",
					
					"x" : 35,
					"y" : 32,
					
					"image" : "icon/item/00010.tga",
				},
				{
					"name" : "ItemPrice",
					"type" : "resizable_text_value",
					"horizontal_align" : "right",
					
					"x" : 100,
					"y" : 18,
					
					"width" : 100,
					"height" : 18,
					
					"text" : "Precio: 9000 AP's",
					"all_lines" : 1,
				},
				{
					"name" : "ItemAmountSlot",
					"type" : "resizable_text_value",
					"horizontal_align" : "right",
					
					"x" : 100,
					"y" : 18*2,
					
					"width" : 100,
					"height" : 18,
					
					"all_lines" : 1,
					
					"children" :
					(
						{
							"name" : "ItemAmountTxt",
							"type" : "text",
							"all_align" : 1,
							
							"x" : 11,
							"y" : 0,
							"outline" : 1,
							
							"text" : "ud.",
						},
						{
							"name" : "ItemAmount",
							"type" : "editline",
							
							"x" : (100/2) - 13,
							"y" : 3,
							
							"width" : 10,
							"height" : 18,
							
							"text" : "1",
							"outline" : 1,
							"input_limit" : 3,
							"only_number" : 1,
						},
					),
				},
				{
					"name" : "BuyButton",
					"type" : "button",
					"horizontal_align" : "right",
					"vertical_align" : "bottom",
					
					"x" : 75+13,
					"y" : 35+8,
					
					"default_image" : "d:/ymir work/ui/achievementsystem/buy_btn_1.tga",
					"over_image" : "d:/ymir work/ui/achievementsystem/buy_btn_2.tga",
					"down_image" : "d:/ymir work/ui/achievementsystem/buy_btn_3.tga",
				},
			),
		},
	),
}