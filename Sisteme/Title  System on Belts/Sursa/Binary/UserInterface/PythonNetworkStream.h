// 1) Search: bool SendSpecial(int nLen, void * pvBuf);
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		bool SendChangeTitle(int iTitle);
#endif


// 1) Search: bool RecvObserverAddPacket();
// 2) Before this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
		bool RecvTitleInformationPacket();
#endif