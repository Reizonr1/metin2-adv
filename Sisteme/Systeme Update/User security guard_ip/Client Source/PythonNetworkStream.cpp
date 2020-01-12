Search:
void CPythonNetworkStream::SetLoginInfo(const char* c_szID, const char* c_szPassword)
{
	m_stID = c_szID;
	m_stPassword = c_szPassword;
}

Change:
#ifdef USER_SECURITY_GUARD
void CPythonNetworkStream::SetLoginInfo(const char* c_szID, const char* c_szPassword, const char* c_szGuard)
{
	m_stID=c_szID;
	m_stPassword=c_szPassword;
	m_stGuard = c_szGuard;
}
#else
void CPythonNetworkStream::SetLoginInfo(const char* c_szID, const char* c_szPassword)
{
	m_stID = c_szID;
	m_stPassword = c_szPassword;
}
#endif

---

Search:
void CPythonNetworkStream::ClearLoginInfo( void )
{
	m_stPassword = "";
}

Change:
void CPythonNetworkStream::ClearLoginInfo( void )
{
	m_stPassword = "";
#ifdef USER_SECURITY_GUARD
	m_stGuard = "";
#endif
}
