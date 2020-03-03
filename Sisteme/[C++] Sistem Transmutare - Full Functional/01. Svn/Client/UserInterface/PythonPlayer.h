// 1) Search:
		void	SetItemCount(TItemPos Cell, BYTE byCount);
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		void	SetItemTransmutation(TItemPos itemPos, DWORD dwVnum);
		DWORD	GetItemTransmutation(TItemPos itemPos);
#endif