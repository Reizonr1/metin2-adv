Search:
			bool			bShowSalesText;

Add it under:
#ifdef __OFFLINE_SHOP__
			int				iShowOfflineShop;
#endif

https://puu.sh/sgN8Z/b12da73fbc.png

---

Search:
		bool							IsShowSalesText();

Add it under:
#ifdef __OFFLINE_SHOP__
		int								GetShowOfflineShopFlag();
#endif

https://puu.sh/sgNaw/cf2941e78e.png

---

Search:
		void							SetShowSalesTextFlag(int iFlag);

Add it under:
#ifdef __OFFLINE_SHOP__
		void							SetShowOfflineShop(int iFlag);
#endif

https://puu.sh/sgNbJ/3baf97f90a.png


