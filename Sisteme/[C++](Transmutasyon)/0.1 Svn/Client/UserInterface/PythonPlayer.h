// Search for:
		void	PickCloseMoney();

// Add Before:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
		void	SetItemLook(TItemPos Cell, DWORD dwVnum);
		DWORD	GetItemLook(TItemPos Cell);
#endif

// Search for:
		bool	IsEquipItemInSlot(TItemPos iSlotIndex);

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
		void	SetActivedChangeLookSlot(int ChangeLookSlot, int itemPos);
		int		FindActivedChangeLookSlot(int ChangeLookSlot);
		int		FindUsingChangeLookSlot(int ChangeLookSlot);
#endif

// Search for:
	private:
		std::map<DWORD, DWORD> m_kMap_dwAffectIndexToSkillIndex;

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	public:
		signed int				m_ChangeLookRefineActivedSlot[3];
#endif
