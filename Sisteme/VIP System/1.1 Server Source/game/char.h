//1.0 suchen:		
		void			FlushDelayedSaveItem();	
//1.0 dahinter:		
		void			RefreshVip();	

//1.1 suchen:
		int					GetAlignment() const;
//1.1 dahinter:		
#ifdef ENABLE_VIP_SYSTEM
		int					GetVip() const;
		int					GetRealVip() const;
		void				ResetVip();
		void				SetVip(int VIP_LEVEL);
		void				ShowVip(bool bShow);
#endif		

//1.2 suchen:
		int					m_iAlignment;		
		int					m_iRealAlignment;
//1.2 dahinter:
#ifdef ENABLE_VIP_SYSTEM
		int					m_iVip;	
		int					m_iRealVip;
#endif		
