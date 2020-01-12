// 1) Search: ACMD(do_inventory);
// 2) After make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
ACMD(do_attr_transfer);
#endif

// 1) Search: {"inventory", do_inventory, 0, POS_DEAD, GM_LOW_WIZARD},
// 2) After make a new line and paste:
#ifdef __ATTR_TRANSFER_SYSTEM__
	{"attrtransfer", do_attr_transfer, 0, POS_DEAD, GM_PLAYER},
#endif