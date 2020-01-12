import uiScriptLocale
import app

ROOT = "d:/ymir work/ui/game/"

BOARD_ADD_X = 10
BOARD_X = SCREEN_WIDTH - (140 + BOARD_ADD_X)
BOARD_WIDTH = (140 + BOARD_ADD_X)
BOARD_HEIGHT = 40

window = {
	"name" : "ExpandedMoneyTaskbar",
	
	"x" : BOARD_X,
	"y" : SCREEN_HEIGHT - 65,

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"style" : ("float",),

	"children" :
	[
		{
			"name" : "ExpanedMoneyTaskBar_Board",
			"type" : "board",

			"x" : -100,
			"y" : 0,

			"width" : BOARD_WIDTH+100,
			"height" : BOARD_HEIGHT,

			"children" :
			[
				## Print
				{
					"name":"Money_Icon",
					"type":"image",
					
					"x":118 + BOARD_ADD_X,
					"y":11,

					"image":"d:/ymir work/ui/game/windows/money_icon.sub",
				},
				{
					"name":"Money_Slot",
					"type":"button",

					"x":139 + BOARD_ADD_X,
					"y":10,

					#"horizontal_align":"center",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_03.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_03.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_03.sub",

					"children" :
					(
						{
							"name" : "Money",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "9,999,999,999",
						},
					),
				},
				## Gaya
				{
					"name":"Gem_Icon",
					"type":"image",
					
					"x":BOARD_ADD_X,
					"y":12,

					"image":"gaya.tga",
				},
				{
					"name":"Money_Slot",
					"type":"button",

					"x":18 + BOARD_ADD_X,
					"y":10,

					#"horizontal_align":"center",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_03.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_03.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_03.sub",

					"children" :
					(
						{
							"name" : "Gem",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "1234567",
						},
					),
				},
			],
		},		
	],
}
				