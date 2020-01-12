Search:
		void SetTabName(BYTE tabIdx, const char* name);
		const char* GetTabName(BYTE tabIdx);

Add it under:
#ifdef __OFFLINE_SHOP__
		void SetMoney(uint64_t llMoney) { m_llMoney = llMoney; };
		uint64_t GetMoney() { return m_llMoney; };
#endif

https://puu.sh/sgMoQ/83bdc6a6f3.png

---

Search:
		void AddPrivateShopItemStock(TItemPos ItemPos, BYTE byDisplayPos, DWORD dwPrice);

Change:
#ifdef __OFFLINE_SHOP__
		void AddPrivateShopItemStock(TItemPos ItemPos, BYTE byDisplayPos, DWORD dwPrice, DWORD dwPrice2, DWORD dwPrice3, DWORD dwPrice4);
#else
		void AddPrivateShopItemStock(TItemPos ItemPos, BYTE byDisplayPos, DWORD dwPrice);
#endif

https://puu.sh/sgMqk/01f9d2d5d8.png

---

Search:
		int GetPrivateShopItemPrice(TItemPos ItemPos);
		void BuildPrivateShop(const char * c_szName);

Change:
		int GetPrivateShopItemPrice(TItemPos ItemPos);
#ifdef __OFFLINE_SHOP__
		int GetPrivateShopItemPrice2(TItemPos ItemPos);
		int GetPrivateShopItemPrice3(TItemPos ItemPos);
		int GetPrivateShopItemPrice4(TItemPos ItemPos);

		void BuildPrivateShop(const char * c_szName, BYTE bType, BYTE bSize, BYTE bColor);
#else
		void BuildPrivateShop(const char * c_szName);
#endif

https://puu.sh/sgMs6/507c37c668.png

---

Search:
		ShopTab m_aShoptabs[SHOP_TAB_COUNT_MAX];

Add it under:
#ifdef __OFFLINE_SHOP__
		uint64_t m_llMoney;
#endif

https://puu.sh/sgMti/f7a353f04d.png




