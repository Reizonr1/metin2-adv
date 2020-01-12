// Search in :

int get_Item_SubType_Value(unsigned int type_value, string inputString)
{
	
// This:

"ARMOR_NECK", "ARMOR_EAR",

// Add after :


#ifdef ENABLE_PENDANT
				"ARMOR_PENDANT",
#endif


// Final example :

###				static string arSub2[] = { "ARMOR_BODY", "ARMOR_HEAD", "ARMOR_SHIELD", "ARMOR_WRIST", "ARMOR_FOOTS",
###							"ARMOR_NECK", "ARMOR_EAR",
###			#ifdef ENABLE_PENDANT
###							"ARMOR_PENDANT",
###			#endif
###							"ARMOR_NUM_TYPES"};


// Search in :

int get_Item_WearFlag_Value(string inputString)
{
	

// After the lase WEAR_  ADD THIS :

#ifdef ENABLE_PENDANT
					"WEAR_PENDANT"
#endif	


// Example : "WEAR_HAIR", "WEAR_PENDANT"
