// 1) Search: COSTUME_NUM_TYPES,
// 2) Before this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
			USE_EFFECT,
#endif


// 1) Search: WEAR_RING1,
// 2) Before this make a new line and paste:
#ifdef ENABLE_EFFECT_SYSTEM
			WEAR_EFFECT_ARMOR,
			WEAR_EFFECT_WEAPON,
#endif


// 1) Search: WEARABLE_COSTUME_HAIR = (1 << 13),
// 2) After this make a new line and paste (IF ISN'T THIS THE LAST, YOU NEED TO PASTE AFTER THE LAST ONE):
#ifdef ENABLE_EFFECT_SYSTEM
			WEARABLE_EFFECT_ARMOR = (1 << 14),
			WEARABLE_EFFECT_WEAPON = (1 << 15),
#endif