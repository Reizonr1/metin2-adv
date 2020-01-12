// Seach for:
	HEADER_GC_TARGET			 	= 63,

// Add (Under):
#ifdef __SEND_TARGET_INFO__
	HEADER_GC_TARGET_INFO			= 58,
	HEADER_CG_TARGET_INFO_LOAD		= 59,
#endif

// Search for:
typedef struct packet_target

// Add (Under & Whole function):
#ifdef __SEND_TARGET_INFO__
typedef struct packet_target_info
{
	BYTE	header;
	DWORD	dwVID;
	DWORD	race;
	DWORD	dwVnum;
	BYTE	count;
} TPacketGCTargetInfo;

typedef struct packet_target_info_load
{
	BYTE header;
	DWORD dwVID;
} TPacketCGTargetInfoLoad;
#endif