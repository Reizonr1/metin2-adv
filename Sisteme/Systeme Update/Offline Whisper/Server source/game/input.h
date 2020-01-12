Search:
		int			Chat(LPCHARACTER ch, const char * data, size_t uiBytes);

Add it under:
#ifdef OFFLINE_MESSAGE
		void		OfflineWhisper(LPCHARACTER ch, const char * data);
#endif
