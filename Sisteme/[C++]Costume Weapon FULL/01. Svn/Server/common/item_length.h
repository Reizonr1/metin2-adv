// 1) Search: COSTUME_HAIR = ARMOR_HEAD,
// 2) Make a new line and paste:
#ifdef __WEAPON_COSTUME_SYSTEM__
	COSTUME_WEAPON,
#endif

// 1) Search: WEARABLE_COSTUME_HAIR = (1 << 13),
// 2) Make a new line and paste:
#ifdef __WEAPON_COSTUME_SYSTEM__
	WEARABLE_COSTUME_WEAPON = (1 << 14),
#endif