// 1) Search: static string arSub28[] = {"COSTUME_BODY", "COSTUME_HAIR",};
// 2) Replace with:
	static string arSub28[] = {"COSTUME_BODY", "COSTUME_HAIR",
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
	"COSTUME_WEAPON",
#endif
	};

// 1) Search: string arWearrFlag[] = {"WEAR_BODY", "WEAR_HEAD", "WEAR_FOOTS", "WEAR_WRIST", "WEAR_WEAPON", "WEAR_NECK", "WEAR_EAR", "WEAR_SHIELD", "WEAR_UNIQUE", "WEAR_ARROW", "WEAR_HAIR", "WEAR_ABILITY", "WEAR_COSTUME_BODY", "WEAR_COSTUME_HAIR",};
// 2) Replace with:
	string arWearrFlag[] = {"WEAR_BODY", "WEAR_HEAD", "WEAR_FOOTS", "WEAR_WRIST", "WEAR_WEAPON", "WEAR_NECK", "WEAR_EAR", "WEAR_SHIELD", "WEAR_UNIQUE", "WEAR_ARROW", "WEAR_HAIR", "WEAR_ABILITY", "WEAR_COSTUME_BODY", "WEAR_COSTUME_HAIR",
#ifdef ENABLE_COSTUME_WEAPON_SYSTEM
	"WEAR_COSTUME_WEAPON",
#endif
	};