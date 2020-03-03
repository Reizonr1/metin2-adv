import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/game/windows/"
ROOT = "d:/ymir work/ui/game/"
SUPPORT_DIRECTORY = "d:/ymir work/ui/support/"
SMALL_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_00.sub"
MIDDLE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_01.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_03.sub"
XLARGE_BUTTON_FILE = "d:/ymir work/ui/public/xlarge_button_03.sub"
BASE_SLOT_FILE = "d:/ymir work/ui/public/Slot_Base.sub"

SUPPORT_BG_WIDTH		= 352
SUPPORT_BG_HEIGHT	= 416

LONG_LABEL_WIDTH	= 266
LONG_LABEL_HEIGHT	= 19

SHORT_LABLE_WIDTH	= 90
SHORT_LABLE_HEIGHT	= 20

MIDDLE_LABLE_WIDTH	= 168
MIDDLE_LABLE_HEIGHT	= 20

EXP_GAGUE_INTERVAL	= 2
EXP_IMG_WIDTH		= 16
EXP_IMG_HEIGHT		= 16

GOLD_COLOR	= 0xFFFEE3AE
WHITE_COLOR = 0xFFFFFFFF
ORANGE_COLOR = 0xFFF2A505
	
window = {
	"name" : "SupportInformationWindow",
	"style" : ("movable", "float",),
	
	"x" : SCREEN_WIDTH - 176 -200 -146 -145,
	"y" : SCREEN_HEIGHT - 37 - 565,

	"width" : SUPPORT_BG_WIDTH,
	"height" : SUPPORT_BG_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : SUPPORT_BG_WIDTH,
			"height" : SUPPORT_BG_HEIGHT,
			
			"children" :
			(
				## Support UI BG
				{ "name" : "PetUIBG", "type" : "expanded_image", "style" : ("attach",), "x" : 0, "y" : 0, "image" : "d:/ymir work/ui/support/support_bg.tga" },
				
				## Support Information Title
				{ 
					"name" : "TitleWindow", "type" : "window", "x" : 10, "y" : 10, "width" : SUPPORT_BG_WIDTH-10-15, "height" : 15, "style" : ("attach",),
					"children" :
					(
						{"name":"TitleName", "type":"text", "x":0, "y":0, "text":"Support Character System", "all_align" : "center"},
					),	
				},
				
				## Close Button
				{ 
					"name" : "CloseButton", 
					"type" : "button", 
					"x" : SUPPORT_BG_WIDTH -10-15, 
					"y" : 10, 
					"tooltip_text" : "Close", 
					"default_image" : "d:/ymir work/ui/public/close_button_01.sub",	
					"over_image" : "d:/ymir work/ui/public/close_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/close_button_03.sub",
				},
				{
					"name" : "SlotSupportImage",
					"type" : "slot",
					"x" : 25,
					"y" : 226,
					"width" : 32,
					"height" : 32,
					
					"slot" : ({"index":0, "x":0, "y":0, "width":32, "height":32},),
				},
				
				## Support Name Window
				{ 
					"name" : "SupportsNameWindow", "type" : "window", "x" : 227, "y" : 30, "width" : SHORT_LABLE_WIDTH, "height" : SHORT_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"SupportsNameWindows", "type":"text", "x":0, "y":0, "text": "Name", "color":GOLD_COLOR, "all_align" : "center"},
					),	
				},
				##Slot Support
				{
					"name" : "CombSlot",
					"type" : "slot",
			
					"x" : 8,
					"y" : 90,
			
					"width" : 300,
					"height" : 300,
			
					"slot" :
					(
						{"index":1, "x":69, "y":220, "width":31, "height":96},
						{"index":2, "x":243, "y":243, "width":32, "height":32},
					),
					
					"children" :
					(
						{
							"name" : "Slot1_Name",
							"type":"text",
							"x":85,
							"y":200,
							"text" : "Costume",
							"text_horizontal_align":"center"
						},
						{
							"name" : "Slot2_Name",
							"type":"text",
							"x":260,
							"y":200,
							"text" : "Hair",
							"text_horizontal_align":"center"
						},
					),
				},
				## Support Name
				{ 
					"name" : "NameWindow", "type" : "window", "x" : 136, "y" : 26+SHORT_LABLE_HEIGHT+3, "width" : LONG_LABEL_WIDTH, "height" : LONG_LABEL_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"SupportsName", "type":"text", "x":0, "y":0, "text": "", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "all_align" : "center"},
					),	
				},
				
				## Level Title
				{ 
					"name" : "LevelWindow", "type" : "window", "x" : 228, "y" : 72, "width" : SHORT_LABLE_WIDTH, "height" : SHORT_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"LevelTitle", "type":"text", "x":0, "y":0, "text": "Level", "color":GOLD_COLOR, "all_align" : "center"},
					),	
				},
				## Level Value
				{ 
					"name" : "LevelValueWindow", "type" : "window", "x" : 228, "y" : 69+SHORT_LABLE_HEIGHT+3, "width" : SHORT_LABLE_WIDTH, "height" : SHORT_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"LevelValue", "type":"text", "x":0, "y":0, "text": "", "color":WHITE_COLOR, "all_align" : "center"},
					),	
				},
				## Specialita Title
				{ 
					"name" : "SpecialityWindow", "type" : "window", "x" : 228, "y" : 115, "width" : SHORT_LABLE_WIDTH, "height" : SHORT_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"SpecialityTitle", "type":"text", "x":0, "y":0, "text": "Speciality", "color":GOLD_COLOR, "all_align" : "center"},
					),	
				},
				## Speciality Value
				{ 
					"name" : "SpecialityValueWindow", "type" : "window", "x" : 228, "y" : 111+SHORT_LABLE_HEIGHT+3, "width" : SHORT_LABLE_WIDTH, "height" : SHORT_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"SpecialityValue", "type":"text", "x":0, "y":0, "text": "", "color":WHITE_COLOR, "all_align" : "center"},
					),	
				},			
				## EXP Title
				{ 
					"name" : "ExpWindow", "type" : "window", "x" : 228, "y" : 158, "width" : SHORT_LABLE_WIDTH, "height" : SHORT_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"ExpTitle", "type":"text", "x":0, "y":0, "text": "Experience", "color":GOLD_COLOR, "all_align" : "center"},
					),	
				},
				## EXP Gauge
				{
					"name" : "UpBringing_Support_EXP_Gauge_Board",
					"type" : "window",
					"style": ("ltr",),

					"x" : 232,
					"y" : 180,
				
					"width"		: EXP_IMG_WIDTH * 5 + EXP_GAGUE_INTERVAL * 4,
					"height"	: EXP_IMG_HEIGHT,

					"children" :
					(
						{
							"name" : "UpBringing_Support_EXPGauge_01",
							"type" : "expanded_image",

							"x" : 0,
							"y" : 0,

							"image" : SUPPORT_DIRECTORY + "exp_gauge/exp_on.sub",
						},
						{
							"name" : "UpBringing_Support_EXPGauge_02",
							"type" : "expanded_image",

							"x" : EXP_IMG_WIDTH + EXP_GAGUE_INTERVAL + 1,
							"y" : 0,

							"image" : SUPPORT_DIRECTORY + "exp_gauge/exp_on.sub",
						},
						{
							"name" : "UpBringing_Support_EXPGauge_03",
							"type" : "expanded_image",

							"x" : EXP_IMG_WIDTH * 2 + EXP_GAGUE_INTERVAL * 2 + 3,
							"y" : 0,

							"image" : SUPPORT_DIRECTORY + "exp_gauge/exp_on.sub",
						},
						{
							"name" : "UpBringing_Support_EXPGauge_04",
							"type" : "expanded_image",

							"x" : EXP_IMG_WIDTH * 3 + EXP_GAGUE_INTERVAL * 3 + 4,
							"y" : 0,

							"image" : SUPPORT_DIRECTORY + "exp_gauge/exp_on.sub",
						},
					),
				}, 
				#End of EXP
				{ 
					"name" : "AbilitiesWindow", "type" : "window", "x" : 43, "y" : 202, "width" : LONG_LABEL_WIDTH, "height" : LONG_LABEL_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"AbilitiesName", "type":"text", "x":0, "y":0, "text": "Bonus", "color":ORANGE_COLOR, "all_align" : "center"},
					),	
				},
				##Equip
				{ 
					"name" : "EquipWindow", "type" : "window", "x" : 43, "y" : 265, "width" : LONG_LABEL_WIDTH, "height" : LONG_LABEL_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"EquipName", "type":"text", "x":0, "y":0, "text": "Equipment", "color":ORANGE_COLOR, "all_align" : "center"},
					),	
				},		
				## Int Title
				{ 
					"name" : "IntWindow", "type" : "window", "x" : 25, "y" : 232, "width" : MIDDLE_LABLE_WIDTH, "height" : MIDDLE_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"IntTitle", "type":"text", "x":0, "y":0, "text": "Intelligence Value", "color":GOLD_COLOR, "all_align" : "center"},
					),	
				},
				## Int Value
				{ 
					"name" : "IntValueWindow", "type" : "window", "x" : -10 + MIDDLE_LABLE_WIDTH, "y" : 232, "width" : MIDDLE_LABLE_WIDTH, "height" : MIDDLE_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"SupportIntValue", "type":"text", "x":0, "y":0, "text": "", "color":WHITE_COLOR, "all_align" : "center"},
					),	
				},
			),			
		},
	),
}
