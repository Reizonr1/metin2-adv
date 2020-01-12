Search:
	Set(HEADER_CG_WHISPER, sizeof(TPacketCGWhisper), "Whisper", true);

Add it under:
#ifdef OFFLINE_MESSAGE
	Set(HEADER_CG_OFFLINE_WHISPER, sizeof(TPacketCGOfflineMessage), "OfflineWhisper", true);
#endif
