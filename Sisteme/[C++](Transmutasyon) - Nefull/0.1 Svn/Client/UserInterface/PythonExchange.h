// Search for:
			TPlayerItemAttribute	item_attr[EXCHANGE_ITEM_MAX_NUM][ITEM_ATTRIBUTE_SLOT_MAX_NUM];

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
			DWORD					item_look[EXCHANGE_ITEM_MAX_NUM];
#endif

// Search for:
		void			SetItemToTarget(DWORD pos, DWORD vnum, BYTE count);
		void			SetItemToSelf(DWORD pos, DWORD vnum, BYTE count);

// Replace their function with:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
		DWORD			GetItemLookVnumFromTarget(BYTE pos);
		DWORD			GetItemLookVnumFromSelf(BYTE pos);

		void			SetItemToTarget(DWORD pos, DWORD vnum, BYTE count, DWORD dwLookVnum);
		void			SetItemToSelf(DWORD pos, DWORD vnum, BYTE count, DWORD dwLookVnum);
#else
		void			SetItemToTarget(DWORD pos, DWORD vnum, BYTE count);
		void			SetItemToSelf(DWORD pos, DWORD vnum, BYTE count);
#endif
