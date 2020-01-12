Search:
		LPCHARACTER             CreateCharacter(const char * name, DWORD dwPID = 0);

Add it under:
#ifdef __OFFLINE_SHOP__
		LPCHARACTER             CreateCharacterOffShop(const char * name);
#endif

https://puu.sh/sgFph/22c9d4e6bc.png
---

Search:
		LPCHARACTER		SpawnMob(DWORD dwVnum, long lMapIndex, long x, long y, long z, bool bSpawnMotion = false, int iRot = -1, bool bShow = true);

Add it under:
#ifdef __OFFLINE_SHOP__
		LPCHARACTER		SpawnOffShop(DWORD dwVnum, const char* szName, long lMapIndex, long x, long y, long z, bool bSpawnMotion = false, int iRot = -1, bool bShow = true);
#endif

https://puu.sh/sgFq5/c98b68c775.png
---

Search:
		LPCHARACTER		SpawnMobRange(DWORD dwVnum, long lMapIndex, int sx, int sy, int ex, int ey, bool bIsException = false, bool bSpawnMotion = false, bool bAggressive = false);

Add it under:
#ifdef __OFFLINE_SHOP__
		LPCHARACTER		SpawnOffShopRange(DWORD dwVnum, const char* szName, long lMapIndex, int sx, int sy, int ex, int ey, bool bIsException = false, bool bSpawnMotion = false, bool bAggressive = false);
#endif

https://puu.sh/sgFqU/db1bdfe5b2.png