import uiScriptLocale

window = {
	"name" : "ShopDialog",

	"x" : SCREEN_WIDTH - 400,
	"y" : 10,

	"style" : ("movable", "float",),

	"width" : 184,
	"height" : 328,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 184,
			"height" : 328,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 7,
					"y" : 8,

					"width" : 169,
					"color" : "gray",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":84, "y":4, "text":uiScriptLocale.SHOP_TITLE, "text_horizontal_align":"center" },
					),
				},

				{
					"name" : "ItemSlot_40", "type" : "grid_table", "x" : 12, "y" : 34,	"start_index" : 0,
					"x_count" : 5, "y_count" : 8, "x_step" : 32, "y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
				{
					"name" : "ItemSlot_50", "type" : "grid_table", "x" : 12, "y" : 34,	"start_index" : 0,
					"x_count" : 5, "y_count" : 10, "x_step" : 32, "y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
				{
					"name" : "ItemSlot_60", "type" : "grid_table", "x" : 12, "y" : 34,	"start_index" : 0,
					"x_count" : 6, "y_count" : 10, "x_step" : 32, "y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},				
				{
					"name" : "ItemSlot_70", "type" : "grid_table", "x" : 12, "y" : 34,	"start_index" : 0,
					"x_count" : 7, "y_count" : 10, "x_step" : 32, "y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
					{
					"name" : "ItemSlot_80", "type" : "grid_table", "x" : 12, "y" : 34,	"start_index" : 0,
					"x_count" : 8, "y_count" : 10, "x_step" : 32, "y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
					{
					"name" : "ItemSlot_90", "type" : "grid_table", "x" : 12, "y" : 34,	"start_index" : 0,
					"x_count" : 9, "y_count" : 10, "x_step" : 32, "y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},

				## Buy
				{
					"name" : "BuyButton",
					"type" : "toggle_button",

					"x" : 21,
					"y" : 295,

					"width" : 61,
					"height" : 21,

					"text" : uiScriptLocale.SHOP_BUY,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				## Sell
				{
					"name" : "SellButton",
					"type" : "toggle_button",

					"x" : 104,
					"y" : 295,

					"width" : 61,
					"height" : 21,

					"text" : uiScriptLocale.SHOP_SELL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				## Move
				{
					"name" : "MoveButton",
					"type" : "button",

					"x" : -35,
					"y" : 295+25-7,

					"horizontal_align" : "center",

					"text" : "Move",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				## Close
				{
					"name" : "CloseButton",
					"type" : "button",

					"x" : 35,
					"y" : 295+25-7,

					"horizontal_align" : "center",

					"text" : uiScriptLocale.PRIVATE_SHOP_CLOSE_BUTTON,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				
				
				{
					"name" : "MoneySlot",
					"type" : "text",

					"x" : 20,
					"y" : 295,

					"text" : "Gain:",

					"children" :
					(
						{
							"name" : "MoneySlot2",
							"type" : "image",

							"x" : 36,
							"y" : -2,

							"image" : "d:/ymir work/ui/public/Parameter_Slot_04.sub",

							"children" :
							(
								{
									"name" : "Money",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"text" : "0 Yang",

									"all_align" : "center"
								},
							),
						},
					),
				},


				## MiddleTab1
				{
					"name" : "MiddleTab1",
					"type" : "radio_button",

					"x" : 21,
					"y" : 295,

					"width" : 61,
					"height" : 21,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				## MiddleTab2
				{
					"name" : "MiddleTab2",
					"type" : "radio_button",

					"x" : 104,
					"y" : 295,

					"width" : 61,
					"height" : 21,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				## SmallTab1
				{
					"name" : "SmallTab1",
					"type" : "radio_button",

					"x" : 21,
					"y" : 295,

					"width" : 43,
					"height" : 21,

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
				},

				## SmallTab2
				{
					"name" : "SmallTab2",
					"type" : "radio_button",

					"x" : 71,
					"y" : 295,

					"width" : 43,
					"height" : 21,

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
				},

				## SmallTab3
				{
					"name" : "SmallTab3",
					"type" : "radio_button",

					"x" : 120,
					"y" : 295,

					"width" : 43,
					"height" : 21,

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
				},
			),
		},
	),
}