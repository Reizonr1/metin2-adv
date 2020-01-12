Find:
"name" : "GameOptionDialog",

Search:
"height" : 25*12+8,

Change like this(+1 to 2.number):
"height" : 25*13+8,


Find:
"name" : "board",

Search:
"height" : 25*12+8,

Change like this(+1 to 2.number):
"height" : 25*13+8,

https://puu.sh/sgQIq/9d2a87da0d.png

---

Search:
				{
					"name" : "salestext_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 265,

					"text" : uiScriptLocale.OPTION_SALESTEXT_VIEW_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

Add it under:
				{
					"name" : "show_offline_shop_name",
					"type" : "text",

					"multi_line" : 1,

					"x" : LINE_LABEL_X,
					"y" : 290+2,

					"text" : "Offline Shops",
				},
				{
					"name" : "show_offline_shop_on",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 290,

					"text" : "Show",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "show_offline_shop_wome",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 290,

					"text" : "MyShops",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "show_offline_shop_off",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
					"y" : 290,

					"text" : "Hide",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
