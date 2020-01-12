import uiScriptLocale

window = {
	"name" : "OfflineShopBankWindow",
	
	"style" : ("movable", "float", ),
	
	"x" : 0,
	"y" : 0,
	
	"width" : 332,
	"height" : 177,
	
	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",
			
			"style" : ("attach", ),
			
			"x" : 0,
			"y" : 0,
			
			"width" : 332,
			"height" : 177,
			
			"title" : "Offline Shop Bank",
			
			"children" :
			(
				{
					"name" : "icon",
					"type" : "expanded_image",
					
					"x" : 15,
					"y" : 43,
					
					"image" : uiScriptLocale.LOCALE_OFFLINESHOP_PATH + "/moneybag.tga",
				},
				
				{
					"name" : "CurrentMoneySlot",
					"type" : "slotbar",
					
					"x" : 108,
					"y" : 57,
					
					"width" : 210,
					"height" : 18,
					
					"children" :
					(
						{
							"name" : "CurrentMoneyLine",
							"type" : "text",
							
							"x" : 3,
							"y" : 3,
							
							"width" : 210,
							"height" : 16,
							
							"input_limit" : 12,
							"text" : "Current Money",
						},
					),
				},

				{
					"name" : "RequiredMoneySlot",
					"type" : "slotbar",
					
					"x" : 108,
					"y" : 86,
					
					"width" : 210,
					"height" : 18,
					
					"children" :
					(
						{
							"name" : "RequiredMoneyLine",
							"type" : "editline",
							
							"x" : 3,
							"y" : 3,
							
							"width" : 210,
							"height" : 16,
							
							"input_limit" : 12,
							"text" : "Enter required money",
						},
					),
				},
				
				{
					"name" : "withdraw_button",
					"type" : "button",
					
					"x" : 113,
					"y" : 145,
					
					"text" : "Withdraw",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				{
					"name" : "cancel_button",
					"type" : "button",
					
					"x" : 207,
					"y" : 144,
					
					"text" : "Cancel",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",					
				},
			),
		},
	),
}