import uiScriptLocale

ROOT = "d:/ymir work/ui/game/"
ROW_BACKGROUND 	= 'd:/ymir work/ui/public/slot_base.sub'
ICON_FILE 		= "d:/ymir work/ui/slot.tga"

BOARD_WIDTH  = 250
BOARD_HEIGHT = 90
ROW_START    = 28

TITLE_COLOR = {
	"r" : 254.0/255.0,
	"g" : 253.0/255.0,
	"b" : 196.0/255.0,
}

window = {
	"name" : "ExchangeDialog",

	"x" : SCREEN_WIDTH - 175 - BOARD_WIDTH,
	"y" : 65,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH, 
			"height" : BOARD_HEIGHT,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,
 
					"width" : BOARD_WIDTH - 14, 
					"color" : "gray",

					"children" :
					(
						{
							"name" : "Title", "type" : "text", "text" : "Duello Istegi", "x" : 0, "y" : -1,
							"fontsize" : "LARGE", "outline" : 1, "all_align" : "center",
							"r" : TITLE_COLOR["r"], "g" : TITLE_COLOR["g"], "b" : TITLE_COLOR["b"], "a" : 1.0 
						},
					),
				},
				
				{
					"name" : "Guide_Background_0", "type" : "image", 
					"x" : 5 + 0, "y" : ROW_START + (0 * 58) + 0, 
					"width" : BOARD_WIDTH - 10, "height" : 58,
				},
				
				{ 
					"name" : "CharacterIcon", "type" : "image", 
					"x" : 5 + 5, "y" : ROW_START + (0 * 58) + 7, 
					"width" : 32, "height" : 32, "image" : ICON_FILE,
				},
				{ 
					"name" : "RequesterName", "type" : "text", "text" : "Title", 
					"x" : 5 + 45, "y" : ROW_START + (0 * 58) + 7,
					"fontsize" : "LARGE", "outline" : 1, "horizontal_align" : "left",
					"r" : TITLE_COLOR["r"], "g" : TITLE_COLOR["g"], "b" : TITLE_COLOR["b"], "a" : 1.0
				},
				{ 
					"name" : "DuelText", "type" : "text", "text" : "Message 1",
					"x" : 5 + 45, "y" : ROW_START + (0 * 58) + 22
				},


				## Owner
				{
					"name" : "Owner",
					"type" : "window",

					"x" : 144,
					"y" : 33,

					"width" : 130,
					"height" : 130,

					"children" :
					(
						{
							"name" : "ApplyButton",
							"type" : "button",

							"x" : 53,
							"y" : 2,
					
							"text_color" : 0xffffffff,

							"text" : uiScriptLocale.EXCHANGE_ACCEPT,

							"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
						},
						
						{
							"name" : "DenyButton",
							"type" : "button",

							"x" : 53,
							"y" : 27,
					
							"text_color" : 0xffffffff,

							"text" : "Reddet",
							#reject

							"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
						},
					),
				},
			),
		},
	),
}