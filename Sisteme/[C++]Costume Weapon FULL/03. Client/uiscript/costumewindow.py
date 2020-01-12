import app
import item
import uiScriptLocale

COSTUME_START_INDEX = item.COSTUME_SLOT_START

if app.ENABLE_COSTUME_WEAPON_SYSTEM:
	window = {
		"name" : "CostumeWindow",
		"x" : SCREEN_WIDTH - 175 - 140,
		"y" : SCREEN_HEIGHT - 37 - 565,
		"style" : ("movable", "float",),
		"width" : 140,
		"height" : 180 + 47,
		"children" :
		(
			{
				"name" : "board",
				"type" : "board",
				"style" : ("attach",),
				"x" : 0,
				"y" : 0,
				"width" : 140,
				"height" : 180 + 47,
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
							{
								"name":"TitleName",
								"type":"text",
								"x":60,
								"y":3,
								"text":uiScriptLocale.COSTUME_WINDOW_TITLE,
								"text_horizontal_align":"center"
							},
						),
					},
					{
						"name" : "Costume_Base",
						"type" : "image",
						"x" : 13,
						"y" : 38,
						"image" : "d:/ymir work/ui/costume_bg.dds",
						"children" :
						(
							{
								"name" : "CostumeSlot",
								"type" : "slot",
								"x" : 3,
								"y" : 3,
								"width" : 127,
								"height" : 145,
								"slot" : (
											{"index":COSTUME_START_INDEX+0, "x":61, "y":45, "width":32, "height":64},
											{"index":COSTUME_START_INDEX+1, "x":61, "y": 8, "width":32, "height":32},
											{"index":COSTUME_START_INDEX+2, "x":10, "y":5, "width":32, "height":96},
								),
							},
						),
					},
				),
			},
		),
	}
else:
	window = {
		"name" : "CostumeWindow",
		"x" : SCREEN_WIDTH - 175 - 140,
		"y" : SCREEN_HEIGHT - 37 - 565,
		"style" : ("movable", "float",),
		"width" : 140,
		"height" : 180 + 47,
		"children" :
		(
			{
				"name" : "board",
				"type" : "board",
				"style" : ("attach",),
				"x" : 0,
				"y" : 0,
				"width" : 140,
				"height" : 180 + 47,
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
							{
								"name":"TitleName",
								"type":"text",
								"x":60,
								"y":3,
								"text":uiScriptLocale.COSTUME_WINDOW_TITLE,
								"text_horizontal_align":"center"
							},
						),
					},
					{
						"name" : "Costume_Base",
						"type" : "image",
						"x" : 13,
						"y" : 38,
						"image" : "d:/ymir work/ui/costume_bg.dds",
						"children" :
						(
							{
								"name" : "CostumeSlot",
								"type" : "slot",
								"x" : 3,
								"y" : 3,
								"width" : 127,
								"height" : 145,
								"slot" : (
											{"index":COSTUME_START_INDEX+0, "x":61, "y":45, "width":32, "height":64},
											{"index":COSTUME_START_INDEX+1, "x":61, "y": 8, "width":32, "height":32},
								),
							},
						),
					},
				),
			},
		),
	}

