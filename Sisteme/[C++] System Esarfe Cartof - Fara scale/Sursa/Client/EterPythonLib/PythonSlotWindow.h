// 1) Search: BOOL	bActive;
// 2) Make a new line and paste:
				BOOL	bAcceActive;

// 1) Search: void DeactivateSlot(DWORD dwIndex);
// 2) Make a new line and paste:
			void ActivateAcceSlot(DWORD dwIndex);
			void DeactivateAcceSlot(DWORD dwIndex);

// 1) Search: void __DestroySlotEnableEffect();
// 2) Make a new line and paste:
			void __CreateAcceSlotEnableEffect();
			void __DestroySlotAcceEnableEffect();

// 1) Search: CAniImageBox * m_pSlotActiveEffect;
// 2) Make a new line and paste:
			CAniImageBox * m_pSlotAcceActiveEffect;