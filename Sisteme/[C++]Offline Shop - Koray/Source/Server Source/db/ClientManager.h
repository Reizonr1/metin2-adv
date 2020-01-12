Search:
	bool		InitializeShopTable();

Add it under:
#ifdef __OFFLINE_SHOP__
	bool		InitializeOfflineShopTable();
#endif

http://i.imgur.com/e4f5D0e.png

---

Search:
	void		QUERY_SAFEBOX_CHANGE_PASSWORD(CPeer * pkPeer, DWORD dwHandle, TSafeboxChangePasswordPacket * p);

Add it under:
#ifdef __OFFLINE_SHOP__
	void		QUERY_COLLECT_OFFLINE_SHOP_ITEM(CPeer * pkPeer, DWORD dwHandle, DWORD pid);
#endif

http://i.imgur.com/nNT88Ht.png

---

Search:
	int					m_iShopTableSize;
	TShopTable *		m_pShopTable;

Add it under:
#ifdef __OFFLINE_SHOP__
	int					m_iOfflineShopTableSize;
	TOfflineShopTable *	m_pOfflineShopTable;
#endif

http://i.imgur.com/zOyzyCe.png

---

Search:
	void RequestChannelStatus(CPeer* peer, DWORD dwHandle);

Add it under:
#ifdef __OFFLINE_SHOP__
	void SafeboxMoney(TSafeboxMoney* pData);
	void PrivateShopEntry(TOfflineShopTable* pData);
	void PrivateShopRemove(TOfflineShopTable* pData);
#endif

http://i.imgur.com/V6Ja2m7.png

