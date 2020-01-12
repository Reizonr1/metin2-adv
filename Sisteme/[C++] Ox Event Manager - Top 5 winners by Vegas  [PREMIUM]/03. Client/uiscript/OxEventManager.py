import localeInfo, grp, oxevent

ROOT_PATH = "d:/ymir work/ui/path_oxevent/board/"
CREATE_BOARD_X = 400
CREATE_BOARD_Y = 180
COLOR_LINE = 0xff5b5e5e
BOARD_X = 235
BOARD_Y = 190

window = {
	"name" : "OxEventManager",
    "x" : SCREEN_WIDTH - 228 + 100,
    "y" : SCREEN_HEIGHT - 37 - 670,

	"style" : ("movable", "float",),
	
	"width" : CREATE_BOARD_X + 100,
	"height" : CREATE_BOARD_Y,
	
	"children" :
	(
				{
					"name" : "ButtonsBoard",
					"type" : "board",
					"style" : ("attach",),

					"x" : -42,
					"y" : +24,
					"vertical_align":"center",
					"width" : 110,
					"height" : 128,

					"children" :
					(
						### Button Open Gates
						{
							"name" : "open_button_btn",
							"type" : "button",
							"x" : 7,
							"y" : 10,
							"text" : "Open gates",
							"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",
						},
						
						### Button Close Gates
						{
							"name" : "close_gates_btn",
							"type" : "button",
							"x" : 7,
							"y" : 10 + 22,
							"text" : "Close gates",
							"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",
						},	
						
						### Button Ask Question
						{
							"name" : "ask_question_btn",
							"type" : "button",
							"x" : 7,
							"y" : 10 + 22 + 22,
							"text" : "Run a question",
							"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",
						},	
						
						### Button Close Event
						{
							"name" : "close_event_btn",
							"type" : "button",
							"x" : 7,
							"y" : 10 + 22 + 22 + 22,
							"text" : "Finish event",
							"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",
						},	
						
						### Button Force Close Event
						{
							"name" : "force_close_event_btn",
							"type" : "button",
							"x" : 7,
							"y" : 10 + 22 + 22 + 22 + 22,
							"text" : "Force close",
							"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",
						},	
					),
				},
				
		{
			"name" : "ItemBoard",
			"type" : "board",
			"style" : ("attach",),

			"x" : CREATE_BOARD_X+30,
			"y" : 31,
			"vertical_align":"center",

			"width" : 15,
			"height" : 114,
			"children" :
			(
				{
					"name" : "Slot",
					"type" : "grid_table",
					"x" : 21,
					"y" : 9,
					"start_index" : 0,
					"x_count" : 1,
					"y_count" : 3,
					"x_step" : 32,
					"y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
				{
					"name":"slot_image_value",
					"type":"image",
					"x": 22,
					"y": 9,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
			),
		},
		{
			"name" : "Board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),
			"title" : localeInfo.OXEVENT_MANAGER_TITLENAME,
			"x" : +50,
			"y" : 0,
			"width" : CREATE_BOARD_X,
			"height" : CREATE_BOARD_Y,
			"children" :
			(
				{
					"name" : "BackgroundA",
					"type" : "bar",
					"x" : 7,
					"y" : 30,
					"width" : CREATE_BOARD_X-15,
					"height" : CREATE_BOARD_Y-39,
					"color" : grp.GenerateColor(0.0, 0.0, 0.0, 0.4),
				},

				{
					"name" : "ImageLine",
					"type" : "image",
					"x" : 19,
					"y" : 40,
					"image" : ROOT_PATH + "over_line.tga",
				},

				{ "name" : "LINE_BGCREATE_LEFT", "type" : "line", "x" : 8, "y" : 30, "width" : 0, "height" : CREATE_BOARD_Y-40, "color" : COLOR_LINE, },

				{ "name" : "LINE_BGCREATE_RIGHT", "type" : "line", "x" : CREATE_BOARD_X-10, "y" : 30, "width" : 0, "height" : CREATE_BOARD_Y-40, "color" : COLOR_LINE, },

				{ "name" : "LINE_BGCREATE_DOWN", "type" : "line", "x" : 8, "y" : CREATE_BOARD_Y-10, "width" : CREATE_BOARD_X-17, "height" : 0, "color" : COLOR_LINE, },

				{ "name" : "LINE_BGCREATE_UP", "type" : "line", "x" : 8, "y" : 30, "width" : CREATE_BOARD_X-17, "height" : 0, "color" : COLOR_LINE, },

				{ "name" : "LINE_BG_LEFT", "type" : "line", "x" : 15, "y" : 35, "width" : 0, "height" : CREATE_BOARD_Y-48, "color" : COLOR_LINE, },

				{ "name" : "LINE_BG_RIGHT", "type" : "line", "x" : CREATE_BOARD_X-16, "y" : 35, "width" : 0, "height" : CREATE_BOARD_Y-48, "color" : COLOR_LINE, },

				{ "name" : "LINE_BG_UP", "type" : "line", "x" : 16, "y" : 35, "width" : CREATE_BOARD_X-32, "height" : 0, "color" : COLOR_LINE, },
				

				{ "name" : "LINE_UP_DOWN_A", "type" : "line", "x" : 16, "y" : 65, "width" : CREATE_BOARD_X-32, "height" : 0, "color" : COLOR_LINE, },
				{ "name" : "LINE_UP_DOWN_B", "type" : "line", "x" : 16, "y" : 92, "width" : CREATE_BOARD_X-32, "height" : 0, "color" : COLOR_LINE, },
				{ "name" : "LINE_UP_DOWN_C", "type" : "line", "x" : 16, "y" : CREATE_BOARD_Y-14, "width" : CREATE_BOARD_X-32, "height" : 0, "color" : COLOR_LINE, },
				
				# Text
				{
					"name": "textParticipants",
					"type":"text",
					"x": 22,
					"y": 44,
					"text": localeInfo.OXEVENT_MANAGER_USER_TEXT,
				},
				
				{
					"name": "current_participants",
					"type":"text",
					"x": 300,
					"y": 44,
				},
				
				### Button Rewards Players
				{
					"name" : "reward_players_btn",
					"type" : "button",
					"x" : 20,
					"y" : 130,
					"text" : localeInfo.OXEVENT_MANAGER_BTN_REWARD,
					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",
				},
				
				{
					"name" : "clear_reward_btn",
					"type" : "button",
					"x" : 200,
					"y" : 130,
					"text" : localeInfo.OXEVENT_MANAGER_BTN_CLEAR,
					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",
				},
				
				{
					"name":"TitleBar", "type":"horizontalbar", "x": 20, "y":72, "width": CREATE_BOARD_X-40,
					"children" :
					(
						{
							"name": "textLine",
							"type": "text",
							"x": 8,
							"y": 2,
							"text": localeInfo.OXEVENT_MANAGER_HORIZONTALBAR_TEXT,
						},
						
						{
							"name": "nameItem",
							"type":"text",
							"x": 0,
							"y": 29,
							"text": localeInfo.OXEVENT_MANAGER_NAME_ITEM,
						},							
						
						{
							"name": "countItem",
							"type":"text",
							"x": 260,
							"y": 29,
							"text": localeInfo.OXEVENT_MANAGER_COUNT,
						},								
						
					),
				},
				
				{
					"name" : "slot_vnum",
					"type" : "slotbar",
					"x" : 75,
					"y" : 98,
					"width" : 200,
					"height" : 20,
					"children" :
					(
						{
							"name" : "slot_vnum_value",
							"type" : "editline",
							"x" : 5,
							"y" : 3,
							"width" : 197,
							"height" : 17,
							"input_limit" : 25,
						},
					),
				},
				
				{
					"name" : "slot_count",
					"type" : "slotbar",
					"x" : 330,
					"y" : 98,
					"width" : 25,
					"height" : 20,
					"children" :
					(
						{
							"name" : "slot_count_value",
							"type" : "editline",
							"x" : 3,
							"y" : 3,
							"width" : 197,
							"height" : 17,
							"input_limit" : 3,
						},
					),
				},
				
				{
					"name" : "listbox_bar",
					"type" : "slotbar",
					"x" : 70,
					"y" : 118,
					"width" : 200,
					"height" : 70,
					"children" :
					(
						{
							"name" : "ListBox",
							"type" : "listbox2",
							"x" : 0,
							"y" : 0,
							"row_count" : oxevent.MAX_ROWS,
							"width" : 200,
							"height" : 200,
						},
					),
				},
			),
		},
	),
}