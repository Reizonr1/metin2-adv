*pvp.cpp

Find - Bul:
	// NOTIFY_PVP_MESSAGE
	LPDESC pkVictimDesc = pkVictim->GetDesc();
	if (pkVictimDesc)
	{
		TPacketGCWhisper pack;

		int len = MIN(CHAT_MAX_LEN, strlen(msg) + 1);

		pack.bHeader = HEADER_GC_WHISPER;
		pack.wSize = sizeof(TPacketGCWhisper) + len;
		pack.bType = WHISPER_TYPE_SYSTEM;
		strlcpy(pack.szNameFrom, pkChr->GetName(), sizeof(pack.szNameFrom));

		TEMP_BUFFER buf;

		buf.write(&pack, sizeof(TPacketGCWhisper));
		buf.write(msg, len);

		pkVictimDesc->Packet(buf.read_peek(), buf.size());
	}
	// END_OF_NOTIFY_PVP_MESSAGE

Change - Değiştir:
	// NOTIFY_PVP_GUI
	LPDESC pkVictimDesc = pkVictim->GetDesc();
	if (pkVictimDesc) {
		const char* pkVictimName = pkChr->GetName();
		int pkVictimLevel = pkChr->GetLevel();
		int pkVictimVID = pkChr->GetVID();
		DWORD pkVictimRace = pkChr->GetRaceNum();

		if ((!pkVictimName) || (pkVictimLevel < 0 || pkVictimLevel > 200) || (pkVictimVID < 0) || (pkVictimRace < 0 || pkVictimRace > 8)) {
			sys_err("Duel system unknown error: Name: %s Level: %d VID: %d Race: %d", pkVictimName, pkVictimLevel, pkVictimVID, pkVictimRace);
			return;
		}

		pkVictim->ChatPacket(CHAT_TYPE_COMMAND, "pvpchallenge %s %d %d %d", pkVictimName, pkVictimLevel, pkVictimVID, pkVictimRace);
	}
	// END_OF_NOTIFY_PVP_GUI



Find - Bul:
bool CPVPManager::Dead(LPCHARACTER pkChr, DWORD dwKillerPID)

Add it upper - Üstüne ekle:
void CPVPManager::Reject(LPCHARACTER pkChr, LPCHARACTER pkChr2)
{
	CPVPSetMap::iterator it = m_map_pkPVPSetByID.find(pkChr->GetPlayerID());

	if (it == m_map_pkPVPSetByID.end())
		return;

	TR1_NS::unordered_set<CPVP*>::iterator it2 = it->second.begin();

	while (it2 != it->second.end())
	{
		CPVP * pkPVP = *it2++;

		DWORD dwCompanionPID;

		if (pkPVP->m_players[0].dwPID == pkChr->GetPlayerID())
			dwCompanionPID = pkPVP->m_players[1].dwPID;
		else
			dwCompanionPID = pkPVP->m_players[0].dwPID;

		if (dwCompanionPID == pkChr2->GetPlayerID())
		{
			if (pkPVP->IsFight()) {
				pkChr->ChatPacket(CHAT_TYPE_INFO, "Duellodayken bunu yapamazsin"); //you can not use this in duel
				return;
			}

			pkPVP->Packet(true);
			Delete(pkPVP);

			pkChr2->ChatPacket(CHAT_TYPE_INFO, "%s Duello teklifini reddetti", pkChr->GetName()); // %s is rejected your duel
		}
	}
}
