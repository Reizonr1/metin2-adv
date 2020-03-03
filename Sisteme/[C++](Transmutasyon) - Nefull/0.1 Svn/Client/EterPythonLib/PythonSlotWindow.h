// Define:
#define ENABLE_CHANGE_LOOK_SYSTEM

// Search for:
				BOOL	bActive;

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
				BOOL	bChangeLookActive;
				BOOL	bSlotCoverImage;
#endif

// Search for:
			void SetSlotCoolTime(DWORD dwIndex, float fCoolTime, float fElapsedTime = 0.0f);

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
			void EnableSlotCoverImage(DWORD dwIndex);
			void DisableSlotCoverImage(DWORD dwIndex);
#endif

// Search for:
			void DeactivateSlot(DWORD dwIndex);

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
			void ActivateChangeLookSlot(DWORD dwIndex);
			void DeactivateChangeLookSlot(DWORD dwIndex);
#endif

// Search for:
			void __CreateSlotEnableEffect();

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
			void __CreateSlotChangeLookEnableEffect();
			void __CreateSlotCoverImage();
#endif

// Search for:
			void __DestroySlotEnableEffect();

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
			void __DestroySlotChangeLookEnableEffect();
			void __DestroySlotCoverImage();
#endif

// Search for:
			CAniImageBox * m_pSlotActiveEffect;

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
			CAniImageBox * m_pSlotChangeLookActiveEffect[3];
			CAniImageBox * m_pSlotCoverImage;
#endif
