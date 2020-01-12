//1.) Search for:
		if (pAttacker)
			SendDamagePacket(pAttacker, dam, damageFlag);
//2.) Delete and replace with:
#ifdef WJ_SHOW_STROKE_INFO
		if (pAttacker)
		{
			SendDamagePacket(pAttacker, dam, damageFlag);

			if (IsRaceInfo(GetRaceNum()))
				pAttacker->RegisterStroke((DWORD) GetVID());
		}
#else
		if (pAttacker)
			SendDamagePacket(pAttacker, dam, damageFlag);
#endif

//1.) Search for:
bool CHARACTER::CanFight() const
{
	return m_pointsInstant.position >= POS_FIGHTING ? true : false;
}
//2.) Add after:
#ifdef WJ_SHOW_STROKE_INFO
bool IsRaceInfo(DWORD raceIndex) // Custom list
{
	switch (raceIndex)
	{
		case 691:
		case 1191:
		case 2492:
		case 2493:
		case 1095:
			return true;
	}
	return false;
}

bool CHARACTER::GetStrokeByVid(DWORD dwTargetVID, DWORD * iAmount)
{
	itertype(m_CharacterStrokeInfo) it = m_CharacterStrokeInfo.find(dwTargetVID);

	if (it == m_CharacterStrokeInfo.end())
		return false;

	*iAmount = it->second;
}

void CHARACTER::RegisterStroke(DWORD dwTargetVID)
{
	DWORD iCount = 0;
	DWORD iTotalAmount = 0;

	if (!GetStrokeByVid(dwTargetVID, &iCount))
	{
		m_CharacterStrokeInfo.insert(std::make_pair(dwTargetVID, 1));
	}

	iTotalAmount = iCount += 1;
	m_CharacterStrokeInfo[dwTargetVID] = iTotalAmount;
	ChatPacket(CHAT_TYPE_COMMAND, "RegisterStroke %d %d", dwTargetVID, iTotalAmount);	
}
#endif