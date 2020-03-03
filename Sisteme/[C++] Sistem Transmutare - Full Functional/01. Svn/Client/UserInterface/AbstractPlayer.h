// 1) Search:
		virtual void	SetItemCount(TItemPos itemPos, BYTE byCount) = 0;
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		virtual void	SetItemTransmutation(TItemPos itemPos, DWORD dwVnum) = 0;
		virtual DWORD	GetItemTransmutation(TItemPos itemPos) = 0;
#endif