//Cauta ACMD(do_party_request); si adauga deasupra:
ACMD(do_change_race);

//Adauga in struct command_info cmd_info[]

	{ "change_race",	do_change_race,	0,				POS_DEAD,	GM_PLAYER	},