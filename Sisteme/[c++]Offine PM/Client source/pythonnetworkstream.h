Search:
		bool SendWhisperPacket(const char * name, const char * c_szChat);

Add it under:
#ifdef OFFLINE_MESSAGE
		bool SendOfflineMessagePacket(const char* szTargetName, const char* szText);
#endif
