daugi la inceput in caz ca nu ai:
#include "db.h"

cauti:
	void RegisterPCFunctionTable()

iar deasupra lui adaugi:


#ifdef __ONEX_VIP__
	int pc_onex_verify_vip(lua_State * L)
	{
		//usage pc.onex_verfy_vip(pid) 
		//LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();

			if (!lua_isnumber(L, 1))
			{
				sys_err("[VIP]: nu exista pid.");
				return 0;
			}
			long int pid_char = lua_tonumber(L, 1);
			std::auto_ptr<SQLMsg> pmsg(DBManager::instance().DirectQuery("SELECT COUNT(*) FROM player.player_VIP_oneX WHERE PID_VIP = %u", pid_char));
				MYSQL_ROW row = mysql_fetch_row(pmsg->Get()->pSQLResult);

				BYTE exista = 0;
				str_to_number(exista, row[0]);

				if (exista)
					
					lua_pushboolean(L, true);
		return 1;
	}
	
	int pc_onex_add_vip(lua_State * L)
	{

		LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();

		if (!lua_isnumber(L, 1))
		{
			sys_err("Timp invalid");
			return 0;
		}

		if (!lua_isnumber(L, 2))
		{
			sys_err("Fara timp invalid");
			return 0;
		}
		time_t t1 = time(0);
		long long timp_calcuat = t1 +((int)lua_tonumber(L, 1) * 86400);
		char query[1024];
		sprintf(query, "INSERT INTO player.player_VIP_oneX SET");
		sprintf(query, "%s PID_VIP='%d'", query, ch->GetPlayerID());
		sprintf(query, "%s, TIMP='%d'", query, timp_calcuat);
		sprintf(query, "%s, FARA_TIMP='%d'", query, (int)lua_tonumber(L, 2));
		DBManager::instance().DirectQuery(query);
		ch->oneX_vip();
		return 0;
	}
#endif 

cauti:
		luaL_reg pc_functions[] = 
iar in lista adaugi:

#ifdef __ONEX_VIP__
			
			{ "verify_vip_onex",	pc_onex_verify_vip	},
			{ "adauga_vip_onex",	pc_onex_add_vip	},					
#endif

