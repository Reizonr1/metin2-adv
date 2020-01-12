Search:
		CSafebox(LPCHARACTER pkChrOwner, int iSize, DWORD dwGold);

Change:
#ifdef __OFFLINE_SHOP__
		CSafebox(LPCHARACTER pkChrOwner, int iSize, uint64_t dwGold);
#else
		CSafebox(LPCHARACTER pkChrOwner, int iSize, DWORD dwGold);
#endif

https://puu.sh/sgHEx/b4c00bfe25.png

---

Search:
		void		SetWindowMode(BYTE bWindowMode);

Add it under:
#ifdef __OFFLINE_SHOP__
		void		SetGold(int64_t llGold);
		uint64_t	GetGold() { return  m_lGold; };
#endif

https://puu.sh/sgHHh/d1a20ae2b0.png

---

Search:
		long		m_lGold;

Change:
#ifdef __OFFLINE_SHOP__
		uint64_t	m_lGold;
#else
		long		m_lGold;
#endif

https://puu.sh/sgHIw/ef55c28dc1.png