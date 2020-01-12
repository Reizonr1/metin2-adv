Search:
LPCHARACTER CHARACTER_MANAGER::CreateCharacter(const char * name, DWORD dwPID)
{
	...
}

Add it under:
#ifdef __OFFLINE_SHOP__
LPCHARACTER CHARACTER_MANAGER::CreateCharacterOffShop(const char * name)
{
	DWORD dwVID = AllocVID();

#ifdef M2_USE_POOL
	LPCHARACTER ch = pool_.Construct();
#else
	LPCHARACTER ch = M2_NEW CHARACTER;
#endif
	ch->Create(name, dwVID, true);

	m_map_pkChrByVID.insert(std::make_pair(dwVID, ch));

	return (ch);
}
#endif

https://puu.sh/sgFkS/3806a0a886.png

---

Search:
LPCHARACTER CHARACTER_MANAGER::SpawnMob(DWORD dwVnum, long lMapIndex, long x, long y, long z, bool bSpawnMotion, int iRot, bool bShow)
{
	...
}

Add it under:

#ifdef __OFFLINE_SHOP__
LPCHARACTER CHARACTER_MANAGER::SpawnOffShop(DWORD dwVnum, const char* szName, long lMapIndex, long x, long y, long z, bool bSpawnMotion, int iRot, bool bShow)
{
	const CMob * pkMob = CMobManager::instance().Get(dwVnum);
	if (!pkMob)
	{
		sys_err("SpawnOffShop: no mob data for vnum %u", dwVnum);
		return NULL;
	}

	if (!(pkMob->m_table.bType == CHAR_TYPE_NPC || pkMob->m_table.bType == CHAR_TYPE_HORSE || pkMob->m_table.bType == CHAR_TYPE_WARP || pkMob->m_table.bType == CHAR_TYPE_GOTO) || mining::IsVeinOfOre(dwVnum))
	{
		LPSECTREE tree = SECTREE_MANAGER::instance().Get(lMapIndex, x, y);

		if (!tree)
		{
			sys_log(1, "SpawnOffShop: no sectree for spawn at %d %d mobvnum %d mapindex %d", x, y, dwVnum, lMapIndex);
			return NULL;
		}

		DWORD dwAttr = tree->GetAttribute(x, y);

		bool is_set = false;

		if (mining::IsVeinOfOre(dwVnum)) is_set = IS_SET(dwAttr, ATTR_BLOCK);
		else is_set = IS_SET(dwAttr, ATTR_BLOCK | ATTR_OBJECT);

		if (is_set)
		{
			// SPAWN_BLOCK_LOG
			static bool s_isLog = quest::CQuestManager::instance().GetEventFlag("spawn_block_log");
			static DWORD s_nextTime = get_global_time() + 10000;

			DWORD curTime = get_global_time();

			if (curTime>s_nextTime)
			{
				s_nextTime = curTime;
				s_isLog = quest::CQuestManager::instance().GetEventFlag("spawn_block_log");

			}

			if (s_isLog)
				sys_log(0, "SpawnOffShop: BLOCKED position for spawn %s %u at %d %d (attr %u)", pkMob->m_table.szName, dwVnum, x, y, dwAttr);
			// END_OF_SPAWN_BLOCK_LOG
			return NULL;
		}

		if (IS_SET(dwAttr, ATTR_BANPK))
		{
			sys_log(0, "SpawnOffShop: BAN_PK position for mob spawn %s %u at %d %d", pkMob->m_table.szName, dwVnum, x, y);
			return NULL;
		}
	}

	LPSECTREE sectree = SECTREE_MANAGER::instance().Get(lMapIndex, x, y);
	if (!sectree)
	{
		sys_log(0, "SpawnOffShop: cannot create monster at non-exist sectree %d x %d (map %d)", x, y, lMapIndex);
		return NULL;
	}

	LPCHARACTER ch = CHARACTER_MANAGER::instance().CreateCharacterOffShop(szName);
	if (!ch)
	{
		sys_log(0, "SpawnOffShop: cannot create new character");
		return NULL;
	}

	if (iRot == -1)
		iRot = number(0, 360);

	ch->SetProto(pkMob);

	// if mob is npc with no empire assigned, assign to empire of map
	if (pkMob->m_table.bType == CHAR_TYPE_NPC)
	if (ch->GetEmpire() == 0)
		ch->SetEmpire(SECTREE_MANAGER::instance().GetEmpireFromMapIndex(lMapIndex));

	ch->SetRotation(iRot);

	if (bShow && !ch->Show(lMapIndex, x, y, z, bSpawnMotion))
	{
		M2_DESTROY_CHARACTER(ch);
		sys_log(0, "SpawnOffShop: cannot show monster");
		return NULL;
	}

	return (ch);
}
#endif

https://puu.sh/sgFmk/9dadd1065f.png
---

Search:
LPCHARACTER CHARACTER_MANAGER::SpawnMobRange(DWORD dwVnum, long lMapIndex, int sx, int sy, int ex, int ey, bool bIsException, bool bSpawnMotion, bool bAggressive )
{
	...
}

Add it under:
#ifdef __OFFLINE_SHOP__
LPCHARACTER CHARACTER_MANAGER::SpawnOffShopRange(DWORD dwVnum, const char* szName, long lMapIndex, int sx, int sy, int ex, int ey, bool bIsException, bool bSpawnMotion, bool bAggressive)
{
	const CMob * pkMob = CMobManager::instance().Get(dwVnum);
	if (!pkMob)
		return NULL;

	if (pkMob->m_table.bType == CHAR_TYPE_STONE)
		bSpawnMotion = true;


	int i = 16;
	while (i--)
	{
		int x = number(sx, ex);
		int y = number(sy, ey);

		LPCHARACTER ch = SpawnOffShop(dwVnum, szName, lMapIndex, x, y, 0, bSpawnMotion);
		if (ch)
		{
			sys_log(1, "OFFSHOP_SPAWN: %s(%d) %dx%d", ch->GetName(), (DWORD)ch->GetVID(), ch->GetX(), ch->GetY());
			if (bAggressive)
				ch->SetAggressive();

			return (ch);
		}
	}
	return NULL;
}
#endif

https://puu.sh/sgFnw/4893c61cc5.png