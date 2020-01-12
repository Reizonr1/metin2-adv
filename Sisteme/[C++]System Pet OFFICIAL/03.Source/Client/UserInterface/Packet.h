//Search in this file:
	HEADER_GC_SCRIPT							= 45,
    HEADER_GC_QUEST_CONFIRM                     = 46,

//Add after:

#ifdef NEW_PET_SYSTEM
	HEADER_CG_PetSetName						= 147,
#endif

//Search in this file:

typedef struct command_login5
{
    BYTE	header;
    char	authKey[OPENID_AUTHKEY_LEN + 1];
    DWORD	adwClientKey[4];
} TPacketCGLogin5;

//Add after:

#ifdef NEW_PET_SYSTEM
typedef struct packet_RequestPetName
{
	BYTE byHeader;
	char petname[13];
} TPacketCGRequestPetName;
#endif

//Search in this file:
//In typedef struct packet_update_char
	DWORD		dwGuildID;
    short       sAlignment;

//Add after:
#ifdef NEW_PET_SYSTEM
	DWORD		dwLevel;
#endif