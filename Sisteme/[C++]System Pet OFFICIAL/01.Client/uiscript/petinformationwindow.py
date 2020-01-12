import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/game/windows/"
ROOT = "d:/ymir work/ui/game/"
PET_UI_ROOT = "d:/ymir work/ui/pet/"
SMALL_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_00.sub"
MIDDLE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_01.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_03.sub"
XLARGE_BUTTON_FILE = "d:/ymir work/ui/public/xlarge_button_03.sub"
BASE_SLOT_FILE = "d:/ymir work/ui/public/Slot_Base.sub"

PET_UI_BG_WIDTH		= 352
PET_UI_BG_HEIGHT	= 416

## Evol Name, Pet Name, Pet Abilities
LONG_LABEL_WIDTH	= 266
LONG_LABEL_HEIGHT	= 19

## Level, exp, age, life
SHORT_LABLE_WIDTH	= 90
SHORT_LABLE_HEIGHT	= 20

## Defence, Magic Defence, HP
MIDDLE_LABLE_WIDTH	= 168
MIDDLE_LABLE_HEIGHT	= 20

## EXP Gague interval
EXP_GAGUE_INTERVAL	= 2
EXP_IMG_WIDTH		= 16
EXP_IMG_HEIGHT		= 16

## TEXT COLOR
GOLD_COLOR	= 0xFFFEE3AE
WHITE_COLOR = 0xFFFFFFFF
	
