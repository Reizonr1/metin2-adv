//Search in this file:
//In CPythonNetworkStream::RecvCharacterUpdatePacket()
	kNetUpdateActorData.m_kAffectFlags.CopyData(0, sizeof(chrUpdatePacket.dwAffectFlag[0]), &chrUpdatePacket.dwAffectFlag[0]);
	kNetUpdateActorData.m_kAffectFlags.CopyData(32, sizeof(chrUpdatePacket.dwAffectFlag[1]), &chrUpdatePacket.dwAffectFlag[1]);
	kNetUpdateActorData.m_sAlignment=chrUpdatePacket.sAlignment;

//Add after:
#ifdef NEW_PET_SYSTEM
	kNetUpdateActorData.m_dwLevel=chrUpdatePacket.dwLevel;
#endif