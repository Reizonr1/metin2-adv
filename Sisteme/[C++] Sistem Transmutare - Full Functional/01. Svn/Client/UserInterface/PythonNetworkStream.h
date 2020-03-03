// 1) Search:
		void __TEST_SetSkillGroupFake(int iIndex);
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		bool	SendClClosePacket();
		bool	SendClAddPacket(TItemPos tPos, BYTE bPos);
		bool	SendClRemovePacket(BYTE bPos);
		bool	SendClRefinePacket();
#endif


// 1) Search:
		bool	RecvChannelPacket();
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
		bool	RecvChangeLookPacket();
#endif