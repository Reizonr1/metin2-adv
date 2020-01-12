import uiScriptLocale
window = {
	"name" : "ExtendedInventoryWindow",
    "x" : SCREEN_WIDTH - 176-200,
    "y" : SCREEN_HEIGHT - 37 - 570,

	"style" : ("movable", "float",),
	"width" : 176,
	"height" : 395,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"x" : 0,
			"y" : 0,
			"width" : 176,
			"height" : 395,
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),
					"x" : 8,
					"y" : 7,
					"width" : 161,
					"color" : "yellow",
					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":77, "y":3, "text":uiScriptLocale.EXTENDED_INVENTORY_TITLE, "text_horizontal_align":"center" },
					),
				},
				
				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",
					"x" : 8,
					"y" : 35,
					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 9,
					"x_step" : 32,
					"y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},
				
				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",

					"x" : 10,
					"y" : 328,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,

					"children" :
					(
						{
							"name" : "Inventory_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "I",
						},
					),
				},
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",

					"x" : 10 + 52,
					"y" : 328,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,

					"children" :
					(
						{
							"name" : "Inventory_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "II",
						},
					),
				},
				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",

					"x" : 10 + 104,
					"y" : 328,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_3,

					"children" :
					(
						{
							"name" : "Inventory_Tab_03_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "III",
						},
					),
				},
				## Button
				{
					"name" : "SkillBookButton",
					"type" : "radio_button",
					"x" : 8,
					"y" : 47,
					"tooltip_text" : uiScriptLocale.SKILL_BOOK_INVENTORY,
					"vertical_align" : "bottom",
					"default_image" : "d:/ymir work/ui/bk_env_1.tga",
					"over_image" : "d:/ymir work/ui/bk_env_2.tga",
					"down_image" : "d:/ymir work/ui/bk_env_3.tga",
				},
				{
					"name" : "UpgradeItemsButton",
					"type" : "radio_button",
					"x" : 47,
					"y" : 47,
					"tooltip_text" : uiScriptLocale.UPGRADE_ITEMS_INVENTORY,
					"vertical_align" : "bottom",
					"default_image" : "d:/ymir work/ui/yuk_env_1.tga",
					"over_image" : "d:/ymir work/ui/yuk_env_2.tga",
					"down_image" : "d:/ymir work/ui/yuk_env_3.tga",
				},
				{
					"name" : "StoneButton",
					"type" : "radio_button",
					"x" : 89,
					"y" : 47,
					"tooltip_text" : uiScriptLocale.STONE_INVENTORY,
					"vertical_align" : "bottom",
					"default_image" : "d:/ymir work/ui/tas_env_1.tga",
					"over_image" : "d:/ymir work/ui/tas_env_2.tga",
					"down_image" : "d:/ymir work/ui/tas_env_3.tga",
				},
				{
					"name" : "SandikButton",
					"type" : "radio_button",
					"x" : 131,
					"y" : 47,
					"tooltip_text" : uiScriptLocale.SANDIK_INVENTORY,
					"vertical_align" : "bottom",
					"default_image" : "d:/ymir work/ui/sandik_env_1.tga",
					"over_image" : "d:/ymir work/ui/sandik_env_2.tga",
					"down_image" : "d:/ymir work/ui/sandik_env_3.tga",
				},
			),
		},
	),
}
