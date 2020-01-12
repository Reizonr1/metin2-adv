BOARD_WIDTH = 240
BOARD_HEIGHT = 95

window = {
	"name" : "FinishedAchievementDialog",
	
	"x" : SCREEN_WIDTH - (BOARD_WIDTH + 4),
	"y" : SCREEN_HEIGHT - (BOARD_HEIGHT + 18),
	
	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,
	
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			
			"x" : 0,
			"y" : 0,
			
			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
			
			"children" :
			(
				{
					"name" : "AchievementIcon",
					"type" : "image",
					"vertical_align" : "center",
					
					"x" : 20,
					"y" : 0,
					
					"image" : "d:/ymir work/ui/achievementsystem/achievement_icon.tga",
				},
				{
					"name" : "FirstLine",
					"type" : "text",
					"text_vertical_align" : "center",
					"vertical_align" : "center",
					
					"x" : 20+65+12,
					"y" : -21,
					"outline" : 1,
					
					"text" : "Has alcanzado un logro:",
				},
				{
					"name" : "SecondLine",
					"type" : "text",
					"text_vertical_align" : "center",
					"vertical_align" : "center",
					
					"x" : 20+65+12,
					"y" : 0,
					"outline" : 1,
					
					"text" : "Subir al nivel 100",
				},
				{
					"name" : "ThirdLine",
					"type" : "text",
					"text_vertical_align" : "center",
					"vertical_align" : "center",
					
					"x" : 20+65+12,
					"y" : 21,
					"outline" : 1,
					
					"text" : "Puntos: 1000",
				},
			),
		},
	),
}