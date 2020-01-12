Search:
	## 600 - (width + ¿À¸¥ÂÊÀ¸·Î ºÎÅÍ ¶ç¿ì±â 24 px)
	"x" : SCREEN_WIDTH - 176,
	"y" : SCREEN_HEIGHT - 37 - 565,

	"style" : ("movable", "float",),

	"width" : 176,
	"height" : 565,

Change "height" value with +20:
	## 600 - (width + ¿À¸¥ÂÊÀ¸·Î ºÎÅÍ ¶ç¿ì±â 24 px)
	"x" : SCREEN_WIDTH - 176,
	"y" : SCREEN_HEIGHT - 37 - 565,

	"style" : ("movable", "float",),

	"width" : 176,
	"height" : 585,

---

Search:
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 176,
			"height" : 565,

Change "height" value with +20:
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 176,
			"height" : 585,

---

Search:
				{
					"name":"Money_Slot",
					"type":"button",

					"x":8,
					"y":28,

					"horizontal_align":"center",
					"vertical_align":"bottom",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

					"children" :
					(
						{
							"name":"Money_Icon",
							"type":"image",

							"x":-18,
							"y":2,

							"image":"d:/ymir work/ui/game/windows/money_icon.sub",
						},

						{
							"name" : "Money",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "123456789",
						},
					),
				},

Add it under:
				{
					"name" : "Bar_First_Icon",
					"type" : "button",

					"x":7,
					"y":47,

					"vertical_align":"bottom",

					"default_image" : "d:/ymir work/ui/bar_1.tga",
					"over_image" : "d:/ymir work/ui/bar_1.tga",
					"down_image" : "d:/ymir work/ui/bar_1.tga",
				},

				{
					"name":"Bar_First_Slot",
					"type":"button",

					"x":22,
					"y":48,

					"vertical_align":"bottom",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_00.sub",

					"children" :
					(
						{
							"name" : "BarFirstText",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "Unknown",
						},
					),
				},

				{
					"name" : "Bar_Second_Icon",
					"type" : "button",

					"x":61,
					"y":47,

					"vertical_align":"bottom",

					"default_image" : "d:/ymir work/ui/bar_2.tga",
					"over_image" : "d:/ymir work/ui/bar_2.tga",
					"down_image" : "d:/ymir work/ui/bar_2.tga",
				},

				{
					"name":"Bar_Second_Slot",
					"type":"button",

					"x":76,
					"y":48,

					"vertical_align":"bottom",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_00.sub",

					"children" :
					(
						{
							"name" : "BarSecondText",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "Unknown",
						},
					),
				},
				{
					"name" : "Bar_Third_Icon",
					"type" : "button",

					"x":115,
					"y":47,

					"vertical_align":"bottom",

					"default_image" : "d:/ymir work/ui/bar_3.tga",
					"over_image" : "d:/ymir work/ui/bar_3.tga",
					"down_image" : "d:/ymir work/ui/bar_3.tga",
				},

				{
					"name":"Bar_Third_Slot",
					"type":"button",

					"x":130,
					"y":48,

					"vertical_align":"bottom",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_00.sub",

					"children" :
					(
						{
							"name" : "BarThirdText",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "Unknown",
						},
					),
				},
