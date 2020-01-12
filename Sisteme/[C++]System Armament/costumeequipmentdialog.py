import uiScriptLocale

window = {
	"name" : "CostumeEquipmentDialog",

	"x" : 0,
	"y" : 0,

	"width" : 139,
	"height" : 145,

	"children" :
	(
		{
			"name" : "ExpandButton",
			"type" : "button",

			"x" : 2,
			"y" : 15,

			"default_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_normal.tga",
			"over_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_over.tga",
			"down_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_down.tga",
			"disable_image" : "d:/ymir work/ui/game/belt_inventory/btn_expand_disabled.tga",
		},

		{
			"name" : "CostumeEquipmentLayer",

			"x" : 5,
			"y" : 0,

			"width" : 139,
			"height" : 145,

			"children" :
			(
				{
					"name" : "MinimizeButton",
					"type" : "button",

					"x" : 2,
					"y" : 15,

					"default_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_normal.tga",
					"over_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_over.tga",
					"down_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_down.tga",
					"disable_image" : "d:/ymir work/ui/game/belt_inventory/btn_minimize_disabled.tga",
				},

				{
					"name" : "CostumeEquipmentBoard",
					"type" : "board",
					"style" : ("attach", "float"),

					"x" : 10,
					"y" : 0,

					"width" : 129,
					"height" : 145,

					"children" :
					(
						{
							"name" : "Costume_Base",
							"type" : "image",

							"x" : 8,
							"y" : 8,

							"image" : uiScriptLocale.LOCALE_UISCRIPT_PATH + "costume/costume_bg.jpg",

							"children" :
							(
								{
									"name" : "CostumeEquipmentSlot",
									"type" : "slot",

									"x" : 3,
									"y" : 3,

									"width" : 127,
									"height" : 145,

									"slot" : (
										{"index":11, "x":61, "y":45, "width":32, "height":64},
										{"index":12, "x":61, "y": 8, "width":32, "height":32},
										#{"index":16, "x":5, "y":145, "width":32, "height":32},
									),
								},
							),
						},
					),
				},
			),
		},
	),
}
