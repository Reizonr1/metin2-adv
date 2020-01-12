// 1) Search: "COSTUME_HAIR",
// 2) If: "COSTUME_HAIR", is not the last subtype of costume type, add this after last one:
// 3) After make new line and paste:
#ifdef __EFFECT_SYSTEM__
								, "USE_EFFECT"
#endif


// 1) Search: "WEAR_COSTUME_HAIR",
// 2) If: "WEAR_COSTUME_HAIR", is not the last costumes wear cell, add this after last one:
// 3) After make new line and paste:
#ifdef __EFFECT_SYSTEM__
								, "WEAR_EFFECT_ARMOR", 
								"WEAR_EFFECT_WEAPON"
#endif