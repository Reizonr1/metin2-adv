Search:
		bool SendShootPacket(UINT uSkill);

Add it under:
#ifdef __OFFLINE_SHOP__
		void SetShopMoveMode(int iType);
#endif

https://puu.sh/sgLhV/5a67520852.png

---

Search:
		bool SendSafeBoxMoneyPacket(BYTE byState, DWORD dwMoney);

Change:
#ifdef __OFFLINE_SHOP__
		bool SendSafeBoxMoneyPacket(BYTE byState, uint64_t dwMoney);
#else
		bool SendSafeBoxMoneyPacket(BYTE byState, long dwMoney);
#endif

https://puu.sh/sgLjB/6762077d71.png
---

Search:
		bool SendBuildPrivateShopPacket(const char * c_szName, const std::vector<TShopItemTable> & c_rSellingItemStock);

Change:
#ifdef __OFFLINE_SHOP__
		bool SendBuildPrivateShopPacket(const char * c_szName, BYTE bType, BYTE bSize, BYTE bColor, const std::vector<TShopItemTable> & c_rSellingItemStock);
		void DisappearShopSign(DWORD dwVID);
		void AppearShopSign(DWORD dwVID, std::string stSign = "");
#else
		bool SendBuildPrivateShopPacket(const char * c_szName, const std::vector<TShopItemTable> & c_rSellingItemStock);
#endif

https://puu.sh/sgLkT/a1d2ebe681.png
---

Search:
		std::string m_stMarkIP;

Add it under:
#ifdef __OFFLINE_SHOP__
		std::map<DWORD, std::string> m_mapShopSign;
#endif

https://puu.sh/sgLnQ/0edcfc0fc1.png