// Search for:
typedef struct packet_item
{
    DWORD       vnum;
    BYTE        count;
	DWORD		flags;
	DWORD		anti_flags;
	long		alSockets[ITEM_SOCKET_SLOT_MAX_NUM];
    TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_SLOT_MAX_NUM];
} TItemData;

// Replace their function with:
typedef struct packet_item
{
    DWORD       vnum;
    BYTE        count;
	DWORD		flags;
	DWORD		anti_flags;
	long		alSockets[ITEM_SOCKET_SLOT_MAX_NUM];
    TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_SLOT_MAX_NUM];
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	DWORD		dwVnum;
#endif
} TItemData;

// Search for:
typedef struct packet_shop_item
{
    DWORD       vnum;
    DWORD       price;
    BYTE        count;
	BYTE		display_pos;
	long		alSockets[ITEM_SOCKET_SLOT_MAX_NUM];
    TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_SLOT_MAX_NUM];
} TShopItemData;

// Replace their function with:
typedef struct packet_shop_item
{
    DWORD       vnum;
    DWORD       price;
    BYTE        count;
	BYTE		display_pos;
	long		alSockets[ITEM_SOCKET_SLOT_MAX_NUM];
    TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_SLOT_MAX_NUM];
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	DWORD		dwLookVnum;
#endif
} TShopItemData;
