*locale/xx/ui/createcharacterwindow.py

Find - Bul:
"height" : 300 + TEMPORARY_HEIGHT,

Change - Değiştir:
"height" : 340 + TEMPORARY_HEIGHT,

http://puu.sh/jSYw5/e122c0454f.png



Find - Bul:
{
	"name" : "character_shape",
	"type" : "text",

	"x" : 43,
	"y" : 270,

	"text" : uiScriptLocale.CREATE_SHAPE,

	"text_horizontal_align" : "center",
},

Add it under- Altına ekle:
				{
					"name" : "character_pin",
					"type" : "text",

					"x" : 43,
					"y" : 270 + TEMPORARY_HEIGHT,

					"text" : "Pin: ",

					"text_horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "character_pin_slot",
							"type" : "image",

							"x" : 40 - 1,
							"y" : -2,

							"image" : "d:/ymir work/ui/public/parameter_slot_04.sub",
						},
						{
							"name" : "character_pin_value",
							"type" : "editline",

							"x" : 40 - 1 + 3,
							"y" : 0,

							"input_limit" : 9,

							"width" : 90,
							"height" : 20,

							"secret_flag" : 1,
						},
					),
				},


http://puu.sh/jSYzV/fc8ef57a64.png
http://puu.sh/jSYBY/40d8b341e4.png


Find - Bul: / 2X /
"y" : 265 + TEMPORARY_HEIGHT,

Change - Değiştir: / 2X /
"y" : 300 + TEMPORARY_HEIGHT,

http://puu.sh/jSYF7/859647ea5e.png