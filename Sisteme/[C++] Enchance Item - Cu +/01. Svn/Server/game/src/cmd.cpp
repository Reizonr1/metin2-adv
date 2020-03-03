// 1) Search: ACMD(do_cube);
// 2) Before this make a new line and paste:
#ifdef __NEW_ENCHANT_ATTR__
ACMD(do_enchant_new);
ACMD(do_enchant_old);
#endif


// 1) Search: {"cube", do_cube, 0, POS_DEAD, GM_PLAYER},
// 2) Before this make a new line and paste:
#ifdef __NEW_ENCHANT_ATTR__
	{"enchant_new", do_enchant_new, 0, POS_DEAD, GM_PLAYER},
	{"enchant_old", do_enchant_old, 0, POS_DEAD, GM_PLAYER},
#endif