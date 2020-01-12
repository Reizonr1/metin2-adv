Search:
		void		Warp(LPCHARACTER ch, const char * pcData);

Add it under:
#ifdef __OFFLINE_SHOP__
		void		SafeboxMoney(LPCHARACTER ch, const char * data);
#endif

https://puu.sh/sgGxV/24db1d5461.png
---

Search:
	void		ItemAward(const char * c_pData);

Add it under:
#ifdef __OFFLINE_SHOP__
	void		CollectOfflineShopItem(LPDESC d, const char * c_pData);
#endif

https://puu.sh/sgGyL/c94eb40765.png
---

Search:
	void		RespondChannelStatus(LPDESC desc, const char* pcData);

Add it under:
#ifdef __OFFLINE_SHOP__
	void		SafeboxMoney(TSafeboxMoney* pcData);
#endif

https://puu.sh/sgGzL/58ab8c4dd2.png