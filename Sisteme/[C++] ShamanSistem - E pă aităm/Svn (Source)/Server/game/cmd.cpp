// Check this:

ACMD(do_polymorph);
ACMD(do_polymorph_item);

// Add this:

ACMD(do_support_system);
ACMD(do_support_system_d);

// Check this:

	{ "\n",		NULL,			0,			POS_DEAD,	GM_IMPLEMENTOR	}
	
// Add above:

	{ "support_system", do_support_system, 0, POS_DEAD, GM_PLAYER },
	{ "support_system_d", do_support_system_d, 0, POS_DEAD, GM_PLAYER },
	
