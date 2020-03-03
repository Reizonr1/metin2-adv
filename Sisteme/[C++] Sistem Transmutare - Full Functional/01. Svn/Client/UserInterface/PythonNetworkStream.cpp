// 1) Search:
			Set(HEADER_GC_DRAGON_SOUL_REFINE,		CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCDragonSoulRefine), STATIC_SIZE_PACKET));
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
			Set(HEADER_GC_CL, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketChangeLook), STATIC_SIZE_PACKET));
#endif