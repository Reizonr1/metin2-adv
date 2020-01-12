*cmd.cpp

Find - Bul:
ACMD(do_pvp);

Add it under- Altına ekle:
ACMD(do_deny_pvp);



Find - Bul:
	{ "pvp",		do_pvp,			0,			POS_DEAD,	GM_PLAYER	},
	
Add it under- Altına ekle:
	{ "deny_pvp",		do_deny_pvp,		0,			POS_DEAD,	GM_PLAYER	},