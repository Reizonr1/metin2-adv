import uiScriptLocale
import item
import app
BUTTON_ROOT = "d:/ymir work/ui/public/"
window = {
	"name" : "ChangeLookWindow",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 205,
	"height" : 270,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 205,
			"height" : 270,
		
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : 190,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":95, "y":3, "text":"", "text_horizontal_align":"center" },
					),
				},
				
				## Slot
				{
					"name" : "ChangeLook_SlotImg",
					"type" : "image",
					
					"x" : 9,
					"y" : 35,
					
					"image" : uiScriptLocale.LOCALE_UISCRIPT_PATH + "changelook/ingame_convert.tga",
					
					"children" :
					(
						{
							"name" : "ChangeLookSlot",
							"type" : "slot",
					
							"x" : 3,
							"y" : 3,
					
							"width" : 190,
							"height" : 200,
					
							"slot" : (
								{"index":0, "x":26, "y":30, "width":31, "height":96},  # 메인
								{"index":1, "x":125, "y":30, "width":31, "height":96},  # 서브
							),
						},
					),
				},
				## 비용
				{
					"name" : "Cost",
					"type" : "text",
					"text" : "",
					"text_horizontal_align" : "center",
					"x" : 105,
					"y" : 215,
				},
				## Button
				{
					"name" : "AcceptButton",
					"type" : "button",

					"x" : 40,
					"y" : 235,
					"default_image" : BUTTON_ROOT+"AcceptButton00.sub",
					"over_image" : BUTTON_ROOT+"AcceptButton01.sub",
					"down_image" : BUTTON_ROOT+"AcceptButton02.sub",
				},
				{
					"name" : "CancelButton",
					"type" : "button",

					"x" : 114,
					"y" : 235,
					"default_image" : BUTTON_ROOT+"CancleButton00.sub",
					"over_image" : BUTTON_ROOT+"CancleButton01.sub",
					"down_image" : BUTTON_ROOT+"CancleButton02.sub",
				},
				## ChangeLookToolTip Button
				{
					"name" : "ChangeLookToolTIpButton",
					"type" : "button",

					"x" : 155,
					"y" : 8,

					"default_image" : "d:/ymir work/ui/pattern/q_mark_01.tga",
					"over_image" : "d:/ymir work/ui/pattern/q_mark_02.tga",
					"down_image" : "d:/ymir work/ui/pattern/q_mark_01.tga",
				},			
			),
		},
	),
}

