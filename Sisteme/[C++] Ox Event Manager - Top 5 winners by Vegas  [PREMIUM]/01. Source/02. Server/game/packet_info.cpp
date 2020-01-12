//1.) Search:
    Set(HEADER_CG_CHAT, sizeof(TPacketCGChat), "Chat", true);
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
	Set(HEADER_CG_OXEVENT_MANAGER, sizeof(TPacketCGOxEventManager), "TPacketCGOxEventManager", true);
#endif