import uiScriptLocale
import twix_work

window = {
	"name" : "CreateCharacterWindow",
	"x" : 0, "y" : 0,
	"width" : SCREEN_WIDTH,	"height" : SCREEN_HEIGHT,
	"children" : (
		{
			"name" : "BackGround",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 0,

			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,

			"image" : "d:/ymir work/ui/intro/login/background.tga",

			"children" : (
				{
					"name" : "board_main",
					"type" : "window",

					"x" : -380,
					"y" : 150,

					"width" : 352,
					"height" : 457,

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

									"x": 65,
									"y": 23,

									"color" : twix_work.COLOR_LOGIN_TEXT,

									"text" : uiScriptLocale.CREATE_NAME,
									
									"fontname" : "Tahoma:16",
								},
								{
									"name" : "name_slotbar",
									"type" : "input",

									"x" : 145,
									"y" : 43,

									"width" : 150,
									"children" : (
										{
											"name" : "name",
											"type" : "editline",

											"x" : 12,
											"y" : -18,

											"width" : 200,
											"height" : 16,
											"color" : 0xffc8aa80,
											"input_limit": 16,
											"enable_codepage": 0,
										},
									),
								},
								{
									"name" : "char1",
									"type" : "radio_button",

									"x" : -70, 
									"y" : -85,

									"vertical_align" : "center",
									"horizontal_align" : "center",

									"default_image" : "d:/ymir work/ui/intro/create/warrior_0.tga",
									"over_image" : "d:/ymir work/ui/intro/create/warrior_1.tga",
									"down_image" : "d:/ymir work/ui/intro/create/warrior_2.tga",
								},
								{
									"name" : "char2",
									"type" : "radio_button",

									"x" : 70, 
									"y" : -85,

									"vertical_align" : "center",
									"horizontal_align" : "center",

									"default_image" : "d:/ymir work/ui/intro/create/assassin_0.tga",
									"over_image" : "d:/ymir work/ui/intro/create/assassin_1.tga",
									"down_image" : "d:/ymir work/ui/intro/create/assassin_2.tga",
								},
								{
									"name" : "char3",
									"type" : "radio_button",

									"x" : -70,
									"y" : -20,

									"vertical_align" : "center",
									"horizontal_align" : "center",

									"default_image" : "d:/ymir work/ui/intro/create/sura_0.tga",
									"over_image" : "d:/ymir work/ui/intro/create/sura_1.tga",
									"down_image" : "d:/ymir work/ui/intro/create/sura_2.tga",
								},
								{
									"name" : "char4",
									"type" : "radio_button",

									"x" : 70,
									"y" : -20,

									"vertical_align" : "center",
									"horizontal_align" : "center",

									"default_image" : "d:/ymir work/ui/intro/create/shaman_0.tga",
									"over_image" : "d:/ymir work/ui/intro/create/shaman_1.tga",
									"down_image" : "d:/ymir work/ui/intro/create/shaman_2.tga",
								},
								{
									"name" : "shape1",
									"type" : "radio_button",

									"x" : 52,
									"y" : 178,

									"default_image" : "d:/ymir work/ui/intro/create/button_normal.tga",
									"over_image" : "d:/ymir work/ui/intro/create/button_hover.tga",
									"down_image" : "d:/ymir work/ui/intro/create/button_active.tga",
									"disable_image" : "d:/ymir work/ui/intro/create/button_freese.tga",
									
									"children" : 
									(
										{
											"name" : "txt",
											"type" : "text",
										
											"x" : (114/2),
											"y" : 13,
										
											"text" : "Skin 1",
											"fontname" : "Tahoma:14",
												
											"r" : 1,
											"g" : 1,
											"b" : 1,
												
											"text_horizontal_align" : "center",
										},
									),
								},
								{
									"name" : "shape2",
									"type" : "radio_button",

									"x" : 195,
									"y" : 178,

									"default_image" : "d:/ymir work/ui/intro/create/button_normal.tga",
									"over_image" : "d:/ymir work/ui/intro/create/button_hover.tga",
									"down_image" : "d:/ymir work/ui/intro/create/button_active.tga",
									"disable_image" : "d:/ymir work/ui/intro/create/button_freese.tga",
									
									"children" : 
									(
										{
											"name" : "txt",
											"type" : "text",
										
											"x" : (114/2),
											"y" : 13,
										
											"text" : "Skin 2",
											"fontname" : "Tahoma:14",
												
											"r" : 1,
											"g" : 1,
											"b" : 1,
												
											"text_horizontal_align" : "center",
										},
									),
								},
								{
									"name" : "gender_man",
									"type" : "radio_button",

									"x" : 52,
									"y" : 220,

									"default_image" : "d:/ymir work/ui/intro/create/button_normal.tga",
									"over_image" : "d:/ymir work/ui/intro/create/button_hover.tga",
									"down_image" : "d:/ymir work/ui/intro/create/button_active.tga",
									"disable_image" : "d:/ymir work/ui/intro/create/button_freese.tga",
									
									"children" : 
									(
										{
											"name" : "txt",
											"type" : "text",
										
											"x" : (114/2),
											"y" : 13,
										
											"text" : uiScriptLocale.CREATE_MAN,
											"fontname" : "Tahoma:14",
												
											"r" : 1,
											"g" : 1,
											"b" : 1,
												
											"text_horizontal_align" : "center",
										},
									),
								},
								{
									"name" : "gender_woman",
									"type" : "radio_button",

									"x" : 195,
									"y" : 220,

									"default_image" : "d:/ymir work/ui/intro/create/button_normal.tga",
									"over_image" : "d:/ymir work/ui/intro/create/button_hover.tga",
									"down_image" : "d:/ymir work/ui/intro/create/button_active.tga",
									"disable_image" : "d:/ymir work/ui/intro/create/button_freese.tga",
									
									"children" : 
									(
										{
											"name" : "txt",
											"type" : "text",
									
											"x" : (114/2),
											"y" : 13,
									
											"text" : uiScriptLocale.CREATE_WOMAN,
											"fontname" : "Tahoma:14",
											
											"r" : 1,
											"g" : 1,
											"b" : 1,
											
											"text_horizontal_align" : "center",
										},
									),
								},
								{
									"name" : "create_button",
									"type" : "button",

									"x" : 122,
									"y" : 275,
									
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
			),
		},
	),
}
