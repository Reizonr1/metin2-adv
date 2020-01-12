Search:
void CInputAuth::Login(LPDESC d, const char * c_pData)
{
	TPacketCGLogin3 * pinfo = (TPacketCGLogin3 *) c_pData;


Find:
				"UNIX_TIMESTAMP(money_drop_rate_expire),"

Add it under:
#ifdef USER_SECURITY_GUARD
				"guard_status,"
#endif



---

Find:
				"UNIX_TIMESTAMP(money_drop_rate_expire),"

Add it under:
#ifdef USER_SECURITY_GUARD
				"guard_status,"
#endif
