import uiScriptLocale

BACK_IMG_PATH = "d:/ymir work/ui/pattern/"
ROOT_PATH = "d:/ymir work/patrontakip/"

window = {
	"name" : "BossTrackingSystemWindow",
	"x" : (SCREEN_WIDTH -518) / 2,
	"y" : (SCREEN_HEIGHT - 380) / 2,
	"style" : ("movable","float",),
	"width" : 518,
	"height" : 380,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 518,
			"height" : 380,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 503,
					"color" : "yellow",
					
					"children" :
					(
						{ "name":"title_name_old", "type":"text", "x":0, "y":-1, "text": uiScriptLocale.BOSSTRACKINGTITLE, "all_align":"center" },
					),
				},

				## menu_list bg
				{
					"name" : "menu_list",
					"type" : "window",

					"x" : 14,
					"y" : 36,

					"width" : 169,
					"height" : 326,

					"children" :
					(
						## LeftTop
						{
							"name" : "left_top",
							"type" : "image",
							"x" : 0,
							"y" : 0,
							"image" : BACK_IMG_PATH+"border_A_left_top.tga",
						},
						## RightTop
						{
							"name" : "right_top",
							"type" : "image",
							"x" : 169-16,
							"y" : 0,
							"image" : BACK_IMG_PATH+"border_A_right_top.tga",
						},
						## LeftBottom
						{
							"name" : "left_bottom",
							"type" : "image",
							"x" : 0,
							"y" : 326-16,
							"image" : BACK_IMG_PATH+"border_A_left_bottom.tga",
						},
						## RightBottom
						{
							"name" : "right_bottom",
							"type" : "image",
							"x" : 169-16,
							"y" : 326-16,
							"image" : BACK_IMG_PATH+"border_A_right_bottom.tga",
						},
						## leftcenterImg
						{
							"name" : "left_center_img",
							"type" : "expanded_image",
							"x" : 0,
							"y" : 15,
							"image" : BACK_IMG_PATH+"border_A_left.tga",
							"rect" : (0.0, 0.0, 0, 18),
						},
						## rightcenterImg
						{
							"name" : "right_center_img",
							"type" : "expanded_image",
							"x" : 169-16,
							"y" : 15,
							"image" : BACK_IMG_PATH+"border_A_right.tga",
							"rect" : (0.0, 0.0, 0, 18),
						},
						## topcenterImg
						{
							"name" : "top_center_img",
							"type" : "expanded_image",
							"x" : 15,
							"y" :  0,
							"image" : BACK_IMG_PATH+"border_A_top.tga",
							"rect" : (0.0, 0.0, 8, 0),
						},
						## bottomcenterImg
						{
							"name" : "bottom_center_img",
							"type" : "expanded_image",
							"x" : 15,
							"y" : 326-16,
							"image" : BACK_IMG_PATH+"border_A_bottom.tga",
							"rect" : (0.0, 0.0, 8, 0),
						},
						## centerImg
						{
							"name" : "center_img",
							"type" : "expanded_image",
							"x" : 15,
							"y" : 15,
							"image" : BACK_IMG_PATH+"border_A_center.tga",
							"rect" : (0.0, 0.0, 8, 18),
						},
						{ "name" : "btnMenuCadi", "type" : "button", "x" : 5, "y" : 15, "text"	:	"","default_image" : ROOT_PATH + "button_1.tga", "over_image" : ROOT_PATH + "button_2.tga", "down_image" : ROOT_PATH + "button_2.tga", },
						{ "name" : "btnMenuAlevKral", "type" : "button", "x" : 5, "y" : 45, "text"	:	"","default_image" : ROOT_PATH + "button_1.tga", "over_image" : ROOT_PATH + "button_2.tga", "down_image" : ROOT_PATH + "button_2.tga", },
						{ "name" : "btnMenuKOrumcek", "type" : "button", "x" : 5, "y" : 75, "text"	:	"","default_image" : ROOT_PATH + "button_1.tga", "over_image" : ROOT_PATH + "button_2.tga", "down_image" : ROOT_PATH + "button_2.tga", },
						{ "name" : "btnMenuKEjder", "type" : "button", "x" : 5, "y" : 105, "text"	:	"","default_image" : ROOT_PATH + "button_1.tga", "over_image" : ROOT_PATH + "button_2.tga", "down_image" : ROOT_PATH + "button_2.tga", },
						{ "name" : "btnMenuDokuzKuyruk", "type" : "button", "x" : 5, "y" : 135, "text"	:	"","default_image" : ROOT_PATH + "button_1.tga", "over_image" : ROOT_PATH + "button_2.tga", "down_image" : ROOT_PATH + "button_2.tga", },
						{ "name" : "btnMenuGeneral", "type" : "button", "x" : 5, "y" : 165, "text"	:	"","default_image" : ROOT_PATH + "button_1.tga", "over_image" : ROOT_PATH + "button_2.tga", "down_image" : ROOT_PATH + "button_2.tga", },
						{ "name" : "btnMenuOrumcekBarones", "type" : "button", "x" : 5, "y" : 195, "text"	:	"","default_image" : ROOT_PATH + "button_1.tga", "over_image" : ROOT_PATH + "button_2.tga", "down_image" : ROOT_PATH + "button_2.tga", },
						{ "name" : "btnMenuHayaletAgac", "type" : "button", "x" : 5, "y" : 225, "text"	:	"","default_image" : ROOT_PATH + "button_1.tga", "over_image" : ROOT_PATH + "button_2.tga", "down_image" : ROOT_PATH + "button_2.tga", },
						{ "name" : "btnMenuKomutan", "type" : "button", "x" : 5, "y" : 255, "text"	:	"","default_image" : ROOT_PATH + "button_1.tga", "over_image" : ROOT_PATH + "button_2.tga", "down_image" : ROOT_PATH + "button_2.tga", },
						{ "name" : "btnMenuKaranlikLider", "type" : "button", "x" : 5, "y" : 285, "text"	:	"","default_image" : ROOT_PATH + "button_1.tga", "over_image" : ROOT_PATH + "button_2.tga", "down_image" : ROOT_PATH + "button_2.tga", },
						
						{ "name" : "1", "type" : "text", "x" : 40, "y" : 20, "text"	:	"Güçlü Buz Cadýsý",},
						{ "name" : "2", "type" : "text", "x" : 40, "y" : 50, "text"	:	"Alev Kral",},
						{ "name" : "3", "type" : "text", "x" : 40, "y" : 80, "text"	:	"Kraliçe Örümcek",},
						{ "name" : "4", "type" : "text", "x" : 40, "y" : 110, "text"	:	"Sarý Kaplan Hayaleti",},
						{ "name" : "5", "type" : "text", "x" : 40, "y" : 140, "text"	:	"Ork Reisi",},
						{ "name" : "6", "type" : "text", "x" : 40, "y" : 170, "text"	:	"Dokuz Kuyruk",},
						{ "name" : "7", "type" : "text", "x" : 40, "y" : 200, "text"	:	"Dev Çöl Kaplumbaðasý",},
						{ "name" : "8", "type" : "text", "x" : 40, "y" : 230, "text"	:	"Dev Hayalet Aðaç",},
						{ "name" : "9", "type" : "text", "x" : 40, "y" : 260, "text"	:	"Komutan",},
						{ "name" : "10", "type" : "text", "x" : 40, "y" : 290, "text"	:	"Karanlýk Hayalet Lider",},
						
						{
							"name" : "one_image",
							"type" : "image",
							"x" : 10,
							"y" : 15,
							"image" : ROOT_PATH+"1.png",
						},
						{
							"name" : "two_image",
							"type" : "image",
							"x" : 10,
							"y" : 10+35,
							"image" : ROOT_PATH+"2.png",
						},
						{
							"name" : "two_image",
							"type" : "image",
							"x" : 10,
							"y" : 10+35+30,
							"image" : ROOT_PATH+"3.png",
						},
						{
							"name" : "two_image",
							"type" : "image",
							"x" : 10,
							"y" : 10+35+30+30,
							"image" : ROOT_PATH+"4.png",
						},
						{
							"name" : "two_image",
							"type" : "image",
							"x" : 10,
							"y" : 10+35+30+30+30,
							"image" : ROOT_PATH+"5.png",
						},
						{
							"name" : "two_image",
							"type" : "image",
							"x" : 10,
							"y" : 10+35+30+30+30+30,
							"image" : ROOT_PATH+"6.png",
						},
						{
							"name" : "two_image",
							"type" : "image",
							"x" : 10,
							"y" : 10+35+30+30+30+30+30,
							"image" : ROOT_PATH+"7.png",
						},
						{
							"name" : "two_image",
							"type" : "image",
							"x" : 10,
							"y" : 10+35+30+30+30+30+30+30,
							"image" : ROOT_PATH+"8.png",
						},
						{
							"name" : "two_image",
							"type" : "image",
							"x" : 10,
							"y" : 10+35+30+30+30+30+30+30+30,
							"image" : ROOT_PATH+"9.png",
						},
						{
							"name" : "two_image",
							"type" : "image",
							"x" : 10,
							"y" : 10+35+30+30+30+30+30+30+30+30,
							"image" : ROOT_PATH+"10.png",
						},


					),
				},

				{
					"name" : "bosstime_window",
					"type" : "window",

					"x" : 191,
					"y" : 36,

					"width" : 312,
					"height" : 296,
					
					"children" :
					(
						## LeftTop
						{
							"name" : "left_top",
							"type" : "image",
							"x" : 0,
							"y" : 0,
							"image" : ROOT_PATH+"right_img.png",
						},
						
						{
							"name" : "CH1Time_slotbar",
							"type" : "slotbar",
							"x" : 80-63,
							"y" : 190-49,
							"width" : 0,
							"height" : 0,
							"children" :
							(
								{
									"name" : "CH1Time",
									"type" : "text",
									"x" : 8,
									"y" : 3,
									"text" : "CH1: 0 Saat 0 Dakika 0 Saniye",
								},
							),
						},
						{
							"name" : "CH2Time_slotbar",
							"type" : "slotbar",
							"x" : 80+87,
							"y" : 190-49,
							"width" : 0,
							"height" : 0,
							"children" :
							(
								{
									"name" : "CH2Time",
									"type" : "text",
									"x" : 8,
									"y" : 3,
									"text" : "CH2: 0 Saat 0 Dakika 0 Saniye",
								},
							),
						},
						{
							"name" : "CH3Time_slotbar",
							"type" : "slotbar",
							"x" : 80-63,
							"y" : 190-27,
							"width" : 0,
							"height" : 0,
							"children" :
							(
								{
									"name" : "CH3Time",
									"type" : "text",
									"x" : 8,
									"y" : 3,
									"text" : "CH3: 0 Saat 0 Dakika 0 Saniye",
								},
							),
						},
						{
							"name" : "CH4Time_slotbar",
							"type" : "slotbar",
							"x" : 80+87,
							"y" : 190-27,
							"width" : 0,
							"height" : 0,
							"children" :
							(
								{
									"name" : "CH4Time",
									"type" : "text",
									"x" : 8,
									"y" : 3,
									"text" : "CH4: 0 Saat 0 Dakika 0 Saniye",
								},
							),
						},
						
						{
							"name" : "CH5Time_slotbar",
							"type" : "slotbar",
							"x" : 80-63,
							"y" : 190-5,
							"width" : 0,
							"height" : 0,
							"children" :
							(
								{
									"name" : "CH5Time",
									"type" : "text",
									"x" : 8,
									"y" : 3,
									"text" : "CH5: 0 Saat 0 Dakika 0 Saniye",
								},
							),
						},
						{
							"name" : "CH6Time_slotbar",
							"type" : "slotbar",
							"x" : 80+87,
							"y" : 190-5,
							"width" : 0,
							"height" : 0,
							"children" :
							(
								{
									"name" : "CH6Time",
									"type" : "text",
									"x" : 8,
									"y" : 3,
									"text" : "CH6: 0 Saat 0 Dakika 0 Saniye",
								},
							),
						},
						
					),	
				},

				{
					"name" : "list",
					"type" : "window",

					"x" : 194,
					"y" : 65,

					"width" : 300,
					"height" : 21,

					"children" :
					(
						{
							"name" : "sub_titlebar",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"image" : "d:/ymir work/ui/public/battle/column_titlebar.sub",
						},
						{ "name" : "title_name", "type" : "text", "x" : 12, "y" : 2, "text" : "Güçlü Buz Cadýsý", "color":0xFFFEE3AE, },
						{ "name" : "title_name_2", "type" : "text", "x" : 12, "y" : 22, "text" : "Seviye", },
						{ "name" : "title_name_3", "type" : "text", "x" : 12, "y" : 42, "text" : "Map Ismi", },
						{ "name" : "title_name_4", "type" : "text", "x" : 12, "y" : 62, "text" : "Tilsim text", },
						{ "name" : "title_name_5", "type" : "text", "x" : 12, "y" : 84, "text" : "Kaç dkda cikar", },
						{ "name" : "title_name_6", "type" : "text", "x" : 12, "y" : 84+116, "text" : "Eþya Drobu", },
					),
				},
			),
		},
	),
}