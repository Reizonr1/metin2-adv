Search:
		void			SendGreetMessage();

Add it under:
#ifdef OFFLINE_MESSAGE
		void			SaveOfflineMessage(const char* szMsg, DWORD dwTargetPID);
		void			ClearOfflineMessageBox(DWORD dwTargetPID);
		void			ReadOfflineMessageBox();
#endif
