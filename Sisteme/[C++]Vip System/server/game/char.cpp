cauti:


void CHARACTER::SetEmpire(BYTE bEmpire)
{
	m_bEmpire = bEmpire;
}
iar sub adaugi:

#ifdef __ONEX_VIP__
bool CHARACTER::onex_vip_timp()
{
	//timp actual
	time_t t1 = time(0);

	std::auto_ptr<SQLMsg> oneXs(DBManager::instance().DirectQuery("SELECT TIMP,FARA_TIMP FROM player.player_VIP_oneX WHERE PID_VIP = %u", GetPlayerID()));
	MYSQL_ROW row = mysql_fetch_row(oneXs->Get()->pSQLResult);
	//timp ramas
	 long int time = atoi(row[0]);
	//fara timp
	 int no_time = atoi(row[1]);

	if (no_time != 1)
	{
		if (t1 >= time)
		{
			DBManager::instance().DirectQuery("DELETE FROM player.player_VIP_oneX WHERE PID_VIP =  %u", GetPlayerID());
			return 0;
		}
	}
}

void CHARACTER::oneX_vip()
{
	std::auto_ptr<SQLMsg> pmsg(DBManager::instance().DirectQuery("SELECT COUNT(*) FROM player.player_VIP_oneX WHERE PID_VIP = %u", GetPlayerID()));
	MYSQL_ROW row = mysql_fetch_row(pmsg->Get()->pSQLResult);

	BYTE exista = 0;
	str_to_number(exista, row[0]);

	if (exista)
	{
		if (onex_vip_timp())
		{
			//sys_log(0, "[oneX]: VIP debug Nume: %s PID: %d", GetName(), GetPlayerID());
			m_afAffectFlag.Set(AFF_VIP);
		}
	}
}
#endif

cauti:
void CHARACTER::SetPlayerProto(const TPlayerTable * t)

iar sub:
	SetStamina(t->stamina);

adaugi:
	
#ifdef __ONEX_VIP__
	oneX_vip();
#endif




