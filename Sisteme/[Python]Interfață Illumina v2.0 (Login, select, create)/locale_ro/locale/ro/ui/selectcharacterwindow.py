import uiScriptLocale
import twix_work

window = {
	"name" : "selectcharacterwindow",
	"x" : 0, "y" : 0,
	"width" : SCREEN_WIDTH,	"height" : SCREEN_HEIGHT,
	"children" : (
		{
			"name" : "BackGround",
			"type" : "expanded_image",
			"x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image" : "d:/ymir work/ui/intro/select/select.tga",
			"children" : (
				{
					"name" : "board_main",
					"type" : "window",
					"x" : -400, "y" : 150,
					"width" : 352, "height" : 457,
					"vertical_align" : "center",
					"horizontal_align" : "center",
					"children" :(
						{
							"name" : "board",
							"type" : "thinboardtwix",

							"x" : (SCREEN_WIDTH - 1250) / 2,
							"y" : (SCREEN_HEIGHT - 1250) / 2 + (50 * (float(SCREEN_HEIGHT) / 768.0)),

							"width" : 360,
							"height" : 330,

							"children" : (
								{
									"name": "dialog_name_slotbar",
									"type": "text",

									"x": 30,
									"y": 40,

									"color" : twix_work.COLOR_LOGIN_TEXT,

									"text" : uiScriptLocale.SELECT_NAME,
									
									"fontname" : "Tahoma:16",
								},
								{
									"name" : "name_slotbar",
									"type" : "input",

									"x" : 145,
									"y" : 60,

									"width" : 150,

									"children" : (
										{
											"name" : "name",
											"type" : "text",
											"x" : 0,
											"y" : -13,
											"all_align" : True,
										},
									),
								},
								{
									"name": "dialog_level_slotbar",
									"type": "text",

									"x": 30,
									"y": 80,

									"color" : twix_work.COLOR_LOGIN_TEXT,

									"text" : uiScriptLocale.SELECT_LEVEL,
									
									"fontname" : "Tahoma:16",
								},
								{
									"name" : "level_slotbar",
									"type" : "input",

									"x" : 145,
									"y" : 100,

									"width" : 150,
									"children" : (
										{
											"name" : "level",
											"type" : "text",
											"x" : 0,
											"y" : -13,
											"all_align" : True,
										},
									),
								},
								{
									"name": "dialog_guild_slotbar",
									"type": "text",

									"x": 30,
									"y": 120,

									"color" : twix_work.COLOR_LOGIN_TEXT,

									"text" : uiScriptLocale.GUILD_INFO_NAME,
									
									"fontname" : "Tahoma:16",
								},
								{
									"name" : "guild_slotbar",
									"type" : "input",

									"x" : 145,
									"y" : 140,

									"width" : 150,
									"children" : (
										{
											"name" : "guild",
											"type" : "text",
											"x" : 0,
											"y" : -13,
											"all_align" : True,
										},
									),
								},
								{
									"name": "dialog_empire_slotbar",
									"type": "text",

									"x": 30,
									"y": 160,

									"color" : twix_work.COLOR_LOGIN_TEXT,

									"text" : uiScriptLocale.SELECT_EMPIRE_NAME,
									
									"fontname" : "Tahoma:16",
								},
								{
									"name" : "empire_slotbar",
									"type" : "input",

									"x" : 145,
									"y" : 180,

									"width" : 150,
									"children" : (
										{
											"name" : "empire",
											"type" : "text",
											"x" : 0,
											"y" : -13,
											"all_align" : True,
										},
									),
								},
								{
									"name": "dialog_playtime_slotbar",
									"type": "text",

									"x": 30,
									"y": 200,

									"color" : twix_work.COLOR_LOGIN_TEXT,

									"text" : uiScriptLocale.SELECT_PLAYTIME,
									
									"fontname" : "Tahoma:16",
								},
								{
									"name" : "playtime_slotbar",
									"type" : "input",

									"x" : 145,
									"y" : 220,

									"width" : 150,
									"children" : (
										{
											"name" : "playtime",
											"type" : "text",
											"x" : 0,
											"y" : -13,
											"all_align" : True,
										},
									),
								},
								{
									"name" : "delete_button",
									"type" : "button",
									"x" : 190,
									"y" : 269,
									
									"text" : uiScriptLocale.SELECT_DELETE,
									"text_height" : 6,
							
									"text_color" : twix_work.COLOR_HOVER,

									"default_image": "d:/ymir work/ui/intro/select/buttons/btn_option_on.tga",
									"over_image": "d:/ymir work/ui/intro/select/buttons/btn_option_ds.tga",
									"down_image": "d:/ymir work/ui/intro/select/buttons/btn_option_dn.tga",
								},
								{
									"name" : "select_button",
									"type" : "button",

									"x" : 50, 
									"y" : 269,

									"text" : uiScriptLocale.SELECT_SELECT,
									"text_height" : 6,
									
									"text_color" : twix_work.COLOR_HOVER,

									"default_image": "d:/ymir work/ui/intro/select/buttons/btn_option_on.tga",
									"over_image": "d:/ymir work/ui/intro/select/buttons/btn_option_ds.tga",
									"down_image": "d:/ymir work/ui/intro/select/buttons/btn_option_dn.tga",
								},
								{
									"name" : "create_button",
									"type" : "button",

									"x" : 50,
									"y" : 269,
									
									"text" : uiScriptLocale.SELECT_CREATE,
									"text_height" : 6,
									
									"text_color" : twix_work.COLOR_HOVER,

									"default_image": "d:/ymir work/ui/intro/select/buttons/btn_option_on.tga",
									"over_image": "d:/ymir work/ui/intro/select/buttons/btn_option_ds.tga",
									"down_image": "d:/ymir work/ui/intro/select/buttons/btn_option_dn.tga",
								},
							),
						},
					),
				},
				{
					"name" : "left_button",
					"type" : "button",

					"x" : -90,
					"y" : 10,

					"vertical_align" : "center",
					"horizontal_align" : "center",
					"default_image" : "d:/ymir work/ui/intro/select/buttons/titlebar_collapse_01_normal.tga",
					"over_image" : "d:/ymir work/ui/intro/select/buttons/titlebar_collapse_02_hover.tga",
					"down_image" : "d:/ymir work/ui/intro/select/buttons/titlebar_collapse_03_active.tga",
				},
				{
					"name" : "right_button",
					"type" : "button",

					"x" : 90,
					"y" : 10,

					"vertical_align" : "center",
					"horizontal_align" : "center",
					"default_image" : "d:/ymir work/ui/intro/select/buttons/titlebar_expand_01_normal.tga",
					"over_image" : "d:/ymir work/ui/intro/select/buttons/titlebar_expand_02_hover.tga",
					"down_image" : "d:/ymir work/ui/intro/select/buttons/titlebar_expand_03_active.tga",
				},
			),
		},
	),
}
