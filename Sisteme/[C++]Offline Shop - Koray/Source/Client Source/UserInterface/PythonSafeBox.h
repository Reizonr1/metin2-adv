Search:
		void SetMoney(DWORD dwMoney);
		DWORD GetMoney();

Change:
#ifdef __OFFLINE_SHOP__
		void SetMoney(uint64_t dwMoney);
		uint64_t GetMoney();
#else
		void SetMoney(DWORD dwMoney);
		DWORD GetMoney();
#endif

https://puu.sh/sgMl9/156e29844e.png

---

Search:
		DWORD m_dwMoney;

Change:
#ifdef __OFFLINE_SHOP__
		uint64_t m_dwMoney;
#else
		DWORD m_dwMoney;
#endif


https://puu.sh/sgMmA/b08aca92c7.png