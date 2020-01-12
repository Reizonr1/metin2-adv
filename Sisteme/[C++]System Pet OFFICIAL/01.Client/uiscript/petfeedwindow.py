import uiScriptLocale


EXP_Y_ADD_POSITION = 0

window = {
	"name" : "PetFeedWindow",
	"style" : ("movable", "float",),
	
	"x" : SCREEN_WIDTH - 500 + 328 -148,
	"y" : SCREEN_HEIGHT - 595 + 240,	

	"width" : 130,
	"height" : 170,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 130,
			"height" : 170,

			"children" :
			(
				## Pet Feed Title
				{
					"name" : "PetFeed_TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : 128,
					
					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":0, "text":"", "all_align":"center" },
					),
				},
				## Pet Feed Area
				{
					"name" : "Pet_Feed_Area",
					"type" : "window",
					"style" : ("attach",),
					
					"x" : 0,
					"y" : 26,
					
					"width" : 128,
					"height" : 144,
					"children" :
					(								
						## Pet Feed Slot
						{
							"name" : "FeedItemSlot",
							"type" : "grid_table",

							"x" : 17,
							"y" : 4,

							"start_index" : 0,
							"x_count" : 3,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"image" : "d:/ymir work/ui/public/Slot_Base.sub"
						},
						
						## Pet Feed Button
						{
							"name" : "FeedButton",
							"type" : "button",

							"x" : 50,
							"y" : 110,

							"text" : "Feed",

							"default_image" : "d:/ymir work/ui/dragonsoul/m_button01.tga",
							"over_image" : "d:/ymir work/ui/dragonsoul/m_button02.tga",
							"down_image" : "d:/ymir work/ui/dragonsoul/m_button03.tga",
						},
					),						
					
				}, ## End of Pet Feed Area
			),				
		},
	),
}
