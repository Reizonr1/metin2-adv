//1.) Search:
	{ "ungroup",	do_ungroup,		0,			POS_DEAD,	GM_PLAYER	},
//2.) Add bellow:
#ifdef ENABLE_TELEPORT_COMMAND
	{ "teleport", do_teleport,		0,			POS_DEAD,	GM_PLAYER},	
#endif
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
//3.) Search:
ACMD(do_ungroup);
//4.) Add bellow:
#ifdef ENABLE_TELEPORT_COMMAND
ACMD(do_teleport);
#endif
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""