// 1) Search: COSTUME_NUM_TYPES,
// 2) Before make new line and paste:
#ifdef __EFFECT_SYSTEM__
	USE_EFFECT,
#endif


// 1) Search: WEARABLE_COSTUME_HAIR = (1 << 13),
// 2) After make new line and paste (IF ISN'T THIS THE LAST, YOU NEED TO PASTE AFTER THE LAST ONE):
#ifdef __EFFECT_SYSTEM__
	WEARABLE_EFFECT_ARMOR = (1 << 14),
	WEARABLE_EFFECT_WEAPON = (1 << 15),
#endif