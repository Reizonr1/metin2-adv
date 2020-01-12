//Find
HEADER_CG_WHISPER				= 19,

///Add
#ifdef NEW_ADD_INVENTORY
	ENVANTER_BLACK		            = 23,
#endif

//Find
typedef struct command_item_move
{
	BYTE 	header;
	TItemPos	Cell;
	TItemPos	CellTo;
	BYTE	count;
} TPacketCGItemMove;

///Add
#ifdef NEW_ADD_INVENTORY
typedef struct envanter_paketi
{
	BYTE		header;
} TPacketCGEnvanter;
#endif