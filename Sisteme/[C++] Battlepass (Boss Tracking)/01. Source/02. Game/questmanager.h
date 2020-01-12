// Cauta
			void		SetEventFlag(const string& name, int value);
			int			GetEventFlag(const string& name);
			void		BroadcastEventFlagOnLogin(LPCHARACTER ch);

// Adauga
#ifdef ENABLE_BOSS_TRACKING
			int			GetEventFlagBR(const string& name1, const string& name2);
			void		RequestSetEventFlagBR(const string& name1, const string& name2, int value);
#endif