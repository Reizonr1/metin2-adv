[..]

//find void BuildPrivateShop and replace with this
#ifndef ENABLE_OFFLINE_SHOP
		void BuildPrivateShop(const char * c_szName);
#else
		void BuildPrivateShop(const char * c_szName, DWORD days);
#endif
#ifdef ENABLE_FULL_YANG
		void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice);
		long long GetPrivateShopItemPrice(TItemPos ItemPos);
#else
		void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice);
		int GetPrivateShopItemPrice(TItemPos ItemPos);
#endif
[..]