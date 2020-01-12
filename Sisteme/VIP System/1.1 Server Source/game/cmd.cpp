//1.0 suchen:
struct command_info cmd_info[] =
//1.0 davor:
#ifdef ENABLE_VIP_SYSTEM
ACMD(refresh_vip);
#endif

//1.1 suchen:
	{ "\n",		NULL,			0,			POS_DEAD,	GM_IMPLEMENTOR	}
//1.1 davor:
#ifdef ENABLE_VIP_SYSTEM
	{ "refresh_vip",		refresh_vip,		0, 	POS_DEAD,	GM_PLAYER	},
#endif
