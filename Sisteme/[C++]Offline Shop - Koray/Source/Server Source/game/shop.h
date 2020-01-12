Search:
		typedef struct shop_item
		{
			DWORD	vnum;		// ¾ÆÀÌÅÛ ¹øÈ£
			long	price;		// °¡°İ
			BYTE	count;		// ¾ÆÀÌÅÛ °³¼ö

			LPITEM	pkItem;
			int		itemid;		// ¾ÆÀÌÅÛ °íÀ¯¾ÆÀÌµğ

			shop_item()
			{
				vnum = 0;
				price = 0;
				count = 0;
				itemid = 0;
				pkItem = NULL;
			}
		} SHOP_ITEM;

Change:
		typedef struct shop_item
		{
			DWORD	vnum;		// ¾ÆÀÌÅÛ ¹øÈ£
			long	price;		// °¡°İ
#ifdef __OFFLINE_SHOP__
			long	price2;
			long	price3;
			long	price4;
#endif
			BYTE	count;		// ¾ÆÀÌÅÛ °³¼ö

			LPITEM	pkItem;
			int		itemid;		// ¾ÆÀÌÅÛ °íÀ¯¾ÆÀÌµğ
#ifdef __OFFLINE_SHOP__		
			int		isSold;
#endif

			shop_item()
			{
				vnum = 0;
				price = 0;
#ifdef __OFFLINE_SHOP__
				price2 = 0;
				price3 = 0;
				price4 = 0;
#endif				
				count = 0;
				itemid = 0;
#ifdef __OFFLINE_SHOP__
				isSold = 0;
#endif
				pkItem = NULL;
			}
		} SHOP_ITEM;

https://puu.sh/sgIYn/4356ae46bf.png

---

Search:
		bool	Create(DWORD dwVnum, DWORD dwNPCVnum, TShopItemTable * pItemTable);
		void	SetShopItems(TShopItemTable * pItemTable, BYTE bItemCount);

Change:
		bool	Create(DWORD dwVnum, DWORD dwNPCVnum, TShopItemTable * pItemTable);
#ifdef __OFFLINE_SHOP__
		bool	Create(TOfflineShopTable* table);
		void	SetShopItems(LPCHARACTER pkOwner, TShopItemTable * pItemTable, BYTE bItemCount);
#else
		void	SetShopItems(TShopItemTable * pItemTable, BYTE bItemCount);
#endif

https://puu.sh/sgJ0t/3597038c8d.png

---

Search:
		virtual void	SetPCShop(LPCHARACTER ch);
		virtual bool	IsPCShop()	{ return m_pkPC ? true : false; }

Change:
		virtual void		SetPCShop(LPCHARACTER ch) { m_pkPC = ch; };
		virtual LPCHARACTER GetPCShop() { return m_pkPC; }
		virtual bool		IsPCShop() { return m_pkPC ? true : false; };

#ifdef __OFFLINE_SHOP__
		virtual void SetOwner(DWORD dwOwnerAID, DWORD dwOwnerPID);
		virtual DWORD GetOwner() { return m_dwOwnerPID; };
		virtual bool HasOwner() { return m_dwOwnerPID ? true : false; };

		virtual uint64_t GetMoney() { return m_Money; };

		virtual void SetShopColor(BYTE bColor) { m_bColor = bColor; };
		virtual void SetShopSize(BYTE bSize) { m_bSize = bSize; };
		
		virtual void SetLocked(bool bType) { m_bIsLocked = bType; };
		virtual bool IsLocked() { return m_bIsLocked; };

		DWORD GetSoldItemVnum(BYTE pos);
		BYTE GetSoldCount(BYTE pos);
		long GetSoldPrice(BYTE pos, BYTE type);
		const long* GetSoldSockets(BYTE pos);
		const TPlayerItemAttribute* GetSoldAttributes(BYTE pos);
#if 0
		const char* GetSoldNewOwner(BYTE pos);
		DWORD GetSoldDate(BYTE pos);
#endif
#endif

https://puu.sh/sgJ2C/38e4b0b39d.png

---

Search:
		DWORD	GetVnum() { return m_dwVnum; }
		DWORD	GetNPCVnum() { return m_dwNPCVnum; }

Add it under:
#ifdef __OFFLINE_SHOP__
		void	Apply();
		void	Remove();
#endif

https://puu.sh/sgJ44/018c5fa5a9.png

---

Search:
		LPCHARACTER			m_pkPC;

Add it under:
#ifdef __OFFLINE_SHOP__
		typedef struct shop_sold_info
		{
			CShop* lpShop;
			DWORD vnum;
			long Price;
			long Price2;
			long Price3;
			long Price4;
			BYTE Count;
			long	alSockets[ITEM_SOCKET_MAX_NUM];
			TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_MAX_NUM];
#if 0
			DWORD	soldDate;
			char	newOwner[CHARACTER_NAME_MAX_LEN + 1];
#endif
		} SShopSoldData;
		std::map<BYTE, SShopSoldData> m_SoldItems;

		bool				m_bIsLocked;
		DWORD				m_dwOwnerAID;
		DWORD				m_dwOwnerPID;
		uint64_t			m_Money;
		BYTE				m_bSize;
		BYTE				m_bColor;
#endif


https://puu.sh/sgJ5q/adeac16eed.png
https://puu.sh/sgJ6o/64ba897853.png




