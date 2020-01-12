import localeInfo

window = {
	"name" : "OxEventManagerLogin",
	"x" : 0,
	"y" : 0,
	"style" : ("movable", "float",),
	"width" : 240,
	"height" : 90,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"x" : 0,
			"y" : 0,
			"width" : 230,
			"height" : 90,
			"children" :
			(
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,
 
					"width" : 217,
					"color" : "gray",

					"children" :
					(
						{
							"name" : "TitleName",
							"type" : "text",
							"x" : 0,
							"y" : 3,
							"horizontal_align" : "center",
							"text" : localeInfo.OXEVENT_MANAGER_LOGIN_TITLENAME,
							"text_horizontal_align":"center"
						},
					),
				},
				{
					"name" : "currentLine",
					"type" : "image",
					"x" : 126,
					"y" : 34,
					"image" : "d:/ymir work/ui/public/Parameter_Slot_03.sub",
					"children" :
					(
						{
							"name" : "currentLine_Text",
							"type" : "text",
							"x" : -110,
							"y" : 3,
							"text" : localeInfo.OXEVENT_MANAGER_LOGIN_PASSWORD,
						},
						{
							"name" : "currentLine_Value",
							"type" : "editline",
							"x" : 3,
							"y" : 3,
							"width" : 100,
							"height" : 18,
							"input_limit" : 12,
						},
					),
				},
				
				{
					"name" : "accept_button",
					"type" : "button",
					"x" : -50,
					"y" : 60,
					"text" : localeInfo.OXEVENT_MANAGER_LOGIN_CONNECT,
					"horizontal_align" : "center",
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},

				{
					"name" : "cancel_button",
					"type" : "button",
					"x" : 40,
					"y" : 60,
					"horizontal_align" : "center",
					"text" : localeInfo.OXEVENT_MANAGER_LOGIN_CANCEL,
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
			),
		},
	),
}