// Cauta
	int	CQuestManager::GetEventFlag(const string& name)
	{
		map<string,int>::iterator it = m_mapEventFlag.find(name);

		if (it == m_mapEventFlag.end())
			return 0;

		return it->second;
	}

// Adauga
#ifdef ENABLE_BOSS_TRACKING
	void CQuestManager::RequestSetEventFlagBR(const string& name1, const string& name2, int value)
	{
		const string& name = name1 + name2;
		TPacketSetEventFlag p;
		strlcpy(p.szFlagName, name.c_str(), sizeof(p.szFlagName));
		p.lValue = value;
		db_clientdesc->DBPacket(HEADER_GD_SET_EVENT_FLAG, 0, &p, sizeof(TPacketSetEventFlag));
	}

	int	CQuestManager::GetEventFlagBR(const string& name1, const string& name2)
	{
		const string& name = name1 + name2;
		map<string, int>::iterator it = m_mapEventFlag.find(name);

		if (it == m_mapEventFlag.end())
			return 0;

		return it->second;
	}
#endif