// Search for:
		int			GetLevelLimit();

// Add Before:
#ifdef __CHANGE_LOOK_SYSTEM__
		void	SetItemLook(DWORD look);
		DWORD	GetItemLook()		{ return m_dwLook; }
#ifdef __QUIVER_SYSTEM__
		bool	IsWeapon()		{ return m_pProto ? m_pProto->bType == ITEM_WEAPON && m_pProto->bSubType != WEAPON_ARROW  && m_pProto->bSubType != WEAPON_QUIVER : false; }
#else
		bool	IsWeapon()		{ return m_pProto ? m_pProto->bType == ITEM_WEAPON && m_pProto->bSubType != WEAPON_ARROW : false; }
#endif
		bool	IsArmor()		{ return m_pProto ? m_pProto->bType == ITEM_ARMOR && m_pProto->bSubType == ARMOR_BODY : false;}
#endif

// Search for:
		DWORD		m_dwSIGVnum;

// Add Under:
#ifdef __CHANGE_LOOK_SYSTEM__
		DWORD		m_dwLook;
#endif
