// 1) Search: typedef struct SSimplePlayerInformation
// 2) Delete their function and paste:
typedef struct SSimplePlayerInformation
{
    DWORD	dwID;
    char	szName[CHARACTER_NAME_MAX_LEN + 1];
    BYTE	byJob;
    BYTE	byLevel;
    DWORD	dwPlayMinutes;
    BYTE	byST, byHT, byDX, byIQ;
    WORD	wMainPart;
    BYTE	bChangeName;
	WORD	wHairPart;
	WORD	wAccePart;
    BYTE	bDummy[4];
	long	x, y;
	LONG	lAddr;
	WORD	wPort;
	BYTE	bySkillGroup;
} TSimplePlayerInformation;

// 1) Search: CHR_EQUIPPART_HAIR,
// 2) After make a new line and paste:
	CHR_EQUIPPART_ACCE,

// 1) Search: SE_EQUIP_LOVE_PENDANT,
// 2) After make a new line and paste:
	SE_ACCE_SUCCEDED_1,
	SE_EQUIP_ACCE_1,
	SE_EQUIP_ACCE_2,
	SE_EQUIP_ACCE_3,
	SE_EQUIP_ACCE_4,