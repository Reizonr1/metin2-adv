// Search this :


	else if (GetWearFlag() & WEARABLE_ARROW)
		return WEAR_ARROW;
	
// Add after this :

#ifdef ENABLE_PENDANT
	else if (GetWearFlag() & WEARABLE_PENDANT)
		return WEAR_PENDANT;
#endif

