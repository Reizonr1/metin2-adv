// 1) Search:
	LPCHARACTER		pCubeNpc;
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	LPITEM	pClMaterials[CL_WINDOW_MAX_MATERIALS];
#endif


// 1) Search:
};

ESex GET_SEX(LPCHARACTER ch);
// 2) Replace with:
#ifdef __CHANGELOOK_SYSTEM__
	protected:
		bool	m_bChangeLook;
	
	public:
		bool	isChangeLookOpened() {return m_bChangeLook;}
		void	ChangeLookWindow(bool bOpen = false, bool bRequest = false);
		void	ClearClWindowMaterials();
		LPITEM*	GetClWindowMaterials() {return m_pointsInstant.pClMaterials;}
		BYTE	CheckClEmptyMaterialSlot();
		void	AddClMaterial(TItemPos tPos, BYTE bPos);
		void	RemoveClMaterial(BYTE bPos);
		void	RefineClMaterials();
		bool	CleanTransmutation(LPITEM pkItem, LPITEM pkTarget);
#endif
};

ESex GET_SEX(LPCHARACTER ch);