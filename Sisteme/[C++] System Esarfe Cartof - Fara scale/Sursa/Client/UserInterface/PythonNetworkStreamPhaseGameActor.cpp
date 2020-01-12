// 1) Search: kNetActorData.m_dwHair = 0;
// 2) After make a new line and paste:
	kNetActorData.m_dwAcce = 0;

// 1) Search: kNetActorData.m_dwHair = chrInfoPacket.awPart[CHR_EQUIPPART_HAIR];
// 2) After make a new line and paste:
		kNetActorData.m_dwAcce = chrInfoPacket.awPart[CHR_EQUIPPART_ACCE];

// 1) Search: kNetActorData.m_dwHair = chrAddPacket.awPart[CHR_EQUIPPART_HAIR];
// 2) After make a new line and paste:
	kNetActorData.m_dwAcce = chrAddPacket.awPart[CHR_EQUIPPART_ACCE];

// 1) Search: kNetUpdateActorData.m_dwHair = chrUpdatePacket.awPart[CHR_EQUIPPART_HAIR];
// 2) After make a new line and paste:
	kNetUpdateActorData.m_dwAcce = chrUpdatePacket.awPart[CHR_EQUIPPART_ACCE];

// 1) Search: kNetUpdateActorData.m_dwHair = chrUpdatePacket.awPart[CHR_EQUIPPART_HAIR];
// 2) After make a new line and paste:
	kNetUpdateActorData.m_dwAcce = chrUpdatePacket.awPart[CHR_EQUIPPART_ACCE];