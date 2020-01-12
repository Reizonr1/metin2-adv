//Search in this file:
		void					SetVirtualNumber(DWORD dwVirtualNumber);
		void					SetInstanceType(int iInstanceType);
		void					SetAlignment(short sAlignment);

//Add after:

#ifdef NEW_PET_SYSTEM
		void					SetLevelText(int mLevel);
#endif

//Search in this file:

		BOOL					IsForceVisible();
		BOOL					IsInSafe();

//Add after:
#ifdef NEW_PET_SYSTEM
		BOOL					IsNewPet();
#endif
