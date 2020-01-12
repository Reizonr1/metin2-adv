Search:
	typedef std::map<DWORD, CShop *> TShopMap;

Add it under:
#ifdef __OFFLINE_SHOP__
	typedef std::map< DWORD, std::vector<DWORD> > TOfflineShopMap; // PID - VID Container
#endif

https://puu.sh/sgJra/2fa2ac8f9d.png

---

Search:
	bool	Initialize(TShopTable * table, int size);

Add it under:
#ifdef __OFFLINE_SHOP__
	bool	Initialize(TOfflineShopTable * table, int size);
#endif

https://puu.sh/sgJs7/afa3201e07.png

---

Search:
	void	Destroy();

Add it under:
#ifdef __OFFLINE_SHOP__
	void	GetOfflineShops(DWORD dwPID);
	void	GotoOfflineShop(DWORD dwPID, DWORD dwVID);
	void	WarpOfflineShop(DWORD dwPID, DWORD dwVID);
	void	CloseOfflineShop(DWORD dwPID, DWORD dwVID);
#endif

https://puu.sh/sgJts/3aadbdef79.png

---

Search:
	LPSHOP	CreatePCShop(LPCHARACTER ch, TShopItemTable * pTable, BYTE bItemCount);

Add it under:
#ifdef __OFFLINE_SHOP__
	LPSHOP	CreateOfflineShop(LPCHARACTER ch, BYTE bSize, BYTE bColor, TShopItemTable * pTable, BYTE bItemCount);
	DWORD	GetOfflineShopCount(DWORD dwPID) { return m_map_pkOfflineShop[dwPID].size(); }
	DWORD	GetOfflineShopCount() { return m_map_pkOfflineShop.size(); }
#endif

https://puu.sh/sgJuY/641f3b3d6d.png

---

Search:
	TShopMap	m_map_pkShopByPC;

Add it under:
#ifdef __OFFLINE_SHOP__
	TOfflineShopMap	m_map_pkOfflineShop;
#endif

https://puu.sh/sgJvX/1d62b17d75.png
