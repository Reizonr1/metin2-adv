// 1) Search:
struct TPacketGCItemDelDeprecated
// 2) Inside this struct search:
	BYTE		count;
// 3) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	DWORD	transmutation;
#endif


// 1) Search:
typedef struct packet_item_set
// 2) Inside this struct search:
	BYTE		count;
// 3) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	DWORD	transmutation;
#endif


// 1) Search:
typedef struct packet_item_update
// 2) Inside this struct search:
	BYTE		count;
// 3) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	DWORD	transmutation;
#endif


// 1) Search:
struct packet_shop_item
// 2) Inside this struct search:
	TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_MAX_NUM];
// 3) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	DWORD	transmutation;
#endif


// 1) Search:
struct packet_exchange
// 2) Inside this struct search:
	TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_MAX_NUM];
// 3) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
	DWORD	dwTransmutation;
#endif


// 1) Search (SHOULD BE AT THE END OF FILE):
#pragma pack()
#endif
// 2) Before this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
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
#endif