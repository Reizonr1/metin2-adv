// 1)  Seearch:
	{ "mall_close",	do_mall_close,		0,			POS_DEAD,	GM_PLAYER	},
// 2)  Add bellow:
#ifdef ENABLE_TITLE_SYSTEM		
	{ "prestige_title_name",	do_prestige_title,	0,	POS_DEAD,	GM_PLAYER},	
#endif
"""""""""""""""""""""""""""""""""""""""""
// 1)  Search:
ACMD(do_refine_rod);

// 2) Add bellow:
#ifdef ENABLE_TITLE_SYSTEM	
	ACMD(do_prestige_title);
#endif
"""""""""""""""""""""""""""""""""""""""""