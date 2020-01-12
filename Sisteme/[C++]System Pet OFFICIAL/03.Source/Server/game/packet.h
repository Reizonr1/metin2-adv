//Search in this file:
	HEADER_GC_PING				= 44,
	HEADER_GC_SCRIPT				= 45,
	HEADER_GC_QUEST_CONFIRM			= 46,

//Add after:

#ifdef NEW_PET_SYSTEM
        HEADER_CG_PetSetName = 147,
#endif

//Search in this file:
typedef struct command_matrix_card
{
	BYTE	bHeader;
	char	szAnswer[MATRIX_ANSWER_MAX_LEN + 1];
} TPacketCGMatrixCard;

//Add after this:
#ifdef NEW_PET_SYSTEM
typedef struct packet_RequestPetName
{
	BYTE byHeader;
	char petname[13];

}TPacketCGRequestPetName;
#endif

//Searh in this file:
	DWORD	dwGuildID;
	short	sAlignment;
//From: typedef struct packet_update_char
//Add after:
#ifdef NEW_PET_SYSTEM
	DWORD   dwLevel;
#endif
