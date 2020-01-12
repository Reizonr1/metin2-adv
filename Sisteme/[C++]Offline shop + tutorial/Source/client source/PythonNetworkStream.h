Arat ;
		bool SendShopSellPacketNew(BYTE bySlot, BYTE byCount);

Altına Ekle ;
		// Offline Shop
		bool SendOfflineShopEndPacket();
		bool SendOfflineShopBuyPacket(BYTE byCount);
		bool SendChangeOfflineShopTime(BYTE bTime);
		bool SendChangePriceOfflineShopItem(BYTE bPos, int iPrice);
		bool SendAddOfflineShopItem(BYTE bDisplayPos, BYTE bPos, long lPrice);
		bool SendRemoveOfflineShopItem(BYTE bPos);
		bool SendDestroyOfflineShop();
		bool SendRefreshOfflineShop();
		bool SendRefreshOfflineShopMoney();
		bool SendOfflineShopWithdrawMoney(DWORD dwMoney);

		
		
		
		
Arat ;
		// Private Shop
		bool SendBuildPrivateShopPacket(const char * c_szName, const std::vector<TShopItemTable> & c_rSellingItemStock);

Altına Ekle ;
		// Offline Shop
		bool SendBuildOfflineShopPacket(const char * c_szName, const std::vector<TShopItemTable> & c_rSellingItemStock, BYTE bTime);

		
		
		
		
Arat ;
		bool RecvExchangePacket();

Altına Ekle ;
		bool RecvOfflineShopPacket();
		bool RecvOfflineShopSignPacket();
