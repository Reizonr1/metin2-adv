Search:
				{
					"name" : "salestext_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 240,

					"text" : uiScriptLocale.OPTION_SALESTEXT_VIEW_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				
Add it under:

				{
					"name" : "emotionblock_on_off",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 265+2,

					"text" : "Emotion",
				},
				{
					"name" : "emotionblock_on_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X,
					"y" : 265,

					"text" : "Block",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},