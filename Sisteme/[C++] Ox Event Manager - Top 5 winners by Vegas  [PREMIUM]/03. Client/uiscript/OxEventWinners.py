FACE_PATH = "d:/ymir work/ui/path_oxevent/face/face_unknown.tga"
ROOT_PATH = "d:/ymir work/ui/path_oxevent/board/"
FACE_X = 7
FACE_Y = 4
SELECT_BTN_X = 15
SELECT_BTN_Y = 10
SELECT_BTN_GAP = 44
COLOR_ANSWERS = [30, 72, 168]
COLOR_NAME = [0.8549, 0.8549, 0.8549]
TEXT_ANSWERS_X = 125
TEXT_ANSWERS_Y = 19
TEXT_NAME_X = 140
TEXT_NAME_Y = 3

window = {
	"name" : "OxEventWinners",
	"x" : SCREEN_WIDTH,
	"y" : 0,
	"style" : ("movable", "float",),
	"width" : 175,
	"height" : 240,
	"children" :
	(
		{
			"name" : "board",
			"type" : "thinboard",
			"x" : 0,
			"y" : 0,
			"width" : 0,
			"height" : 0,
			"children" :
			(
				{
					"name" : "character_slot_1",
					"type" : "image", 
					"x" : SELECT_BTN_X,
					"y" : SELECT_BTN_Y,
					"image" : ROOT_PATH + "last_winner_slot.sub",
					"children" :
					(
						{
							"name" : "character_name_1", "type" : "text", "x" : TEXT_NAME_X, "y" : TEXT_NAME_Y, "r" : COLOR_NAME[0], "g" : COLOR_NAME[1], "b" : COLOR_NAME[2], "text" : "", "text_horizontal_align" : "right"
						},
						{
							"name" : "character_answers_1", "type" : "text", "x" : TEXT_ANSWERS_X, "y" : TEXT_ANSWERS_Y, "r" : COLOR_ANSWERS[0], "g" : COLOR_ANSWERS[1], "b" : COLOR_ANSWERS[2], "text" : "", "text_horizontal_align" : "center"
						},
					),
				},	

				{
					"name" : "character_slot_2",
					"type" : "image", 
					"x" : SELECT_BTN_X,
					"y" : SELECT_BTN_Y + SELECT_BTN_GAP,
					"image" : ROOT_PATH + "normal_slot.sub",
					"children" :
					(
						{
							"name" : "character_name_2", "type" : "text", "x" : TEXT_NAME_X, "y" : TEXT_NAME_Y, "r" : COLOR_NAME[0], "g" : COLOR_NAME[1], "b" : COLOR_NAME[2], "text" : "", "text_horizontal_align" : "right"
						},
						{
							"name" : "character_answers_2", "type" : "text", "x" : TEXT_ANSWERS_X, "y" : TEXT_ANSWERS_Y, "r" : COLOR_ANSWERS[0], "g" : COLOR_ANSWERS[1], "b" : COLOR_ANSWERS[2], "text" : "", "text_horizontal_align" : "center"
						},
					),
				},					

				{
					"name" : "character_slot_3",
					"type" : "image", 
					"x" : SELECT_BTN_X,
					"y" : SELECT_BTN_Y + SELECT_BTN_GAP*2,
					"image" : ROOT_PATH + "normal_slot.sub",
					"children" :
					(
						{
							"name" : "character_name_3", "type" : "text", "x" : TEXT_NAME_X, "y" : TEXT_NAME_Y, "r" : COLOR_NAME[0], "g" : COLOR_NAME[1], "b" : COLOR_NAME[2], "text" : "", "text_horizontal_align" : "right"
						},
						{
							"name" : "character_answers_3", "type" : "text", "x" : TEXT_ANSWERS_X, "y" : TEXT_ANSWERS_Y, "r" : COLOR_ANSWERS[0], "g" : COLOR_ANSWERS[1], "b" : COLOR_ANSWERS[2], "text" : "", "text_horizontal_align" : "center"
						},
					),
				},

				{
					"name" : "character_slot_4",
					"type" : "image", 
					"x" : SELECT_BTN_X,
					"y" : SELECT_BTN_Y + SELECT_BTN_GAP*3,
					"image" : ROOT_PATH + "normal_slot.sub",
					"children" :
					(
						{
							"name" : "character_name_4", "type" : "text", "x" : TEXT_NAME_X, "y" : TEXT_NAME_Y, "r" : COLOR_NAME[0], "g" : COLOR_NAME[1], "b" : COLOR_NAME[2], "text" : "", "text_horizontal_align" : "right"
						},
						{
							"name" : "character_answers_4", "type" : "text", "x" : TEXT_ANSWERS_X, "y" : TEXT_ANSWERS_Y, "r" : COLOR_ANSWERS[0], "g" : COLOR_ANSWERS[1], "b" : COLOR_ANSWERS[2], "text" : "", "text_horizontal_align" : "center"
						},
					),
				},
				
				{
					"name" : "character_slot_5",
					"type" : "image", 
					"x" : SELECT_BTN_X,
					"y" : SELECT_BTN_Y + SELECT_BTN_GAP*4,
					"image" : ROOT_PATH + "normal_slot.sub",
					"children" :
					(
						{
							"name" : "character_name_5", "type" : "text", "x" : TEXT_NAME_X, "y" : TEXT_NAME_Y, "r" : COLOR_NAME[0], "g" : COLOR_NAME[1], "b" : COLOR_NAME[2], "text" : "", "text_horizontal_align" : "right"
						},
						{
							"name" : "character_answers_5", "type" : "text", "x" : TEXT_ANSWERS_X, "y" : TEXT_ANSWERS_Y, "r" : COLOR_ANSWERS[0], "g" : COLOR_ANSWERS[1], "b" : COLOR_ANSWERS[2], "text" : "", "text_horizontal_align" : "center"
						},
					),
				},
				
				{
					"name" : "character_face_1",
					"type" : "image",
					"x" : SELECT_BTN_X - FACE_X,
					"y" : SELECT_BTN_Y - FACE_Y,
					"image" : FACE_PATH
				},
				{
					"name" : "character_face_2",
					"type" : "image",
					"x" : SELECT_BTN_X - FACE_X,
					"y" : SELECT_BTN_Y + SELECT_BTN_GAP - FACE_Y,
					"image" : FACE_PATH
				},
				{
					"name" : "character_face_3",
					"type" : "image",
					"x" : SELECT_BTN_X - FACE_X,
					"y" : SELECT_BTN_Y + SELECT_BTN_GAP*2 - FACE_Y,
					"image" : FACE_PATH
				},
				{
					"name" : "character_face_4",
					"type" : "image",
					"x" : SELECT_BTN_X - FACE_X,
					"y" : SELECT_BTN_Y + SELECT_BTN_GAP*3 - FACE_Y,
					"image" : FACE_PATH
				},
				{
					"name" : "character_face_5",
					"type" : "image",
					"x" : SELECT_BTN_X - FACE_X,
					"y" : SELECT_BTN_Y + SELECT_BTN_GAP*4 - FACE_Y,
					"image" : FACE_PATH
				},
			),
		},
	),
}