// 1) Search for: void RegisterGlobalFunctionTable(lua_State* L)
// 2) Paste this under:

	int _mysql_direct_query(lua_State* L)
	{
		// char szQuery[1024];

		if (!lua_isstring(L, 1))
			return 0;
		// strncpy(szQuery, lua_tostring(L, 1), sizeof(szQuery));

		int i=0, m=1;
		MYSQL_ROW row;
		MYSQL_FIELD * field;
		MYSQL_RES * result;
		// SQLMsg * pMsg = DBManager::instance().DirectQuery(szQuery);
		std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery(lua_tostring(L, 1)));
		if (pMsg.get())
		{
			// ret1 (number of affected rows)
			lua_pushnumber(L, pMsg->Get()->uiAffectedRows);
			//-1 if error such as duplicate occurs (-2147483648 via lua)
			//   if wrong syntax error occurs (4294967295 via lua)
			// ret2 (table of affected rows)
			lua_newtable(L);
			if ((result = pMsg->Get()->pSQLResult) &&
					!(pMsg->Get()->uiAffectedRows == 0 || pMsg->Get()->uiAffectedRows == (uint32_t)-1))
			{
				// LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();
				// ch->ChatPacket(CHAT_TYPE_INFO, "<%s> Retrieved %u fields\n", __FUNCTION__, mysql_num_fields(result));
				// ch->ChatPacket(CHAT_TYPE_INFO, "<%s> Retrieved %u rows\n", __FUNCTION__, mysql_num_rows(result));
				// ch->ChatPacket(CHAT_TYPE_INFO, "<%s> Affected %u rows\n", __FUNCTION__, pMsg->Get()->uiAffectedRows);
				// ch->ChatPacket(CHAT_TYPE_INFO, "<%s> Num %u rows\n", __FUNCTION__, pMsg->Get()->uiNumRows);

				while((row = mysql_fetch_row(result)))
				{
					lua_pushnumber(L, m);
					lua_newtable(L);
					while((field = mysql_fetch_field(result)))
					{
						lua_pushstring(L, field->name);
						if (!(field->flags & NOT_NULL_FLAG) && (row[i]==NULL))
						{
							// lua_pushstring(L, "NULL");
							lua_pushnil(L);
						}
						else if (IS_NUM(field->type))
						{
							double val = NAN;
							lua_pushnumber(L, (sscanf(row[i],"%lf",&val)==1)?val:NAN);
						}
						else if (field->type == MYSQL_TYPE_BLOB)
						{
							lua_newtable(L);
							for (DWORD iBlob=0; iBlob < field->max_length; iBlob++)
							{
								lua_pushnumber(L, row[i][iBlob]);
								lua_rawseti(L, -2, iBlob+1);
							}
						}
						else
							lua_pushstring(L, row[i]);
						// LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();
						// ch->ChatPacket(CHAT_TYPE_INFO, "<%s> Retrieved %d flag %s for %s\n", __FUNCTION__, field->type, field->name, row[i]?row[i]:"NULL");
						lua_rawset(L, -3);
						i++;
					}
					mysql_field_seek(result, 0);
					i=0;

					lua_rawset(L, -3);
					m++;
				}
			}
		}
		else {lua_pushnumber(L, 0); lua_newtable(L);}

		// delete pMsg;
		return 2;
	}
	
// 1) Search for: void RegisterGlobalFunctionTable(lua_State* L)
// 2) Paste this above: {	NULL,	NULL	}

			{	"mysql_direct_query",			_mysql_direct_query				},
