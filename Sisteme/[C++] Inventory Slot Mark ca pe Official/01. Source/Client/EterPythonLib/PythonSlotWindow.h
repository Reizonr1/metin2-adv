// 1. Extend the ESlotState enum with these:
// ********************************* BEGIN ********************************* //
#ifdef WJ_ENABLE_TRADABLE_ICON
		SLOT_STATE_CANT_MOUSE_EVENT		= (1 << 4),
		SLOT_STATE_UNUSABLE				= (1 << 5),
#endif
// ********************************** END ********************************** //

// 2.1 Search this:
// ********************************* BEGIN ********************************* //
			BOOL IsEnableSlot(DWORD dwIndex);
// ********************************** END ********************************** //

// 2.2 Add this under:
// ********************************* BEGIN ********************************* //
#ifdef WJ_ENABLE_TRADABLE_ICON
			void SetCanMouseEventSlot(DWORD dwIndex);
			void SetCantMouseEventSlot(DWORD dwIndex);
			void SetUsableSlotOnTopWnd(DWORD dwIndex);
			void SetUnusableSlotOnTopWnd(DWORD dwIndex);
#endif
// ********************************** END ********************************** //
