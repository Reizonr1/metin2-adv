Search:
ACMD(do_mall_close);

Add it under:
#ifdef __OFFLINE_SHOP__
ACMD(do_reloadpos);
ACMD(do_gather);
ACMD(do_moveshop);
ACMD(do_myshops);

ACMD(do_offlineshop_goto);
ACMD(do_offlineshop_warp);
ACMD(do_offlineshop_close);
#endif

https://puu.sh/sgG80/a689489d02.png

---

Search:
	{ "do_clear_affect", do_clear_affect, 	0, POS_DEAD,		GM_LOW_WIZARD},

Add it under:
#ifdef __OFFLINE_SHOP__
	{ "reloadpos", do_reloadpos, 0, POS_DEAD, GM_PLAYER },
	{ "do_gather", do_gather, 0, POS_DEAD, GM_PLAYER },
	{ "do_moveshop", do_moveshop, 0, POS_DEAD, GM_PLAYER },
	{ "do_myshops", do_myshops, 0, POS_DEAD, GM_PLAYER },

	{ "offlineshop_goto", do_offlineshop_goto, 0, POS_DEAD, GM_PLAYER },
	{ "offlineshop_warp", do_offlineshop_warp, 0, POS_DEAD, GM_PLAYER },
	{ "offlineshop_close", do_offlineshop_close, 0, POS_DEAD, GM_PLAYER },
#endif

https://puu.sh/sgG9a/a017290e1b.png