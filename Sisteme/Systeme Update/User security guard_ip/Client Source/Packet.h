Search:
typedef struct command_login3
{
    BYTE	header;
    char	name[ID_MAX_NUM + 1];
    char	pwd[PASS_MAX_NUM + 1];
    DWORD	adwClientKey[4];
} TPacketCGLogin3;

Change:
typedef struct command_login3
{
    BYTE	header;
    char	name[ID_MAX_NUM + 1];
    char	pwd[PASS_MAX_NUM + 1];
    DWORD	adwClientKey[4];
#ifdef USER_SECURITY_GUARD
	char	cGuardCode[6 + 1];
#endif
} TPacketCGLogin3;
