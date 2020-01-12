//Search in this file:
	protected:
		void		Attack(LPCHARACTER ch, const BYTE header, const char* data);

		int			Whisper(LPCHARACTER ch, const char * data, size_t uiBytes);

//Add after:

#ifdef NEW_PET_SYSTEM
		void		BraveRequestPetName(LPCHARACTER ch, const char* c_pData);
#endif

