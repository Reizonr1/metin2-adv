//Search in affect.h this line:
	AFFECT_BOW_DISTANCE,	// 225
	AFFECT_DEF_GRADE,		// 226

//Add After This Code:
#ifdef NEW_PET_SYSTEM
	AFFECT_PET,
#endif

//Search in affect.h this line:
	AFFECT_HORSE_NAME,
	AFFECT_MOUNT_BONUS,

//Add after this code:
#ifdef NEW_PET_SYSTEM
	AFFECT_NEW_PET = 559,
#endif
