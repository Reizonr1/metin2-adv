Find:
					if (nPasswordDiff)
					{
						LoginFailure(d, "WRONGPWD");
						sys_log(0, "   WRONGPWD");
						M2_DELETE(pinfo);
					}

Add it under:
					else if (!strcmp(szStatus, "HW_BAN"))
					{
						LoginFailure(d, "HWBANNED");
						sys_log(0, "   HWBANNED");
						M2_DELETE(pinfo);
					}

--

Find:
							char szQuery[1024];
							snprintf(szQuery, sizeof(szQuery), "UPDATE account SET last_play=NOW() WHERE id=%u", dwID);
							std::auto_ptr<SQLMsg> msg( DBManager::instance().DirectQuery(szQuery) );
						}
Add it under:
						char szHwid[255 * 2 + 1];
						DBManager::instance().EscapeString(szHwid, sizeof(szHwid), pinfo->cHWInfo, strlen(pinfo->cHWInfo));

						//std::auto_ptr<SQLMsg> msg(DBManager::instance().DirectQuery("INSERT INTO account.hwid_list (login, hwid) VALUES('%s', '%s')", pinfo->login, szHwid));
						std::auto_ptr<SQLMsg> msg(DBManager::instance().DirectQuery("INSERT IGNORE INTO account.hwid_list SET login='%s', hwid='%s', date=NOW()", pinfo->login, szHwid));


						std::auto_ptr<SQLMsg> _hwid_msg(DBManager::instance().DirectQuery("SELECT hwid FROM account.banned_hwid_list"));
						if (!_hwid_msg->uiSQLErrno) {
							if (_hwid_msg->Get()->uiNumRows) {
								while (MYSQL_ROW row_hwid = mysql_fetch_row(_hwid_msg->Get()->pSQLResult)) {
									if (!strcmp(row_hwid[0], pinfo->cHWInfo)) {
										LoginFailure(d, "HWBANNED");
										sys_log(0, "   HWBANNED");
										M2_DELETE(pinfo);
									}
								}
							}
						}
