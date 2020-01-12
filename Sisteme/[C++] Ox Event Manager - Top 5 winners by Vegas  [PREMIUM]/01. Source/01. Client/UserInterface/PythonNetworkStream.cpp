//1.) Search:
			Set(HEADER_GC_CHANGE_SPEED,	CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCChangeSpeed), STATIC_SIZE_PACKET));
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
			Set(HEADER_GC_OXEVENT, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketCGOxEvent), STATIC_SIZE_PACKET));
#endif