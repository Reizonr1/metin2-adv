//1.) Search for:
		bool				CanFight() const;
//2.) Add after:
#ifdef WJ_SHOW_STROKE_INFO
		bool				GetStrokeByVid(DWORD dwTargetVID, DWORD * iAmount);
		void				RegisterStroke(DWORD dwTargetVID);
#endif

//1.) Search for:
		EventMap		m_PartyInviteEventMap;
//2.) Add after:
#ifdef WJ_SHOW_STROKE_INFO
		std::map<DWORD, DWORD>	m_CharacterStrokeInfo;
#endif