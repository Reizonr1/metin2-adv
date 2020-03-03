// Search for:
ACMD(do_poison);

// Add Under:
#ifdef __CHANGE_LOOK_SYSTEM__
ACMD(do_transmutate);
#endif

// Search for:
	{ "poison",				do_poison,					0,			POS_DEAD,	GM_IMPLEMENTOR	},

// Add Under:
#ifdef __CHANGE_LOOK_SYSTEM__
	{ "transmutate",		do_transmutate,				0,			POS_DEAD,	GM_PLAYER		},
#endif
