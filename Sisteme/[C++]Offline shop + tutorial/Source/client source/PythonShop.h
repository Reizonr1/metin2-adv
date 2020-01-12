Arat ;
		void SetItemData(BYTE tabIdx, DWORD dwSlotPos, const TShopItemData & c_rShopItemData);
		BOOL GetItemData(BYTE tabIdx, DWORD dwSlotPos, const TShopItemData ** c_ppItemData);

		
Altına Ekle ;
		void SetOfflineShopItemData(DWORD dwIndex, const TShopItemData & c_rShopItemData);
		BOOL GetOfflineShopItemData(DWORD dwIndex, const TShopItemData ** c_ppItemData);

		void SetOfflineShopItemData(BYTE tabIdx, DWORD dwSlotPos, const TShopItemData & c_rShopItemData);
		BOOL GetOfflineShopItemData(BYTE tabIdx, DWORD dwSlotPos, const TShopItemData ** c_ppItemData);
		
		
		
		
		
Arat ;
		void Open(BOOL isPrivateShop, BOOL isMainPrivateShop);
		void Close();
		BOOL IsOpen();
		BOOL IsPrivateShop();
		BOOL IsMainPlayerPrivateShop();

		
Değiştir ;
		void Open(BOOL isPrivateShop, BOOL isMainPrivateShop, BOOL isOfflineShop);
		void Close();
		BOOL IsOpen();
		BOOL IsPrivateShop();
		BOOL IsMainPlayerPrivateShop();
		BOOL IsOfflineShop();
		
		
		
		
		
Arat ;
		void BuildPrivateShop(const char * c_szName);

Altına Ekle ;
		void ClearOfflineShopStock();
		void AddOfflineShopItemStock(TItemPos ItemPos, BYTE byDisplayPos, DWORD dwPrice);
		void DelOfflineShopItemStock(TItemPos ItemPos);
		int	 GetOfflineShopItemPrice(TItemPos ItemPos);
		void BuildOfflineShop(const char * c_szName, BYTE bTime);

		
		

Arat ;
		BOOL				m_isMainPlayerPrivateShop;

Altına Ekle ;
		BOOL				m_isOfflineShop;

		
		
Arat ;
		struct ShopTab
		{
			ShopTab()
			{
				coinType = SHOP_COIN_TYPE_GOLD;
			}
			BYTE				coinType;
			std::string			name;
			TShopItemData		items[SHOP_HOST_ITEM_MAX_NUM];
		};
		
Altına Ekle ;
		struct OfflineShopTab
		{
			OfflineShopTab()
			{
				coinType = SHOP_COIN_TYPE_GOLD;
			}
			BYTE				coinType;
			std::string			name;
			TShopItemData		items[OFFLINE_SHOP_HOST_ITEM_MAX_NUM];
		};
		
		
		
Arat ;
		ShopTab m_aShoptabs[SHOP_TAB_COUNT_MAX];

Altına Ekle ;
		OfflineShopTab m_aOfflineShoptabs[SHOP_TAB_COUNT_MAX];

		
		
		
Arat ;
		typedef std::map<TItemPos, TShopItemTable> TPrivateShopItemStock;
		TPrivateShopItemStock	m_PrivateShopItemStock;

Altına Ekle ;
		typedef std::map<TItemPos, TShopItemTable> TOfflineShopItemStock;
		TOfflineShopItemStock	m_OfflineShopItemStock;

		
		
