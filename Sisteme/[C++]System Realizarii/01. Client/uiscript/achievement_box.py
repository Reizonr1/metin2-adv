BOARD_WIDTH = 500
BOARD_HEIGHT = 56

window = {
	"name" : "AchievementBox",
	
	"x" : 0,
	"y" : 0,
	
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
					"name" : "AchievementTitle",
					"type" : "resizable_text_value",
					
					"x" : 15,
					"y" : -6,
					
					"width" : 100,
					"height" : 18,
					
					"text" : "Category Name",
					"all_lines" : 1,
				},
				{
					"name" : "AchievementPoints",
					"type" : "resizable_text_value",
					
					"x" : 415,
					"y" : 18,
					
					"width" : 68,
					"height" : 25,
					
					"text" : "100",
					"all_lines" : 1,
				},
			),
		},
	),
}