// Search this enum :


enum EArmorSubTypes

// In this enum after 

	ARMOR_EAR,

// Add this : 

#ifdef ENABLE_PENDANT
	ARMOR_PENDANT,
#endif

// Now search this enum :

enum EItemWearableFlag

// Add this after 
	WEARABLE_COSTUME_HAIR 	= (1 << 13),
 // Note : Or the last WEARABLE

// This :
#ifdef ENABLE_PENDANT
	WEARABLE_PENDANT		= (1 << 15),           // atention here  , 15 , if WEARABLE_COSTUME_HAIR 	= (1 << 13), it's 13, you need change 15 with 14.
#endif

/*
Atention , check if you have this include #include "service.h" // #include "CommonDefines.h"
*/

