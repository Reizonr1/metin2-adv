// 1) Search: Set(HEADER_GC_DRAGON_SOUL_REFINE,		CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCDragonSoulRefine), STATIC_SIZE_PACKET));
// 2) After this make a new line and paste:
#ifdef ENABLE_TITLE_SYSTEM
			Set(HEADER_GG_TITLE_ANSWER, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGGTitleInfo), STATIC_SIZE_PACKET));
#endif