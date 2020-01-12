//Seatch in cmd.cpp:
ACMD(do_pcbang_update);
ACMD(do_pcbang_check);

//Add after:
#ifdef NEW_PET_SYSTEM
ACMD(do_CubePetAdd);
ACMD(do_FeedCubePet);
ACMD(do_PetSkill);
ACMD(do_PetEvo);
#endif

//Search in cmd.cpp:

	{ "dragon_soul",				do_dragon_soul,				0,	POS_DEAD,	GM_PLAYER	},
	{ "ds_list",				do_ds_list,				0,	POS_DEAD,	GM_PLAYER	},
	{ "do_clear_affect", do_clear_affect, 	0, POS_DEAD,		GM_LOW_WIZARD},

	
//Add after:
#ifdef NEW_PET_SYSTEM
	{ "cubepetadd",		do_CubePetAdd,	0,	POS_DEAD,	GM_PLAYER },
	{ "feedcubepet",	do_FeedCubePet,	0,	POS_DEAD,	GM_PLAYER },
	{ "petskills",		do_PetSkill,	0,	POS_DEAD,	GM_PLAYER },
	{ "petvoincrease",	do_PetEvo,		0,	POS_DEAD,	GM_PLAYER },
#endif
