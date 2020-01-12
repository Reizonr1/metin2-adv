import uiScriptLocale

window = {
	"name" : "OfflineShopAdminPanelWindow",
	
	"style" : ("movable", "float",),
	
	"x" : 0,
	"y" : 0,
	
	"width" : 314,
	"height" : 210,
	
	"children":
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",
			
			"style" : ("attach", ),
			
			"x" : 0,
			"y" : 0,
			
			"width" : 314,
			"height" : 210,
			
			"title" : "Pazar Paneli (Offline Shop)",
			
			"children" :
			(
				# Icon
				{
					"name" : "icon",
					"type" : "expanded_image",
					
					"x" : 23,
					"y" : 43,
					
					"image" : "locale/de/offlineshop/icon.tga",
				},
				
				# Open Offline Shop
				{
					"name" : "OpenOfflineShopButton",
					"type" : "button",
					
					"x" : 16,
					"y" : 108,
					
					"text" : "Pazar Ac",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				# Close Offline Shop
				{
					"name" : "CloseOfflineShopButton",
					"type" : "button",
					
					"x" : 111,
					"y" : 107,
					
					"text" : "Pazarı Kapat",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				# Change Time
				{
					"name" : "ChangeTimeButton",
					"type" : "button",
					
					"x" : 16,
					"y" : 140,
					
					"text" : "Sure Degistir",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				# Change Price
				{
					"name" : "ChangePriceButton",
					"type" : "button",
					
					"x" : 113,
					"y" : 140,
					
					"text" : "Fiyat Degistir",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				# Remove Item
				{
					"name" : "RemoveItemButton",
					"type" : "button",
					
					"x" : 207,
					"y" : 107,
					
					"text" : "Item Sil",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				# Add Item
				{
					"name" : "AddItemButton",
					"type" : "button",
					
					"x" : 209,
					"y" : 137,
					
					"text" : "Item Ekle",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				# My Bank
				{
					"name" : "MyBankButton",
					"type" : "button",
					
					"x" : 113,
					"y" : 174,
					
					"text" : "Banka",
					
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				# User Name
				{
					"name" : "UserName",
					"type" : "text",
					
					"x" : 78,
					"y" : 59,
					
					"text" : "",
				},
			),
		},
	),
}