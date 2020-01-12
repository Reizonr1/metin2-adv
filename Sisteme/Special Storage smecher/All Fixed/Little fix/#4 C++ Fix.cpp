Exchange fix

exchange.cpp aç ve cauta

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	static CGrid s_grid5(5, SKILL_BOOK_INVENTORY_MAX_NUM / 5 / 4);
	static CGrid s_grid6(5, UPGRADE_ITEMS_INVENTORY_MAX_NUM / 5 / 4);
	static CGrid s_grid7(5, STONE_INVENTORY_MAX_NUM / 5 / 4);
	static CGrid s_grid8(5, SANDIK_INVENTORY_MAX_NUM / 5 / 4);
#endif

değiştir

#ifdef WJ_SPLIT_INVENTORY_SYSTEM
	static CGrid s_grid5(5, SKILL_BOOK_INVENTORY_MAX_NUM / 5 / 3);
	static CGrid s_grid6(5, UPGRADE_ITEMS_INVENTORY_MAX_NUM / 5 / 3);
	static CGrid s_grid7(5, STONE_INVENTORY_MAX_NUM / 5 / 3);
	static CGrid s_grid8(5, SANDIK_INVENTORY_MAX_NUM / 5 / 3);
#endif