window = {
	"name" : "PetInformationWindow",
	"style" : ("movable", "float",),
	
	"x" : SCREEN_WIDTH - 176 -200 -146 -145,	## inven x ÁÂÇ¥¿¡¼­ ´õ »©ÁØ´Ù.
	"y" : SCREEN_HEIGHT - 37 - 565,				## inven y ÁÂÇ¥¿Í °°´Ù.

	"width" : PET_UI_BG_WIDTH,
	"height" : PET_UI_BG_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : PET_UI_BG_WIDTH,
			"height" : PET_UI_BG_HEIGHT,
			
			"children" :
			(
				## Pet UI BG
				{ "name" : "PetUIBG", "type" : "expanded_image", "style" : ("attach",), "x" : 0, "y" : 0, "image" : "d:/ymir work/ui/pet/Pet_UI_bg.tga" },
				
				## Pet Information Title
				{ 
					"name" : "TitleWindow", "type" : "window", "x" : 10, "y" : 10, "width" : PET_UI_BG_WIDTH-10-15, "height" : 15, "style" : ("attach",),
					"children" :
					(
						{"name":"TitleName", "type":"text", "x":0, "y":0, "text":"Pet", "all_align" : "center"},
					),	
				},
				
				## Close Button
				{ 
					"name" : "CloseButton", 
					"type" : "button", 
					"x" : PET_UI_BG_WIDTH -10-15, 
					"y" : 10, 
					"tooltip_text" : "Close", 
					"default_image" : "d:/ymir work/ui/public/close_button_01.sub",	
					"over_image" : "d:/ymir work/ui/public/close_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/close_button_03.sub",
				},
				
				## UpBringing Pet Item Slot
				{
					"name" : "UpBringing_Pet_Slot",
					"type" : "slot",
					"x" : 25,
					"y" : 55,
					"width" : 32,
					"height" : 32,
					
					"slot" : ({"index":0, "x":0, "y":0, "width":32, "height":32},),
				},
				
				## Normal Evol Name + Special Evol Name
				{ 
					"name" : "EvolNameWindow", "type" : "window", "x" : 65, "y" : 50, "width" : LONG_LABEL_WIDTH, "height" : LONG_LABEL_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"EvolName", "type":"text", "x":0, "y":0, "text": "Lv. 3 (Special Evolution)", "r":1.0, "g":0.0, "b":0.0, "a":1.0, "all_align" : "center"},
					),	
				},
				
				## Pet Name
				{ 
					"name" : "NameWindow", "type" : "window", "x" : 65, "y" : 75, "width" : LONG_LABEL_WIDTH, "height" : LONG_LABEL_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"PetName", "type":"text", "x":0, "y":0, "text": "Super Baby White Dragon", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "all_align" : "center"},
					),	
				},
				
				## Level Title
				{ 
					"name" : "LevelWindow", "type" : "window", "x" : 28, "y" : 124, "width" : SHORT_LABLE_WIDTH, "height" : SHORT_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"LevelTitle", "type":"text", "x":0, "y":0, "text": "Level", "color":GOLD_COLOR, "all_align" : "center"},
					),	
				},
				## Level Value
				{ 
					"name" : "LevelValueWindow", "type" : "window", "x" : 28, "y" : 124+SHORT_LABLE_HEIGHT+3, "width" : SHORT_LABLE_WIDTH, "height" : SHORT_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"LevelValue", "type":"text", "x":0, "y":0, "text": "", "color":WHITE_COLOR, "all_align" : "center"},
					),	
				},
				
				## EXP Title
				{ 
					"name" : "ExpWindow", "type" : "window", "x" : 131, "y" : 124, "width" : SHORT_LABLE_WIDTH, "height" : SHORT_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"ExpTitle", "type":"text", "x":0, "y":0, "text": "Experience", "color":GOLD_COLOR, "all_align" : "center"},
					),	
				},
				## EXP Gauge
				{
					"name" : "UpBringing_Pet_EXP_Gauge_Board",
					"type" : "window",
					"style": ("ltr",),

					"x" : 131,
					"y" : 149,
				
					"width"		: EXP_IMG_WIDTH * 5 + EXP_GAGUE_INTERVAL * 4,
					"height"	: EXP_IMG_HEIGHT,

					"children" :
					(
						{
							"name" : "UpBringing_Pet_EXPGauge_01",
							"type" : "expanded_image",

							"x" : 0,
							"y" : 0,

							"image" : PET_UI_ROOT + "exp_gauge/exp_on.sub",
						},
						{
							"name" : "UpBringing_Pet_EXPGauge_02",
							"type" : "expanded_image",

							"x" : EXP_IMG_WIDTH + EXP_GAGUE_INTERVAL,
							"y" : 0,

							"image" : PET_UI_ROOT + "exp_gauge/exp_on.sub",
						},
						{
							"name" : "UpBringing_Pet_EXPGauge_03",
							"type" : "expanded_image",

							"x" : EXP_IMG_WIDTH * 2 + EXP_GAGUE_INTERVAL * 2,
							"y" : 0,

							"image" : PET_UI_ROOT + "exp_gauge/exp_on.sub",
						},
						{
							"name" : "UpBringing_Pet_EXPGauge_04",
							"type" : "expanded_image",

							"x" : EXP_IMG_WIDTH * 3 + EXP_GAGUE_INTERVAL * 3,
							"y" : 0,

							"image" : PET_UI_ROOT + "exp_gauge/exp_on.sub",
						},
						{
							"name" : "UpBringing_Pet_EXPGauge_05",
							"type" : "expanded_image",

							"x" : EXP_IMG_WIDTH * 4 + EXP_GAGUE_INTERVAL * 4,
							"y" : 0,

							"image" : PET_UI_ROOT + "exp_gauge/item_exp_on.sub",
						},
					),
				}, #End of EXP
				
				## AGE Title
				{ 
					"name" : "AgeWindow", "type" : "window", "x" : 232, "y" : 124, "width" : SHORT_LABLE_WIDTH, "height" : SHORT_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"AgeTitle", "type":"text", "x":0, "y":0, "text": "Age", "color":GOLD_COLOR, "all_align" : "center"},
					),	
				},
				## AGE Value
				{ 
					"name" : "AgeValueWindow", "type" : "window", "x" : 232, "y" : 124+SHORT_LABLE_HEIGHT+3, "width" : SHORT_LABLE_WIDTH, "height" : SHORT_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"AgeValue", "type":"text", "x":0, "y":0, "text": "", "color":WHITE_COLOR, "all_align" : "center"},
					),	
				},
				
				## LIFE Title
				{ 
					"name" : "LifeWindow", "type" : "window", "x" : 28, "y" : 169, "width" : 168, "height" : SHORT_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"LifeTitle", "type":"text", "x":0, "y":0, "text": "Duration", "color":GOLD_COLOR, "all_align" : "center"},
					),	
				},
				
				## LIFE Value
				{ 
					"name" : "LifeValueWindow", "type" : "window", "x" : 28, "y" : 192, "width" : 190, "height" : 20, "style" : ("attach",),
					"children" :
					(
						{"name":"LifeTextValue", "type":"text", "x":0, "y":2, "text": "", "color":WHITE_COLOR, "all_align" : "center"},
					),	
				},
				
				## LIFE Time Gauge Bar
				{
					"name" : "LifeGaugeWindow", "type" : "window", "x" : 36, "y":216, "width" : 179, "height" : 12, "style" : ("attach",),
					"children" :
					(
						{
							"name" : "LifeGauge",
							"type" : "ani_image",

							"x" : 0,
							"y" : 0,

							"delay" : 6,
							

							"images" :
							(
								"D:/Ymir Work/UI/Pattern/HPGauge/01.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/02.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/03.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/04.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/05.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/06.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/07.tga",
							),
						},
					),
				},
				
				## UpBringing Pet Feed Button(Life Time Increase)
				{
					"name" : "FeedLifeTimeButton",
					"type" : "toggle_button",

					"x" : 207,
					"y" : 173,

					"default_image" : PET_UI_ROOT + "feed_button/feed_button_default.sub",
					"over_image" : PET_UI_ROOT + "feed_button/feed_button_over.sub",
					"down_image" : PET_UI_ROOT + "feed_button/feed_button_down.sub",
					
					"text" : "Feed",
					"text_color" : GOLD_COLOR,
				},
				
				## UpBringing Pet Feed Button(evolution)
				{
					"name" : "FeedEvolButton",
					"type" : "toggle_button",
					"x" : 207,
					"y" : 194,

					"default_image" : PET_UI_ROOT + "feed_button/feed_button_default.sub",
					"over_image" : PET_UI_ROOT + "feed_button/feed_button_over.sub",
					"down_image" : PET_UI_ROOT + "feed_button/feed_button_down.sub",
					
					"text" : "Evolve",
					"text_color" : GOLD_COLOR,
				},
				
				## UpBringing Pet Feed Button(EXP)
				{
					"name" : "FeedExpButton",
					"type" : "toggle_button",

					"x" : 207,
					"y" : 215,

					"default_image" : PET_UI_ROOT + "feed_button/feed_button_default.sub",
					"over_image" : PET_UI_ROOT + "feed_button/feed_button_over.sub",
					"down_image" : PET_UI_ROOT + "feed_button/feed_button_down.sub",
					
					"text" : "Item EXP",
					"text_color" : GOLD_COLOR,
				},
				
				## Pet Abilities
				{ 
					"name" : "AbilitiesWindow", "type" : "window", "x" : 43, "y" : 259, "width" : LONG_LABEL_WIDTH, "height" : LONG_LABEL_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"AbilitiesName", "type":"text", "x":0, "y":0, "text": "Bonuses", "r":1.0, "g":0.0, "b":0.0, "a":1.0, "all_align" : "center"},
					),	
				},
				
				## HP Title
				{ 
					"name" : "HpWindow", "type" : "window", "x" : 20, "y" : 282, "width" : MIDDLE_LABLE_WIDTH, "height" : MIDDLE_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"HpTitle", "type":"text", "x":0, "y":0, "text": "HP", "color":GOLD_COLOR, "all_align" : "center"},
					),	
				},
				## HP Value
				{ 
					"name" : "HpValueWindow", "type" : "window", "x" : 20 + MIDDLE_LABLE_WIDTH, "y" : 282, "width" : MIDDLE_LABLE_WIDTH, "height" : MIDDLE_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"HpValue", "type":"text", "x":0, "y":0, "text": "", "color":WHITE_COLOR, "all_align" : "center"},
					),	
				},
				
				## Defence Title
				{ 
					"name" : "DefWindow", "type" : "window", "x" : 20, "y" : 304, "width" : MIDDLE_LABLE_WIDTH, "height" : MIDDLE_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"DefTitle", "type":"text", "x":0, "y":0, "text": "Defence", "color":GOLD_COLOR, "all_align" : "center"},
					),	
				},
				## Defence Value
				{ 
					"name" : "DefValueWindow", "type" : "window", "x" : 20 + MIDDLE_LABLE_WIDTH, "y" : 304, "width" : MIDDLE_LABLE_WIDTH, "height" : MIDDLE_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"DefValue", "type":"text", "x":0, "y":0, "text": "", "color":WHITE_COLOR, "all_align" : "center"},
					),	
				},
				
				## SP Title
				{ 
					"name" : "SpWindow", "type" : "window", "x" : 20, "y" : 326, "width" : MIDDLE_LABLE_WIDTH, "height" : MIDDLE_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"SpTitle", "type":"text", "x":0, "y":0, "text": "SP", "color":GOLD_COLOR, "all_align" : "center"},
					),
				},
				## SP Value
				{ 
					"name" : "SpValueWindow", "type" : "window", "x" : 20 + MIDDLE_LABLE_WIDTH, "y" : 326, "width" : MIDDLE_LABLE_WIDTH, "height" : MIDDLE_LABLE_HEIGHT, "style" : ("attach",),
					"children" :
					(
						{"name":"SpValue", "type":"text", "x":0, "y":0, "text": "", "color":WHITE_COLOR, "all_align" : "center"},
					),
				},
				
				## Pet Skill Title
				{ 
					"name" : "PetSkillWindow", "type" : "window", "x" : 11, "y" : 371, "width" : 120, "height" : 20, "style" : ("attach",),
					"children" :
					(
						{"name":"PetSkillTitle", "type":"text", "x":0, "y":0, "text": "Skill", "r":1.0, "g":0.0, "b":0.0, "a":1.0, "all_align" : "center"},
					),
				},
				
				## Pet Skill Slot 0
				{
					"name" : "PetSkillSlot0",
					"type" : "slot",
					
					"x" : 156,
					"y" : 365,
					"width" : 160,
					"height" : 32,
					"image" : BASE_SLOT_FILE,
					
					"slot" : ({"index":0, "x":0, "y":0, "width":32, "height":32},{"index":1, "x":64, "y":0, "width":32, "height":32},{"index":2, "x":128, "y":0, "width":32, "height":32},),
				},
				
				
				
			
			), ## End of board window children			
		},
	),
}
