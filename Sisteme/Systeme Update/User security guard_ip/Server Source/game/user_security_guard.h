#ifndef __METIN2_USER_SECURITY_GUARD_H__
#define __METIN2_USER_SECURITY_GUARD_H__

enum EUserSecurityGuardStatus
{
	USER_SECURITY_GUARD__SERVER_ERROR,				// 0
	USER_SECURITY_GUARD__WEB_UNKNOWN_ERROR,			// 1
	USER_SECURITY_GUARD__WEB_MYSQL_ERROR,			// 2
	USER_SECURITY_GUARD__MAILER_ERROR,				// 3
	USER_SECURITY_GUARD__MAIL_SENDED,				// 4
	USER_SECURITY_GUARD__WEB_CODE_ALREADY_SENDED,	// 5
	USER_SECURITY_GUARD__CODE_IS_VALID,				// 6
	USER_SECURITY_GUARD__CODE_IS_INVALID,			// 7
	USER_SECURITY_GUARD__WEB_IS_OK					// 8
};

// Exports
int UserSecurityGuard_LoginWebserver(const char *login, const char *pwd, const char * guard_code);
int UserSecurityGuard_IncQueryCount();
void UserSecurityGuard_Log();

#endif // __METIN2_USER_SECURITY_GUARD_H__
