Search:
void CAccountConnector::SetLoginInfo(const char * c_szName, const char * c_szPwd)
{
	m_strID = c_szName;
	m_strPassword = c_szPwd;
}

Change:
#ifdef USER_SECURITY_GUARD
void CAccountConnector::SetLoginInfo(const char * c_szName, const char * c_szPwd, const char * c_szGuard)
{
	m_strID = c_szName;
	m_strPassword = c_szPwd;
	m_strGuard = c_szGuard;
}
#else
void CAccountConnector::SetLoginInfo(const char * c_szName, const char * c_szPwd)
{
	m_strID = c_szName;
	m_strPassword = c_szPwd;
}
#endif

---

Search:
void CAccountConnector::ClearLoginInfo( void )
{
	m_strPassword = "";
}

Change:
void CAccountConnector::ClearLoginInfo( void )
{
	m_strPassword = "";
#ifdef USER_SECURITY_GUARD
	m_strGuard = "";
#endif
}

---

Search:
		strncpy(LoginPacket.pwd, m_strPassword.c_str(), PASS_MAX_NUM);

Add it under:
#ifdef USER_SECURITY_GUARD
		strncpy(LoginPacket.cGuardCode, m_strGuard.c_str(), 6);
#endif

---

Search:
LoginPacket.pwd[PASS_MAX_NUM] = '\0';

Add it under:
#ifdef USER_SECURITY_GUARD
		LoginPacket.cGuardCode[6] = '\0';
#endif

---

Search:
		m_strPassword = "";

Add it under:
#ifdef USER_SECURITY_GUARD
		m_strGuard = "";
#endif

---

Search:
	SetLoginInfo("", "");
	SetRecvBufferSize(1024 * 128);
	SetSendBufferSize(2048);
	__Inialize();

Change:
#ifdef USER_SECURITY_GUARD
	SetLoginInfo("", "", "");
#else
	SetLoginInfo("", "");
#endif
	SetRecvBufferSize(1024 * 128);
	SetSendBufferSize(2048);
	__Inialize();


