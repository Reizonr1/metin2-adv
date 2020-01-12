Search:
		int				ChangeEmpire(BYTE empire);

Add it under:
#ifdef __OFFLINE_SHOP__
		bool			CanChangeEmpireOfflineShopCheck();
#endif

http://i.imgur.com/Dm6gWqd.png
---

Search:
		bool			UseItem(TItemPos Cell, TItemPos DestCell = NPOS);

Add it under:
#ifdef __OFFLINE_SHOP__
		bool			HasNearOfflineShop(long newX, long newY);
#endif

http://i.imgur.com/WiE74zo.png
---

Search:
		// Shop related
	public:
		void			SetShop(LPSHOP pkShop);
		LPSHOP			GetShop() const { return m_pkShop; }
		void			ShopPacket(BYTE bSubHeader);

		void			SetShopOwner(LPCHARACTER ch) { m_pkChrShopOwner = ch; }
		LPCHARACTER		GetShopOwner() const { return m_pkChrShopOwner;}

		void			OpenMyShop(const char * c_pszSign, TShopItemTable * pTable, BYTE bItemCount);
		LPSHOP			GetMyShop() const { return m_pkMyShop; }
		void			CloseMyShop();

	protected:

		LPSHOP			m_pkShop;
		LPSHOP			m_pkMyShop;
		std::string		m_stShopSign;
		LPCHARACTER		m_pkChrShopOwner;
		// End of shop

Change:
		// Shop related
	public:
		void			SetShop(LPSHOP pkShop);
		LPSHOP			GetShop() const { return m_pkShop; };
		void			ShopPacket(BYTE bSubHeader);

		void			SetShopOwner(LPCHARACTER ch) { m_pkChrShopOwner = ch; };
		LPCHARACTER		GetShopOwner() const { return m_pkChrShopOwner; };

#ifdef __OFFLINE_SHOP__
		void			SetShopSign(std::string sign) { m_stShopSign = sign; };
		std::string		GetShopSign() const { return m_stShopSign; };

		void			SetOfflineShopOwner(LPCHARACTER ch) { m_pkChrOfflineShopOwner = ch; };
		LPCHARACTER		GetOfflineShopOwner() const { return m_pkChrOfflineShopOwner; };
#endif

		void			OpenMyShop(const char * c_pszSign, TShopItemTable * pTable, BYTE bItemCount);
#ifdef __OFFLINE_SHOP__
		void			OpenOfflineShop(const char * c_pszSign, BYTE bType, BYTE bSize, BYTE bColor, TShopItemTable * pTable, BYTE bItemCount);

		void			SetMyShop(LPSHOP shop) { m_pkMyShop = shop; };
#endif

		LPSHOP			GetMyShop() const { return m_pkMyShop; };
		void			CloseMyShop();

#ifdef __OFFLINE_SHOP__
		void			SetupExpire(int iSec);
#endif

	protected:

		LPSHOP			m_pkShop;
		LPSHOP			m_pkMyShop;
		std::string		m_stShopSign;
		LPCHARACTER		m_pkChrShopOwner;
#ifdef __OFFLINE_SHOP__
		LPCHARACTER		m_pkChrOfflineShopOwner;
#endif
		// End of shop

http://i.imgur.com/rWW0AY3.png
http://i.imgur.com/eNz9ntf.png

---

Search:
		void				LoadSafebox(int iSize, DWORD dwGold, int iItemCount, TPlayerItem * pItems);

Change:
#ifdef __OFFLINE_SHOP__
		void				LoadSafebox(int iSize, uint64_t dwGold, int iItemCount, TPlayerItem * pItems);
#else
		void				LoadSafebox(int iSize, DWORD dwGold, int iItemCount, TPlayerItem * pItems);
#endif

http://i.imgur.com/op6l57y.png
---

Search:
		LPEVENT				m_pkPetSystemUpdateEvent;

Add it under:
#ifdef __OFFLINE_SHOP__
		LPEVENT				m_pkExpireOfflineShopEvent;
#endif

http://i.imgur.com/yVZBJzM.png
---

Search:
		void	SetPotionLimit(int count) { m_nPotionLimit = count; }
		int		GetPotionLimit() const { return m_nPotionLimit; }
	// END_ARENA

Add it under:
#ifdef __OFFLINE_SHOP__
		void	SetCoins(long val);
		void	UpdateCoins(DWORD dwAID, long val);
		long	GetCoins();
#endif

http://i.imgur.com/iXfLWBS.png


