import uiScriptLocale
import twix_work

SERVER_BOARD_HEIGHT = 220 + 180
SERVER_LIST_HEIGHT = 171 + 180

window = {
	"name" : "LoginWindow",
	"sytle" : ("movable",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "bg",
			"type" : "expanded_image",
			"x" : 0,
			"y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image": "d:/ymir work/ui/intro/login/background.tga",
		},

		{
			"name" : "accountLog",
			"type" : "expanded_image",
			"x" : (SCREEN_WIDTH + 262) / 2,
			"y" : (SCREEN_HEIGHT - 300) / 2 + (50 * (float(SCREEN_HEIGHT) / 768.0)),

			"image": "d:/ymir work/ui/intro/login/option_board_3.tga",
			"children" :
			(
				{
					"name": "account_1",
					"type": "text",

					"x": 50,
					"y": 20,

					"color": 0xffb7a06c,
					"text": twix_work.SAVE_EMPTY,
				},
				{
					"name": "account_2",
					"type": "text",

					"x": 50,
					"y": 20+38,

					"color": 0xffb7a06c,
					"text": twix_work.SAVE_EMPTY,
				},
				{
					"name": "account_3",
					"type": "text",

					"x": 50,
					"y": 20+38*2,

					"color": 0xffb7a06c,
					"text": twix_work.SAVE_EMPTY,
				},
				{
					"name": "account_4",
					"type": "text",

					"x": 50,
					"y": 20+38*3,

					"color": 0xffb7a06c,
					"text": twix_work.SAVE_EMPTY,
				},
			),
		},

		{
			"name" : "buttonMinimize",
			"type" : "button",

			"x" : (SCREEN_WIDTH + 610) / 2,
			"y" : (SCREEN_HEIGHT - 204) / 2 + (50 * (float(SCREEN_HEIGHT) / 768.0)),

			"default_image": "d:/ymir work/ui/intro/login/button/btn_belt_close_01_normal.tga",
			"over_image": "d:/ymir work/ui/intro/login/button/btn_belt_close_02_hover.tga",
			"down_image": "d:/ymir work/ui/intro/login/button/btn_belt_close_03_active.tga",
		},

		## Panel_Login
		{
			"name" : "LoginBoard",
			"type" : "thinboardtwix",

			"x" : (SCREEN_WIDTH - 449) / 2,
			"y" : (SCREEN_HEIGHT - 460) / 2 + (50 * (float(SCREEN_HEIGHT) / 768.0)),

			"width" : 360,
			"height" : 330,

			"children" :
			(
				{
					"name": "Hover",
					"type": "text",

					"x": 155,
					"y": 40,

					"text" : "Logare Cont",

					"color": twix_work.COLOR_HOVER,

					"children":
					(
						{
							"name": "hoverImg",
							"type": "image",

							"x": -70,
							"y": 15,

							"image": "d:/ymir work/ui/intro/login/horizontal_bar/center_inverted.tga",
						},
					),
				},
				{
					"name": "Separator_Buttons",
					"type": "image",

					"x": 232,
					"y": 115+5,

					"image": "d:/ymir work/ui/intro/login/separator/separator_buttons.tga",
				},
				{
					"name": "id_editlines",
					"type": "input",

					"x": 40,
					"y": 100+30,

					"width" : 150,

					"children":
					(
						{
							"name": "Separator_ID",
							"type": "image",

							"x": 20,
							"y": -53,

							"image": "d:/ymir work/ui/intro/login/separator/separator_input.tga",
						},
						{
							"name": "Dialog_ID",
							"type": "text",

							"x": 35,
							"y": -45,

							"color" : twix_work.COLOR_LOGIN_TEXT,

							"text" : twix_work.ID_LOGIN,
						},
						
						# {
							# "name": "ID_EditLine",
							# "type": "editline",

							# "x": 10,
							# "y": -20,

							# "width": 211,
							# "height": 34,

							# "input_limit": 16,
							# "enable_codepage": 0,

							# "color": 0xFFFFE099,
						# },
						
					),
				},
				{
					"name": "pwd_editlines",
					"type": "input",

					"x": 40,
					"y": 133+50,

					"width" : 150,

					"children":
					(
						{
							"name": "Separator_PW",
							"type": "image",

							"x": 20,
							"y": -53,

							"image": "d:/ymir work/ui/intro/login/separator/separator_input.tga",
						},
						{
							"name": "Dialog_PW",
							"type": "text",

							"x": 35,
							"y": -45,

							"color" : twix_work.COLOR_LOGIN_TEXT,

							"text" : twix_work.PW_LOGIN,
						},
						
						# {
							# "name": "Password_EditLine",
							# "type": "editline",

							# "x": 10,
							# "y": -20,

							# "width": 211,
							# "height": 38,

							# "input_limit": 16,
							# "secret_flag": 1,
							# "enable_codepage": 0,

							# "color": 0xFFFFE099,
						# },
						
					),
				},
				{
					"name" : "LoginButton",
					"type" : "button",

					"x": 99,
					"y": -20-10,

					"horizontal_align": "center",
					"vertical_align": "center",

					"text" : "Logare",
					"text_color" : twix_work.COLOR_HOVER,

					'default_image' : 'd:/ymir work/ui/intro/login/button/button_normal.tga',
					'down_image' : 'd:/ymir work/ui/intro/login/button/button_hover.tga',
					'over_image' : 'd:/ymir work/ui/intro/login/button/button_normal.tga',
				},
				{
					"name" : "LoginExitButton",
					"type" : "button",

					"x": 99,
					"y": 10-10,

					"horizontal_align": "center",
					"vertical_align": "center",

					"text" : "Iesire Joc",
					"text_color" : twix_work.COLOR_HOVER,

					'default_image' : 'd:/ymir work/ui/intro/login/button/button_normal.tga',
					'down_image' : 'd:/ymir work/ui/intro/login/button/button_hover.tga',
					'over_image' : 'd:/ymir work/ui/intro/login/button/button_normal.tga',
				},
				{
					"name" : "WithoutAccount",
					"type" : "text",

					"x" : 40,
					"y" : 110,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"color" : 0xFFa07970,

					"text" : twix_work.LOGIN_NOACCOUNT,
				},
				{
					"name": "hoverInvert",
					"type": "image",

					"x": 100,
					"y": 240,

					"image": "d:/ymir work/ui/intro/login/horizontal_bar/center.tga",
				},

				{
					"name" : "buttonExpand",
					"type" : "button",

					"x" : 354,
					"y" : 125,

					"default_image": "d:/ymir work/ui/intro/login/button/btn_belt_open_01_normal.tga",
					"over_image": "d:/ymir work/ui/intro/login/button/btn_belt_open_02_hover.tga",
					"down_image": "d:/ymir work/ui/intro/login/button/btn_belt_open_03_active.tga",
				},
			),
		},
	),
}
