// 1) Search:
				CAniImageBox *	pFinishCoolTimeEffect;
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
				CAniImageBox*	pActiveSlotEffect[3];
#endif


// 1) Search:
			void	ReserveDestroyCoolTimeFinishEffect(DWORD dwSlotIndex);
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
			void	ActivateEffect(DWORD dwSlotIndex, float r, float g, float b, float a);
			void	DeactivateEffect(DWORD dwSlotIndex);
#endif