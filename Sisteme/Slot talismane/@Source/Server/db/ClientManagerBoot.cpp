// Now search in :

bool CClientManager::InitializeItemAttrTable()
{
	
// This :

			"SELECT apply, apply+0, prob, lv1, lv2, lv3, lv4, lv5, weapon, body, wrist, foots, neck, head, shield, ear FROM item_attr%s ORDER BY apply",

// Replace with :

#ifdef ENABLE_PENDANT
			"SELECT apply, apply+0, prob, lv1, lv2, lv3, lv4, lv5, weapon, body, wrist, foots, neck, head, shield, ear, pendant FROM item_attr%s ORDER BY apply",
#else
			"SELECT apply, apply+0, prob, lv1, lv2, lv3, lv4, lv5, weapon, body, wrist, foots, neck, head, shield, ear FROM item_attr%s ORDER BY apply",
#endif


// Search :

str_to_number(t.bMaxLevelBySet[ATTRIBUTE_SET_EAR], data[col++]);

// Add after :

#ifdef ENABLE_PENDANT
		str_to_number(t.bMaxLevelBySet[ATTRIBUTE_SET_PENDANT], data[col++]);
#endif


// Search this syslog :
		sys_log(0, "ITEM_ATTR: %-20s %4lu { %3d %3d %3d %3d %3d } { %d %d %d %d %d %d %d }",


// Replace with :

#ifdef ENABLE_PENDANT
		sys_log(0, "ITEM_ATTR: %-20s %4lu { %3d %3d %3d %3d %3d } { %d %d %d %d %d %d %d %d }",
#else
		sys_log(0, "ITEM_ATTR: %-20s %4lu { %3d %3d %3d %3d %3d } { %d %d %d %d %d %d %d }",
#endif


// Now search :

				t.bMaxLevelBySet[ATTRIBUTE_SET_NECK],
				t.bMaxLevelBySet[ATTRIBUTE_SET_HEAD],
				t.bMaxLevelBySet[ATTRIBUTE_SET_SHIELD],
				t.bMaxLevelBySet[ATTRIBUTE_SET_EAR] 
				
				
// Add fter  :
// Atention with :  " , "
#ifdef ENABLE_PENDANT
				,t.bMaxLevelBySet[ATTRIBUTE_SET_PENDANT]
#endif

// #### Screen :

### https://gyazo.com/e2530f1ce99a036d6e997da8e808266e
