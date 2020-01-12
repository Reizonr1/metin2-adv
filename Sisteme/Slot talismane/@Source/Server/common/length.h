// In this enum 


enum EWearPositions
{
	
// Search : 

	WEAR_BELT,				// 26

// Or the last WEAR , why ? Maybe you have this enum different.

// Add this :

#ifdef ENABLE_PENDANT
	WEAR_PENDANT,
#endif

// Now search this enum 

enum EAttributeSet
{
	

	
// After :

	ATTRIBUTE_SET_EAR,
	
// Add this :

#ifdef ENABLE_PENDANT
	ATTRIBUTE_SET_PENDANT,
#endif
