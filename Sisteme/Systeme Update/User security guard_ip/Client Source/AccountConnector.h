Search:
		void SetLoginInfo(const char * c_szName, const char * c_szPwd);

Change:
#ifdef USER_SECURITY_GUARD
		void SetLoginInfo(const char * c_szName, const char * c_szPwd, const char * c_szGuard);
#else
		void SetLoginInfo(const char * c_szName, const char * c_szPwd);
#endif


---

Search:
		std::string m_strPassword;

Add it under:
#ifdef USER_SECURITY_GUARD
		std::string m_strGuard;
#endif
