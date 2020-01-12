//1.) Search:
	HEADER_CG_LOGIN5_OPENID						= 116,
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
	HEADER_CG_OXEVENT_MANAGER					= 117,
#endif

//1.) Search:
	HEADER_GC_MAIN_CHARACTER4_BGM_VOL			= 138,
	// END_OF_SUPPORT_BGM
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
	HEADER_GC_OXEVENT							= 139,
#endif

//1.) Search:
typedef struct packet_item_del
{
    BYTE        header;
    BYTE        pos;
} TPacketGCItemDel;
//2.) Add after:
#ifdef ENABLE_FEATURES_OXEVENT
typedef struct SPacketOxEvent
{
	char	name[12 + 1];
	int		level;
	char	guild[12 + 1];
	int		empire;
	int		job;
	char	date[19 + 1];
	int		correct_answers;
} TPacketCGOxEvent;

typedef struct SPacketOxEventData
{
	BYTE header;
	TPacketCGOxEvent tempInfo[5];
} TPacketCGOxEventData;

typedef struct SPacketCGOxEventManager
{
	BYTE	header;
	int		type;
	char	password[12 + 1];
	int		vnum;
	int		count;
} TPacketCGOxEventManager;
#endif