// Search for:
			Set(HEADER_GC_TARGET,		CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCTarget), STATIC_SIZE_PACKET));

// Add (Under):
#ifdef ENABLE_SEND_TARGET_INFO
			Set(HEADER_GC_TARGET_INFO,	CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCTargetInfo), STATIC_SIZE_PACKET));
#endif
