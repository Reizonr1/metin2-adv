import uiScriptLocale
import item
import gameInfo

ROOT = "d:/ymir work/ui/game/"
YOL = str(gameInfo.CONFIG_YOL)+"itemine_ws/"

GENEL_EK_X = 110 + 55
GENEL_EK_Y = 0
EK_Y = 78
WIDTH = 512
HEIGHT = 260

MY_INFO_EK = 604
MY_INFO_EK_2 = 220
TARGET_INFO_EK_X = 25
TARGET_INFO_EK_X_2 = 110
INFO_EK_Y = 9

INFO_EK_X = 9

WIDTH_GECMIS = 373 + 75
HEIGHT_GECMIS = 206 - 30

BILGI_YOKET = 9000
BUTTON_YOKET = 9000

FACE_SLOT_FILE = "d:/ymir work/ui/game/windows/box_face.sub"

window = {
	"name" : "ItemineDuelloDepoWindow","type": "window", "x" : 0,"y" : 0,"style" : ("movable", "float",),"width" : WIDTH,"height" : HEIGHT, "children" :
	(
		## Animage
		{ "name" : "Animage", "type" : "ani_image", "x" : 66+60, "y" : 0, "delay" : 4,
		
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
		
		{"name" : "board","type" : "board","style" : ("attach",),"x" : 0,"y" : 0,"width" : WIDTH,"height" : HEIGHT,"children" :
			(
				## Title
				{"name" : "TitleBar","type" : "titlebar","style" : ("attach",),"x" : 6,"y" : 8,"width" : WIDTH - 13 - 130,"color" : "yellow","children" :
					({ "name":"TitleName", "type":"text", "x":0, "y":3, "text":"", "text_horizontal_align":"center", "horizontal_align": "center" },),
				},
				
				{"name": "My_Character_Info_Board","type":"board","x":386 - 10,"y":15+15 - 28,"width":103 + 27,"height":167+35, "children" :
					(
					
						{ "name" : "My_Character_Image", "type" : "image", "x" : 0, "y" : 5, "horizontal_align":"center","text_horizontal_align":"center","image" : YOL+"0_karakter.tga", },
						{ "name" : "My_Name", "type" : "text", "x" : 0, "y" : 103, "horizontal_align":"center","text_horizontal_align":"center","text" : "Fatihbab34 " , "fontsize" : "LARGE", },
						{ "name" : "My_Level", "type" : "text", "x" : 0, "y" : 96 + 13 + INFO_EK_Y, "horizontal_align":"center","text_horizontal_align":"center","text" : "Lv. 99 " , "fontsize" : "LARGE", },
						{ "name" : "My_Guild", "type" : "text", "x" : 0 , "y" : 96 + 13 + INFO_EK_Y + 13, "horizontal_align":"center","text_horizontal_align":"center","text" : "TURKIYE " , "fontsize" : "LARGE", },
						{ "name" : "My_MacBilgileri_1", "type" : "text", "x" : 0, "y" : 96 + 26 + INFO_EK_Y + 13, "horizontal_align":"center","text_horizontal_align":"center","text" : "Toplam Maç : ... " , "fontsize" : "LARGE", },
						{ "name" : "My_MacBilgileri_2", "type" : "text", "x" : 0, "y" : 96 + 26 + INFO_EK_Y + 13*2, "horizontal_align":"center","text_horizontal_align":"center","text" : "G/M : ..." , "fontsize" : "LARGE", },
						{ "name" : "My_MacBilgileri_3", "type" : "text", "x" : 0, "y" : 96 + 26 + INFO_EK_Y + 13*3, "horizontal_align":"center","text_horizontal_align":"center","text" : "Kaçma : ... " , "fontsize" : "LARGE", },
					
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
				{"name" : "ItemSlot_Rakip","type" : "grid_table","x" : 13 + 195 - 25,"y" : 16 + 18 + GENEL_EK_Y,"start_index" : 0,"x_count" : 6,"y_count" : 6,"x_step" : 32,"y_step" : 32,"image" : "d:/ymir work/ui/public/Slot_Base.sub"},
				
				#Para Bilgileri
				{"name":"Money_Slot_Rakip","type":"button","x":6 + 27,"y":28+24-20+40+8 - 17 - 33,"vertical_align":"bottom","default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub","over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub","down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub", "children" :
					(
						{"name":"Money_Icon_Rakip","type":"image","x":-18,"y":2,"image":"d:/ymir work/ui/game/windows/money_icon.sub",},
						{"name" : "Money_Rakip","type" : "text","x" : 3,"y" : 3,"horizontal_align" : "right","text_horizontal_align" : "right","text" : "0 Yang",},	
					),
				},
				
				## Onay Bilgileri
					
				{"name" : "hepsinial_button","type" : "button","x" : - 20 - 17 + 98 - 221 + 127 - 11 + 20,"y" : 31,"horizontal_align":"center","vertical_align":"bottom","text" : "Hepsini Al","tooltip_text" : "Düello'ya baþlamak için kabul et!","default_image" : "d:/ymir work/ui/public/Large_Button_01.sub","over_image" : "d:/ymir work/ui/public/Large_Button_02.sub","down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",},
				{"name" : "sil_button","type" : "button","x" :  - 10 + 80 - 17 + 98 - 221 - 35 + 127 - 5 + 35 + 12,"y" : 31,"horizontal_align":"center","vertical_align":"bottom","text" : "Sil","default_image" : "d:/ymir work/ui/public/Large_Button_01.sub","over_image" : "d:/ymir work/ui/public/Large_Button_02.sub","down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",},
				{"name" : "yenile_button","type" : "button","x" :  - 10 + 80 - 17 + 98 - 221 - 35 + 127 - 5 + 35 + 12 + 117,"y" : 31,"horizontal_align":"center","vertical_align":"bottom","text" : "Yenile","default_image" : "d:/ymir work/ui/public/Large_Button_01.sub","over_image" : "d:/ymir work/ui/public/Large_Button_02.sub","down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",},
				#{"name" : "HorizontalLine1","type" : "line","x" : 381 + 6,"y" : 34 + GENEL_EK_Y ,"width" : 0,"height" : 189 + 27,"color" : 0xff777777,},
				#{"name" : "HorizontalLine2","type" : "line","x" : 382 + 6,"y" : 34 + GENEL_EK_Y,"width" : 0,"height" : 189 + 27,"color" : 0xff777777,},
				
				
				## Sayfa Bilgileri
				
				{"name" : "Target_Page_Slot","type" : "slotbar","x" : 140 - 23 + 65,"y" : 31 + BUTTON_YOKET,"width":28,"height":18,"vertical_align":"bottom","horizontal_align":"center","children" :
					(
						{"name" : "Target_Page_Value","type" : "text","x" : 0,"y" : 3,"text" : "I","horizontal_align":"center"},
					),
				},

				{"name" : "Target_Page_Geri","type" : "button","x" : 376,"y" : HEIGHT - 31 + BUTTON_YOKET,"height" : 21,"text" : "<<<","default_image" : "d:/ymir work/ui/public/xsmall_button_01.sub","over_image" : "d:/ymir work/ui/public/xsmall_button_02.sub","down_image" : "d:/ymir work/ui/public/xsmall_button_03.sub",},
				{"name" : "Target_Page_Ileri","type" : "button","x" : 374 + 88,"y" : HEIGHT - 31 + BUTTON_YOKET,"text" : ">>>","default_image" : "d:/ymir work/ui/public/xsmall_button_01.sub","over_image" : "d:/ymir work/ui/public/xsmall_button_02.sub","down_image" : "d:/ymir work/ui/public/xsmall_button_03.sub",},
				
				## Round Bilgileri(Kapatildi-> move in titlebar)
				
				
				#{"name":"Round_Title","type":"text","x":-15 - 170 + 45,"y":26,"text":"Round :","horizontal_align":"center","text_horizontal_align":"center","vertical_align":"bottom"},
				#{"name" : "Round_SlotBar","type" : "slotbar","x" : 35 - 180 + 45,"y" : 22 + 8,"horizontal_align":"center","width" : 28,"height" : 18,"vertical_align":"bottom", "children" :
				#	(
				#		{"name":"Round_Icon","type":"image","x":-18+9000,"y":2,"image":"d:/ymir work/ui/game/windows/money_icon.sub",},
				#		{"name" : "Round_Text","type" : "text","x" : 0,"y" : 3,"horizontal_align" : "center","text_horizontal_align" : "center","text" : "1",},
						#{"name" : "Round_Sayisi","type" : "editline","width" : 26,"height" : 48,"text"	: "1","input_limit" : 1,"x" : 2,"y" : 2,},
				#	),
				#},
				#{"name" : "Round_Ok_Button","type" : "button","x" : 35 + 80 - 170 - 50,"y" : 22 + 8,"vertical_align":"bottom","horizontal_align":"center", "text" : "ok","default_image" : "d:/ymir work/ui/public/small_button_01.sub","over_image" : "d:/ymir work/ui/public/small_button_02.sub","down_image" : "d:/ymir work/ui/public/small_button_03.sub",},
			
			),
		},
	),
}