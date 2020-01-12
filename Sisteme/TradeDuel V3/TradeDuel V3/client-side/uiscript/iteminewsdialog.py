import uiScriptLocale
import item
import gameInfo

ROOT = "d:/ymir work/ui/game/"
YOL = str(gameInfo.CONFIG_YOL)+"itemine_ws/"

GENEL_EK_X = 110 + 55
GENEL_EK_Y = 0
EK_Y = 78
WIDTH = 768
HEIGHT = 260

MY_INFO_EK = 604
MY_INFO_EK_2 = 220
TARGET_INFO_EK_X = 25
TARGET_INFO_EK_X_2 = 110
INFO_EK_Y = 9

WIDTH_GECMIS = 373 + 75
HEIGHT_GECMIS = 206 - 30

BILGI_YOKET = 9000

FACE_SLOT_FILE = "d:/ymir work/ui/game/windows/box_face.sub"

window = {
	"name" : "ItemineDuelloWindow","type": "window", "x" : 0,"y" : 0,"style" : ("movable", "float",),"width" : WIDTH,"height" : HEIGHT + HEIGHT_GECMIS, "children" :
	(
		## Animage
		{ "name" : "Animage", "type" : "ani_image", "x" : 15 + 220, "y" : 5, "delay" : 4,
		
			"images" : ( 
				YOL+"1.tga", 
				YOL+"2.tga", 
				YOL+"3.tga", 
				YOL+"4.tga", 
				YOL+"5.tga", 
				YOL+"6.tga", 
				YOL+"7.tga", 
				YOL+"8.tga", 
				YOL+"9.tga", 
				YOL+"10.tga", 
				YOL+"11.tga", 
				YOL+"12.tga", 
				YOL+"13.tga", 
				YOL+"14.tga", 
				YOL+"15.tga", 
				YOL+"16.tga", 
			),
		
		},
		
		{"name": "Target_Character_Info_Board","type":"board","x":-97,"y":15+20,"width":103,"height":167+35, "children" :
			(
			
				{ "name" : "Target_Character_Image", "type" : "image", "x" : 9, "y" : 5, "image" : YOL+"0_karakter.tga", },
				{ "name" : "Target_Name", "type" : "text", "x" : 8, "y" : 103, "text" : "Fatihbab34 " , "fontsize" : "LARGE", },
				{ "name" : "Target_Level", "type" : "text", "x" : 8, "y" : 96 + 13 + INFO_EK_Y, "text" : "Lv. 99 " , "fontsize" : "LARGE", },
				{ "name" : "Target_Guild", "type" : "text", "x" : 8 , "y" : 96 + 13 + INFO_EK_Y + 13, "text" : "TURKIYE " , "fontsize" : "LARGE", },
				{ "name" : "Target_MacBilgileri_1", "type" : "text", "x" : 7, "y" : 96 + 26 + INFO_EK_Y + 13, "text" : "Toplam Maç : ... " , "fontsize" : "LARGE", },
				{ "name" : "Target_MacBilgileri_2", "type" : "text", "x" : 8, "y" : 96 + 26 + INFO_EK_Y + 13*2, "text" : "G/M : ..." , "fontsize" : "LARGE", },
				{ "name" : "Target_MacBilgileri_3", "type" : "text", "x" : 8, "y" : 96 + 26 + INFO_EK_Y + 13*3, "text" : "Kaçma : ... " , "fontsize" : "LARGE", },
			
			),
		
		},
		
		{"name": "My_Character_Info_Board","type":"board","x":WIDTH-3,"y":15+20,"width":103,"height":167+35, "children" :
			(
			
				{ "name" : "My_Character_Image", "type" : "image", "x" : 9, "y" : 5, "image" : YOL+"0_karakter.tga", },
				{ "name" : "My_Name", "type" : "text", "x" : 8, "y" : 103, "text" : "Fatihbab34 " , "fontsize" : "LARGE", },
				{ "name" : "My_Level", "type" : "text", "x" : 8, "y" : 96 + 13 + INFO_EK_Y, "text" : "Lv. 99 " , "fontsize" : "LARGE", },
				{ "name" : "My_Guild", "type" : "text", "x" : 8 , "y" : 96 + 13 + INFO_EK_Y + 13, "text" : "TURKIYE " , "fontsize" : "LARGE", },
				{ "name" : "My_MacBilgileri_1", "type" : "text", "x" : 7, "y" : 96 + 26 + INFO_EK_Y + 13, "text" : "Toplam Maç : ... " , "fontsize" : "LARGE", },
				{ "name" : "My_MacBilgileri_2", "type" : "text", "x" : 8, "y" : 96 + 26 + INFO_EK_Y + 13*2, "text" : "G/M : ..." , "fontsize" : "LARGE", },
				{ "name" : "My_MacBilgileri_3", "type" : "text", "x" : 8, "y" : 96 + 26 + INFO_EK_Y + 13*3, "text" : "Kaçma : ... " , "fontsize" : "LARGE", },
			
			),
		
		},
		
		{"name" : "board","type" : "board","style" : ("attach",),"x" : 0,"y" : 0,"width" : WIDTH,"height" : HEIGHT,"children" :
			(
				## Title
				{"name" : "TitleBar","type" : "titlebar","style" : ("attach",),"x" : 6,"y" : 8,"width" : WIDTH - 13,"color" : "yellow","children" :
					({ "name":"TitleName", "type":"text", "x":0, "y":3, "text":"Ýtemine Duello Paneli", "text_horizontal_align":"center", "horizontal_align": "center" },),
				},

				## Equipment Slot
				{"name" : "My_EquipImage","type" : "image","x" : 13 + 760 - 195 + 20,"y" : 35 + GENEL_EK_Y,"image" : "d:/ymir work/ui/game/windows/equipment_base.sub",},	
				{"name" : "My_EquipSlot","type" : "slot","x" : 16 + 760 - 195 + 20,"y" : 35 + GENEL_EK_Y,"width" : 130,"height" : 150,
					"slot" : (
								{"index":1, "x":39, "y":37, "width":32, "height":64},
								{"index":2, "x":39, "y":2, "width":32, "height":32},
								{"index":3, "x":39, "y":145-5, "width":32, "height":32},
								{"index":4, "x":75, "y":67, "width":32, "height":32},
								{"index":5, "x":3, "y":3, "width":32, "height":96},
								{"index":6, "x":116, "y":84, "width":32, "height":32},
								{"index":7, "x":116, "y":52, "width":32, "height":32},
								{"index":8, "x":75, "y":35, "width":32, "height":32},
							),
				},
				
				{"name" : "Target_EquipImage","type" : "image","x" : 13,"y" : 35 + GENEL_EK_Y,"image" : "d:/ymir work/ui/game/windows/equipment_base.sub",},	
				{"name" : "Target_EquipSlot","type" : "slot","x" : 16,"y" : 35 + GENEL_EK_Y,"width" : 130,"height" : 150,
					"slot" : (
								{"index":1, "x":39, "y":37, "width":32, "height":64},
								{"index":2, "x":39, "y":2, "width":32, "height":32},
								{"index":3, "x":39, "y":145-5, "width":32, "height":32},
								{"index":4, "x":75, "y":67, "width":32, "height":32},
								{"index":5, "x":3, "y":3, "width":32, "height":96},
								{"index":6, "x":116, "y":84, "width":32, "height":32},
								{"index":7, "x":116, "y":52, "width":32, "height":32},
								{"index":8, "x":75, "y":35, "width":32, "height":32},
							),
				},
				
				#45 Slot Items
				{"name" : "ItemSlot","type" : "grid_table","x" : 13 + 195 + 192 + 15 - 25,"y" : 16 + 18 + GENEL_EK_Y,"start_index" : 0,"x_count" : 6,"y_count" : 6,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "ItemSlot_Rakip","type" : "grid_table","x" : 13 + 195 - 25,"y" : 16 + 18 + GENEL_EK_Y,"start_index" : 0,"x_count" : 6,"y_count" : 6,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				{"name" : "HorizontalLine1","type" : "line","x" : 381,"y" : 34 + GENEL_EK_Y,"width" : 0,"height" : 189,"color" : 0xff777777,},
				{"name" : "HorizontalLine2","type" : "line","x" : 382,"y" : 34 + GENEL_EK_Y,"width" : 0,"height" : 189,"color" : 0xff777777,},
				
				
				#Para Bilgileri
				{"name":"Money_Slot_Rakip","type":"button","x":-30-60 - 195,"y":28+24-20+40+8 - 17 - 33,"horizontal_align":"center","vertical_align":"bottom","default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub","over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub","down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub", "children" :
					(
						{"name":"Money_Icon_Rakip","type":"image","x":-18,"y":2,"image":"d:/ymir work/ui/game/windows/money_icon.sub",},
						{"name" : "Money_Rakip","type" : "text","x" : 3,"y" : 3,"horizontal_align" : "right","text_horizontal_align" : "right","text" : "0 Yang",},	
					),
				},
				
				{"name":"Money_Slot","type":"button","x":8+90 + 200,"y":28+24-20+40+8 - 17 - 33,"horizontal_align":"center","vertical_align":"bottom","default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub","over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub","down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub","children" :
					(
						{"name":"Money_Icon","type":"image","x":-18,"y":2,"image":"d:/ymir work/ui/game/windows/money_icon.sub",},
						{"name" : "Money","type" : "text","x" : 3,"y" : 3,"horizontal_align" : "right","text_horizontal_align" : "right","text" : "0 Yang",},
					),
				},
				
				## Onay Bilgileri
				{"name" : "kabuletti_benim","type" : "ani_image","x" : 388,"y" : 30,"images" : (YOL+"kabul.tga",),},
				{"name" : "kabuletti_rakip","type" : "ani_image","x" : 181,"y" : 29,"images" : (YOL+"kabul.tga",),},	
				{"name" : "kabulet_button","type" : "button","x" : - 20 - 17 + 98,"y" : 31,"horizontal_align":"center","vertical_align":"bottom","text" : "Hazýr","tooltip_text" : "Düello'ya baþlamak için kabul et!","default_image" : "d:/ymir work/ui/public/Large_Button_01.sub","over_image" : "d:/ymir work/ui/public/Large_Button_02.sub","down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",},
				{"name" : "iptal_button","type" : "button","x" :  - 10 + 80 - 17 + 98,"y" : 31,"horizontal_align":"center","vertical_align":"bottom","text" : "iptal","default_image" : "d:/ymir work/ui/public/Large_Button_01.sub","over_image" : "d:/ymir work/ui/public/Large_Button_02.sub","down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",},
				#- 20 - 17, - 10 + 80 - 17	
				## Round Bilgileri
				{"name":"Round_Title","type":"text","x":-15 - 170,"y":26,"text":"Round :","horizontal_align":"center","text_horizontal_align":"center","vertical_align":"bottom"},
				{"name" : "Round_SlotBar","type" : "slotbar","x" : 35 - 180,"y" : 22 + 8,"horizontal_align":"center","width" : 28,"height" : 18,"vertical_align":"bottom", "children" :
					(
						{"name":"Round_Icon","type":"image","x":-18+9000,"y":2,"image":"d:/ymir work/ui/game/windows/money_icon.sub",},
						{"name" : "Round_Text","type" : "text","x" : 0,"y" : 3,"horizontal_align" : "center","text_horizontal_align" : "center","text" : "1",},
						{"name" : "Round_Sayisi","type" : "editline","width" : 26,"height" : 48,"text"	: "1","input_limit" : 1,"x" : 2,"y" : 2,},
					),
				},
				{"name" : "Round_Ok_Button","type" : "button","x" : 35 + 80 - 170 - 50,"y" : 22 + 8,"vertical_align":"bottom","horizontal_align":"center", "text" : "ok","default_image" : "d:/ymir work/ui/public/small_button_01.sub","over_image" : "d:/ymir work/ui/public/small_button_02.sub","down_image" : "d:/ymir work/ui/public/small_button_03.sub",},
			
			),
		},
		
		{
			"name" : "Duello_Gecmis",
			"type" : "thinboard",
			"style" : ("attach",),

			"x" : 0,
			"y" : HEIGHT_GECMIS,

			"width" : WIDTH_GECMIS,
			"height" : HEIGHT_GECMIS,
			
			"vertical_align" : "bottom",
			"horizontal_align" : "center",

			"children" : 
			(
				{
					"name" : "Duello_Gecmis_Scroll",
					"type" : "listbox_scroll",

					"x" : 0,
					"y" : 5,

					"width" : WIDTH_GECMIS,
					"height" : HEIGHT_GECMIS,
				},
			),
		},
		
	),
}