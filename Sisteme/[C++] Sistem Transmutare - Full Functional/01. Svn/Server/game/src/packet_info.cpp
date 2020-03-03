// 1) Search:
	Set(HEADER_CG_STATE_CHECKER, sizeof(BYTE), "ServerStateCheck", false);
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	Set(HEADER_CG_CL, sizeof(TPacketChangeLook), "ChangeLook", true);
#endif