//Find
long lSPRecovery = GetPoint(POINT_SP_RECOVERY);

///Add
#ifdef NEW_ADD_INVENTORY
	long envanterim = Black_Envanter();
#endif

//Find
SetPoint(POINT_PC_BANG_DROP_BONUS, 0);

///Add
#ifdef NEW_ADD_INVENTORY
	SetPoint(POINT_BLACK, envanterim);
#endif

//Find
case POINT_MAX_STAMINA:
	SetMaxStamina(GetMaxStamina() + amount);
	val = GetMaxStamina();
	break;
	
///Add
#ifdef NEW_ADD_INVENTORY
		case POINT_BLACK:
			{
				const int64_t Envantertoplami = static_cast<int64_t>(Black_Envanter()) + static_cast<int64_t>(amount);
				if (Envantertoplami > 18)
				{
					sys_err("[ENVANTER SINIRI HATASI]");
					return;
				}
				Set_Envanter_Black(Black_Envanter() + amount);
				val = Black_Envanter();
			}
			break;
#endif

///Add end of cpp
bool CHARACTER::Envanter_update()
{
// #define anahtar1 72319
#define anahtar2 72320
		for (int black = 0; black < 4; black++)
		{
			if (Black_Envanter() == black)
			{
				int lazim = 2;
				if (CountSpecifyItem(anahtar2) > 1)
				{
					RemoveSpecifyItem(anahtar2, lazim);
				}
				else
				{
					ChatPacket(CHAT_TYPE_COMMAND, "update_envanter_lazim %d", lazim);
					return false;
				}
			}
		}
		for (int black2 = 4; black2 < 6; black2++)
		{
			if (Black_Envanter() == black2)
			{
				int lazim = 3;
				if (CountSpecifyItem(anahtar2) > 1)
				{
					RemoveSpecifyItem(anahtar2, lazim);
				}
				else
				{
					ChatPacket(CHAT_TYPE_COMMAND, "update_envanter_lazim %d", lazim);
					return false;
				}
			}
		}
		for (int black31 = 6; black31 < 9; black31++)
		{
			if (Black_Envanter() == black31)
			{
				int lazim = 4;
				if (CountSpecifyItem(anahtar2) > 1)
				{
					RemoveSpecifyItem(anahtar2, lazim);
				}
				else
				{
					ChatPacket(CHAT_TYPE_COMMAND, "update_envanter_lazim %d", lazim);
					return false;
				}
			}
		}
		for (int black3 = 9; black3 < 12; black3++)
		{
			if (Black_Envanter() == black3)
			{
				int lazim = 5;
				if (CountSpecifyItem(anahtar2) > 1)
				{
					RemoveSpecifyItem(anahtar2, lazim);
				}
				else
				{
					ChatPacket(CHAT_TYPE_COMMAND, "update_envanter_lazim %d", lazim);
					return false;
				}
			}
		}
		for (int black4 = 12; black4 < 15; black4++)
		{
			if (Black_Envanter() == black4)
			{
				int lazim = 6;
				if (CountSpecifyItem(anahtar2) > 1)
				{
					RemoveSpecifyItem(anahtar2, lazim);
				}
				else
				{
					ChatPacket(CHAT_TYPE_COMMAND, "update_envanter_lazim %d", lazim);
					return false;
				}
			}
		}
		for (int black5 = 15; black5 < 18; black5++)
		{	
			if (Black_Envanter() == black5)
			{
				int lazim = 7;
				if (CountSpecifyItem(anahtar2) > 1)
				{
					RemoveSpecifyItem(anahtar2, lazim);
				}
				else
				{
					ChatPacket(CHAT_TYPE_COMMAND, "update_envanter_lazim %d", lazim);
					return false;
				}
			}
		}
	PointChange(POINT_BLACK, 1, false);
	ChatPacket(CHAT_TYPE_COMMAND, "refreshinven");
	UpdatePacket();		
	return true;
}
DWORD CHARACTER::Black_Envanter() const
{
	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT envanter FROM player.player WHERE id = '%u';", GetPlayerID()));
	if (pMsg->Get()->uiNumRows == 0)
		return 200;
	
	MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
	DWORD envanter = 0;
	str_to_number(envanter, row[0]);
	return envanter;
}
void CHARACTER::Set_Envanter_Black(int black)
{
	DBManager::instance().DirectQuery("UPDATE player.player SET envanter = '%d' WHERE id = '%u';", black, GetPlayerID());
}
#endif