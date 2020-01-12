[..]

//find and replace this define
		#ifdef ENABLE_OFFLINE_SHOP
		bool SendBuildPrivateShopPacket(const char * c_szName, const std::vector<TShopItemTable> & c_rSellingItemStock,DWORD days);
		#else
		bool SendBuildPrivateShopPacket(const char * c_szName, const std::vector<TShopItemTable> & c_rSellingItemStock);
		#endif

[..]