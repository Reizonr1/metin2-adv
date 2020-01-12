Find - Bul:
		int					m_iMaxAggro;
		// End of Battle

Add it under- Altına ekle:
		LPEVENT				m_pkShopDurationEvent;
		int					m_dwShopDuration;
		bool				m_bShopDurationIsActive;
	public:
		int					GetShopDuration();
		void				SetShopDuration(){ m_dwShopDuration = get_dword_time(); };
		void				CheckShopDuration(int time);

		void				StartShopDurationEvent();
		void				CancelShopDuration();

		void				StartShopDuration(){ m_bShopDurationIsActive = 1; }
		void				EndShopDuration(){ m_bShopDurationIsActive = 0; }

