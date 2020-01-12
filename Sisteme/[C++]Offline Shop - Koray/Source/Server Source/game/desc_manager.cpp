Search:
	m_set_pkClientDesc.clear();

	//m_AccountIDMap.clear();
	m_map_loginName.clear();
	m_map_handle.clear();

	Initialize();
}

Change:
	m_set_pkClientDesc.clear();

	m_AccountIDMap.clear();
	m_map_loginName.clear();
	m_map_handle.clear();

	Initialize();
}

https://puu.sh/sgGqe/e62a7bc4fc.png

---

Search:
void DESC_MANAGER::ConnectAccount(const std::string& login, LPDESC d)
{
dev_log(LOG_DEB0, "BBBB ConnectAccount(%s)", login.c_str());
	m_map_loginName.insert(DESC_LOGINNAME_MAP::value_type(login,d));
}

void DESC_MANAGER::DisconnectAccount(const std::string& login)
{
dev_log(LOG_DEB0, "BBBB DisConnectAccount(%s)", login.c_str());
	m_map_loginName.erase(login);
}

Change:
void DESC_MANAGER::ConnectAccount(const std::string& login, LPDESC d)
{
	dev_log(LOG_DEB0, "BBBB ConnectAccount(%s)", login.c_str());
	m_map_loginName.insert(DESC_LOGINNAME_MAP::value_type(login,d));
	m_AccountIDMap.insert(DESC_ACCOUNTID_MAP::value_type(d->GetAccountTable().id, d));
}

void DESC_MANAGER::DisconnectAccount(const std::string& login)
{
	dev_log(LOG_DEB0, "BBBB DisConnectAccount(%s)", login.c_str());
	DESC_LOGINNAME_MAP::iterator it = m_map_loginName.find(login);
	if (it != m_map_loginName.end())
	{
		m_AccountIDMap.erase(it->second->GetAccountTable().id);
		m_map_loginName.erase(it);
	}
}

https://puu.sh/sgGrF/94736464ed.png
--

Search:
LPDESC DESC_MANAGER::FindByLoginName(const std::string& login)
{
	DESC_LOGINNAME_MAP::iterator it = m_map_loginName.find(login);

	if (m_map_loginName.end() == it)
		return NULL;

	return (it->second);
}

Add it under:
LPDESC DESC_MANAGER::FindByAID(DWORD dwAID)
{
	DESC_ACCOUNTID_MAP::iterator it = m_AccountIDMap.find(dwAID);

	if (m_AccountIDMap.end() == it)
		return NULL;

	return (it->second);
}

https://puu.sh/sgGtD/09cca5f004.png