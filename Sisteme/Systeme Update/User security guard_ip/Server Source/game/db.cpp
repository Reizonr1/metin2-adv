Search:
#include "spam.h"

Add it under:
#ifdef USER_SECURITY_GUARD
#include "user_security_guard.h"
#endif


---


Search:
void DBManager::AnalyzeReturnQuery(SQLMsg * pMsg)
{
	CReturnQueryInfo * qi = (CReturnQueryInfo *) pMsg->pvUserData;

	switch (qi->iType)
	{
		case QID_AUTH_LOGIN:

Find:
					char szStatus[ACCOUNT_STATUS_MAX_LEN + 1];

Add it under:
#ifdef USER_SECURITY_GUARD
					int iGuardStatus = 0;
#endif



---



Find:
						str_to_number(aiPremiumTimes[PREMIUM_GOLD], row[col++]);

Add it under:
#ifdef USER_SECURITY_GUARD
						str_to_number(iGuardStatus, row[col++]);

						if (!row[col])
						{
							sys_err("error column %d", col);
							M2_DELETE(pinfo);
							break;
						}
#endif

---

Find:
						char szQuery[1024];
						snprintf(szQuery, sizeof(szQuery), "UPDATE account SET last_play=NOW() WHERE id=%u", dwID);
						std::auto_ptr<SQLMsg> msg( DBManager::instance().DirectQuery(szQuery) );

Add it under:
#ifdef USER_SECURITY_GUARD
						sys_log(0, "Guard status: %d", iGuardStatus);
						if (iGuardStatus != 0)
						{
							int userguard_result = UserSecurityGuard_LoginWebserver(pinfo->login, pinfo->passwd, pinfo->cGuardCode);

							if (userguard_result == USER_SECURITY_GUARD__WEB_MYSQL_ERROR || userguard_result == USER_SECURITY_GUARD__SERVER_ERROR)
							{
								LoginFailure(d, "WSRVERR"); // If not connect to webserver return as this error
								sys_log(0, "   WSRVERR");
								M2_DELETE(pinfo);
								return;
							}
							else if (userguard_result == USER_SECURITY_GUARD__WEB_UNKNOWN_ERROR)
							{
								LoginFailure(d, "WBUNKNW"); // If web server give unknown(undefined) error return as this
								sys_log(0, "   WBUNKNW");
								M2_DELETE(pinfo);
								return;
							}
							else if (userguard_result == USER_SECURITY_GUARD__MAIL_SENDED)
							{
								LoginFailure(d, "MSENDED"); // If mail sended to player return as this error
								sys_log(0, "   MSENDED");
								M2_DELETE(pinfo);
								return;
							}
							else if (userguard_result == USER_SECURITY_GUARD__WEB_CODE_ALREADY_SENDED)
							{
								LoginFailure(d, "ALRDSND"); // If code already sended to mail
								sys_log(0, "   ALRDSND");
								M2_DELETE(pinfo);
								return;
							}
							else if (userguard_result == USER_SECURITY_GUARD__MAILER_ERROR)
							{
								LoginFailure(d, "MAILERR"); // If system isn't connect to mail server
								sys_log(0, "   MAILERR");
								M2_DELETE(pinfo);
								return;
							}
							else if (userguard_result == USER_SECURITY_GUARD__CODE_IS_INVALID)
							{
								LoginFailure(d, "NTVALID"); // If guard code isn't valid
								sys_log(0, "   NTVALID");
								M2_DELETE(pinfo);
								return;
							}
							else if (userguard_result == USER_SECURITY_GUARD__CODE_IS_VALID || userguard_result == USER_SECURITY_GUARD__WEB_IS_OK)
							{
								sys_log(0, "Succesfuly confirmed user security guard data. user: %s", pinfo->login);

								char szGuardUpdateQuery[1024];
								snprintf(szGuardUpdateQuery, sizeof(szGuardUpdateQuery), "UPDATE account SET guard_status=1, guard_date=0, guard_code=0, guard_ip='%s' WHERE login='%s'", d->GetHostName(), pinfo->login);
								std::auto_ptr<SQLMsg> msg(DBManager::instance().DirectQuery(szGuardUpdateQuery));
							}
							else{
								LoginFailure(d, "NDEFERR");
								sys_err("Undefined error: %d", userguard_result);
								M2_DELETE(pinfo);
								return;
							}
						}
#endif
