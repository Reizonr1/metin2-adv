# 01. La inceputul fisierului cautati
window = {
	"name" : "SystemDialog",
	"style" : ("float",),

	"x" : (SCREEN_WIDTH  - 200) /2,
	"y" : (SCREEN_HEIGHT - 288) /2, ## valoarea 288 poate sa difere

	"width" : 200,
	"height" : 288, ## valoarea 288 poate sa difere

	"children" :
	(
		{
			"name" : "board",
			"type" : "thinboard",

			"x" : 0,
			"y" : 0,

			"width" : 200,
			"height" : 288, ## valoarea 288 poate sa difere

Modificati height (si SCREEN_HEIGHT) cu valoarea precedenta +30. Mai jos aveti exemplu.
---------
# Exemplu
window = {
	"name" : "SystemDialog",
	"style" : ("float",),

	"x" : (SCREEN_WIDTH  - 200) /2,
	"y" : (SCREEN_HEIGHT - 288+30) /2,

	"width" : 200,
	"height" : 288+30,

	"children" :
	(
		{
			"name" : "board",
			"type" : "thinboard",

			"x" : 0,
			"y" : 0,

			"width" : 200,
			"height" : 288+30,

# 02. Acum cautati
				{
					"name" : "cancel_button",
					"type" : "button",

					"x" : 10,
					"y" : 247,

					"text" : uiScriptLocale.CANCEL,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},

# 03. Adaugati sub
				{
					"name" : "Texturi",
					"type" : "button",

					"x" : 10,
					"y" : 247+30, ## Tot timpul, ca butoanele sa fie ordonate corect, se adauga +30 la "y".

					"text" : "Textura Cer",
					"text_color" : 0xffF8BF24,

					"default_image" : ROOT + "XLarge_Button_02.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_02.sub",
				},