// 1) Search: ACMD(do_inventory);
// 2) After make a new line and paste:
ACMD(do_acce);

// 1) Search: {"inventory", do_inventory, 0, POS_DEAD, GM_LOW_WIZARD},
// 2) After make a new line and paste:
	{"acce", do_acce, 0, POS_DEAD, GM_PLAYER},