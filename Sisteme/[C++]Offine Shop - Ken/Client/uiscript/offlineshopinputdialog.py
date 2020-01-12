import uiScriptLocale

window = {
	"name" : "OfflineShopInputDialog",
	
	"x" : 0,
	"y" : 0,
	
	"style" : ("movable", "float",),
	
	"width" : 386,
	"height" : 194,
	
	"children" :
	(
		# board
		{
			"name" : "board",
			"type" : "board",
			
			"style" : ("attach",),
			
			"x" : 0,
			"y" : 0,
			
			"width" : 386,
			"height" : 194,
			
			"children":
			(
				{
					"name" : "time",
					"type" : "expanded_image",
					
					"x" : 0,
					"y" : 0,
					
					"image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/time.tga",
				},
				
				{
					"name" : "AgreeButton",
					"type" : "button",
					
					"x" : 125,
					"y" : 161,
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
					
					"text" : "Agree",
				},
				
				{
					"name" : "CancelButton",
					"type" : "button",
					
					"x" : 220,
					"y" : 161,
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
					
					"text" : "Cancel",
				},
				
				{
					"name" : "oneHour",
					"type" : "radio_button",
					
					"x" : 113,
					"y" : 39,
					
					"default_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_default.sub",
					"over_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_over.sub",
					"down_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_down.sub",
				},
				
				{
					"name" : "oneHour",
					"type" : "radio_button",
					
					"x" : 113,
					"y" : 39,
					
					"default_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_default.sub",
					"over_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_over.sub",
					"down_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_down.sub",
				},

				{
					"name" : "twoHours",
					"type" : "radio_button",
					
					"x" : 174,
					"y" : 39,
					
					"default_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_default.sub",
					"over_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_over.sub",
					"down_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_down.sub",
				},

				{
					"name" : "fourHours",
					"type" : "radio_button",
					
					"x" : 244,
					"y" : 39,
					
					"default_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_default.sub",
					"over_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_over.sub",
					"down_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_down.sub",
				},

				{
					"name" : "unlimited",
					"type" : "radio_button",
					
					"x" : 310,
					"y" : 39,
					
					"default_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_default.sub",
					"over_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_over.sub",
					"down_image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/new_checkbox_down.sub",
				},

				{
					"name" : "oneHourText",
					"type" : "text",
					
					"x" : 135,
					"y" : 39,
					
					"text" : "1 Hour",
				},
				
				{
					"name" : "twoHoursText",
					"type" : "text",
					
					"x" : 197,
					"y" : 39,
					
					"text" : "2 Hours",
				},
				
				{
					"name" : "fourHoursText",
					"type" : "text",
					
					"x" : 267,
					"y" : 39,
					
					"text" : "4 Hours",
				},
				
				{
					"name" : "unlimitedText",
					"type" : "text",
					
					"x" : 332,
					"y" : 39,
					
					"text" : "Unlimited",
				},
				
				{
					"name" : "title2",
					"type" : "text",
					
					"x" : 28,
					"y" : 123,
					
					"text" : "Offline Shop Name",
				},
				
				## Input Slot
				{
					"name" : "InputSlot",
					"type" : "slotbar",

					"x" : 50,
					"y" : 123,
					
					"width" : 235,
					"height" : 15,
					
					"horizontal_align" : "center",
					
					"children" :
					(
						{
							"name" : "InputValue",
							"type" : "editline",

							"x" : 1,
							"y" : 1,

							"width" : 235,
							"height" : 15,

							"input_limit" : 32,
						},
					),
				},				
			),
		},
	),
}