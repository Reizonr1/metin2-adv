En alta ekle;

void CHARACTER::DelAfk(){
	if (GetShopOwner()) {
		ChatPacket(CHAT_TYPE_INFO, "Pazar acikken bunu yapamazsin");
		return;
	}

	if (GetQuestFlag("auto_afk_system.afk") == 1) {
		SetQuestFlag("auto_afk_system.afk", 0);
		ChatPacket(CHAT_TYPE_COMMAND, "del_afk");
		m_dwLastMoveTime = 0;

		if (IsPolymorphed()) {
			SetPolymorph(0);
			RemoveAffect(AFFECT_POLYMORPH);
		}
	}
}

void CHARACTER::SetAfk(){
	if (GetQuestFlag("auto_afk_system.afk") != 1) {
		SetQuestFlag("auto_afk_system.afk", 1);
		ChatPacket(CHAT_TYPE_COMMAND, "set_afk");
		
		if (!GetShopOwner())
			AddAffect(AFFECT_POLYMORPH, POINT_POLYMORPH, 20036, AFF_POLYMORPH, 60*60*24*365*60, 0, true);
	}
}

bool CHARACTER::IsAfk(){
	DWORD LastMoveTime = GetLastMoveTime();
	int CalcLastMoveSec = (get_dword_time() - LastMoveTime) / 1000 + 0.5; //now - last -> ms to s -> float to int
	int AfkAverageTime = 5 * 60; // 5dk

	if (CalcLastMoveSec > AfkAverageTime)
		return true;
	else
		return false;
}

http://puu.sh/koH3x/7ac75b6eba.png