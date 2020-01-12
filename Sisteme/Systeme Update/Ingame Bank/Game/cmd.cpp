Search:
ACMD(do_refine_rod);

Add it under:
ACMD(do_ingame_bank);

---

Search:
	{ "monsterlog",	do_monsterlog,		0,			POS_DEAD,	GM_LOW_WIZARD	},

Add it under:
	{ "ingame_bank",	do_ingame_bank,		0,			POS_DEAD,	GM_PLAYER	},
