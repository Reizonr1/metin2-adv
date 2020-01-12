//1.0 suchen:
			short	m_sAlignment;
//1.0 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
			short	m_sVip;
#endif	

//1.1 suchen:
			AFFECT_NUM = 64,
//1.1 davor:	
#ifdef ENABLE_VIP_SYSTEM		
			AFFECT_VIP=46,                     //46
#endif			

//1.2 suchen:
		void					SetAlignment(short sAlignment);
//1.2 dahinter:
#ifdef ENABLE_VIP_SYSTEM
		void					SetVip(short sVip);
#endif	
	
//1.3 suchen:	
		int						GetAlignment();
		UINT					GetAlignmentGrade();
		int						GetAlignmentType();
//1.3 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
		int						GetVip();
#endif	

//1.4 suchen:
		short					m_sAlignment;
//1.4 dahinter:	
#ifdef ENABLE_VIP_SYSTEM
		short					m_sVip;
#endif	
