// 1) Search:
typedef struct packet_set_item
// 2) Inside this struct search:
	BYTE		count;
// 3) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	DWORD	transmutation;
#endif


// 1) Search:
typedef struct packet_set_item2
// 2) Inside this struct search:
	BYTE		count;
// 3) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	DWORD	transmutation;
#endif


// 1) Search:
typedef struct packet_update_item
// 2) Inside this struct search:
	BYTE		count;
// 3) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	DWORD	transmutation;
#endif


// 1) Search:
} TPacketGCExchange;
// 2) Before this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	DWORD	dwTransmutation;
#endif


// 1) Search:
} TChannelStatus;
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
enum EChangeLookInfo
{
	CL_WINDOW_MAX_MATERIALS = 2,
	CL_CLEAN_ATTR_VALUE0 = 8,
};

enum
{
	HEADER_CG_CL = 213,
	HEADER_GC_CL = 218,
	CL_SUBHEADER_OPEN = 0,
	CL_SUBHEADER_CLOSE,
	CL_SUBHEADER_ADD,
	CL_SUBHEADER_REMOVE,
	CL_SUBHEADER_REFINE,
};

typedef struct SPacketChangeLook
{
	BYTE	header;
	BYTE	subheader;
	DWORD	dwCost;
	BYTE	bPos;
	TItemPos	tPos;
} TPacketChangeLook;

typedef struct SChangeLookMaterial
{
	BYTE	bHere;
	WORD	wCell;
} TChangeLookMaterial;
#endif