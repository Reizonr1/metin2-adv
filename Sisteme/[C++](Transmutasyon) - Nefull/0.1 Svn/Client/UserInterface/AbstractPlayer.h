// Search for:
		virtual DWORD	GetItemIndex(TItemPos itemPos) = 0;

// Add Before:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
		virtual void	SetItemLook(TItemPos itemPos, DWORD dwVnum) = 0;
		virtual DWORD	GetItemLook(TItemPos itemPos) = 0;
#endif
