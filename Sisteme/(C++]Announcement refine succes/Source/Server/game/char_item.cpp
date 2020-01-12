//1.) Search: (exist 2 function same, DoRefineWithScroll && DoRefine)
			ITEM_MANAGER::instance().RemoveItem(item, "REMOVE (REFINE SUCCESS)");
//2.) Add bellow:
#ifdef ENABLE_ANNOUNCEMENT_REFINE_SUCCES
//mefunction745
			if (pkNewItem->GetRefineLevel() >= ENABLE_ANNOUNCEMENT_REFINE_SUCCES_MIN_LEVEL) 
			{		
				// ** If the item refined (given) after refining is greater than or equal to 7, then will announce the chat. ** //
				// ** I put it to check whether spam do not appear on all items, and +0,1,2,3,4,5,6 ** //
				char szUpgradeAnnouncement[QUERY_MAX_LEN];
				snprintf(szUpgradeAnnouncement, sizeof(szUpgradeAnnouncement), "<Refine> Player [%s] upgraded item [%s] with succes!", GetName(), pkNewItem->GetName()); 
				BroadcastNotice(szUpgradeAnnouncement);
			}
#endif