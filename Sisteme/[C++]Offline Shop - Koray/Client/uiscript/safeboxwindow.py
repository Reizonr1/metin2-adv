Search:
	"name" : "SafeboxWindow",

	"x" : 100,
	"y" : 20,

	"style" : ("movable", "float",),

	"width" : 176,
	"height" : 250,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 176,
			"height" : 250,

Change:
	"name" : "SafeboxWindow",

	"x" : 100,
	"y" : 20,

	"style" : ("movable", "float",),

	"width" : 176,
	"height" : 425,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 176,
			"height" : 425,


https://puu.sh/sgRsM/2277ccae74.png

--

Search:
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

Change:
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 7,
					"y" : 8,

https://puu.sh/sgRuK/996736cd0a.png

--

Search:
				## Button

Add it under:
				{
					"name" : "CollectButton", "type" : "button",
					"x" : -44 + 12, "y" : 78,

					"text" : "Collect Rewards",
					"horizontal_align" : "center", "vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "MyShopsButton", "type" : "button",
					"x" : 32 + 12, "y" : 78,
					
					"text" : "My Shops",
					"horizontal_align" : "center", "vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				
https://puu.sh/sgRxG/ea2614a86d.png

--

Search:
					"name" : "ChangePasswordButton",
					"type" : "button",

					"x" : 0,
					"y" : 58,

Change:
					"name" : "ChangePasswordButton",
					"type" : "button",

					"x" : -44 + 12,
					"y" : 51,


--

Search:
					"name" : "ExitButton",
					"type" : "button",

					"x" : 0,
					"y" : 37,

Change:
					"name" : "ExitButton",
					"type" : "button",

					"x" : 32 + 12,
					"y" : 51,


---

Search:
				{
					"name" : "ExitButton",
					...
				},


Add it under:
				{
					"name":"MoneySlot",
					"type":"button",

					"x":9,
					"y":28,

					"horizontal_align":"center",
					"vertical_align":"bottom",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

					"children" :
					(
						{
							"name":"MoneyIcon",
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

							"text" : "",
						},
					),
				},


https://puu.sh/sgRDK/8e35eabc02.png

