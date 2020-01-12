import item
import uiScriptLocale

COSTUME_START_INDEX = item.COSTUME_SLOT_START

window = {
	"name" : "CostumeWindow",
	"x" : SCREEN_WIDTH - 175 - 140,
	"y" : SCREEN_HEIGHT - 37 - 565,
	"style" : ("movable", "float",),
	"width" : 140,
	"height" : 180 + 47 + 57,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : 140,
			"height" : 180 + 47 + 57,
			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : 130,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":60, "y":3, "text":uiScriptLocale.COSTUME_WINDOW_TITLE, "text_horizontal_align":"center" },
					),
				},
				
				{
					"name" : "TitleBarEffect",
					"type" : "horizontalbar",
					"style" : ("attach",),
					"x" : 11,
					"y" : 219,
					"width" : 118,
					"children" :
					(
						{
							"name" : "TitleName",
							"type" : "text",
							"x" : 0,
							"y" : -1,
							"text" : uiScriptLocale.SPECIAL_EFFECTS_TITLE,
							"all_align" : "center",
						},
					),
				},
				
				{
					"name" : "EffectSlots_Base",
					"type" : "image",
					"x" : 13,
					"y" : 219 + 16,
					"image" : "locale/tr/ui/costume/effect_slot_bg.jpg",
				},
				
				{
					"name" : "Costume_Base",
					"type" : "image",
					"x" : 13,
					"y" : 38,
					"image" : "locale/tr/ui/costume/new_costume_bg.tga",
					"children" :
					(
						{
							"name" : "CostumeSlot",
							"type" : "slot",
							"x" : 3,
							"y" : 3,
							"width" : 127,
							"height" : 236 + 11,
							"slot" : (
										{"index":COSTUME_START_INDEX+0, "x":61, "y":45, "width":32, "height":64},
										{"index":COSTUME_START_INDEX+1, "x":61, "y": 8, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+2, "x":61, "y":125, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+3, "x":10, "y":125, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+4, "x":10, "y":5, "width":32, "height":96},
										{"index":COSTUME_START_INDEX+5, "x":1, "y":4+197, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+6, "x":52, "y": 5+197, "width":32, "height":32},
							),
						},
					),
				},
			),
		},
	),
}

