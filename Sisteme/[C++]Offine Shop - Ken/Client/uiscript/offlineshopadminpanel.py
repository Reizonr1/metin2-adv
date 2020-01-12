import uiScriptLocale

window = {
	"name" : "OfflineShopAdminPanelWindow",
	
	"style" : ("movable", "float",),
	
	"x" : 0,
	"y" : 0,
	
	"width" : 411,
	"height" : 204,
	
	"children":
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",
			
			"style" : ("attach", ),
			
			"x" : 0,
			"y" : 0,
			
			"width" : 411,
			"height" : 204,
			
			"title" : "Offline Shop Admin Panel",
			
			"children" :
			(
				# Icon
				{
					"name" : "icon",
					"type" : "expanded_image",
					
					"x" : 22,
					"y" : 44,
					
					"image" : "locale/en/offlineshop/icon.tga",					
				},
				
				# Get back
				{
					"name" : "GetBackButton",
					"type" : "button",
					
					"x" : 21,
					"y" : 126,
					
					"text" : "Get Back",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",					
				},
				
				# Open Offline Shop
				{
					"name" : "OpenOfflineShopButton",
					"type" : "button",
					
					"x" : 117,
					"y" : 126,
					
					"text" : "Open Shop",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				# Close Offline Shop
				{
					"name" : "CloseOfflineShopButton",
					"type" : "button",
					
					"x" : 118,
					"y" : 166,
					
					"text" : "Close Shop",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				# Change Time
				{
					"name" : "ChangeTimeButton",
					"type" : "button",
					
					"x" : 215,
					"y" : 166,
					
					"text" : "Change Time",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				# Change Price
				{
					"name" : "ChangePriceButton",
					"type" : "button",
					
					"x" : 214,
					"y" : 126,
					
					"text" : "Change Price",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				# Remove Item
				{
					"name" : "RemoveItemButton",
					"type" : "button",
					
					"x" : 310,
					"y" : 166,
					
					"text" : "Remove Item",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				# Add Item
				{
					"name" : "AddItemButton",
					"type" : "button",
					
					"x" : 309,
					"y" : 126,
					
					"text" : "Add Item",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				# My Bank
				{
					"name" : "MyBankButton",
					"type" : "button",
					
					"x" : 21,
					"y" : 166,
					
					"text" : "My Bank",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",										
				},
				
				# User Name
				{
					"name" : "UserName",
					"type" : "text",
					
					"x" : 106,
					"y" : 66,
					
					"text" : "Hello Mrs. Alina",
				},
			),
		},
	),
}