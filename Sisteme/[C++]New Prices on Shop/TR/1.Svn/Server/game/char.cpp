///Herhangi bir yere ekleyin

DWORD CHARACTER::Ep_Miktar()
{
	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT coins FROM account.account WHERE id = '%d';", GetDesc()->GetAccountTable().id));
	if (pMsg->Get()->uiNumRows == 0)
		return 0;
	
	MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
	DWORD ep = 0;
	str_to_number(ep, row[0]);
	return ep;
}

void CHARACTER::Set_Ep(DWORD amount)
{
	DBManager::instance().DirectQuery("UPDATE account.account SET coins = '%d' WHERE id = '%d';", amount, GetDesc()->GetAccountTable().id);
}