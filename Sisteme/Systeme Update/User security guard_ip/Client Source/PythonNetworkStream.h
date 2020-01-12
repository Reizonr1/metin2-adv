Search:
		void SetLoginInfo(const char* c_szID, const char* c_szPassword);

Change:
#ifdef USER_SECURITY_GUARD
		void SetLoginInfo(const char* c_szID, const char* c_szPassword, const char* c_szGuard);
#else
		void SetLoginInfo(const char* c_szID, const char* c_szPassword);
#endif

---

Search:
		std::string	m_stPassword;

Add it under:
#ifdef USER_SECURITY_GUARD
		std::string	m_stGuard;
#endif
