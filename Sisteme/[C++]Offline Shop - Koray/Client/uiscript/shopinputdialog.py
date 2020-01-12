import uiScriptLocale

window = {
	"name" : "InputDialog",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 205,
	"height" : 200,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 205,
			"height" : 200,

			"title" : "",

			"children" :
			(

				## Input Slot
				{
					"name" : "InputSlot",
					"type" : "slotbar",

					"x" : 0,
					"y" : 40,
					"width" : 90,
					"height" : 18,
					"horizontal_align" : "center",

					#"type" : "image",
					#"image" : "d:/ymir work/ui/public/Parameter_Slot_03.sub",

					"children" :
					(
						{
							"name" : "InputValue",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,
						},
					),
				},

				{
					"name" : "TypeBG", "type" : "image",
					"x" : 5, "y" : 75,
					"image" : "d:/ymir work/yellow_bar.tga"
				},				
				{
					"name" : "SizeBG", "type" : "image",
					"x" : 5, "y" : 102,
					"image" : "d:/ymir work/yellow_bar.tga"
				},
				{
					"name" : "ColorBG", "type" : "image",
					"x" : 5, "y" : 129,
					"image" : "d:/ymir work/yellow_bar.tga"
				},
	

				# Type
				{
					"name" : "TypeDesc", "type" : "text",
					"x" : -122, "y" : 78, "text_horizontal_align" : "center", "horizontal_align" : "center",
					"text" : "Type:"
				},

				## TypeTab
				{
					"name" : "TypeTab1", "type" : "radio_button", "tooltip_text" : "Standart pazar (Ucret: 10K)",
					"x" : 60, "y" : 75, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "TypeTab2", "type" : "radio_button", "tooltip_text" : "6 Saat boyunca cevrimdisi pazar (Ucret: 100K)",
					"x" : 100, "y" : 75, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "TypeTab3", "type" : "radio_button", "tooltip_text" : "12 Saat boyunca cevrimdisi pazar (Ucret: 250K)",
					"x" : 140, "y" : 75, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "TypeTab4", "type" : "radio_button", "tooltip_text" : "18 Saat boyunca cevrimdisi pazar (Ucret: 500K)",
					"x" : 180, "y" : 75, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "TypeTab5", "type" : "radio_button", "tooltip_text" : "24 Saat boyunca cevrimdisi pazar (Ucret: 750K)",
					"x" : 220, "y" : 75, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "TypeTab6", "type" : "radio_button", "tooltip_text" : "48 Saat boyunca cevrimdisi pazar (Ucret: 2M)",
					"x" : 260, "y" : 75, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				

					# Size
				{
					"name" : "SizeDesc", "type" : "text",
					"x" : -122, "y" : 105, "text_horizontal_align" : "center", "horizontal_align" : "center",
					"text" : "Size:"
				},

				## SizeTab
				{
					"name" : "SizeTab1", "type" : "radio_button", "tooltip_text" : "40 Slot",
					"x" : 60, "y" : 102, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "SizeTab2", "type" : "radio_button", "tooltip_text" : "50 Slot",
					"x" : 100, "y" : 102, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "SizeTab3", "type" : "radio_button", "tooltip_text" : "60 Slot",
					"x" : 140, "y" : 102, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "SizeTab4", "type" : "radio_button", "tooltip_text" : "70 Slot",
					"x" : 180, "y" : 102, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "SizeTab5", "type" : "radio_button", "tooltip_text" : "80 Slot",
					"x" : 220, "y" : 102, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "SizeTab6", "type" : "radio_button", "tooltip_text" : "90 Slot",
					"x" : 260, "y" : 102, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},


				# Color
				{
					"name" : "ColorDesc", "type" : "text",
					"x" : -122, "y" : 132, "text_horizontal_align" : "center", "horizontal_align" : "center",
					"text" : "Color:"
				},

				## ColorTab
				{
					"name" : "ColorTab1", "type" : "radio_button", "tooltip_text" : "Mavi",
					"x" : 60, "y" : 129, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "ColorTab2", "type" : "radio_button", "tooltip_text" : "Yesil",
					"x" : 100, "y" : 129, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "ColorTab3", "type" : "radio_button", "tooltip_text" : "Sari",
					"x" : 140, "y" : 129, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "ColorTab4", "type" : "radio_button", "tooltip_text" : "Pembe",
					"x" : 180, "y" : 129, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "ColorTab5", "type" : "radio_button", "tooltip_text" : "Bordo",
					"x" : 220, "y" : 129, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},
				{
					"name" : "ColorTab6", "type" : "radio_button", "tooltip_text" : "Acik Sari",
					"x" : 260, "y" : 129, "width" : 61, "height" : 21,
					"default_image" : "d:/ymir work/normal.tga", "over_image" : "d:/ymir work/hover.tga", "down_image" : "d:/ymir work/active.tga",
				},

				
				## Button
				{
					"name" : "AcceptButton",
					"type" : "button",

					"x" : - 61 - 5 + 30,
					"y" : 165,
					"horizontal_align" : "center",

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "CancelButton",
					"type" : "button",

					"x" : 5 + 30,
					"y" : 165,
					"horizontal_align" : "center",

					"text" : uiScriptLocale.CANCEL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}