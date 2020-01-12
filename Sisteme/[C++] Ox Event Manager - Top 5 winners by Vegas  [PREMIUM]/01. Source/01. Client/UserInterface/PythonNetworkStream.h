//1.) Search:
		bool SendChatPacket(const char * c_szChat, BYTE byType = CHAT_TYPE_TALKING);
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
		bool SendOxEventManagerPacket(int type, const char* c_szPassword, int vnum, int count);
#endif

//1.) Search:
		bool __RecvChangeName();
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
		bool RecvOxEventPacket();
#endif