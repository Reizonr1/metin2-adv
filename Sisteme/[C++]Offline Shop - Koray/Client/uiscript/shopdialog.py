Search:
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

Change:
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 7,
					"y" : 8,

---

Search:
				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 12,
					"y" : 34,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 8,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},

Change:
				{
					"name" : "ItemSlot_40", "type" : "grid_table", "x" : 12, "y" : 34,	"start_index" : 0,
					"x_count" : 5, "y_count" : 8, "x_step" : 32, "y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
				{
					"name" : "ItemSlot_50", "type" : "grid_table", "x" : 12, "y" : 34,	"start_index" : 0,
					"x_count" : 5, "y_count" : 10, "x_step" : 32, "y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
				{
					"name" : "ItemSlot_60", "type" : "grid_table", "x" : 12, "y" : 34,	"start_index" : 0,
					"x_count" : 6, "y_count" : 10, "x_step" : 32, "y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},				
				{
					"name" : "ItemSlot_70", "type" : "grid_table", "x" : 12, "y" : 34,	"start_index" : 0,
					"x_count" : 7, "y_count" : 10, "x_step" : 32, "y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
					{
					"name" : "ItemSlot_80", "type" : "grid_table", "x" : 12, "y" : 34,	"start_index" : 0,
					"x_count" : 8, "y_count" : 10, "x_step" : 32, "y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
					{
					"name" : "ItemSlot_90", "type" : "grid_table", "x" : 12, "y" : 34,	"start_index" : 0,
					"x_count" : 9, "y_count" : 10, "x_step" : 32, "y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},

https://puu.sh/sgRHS/9ffc81326c.png

---

Search:
				{
					"name" : "SellButton",
					"type" : "toggle_button",

					"x" : 104,
					"y" : 295,

					"width" : 61,
					"height" : 21,

					"text" : uiScriptLocale.SHOP_SELL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

Add it under:
				## Move
				{
					"name" : "MoveButton",
					"type" : "button",

					"x" : -35,
					"y" : 295+25-7,

					"horizontal_align" : "center",

					"text" : "Move",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},


https://puu.sh/sgRPs/803b3a872f.png

---

Search:
				## Close
				{
					"name" : "CloseButton",
					"type" : "button",

					"x" : 0,
					"y" : 295,

					"horizontal_align" : "center",

					"text" : uiScriptLocale.PRIVATE_SHOP_CLOSE_BUTTON,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},

Change:
				## Close
				{
					"name" : "CloseButton",
					"type" : "button",

					"x" : 35,
					"y" : 295+25-7,

					"horizontal_align" : "center",

					"text" : uiScriptLocale.PRIVATE_SHOP_CLOSE_BUTTON,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				
				
				{
					"name" : "MoneySlot",
					"type" : "text",

					"x" : 20,
					"y" : 295,

					"text" : "Gain:",

					"children" :
					(
						{
							"name" : "MoneySlot2",
							"type" : "image",

							"x" : 36,
							"y" : -2,

							"image" : "d:/ymir work/ui/public/Parameter_Slot_04.sub",

							"children" :
							(
								{
									"name" : "Money",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"text" : "0 Yang",

									"all_align" : "center"
								},
							),
						},
					),
				},


https://puu.sh/sgRXS/b1ff3b32fa.png
