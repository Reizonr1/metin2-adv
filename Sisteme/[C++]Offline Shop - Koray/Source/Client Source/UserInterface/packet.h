Search:
	HEADER_CG_STATE_CHECKER						=

Add it under:
#ifdef __OFFLINE_SHOP__
	HEADER_CG_SAFEBOX_MONEY						= 63,
#endif

https://puu.sh/sgKx8/b476723d4e.png

---

Search:
    HEADER_GC_SAFEBOX_MONEY_CHANGE              = 84,

change:
#ifdef __OFFLINE_SHOP__
	HEADER_GC_SAFEBOX_MONEY_CHANGE				= 103,
#endif

---

Search:
	SHOP_HOST_ITEM_MAX_NUM = 40,

Change:
#ifdef __OFFLINE_SHOP__
	SHOP_HOST_ITEM_MAX_NUM = 90,
#else
	SHOP_HOST_ITEM_MAX_NUM = 40,
#endif

https://puu.sh/sgKzX/4f4b59d4c5.png

---

Search:
typedef struct command_safebox_money
{
    BYTE        bHeader;
    BYTE        bState;
    DWORD       dwMoney;
} TPacketCGSafeboxMoney;

Change:
typedef struct command_safebox_money
{
    BYTE        bHeader;
    BYTE        bState;
#ifdef __OFFLINE_SHOP__
	int64_t		lMoney;
#else
    long       lMoney;
#endif
} TPacketCGSafeboxMoney;

https://puu.sh/sgKBc/00f7afeb2a.png

---

Search:
typedef struct SShopItemTable
{
    DWORD		vnum;
    BYTE		count;

    TItemPos	pos;			// PC »óÁ¡¿¡¸¸ ÀÌ¿ë
    DWORD		price;			// PC »óÁ¡¿¡¸¸ ÀÌ¿ë
    BYTE		display_pos;	//	PC »óÁ¡¿¡¸¸ ÀÌ¿ë, º¸ÀÏ À§Ä¡.
} TShopItemTable;

Change:
typedef struct SShopItemTable
{
    DWORD		vnum;
    BYTE		count;

    TItemPos	pos;			// PC »óÁ¡¿¡¸¸ ÀÌ¿ë
    DWORD		price;			// PC »óÁ¡¿¡¸¸ ÀÌ¿ë
#ifdef __OFFLINE_SHOP__
	DWORD		price2;			// PC »óÁ¡¿¡¸¸ ÀÌ¿ë
	DWORD		price3;			// PC »óÁ¡¿¡¸¸ ÀÌ¿ë
	DWORD		price4;			// PC »óÁ¡¿¡¸¸ ÀÌ¿ë
#endif
	BYTE		display_pos;	//	PC »óÁ¡¿¡¸¸ ÀÌ¿ë, º¸ÀÏ À§Ä¡.
} TShopItemTable;

https://puu.sh/sgKCm/2cf86810db.png

---

Search:
typedef struct SPacketCGMyShop
{
    BYTE        bHeader;
    char        szSign[SHOP_SIGN_MAX_LEN + 1];
    BYTE        bCount;	// count of TShopItemTable, max 39
} TPacketCGMyShop;

Change:
typedef struct SPacketCGMyShop
{
    BYTE        bHeader;
    char        szSign[SHOP_SIGN_MAX_LEN + 1];
#ifdef __OFFLINE_SHOP__
	BYTE        bType;
	BYTE		bSize;
	BYTE		bColor;
#endif
    BYTE        bCount;	// count of TShopItemTable, max 39
} TPacketCGMyShop;

https://puu.sh/sgKDU/e9fca36543.png

---

Search:
typedef struct packet_shop_start
{
	struct packet_shop_item		items[SHOP_HOST_ITEM_MAX_NUM];
} TPacketGCShopStart;

Change:
typedef struct packet_shop_start
{
#ifdef __OFFLINE_SHOP__
	DWORD	vid;
	DWORD	grid_type;
#endif
	DWORD	owner_vid;
	struct packet_shop_item		items[SHOP_HOST_ITEM_MAX_NUM];
} TPacketGCShopStart;

https://puu.sh/sgKF6/bc40425f77.png

---

Search:
typedef struct packet_shop_start_ex // ´ÙÀ½¿¡ TSubPacketShopTab* shop_tabs ÀÌ µû¶ó¿È.
{
	typedef struct sub_packet_shop_tab
	{
		char name[SHOP_TAB_NAME_MAX];
		BYTE coin_type;
		packet_shop_item items[SHOP_HOST_ITEM_MAX_NUM];
	} TSubPacketShopTab;
	DWORD owner_vid;
	BYTE shop_tab_count;
} TPacketGCShopStartEx;

Change:
typedef struct packet_shop_start_ex // ´ÙÀ½¿¡ TSubPacketShopTab* shop_tabs ÀÌ µû¶ó¿È.
{
	typedef struct sub_packet_shop_tab
	{
		char name[SHOP_TAB_NAME_MAX];
		BYTE coin_type;
#ifdef __OFFLINE_SHOP__
		TShopItemData items[SHOP_HOST_ITEM_MAX_NUM];
#else
		packet_shop_item items[SHOP_HOST_ITEM_MAX_NUM];
#endif
	} TSubPacketShopTab;
#ifdef __OFFLINE_SHOP__
	DWORD	vid;
#endif
	DWORD owner_vid;
	BYTE shop_tab_count;
} TPacketGCShopStartEx;

https://puu.sh/sgKGo/f75fa629bb.png

---

Search:
typedef struct packet_shop_update_item
{
	BYTE						pos;
	struct packet_shop_item		item;
} TPacketGCShopUpdateItem;

Change:
typedef struct packet_shop_update_item
{
	BYTE						pos;
#ifdef __OFFLINE_SHOP__
	TShopItemData	item;
#else
	struct packet_shop_item		item;
#endif
} TPacketGCShopUpdateItem;

https://puu.sh/sgKHa/dbaa2b8b9a.png

---

Search:
	SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_EX,

Add it under:
#ifdef __OFFLINE_SHOP__
	SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_COIN,
	SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_GOLDBAR,
	SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_WON,
	SHOP_SUBHEADER_GC_UPDATE_MONEY,
#endif

https://puu.sh/sgKIZ/b8993bb573.png

---

Search:
typedef struct packet_safebox_money_change
{
    BYTE bHeader;
    DWORD dwMoney;
} TPacketGCSafeboxMoneyChange;

Change:
typedef struct packet_safebox_money_change
{
	BYTE bHeader;
#ifdef __OFFLINE_SHOP__
	uint64_t dwMoney;
#else
	DWORD dwMoney;
#endif
} TPacketGCSafeboxMoneyChange;