import uiScriptLocale
import localegame
import gameInfo

ROOT = "d:/ymir work/ui/game/"
YOL = str(gameInfo.CONFIG_YOL)+"varmisinyokmusun/"

WIDTH = 282
HEIGHT = 167+60

window = {
	"name" : "DiceSystem",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 30,

	"width" : WIDTH,
	"height" : HEIGHT,

	"children" :
	(
		{"name" : "board","type": "board", "style" : ("attach",),"x" : 0,"y" : 0,"width": WIDTH, "height": HEIGHT, "children" :
			(
				## Title
				{"name" : "TitleBar","type" : "titlebar","style" : ("attach",),"x" : 6,"y" : 8,"width" : WIDTH - 14,"color" : "yellow","children" :
					({ "name":"TitleName", "type":"text", "x":0, "y":3, "text":str(localegame.DICE_SYSTEM_TITLE), "text_horizontal_align":"center", "horizontal_align": "center" },),
				},
				
				## MiddleBar
				{"name" : "Middle_Bar","type" : "image","x" : 139,"y" : 40,"image" : ROOT + "windows/middlebar.sub",},
				## Owner
				{"name" : "Owner","type" : "window","x" : 144,"y" : 33,"width" : 130,"height" : 200,"children" :
					(
						{"name" : "Owner_Slot","type" : "grid_table","start_index" : 0,"x" : 0,"y" : 0,"x_count" : 4,"y_count" : 3,"x_step" : 32,"y_step" : 32,"x_blank" : 0,"y_blank" : 0,"image" : "d:/ymir work/ui/public/slot_base.sub",},		
						
						{"name": "Owner_Number_ThinBoard", "type": "thinboard", "x":0, "y":100, "width": 129, "height": 60, "children": 
							(
								{"name":"Owner_Number_Text", "type": "text", "text":"", "x": 0, "y":0, "text_horizontal_align":"center","text_vertical_align":"center", "vertical_align":"center","horizontal_align":"center"},
								
							),
						},
						
						{"name" : "Owner_Accept_Light","type" : "button","x" : 62,"y" : 101+63,"default_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub","over_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub","down_image" : "d:/ymir work/ui/game/windows/accept_button_on.sub",},				
						{"name" : "Owner_Accept_Button","type" : "toggle_button","x" : 85,"y" : 101+63,"text" : uiScriptLocale.EXCHANGE_ACCEPT,"default_image" : "d:/ymir work/ui/public/small_button_01.sub","over_image" : "d:/ymir work/ui/public/small_button_02.sub","down_image" : "d:/ymir work/ui/public/small_button_03.sub",},
						
					),
				},	
				
				{"name" : "Target","type" : "window","x" : 10,"y" : 33,"width" : 130,"height" : 200,"children" :
					(
						{"name" : "Target_Slot","type" : "grid_table","start_index" : 0,"x" : 0,"y" : 0,"x_count" : 4,"y_count" : 3,"x_step" : 32,"y_step" : 32,"x_blank" : 0,"y_blank" : 0,"image" : "d:/ymir work/ui/public/slot_base.sub",},		
						
						{"name": "Target_Number_ThinBoard", "type": "thinboard", "x":0, "y":100, "width": 129, "height": 60, "children": 
							(
								{"name":"Target_Number_Text", "type": "text", "text":"", "x": 0, "y":0, "text_horizontal_align":"center","text_vertical_align":"center", "vertical_align":"center","horizontal_align":"center"},
								
							),
						},
						
						{"name" : "Target_Accept_Button","type" : "toggle_button","x" : 1,"y" : 101+63,"text" : uiScriptLocale.EXCHANGE_ACCEPT,"default_image" : "d:/ymir work/ui/public/small_button_01.sub","over_image" : "d:/ymir work/ui/public/small_button_02.sub","down_image" : "d:/ymir work/ui/public/small_button_03.sub",},
						{"name" : "Target_Accept_Light","type" : "button","x" : 46,"y" : 101+63,"default_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub","over_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub","down_image" : "d:/ymir work/ui/game/windows/accept_button_on.sub",},				
						
					),
				},	
	
				
			),
		},
	),
}
