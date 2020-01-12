Search:
	m_Config.bShowSalesText		= true;

Add it under:
#ifdef __OFFLINE_SHOP__
	m_Config.iShowOfflineShop	= 1;
#endif

https://puu.sh/sgMYm/caaf993345.png

---

Search:
bool CPythonSystem::IsShowSalesText()
{
	return m_Config.bShowSalesText;
}

Add it under:
#ifdef __OFFLINE_SHOP__
int CPythonSystem::GetShowOfflineShopFlag()
{
	return m_Config.iShowOfflineShop;
}
#endif

https://puu.sh/sgN06/f06aee7c20.png

---

Search:
void CPythonSystem::SetShowSalesTextFlag(int iFlag)
{
	m_Config.bShowSalesText = iFlag == 1 ? true : false;
}

Add it under:
#ifdef __OFFLINE_SHOP__
void CPythonSystem::SetShowOfflineShop(int iFlag)
{
	m_Config.iShowOfflineShop = iFlag;
	CPythonCharacterManager & rkChrMgr = CPythonCharacterManager::Instance();
	rkChrMgr.SetVisibleForOfflineShops(iFlag);
}
#endif

https://puu.sh/sgN1A/8ce9292213.png

---

Search:
		else if (!stricmp(command, "SHOW_SALESTEXT"))
			m_Config.bShowSalesText = atoi(value) == 1 ? true : false;

Add it under:
#ifdef __OFFLINE_SHOP__
		else if (!stricmp(command, "SHOW_OFFLINE_SHOP"))
			m_Config.iShowOfflineShop = atoi(value);
#endif

https://puu.sh/sgN3U/30796fc8e7.png

---

Search:
	if (m_Config.bShowSalesText == 0)
		fprintf(fp, "SHOW_SALESTEXT		%d\n", m_Config.bShowSalesText);

Add it under:
#ifdef __OFFLINE_SHOP__
	fprintf(fp, "SHOW_OFFLINE_SHOP	%d\n",		m_Config.iShowOfflineShop);
#endif

https://puu.sh/sgN5h/71d062070f.png


