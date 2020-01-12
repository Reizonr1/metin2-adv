Search:
	HEADER_CG_STATE_CHECKER				=

Add it under:
#ifdef __OFFLINE_SHOP__
	HEADER_CG_SAFEBOX_MONEY				= 63,
#endif

https://puu.sh/sgHbG/038bf0022d.png

---

Search:
	HEADER_GC_RESPOND_CHANNELSTATUS					=

Add it under:
#ifdef __OFFLINE_SHOP__
	HEADER_GC_SAFEBOX_MONEY_CHANGE					= 103,
#endif

https://puu.sh/sgHcU/6b23146b8d.png

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

https://puu.sh/sgHeO/f45a5d3d83.png

---

Search:
struct packet_shop_item
{
	DWORD       vnum;
	DWORD       price;
	BYTE        count;
	BYTE		display_pos;
	long	alSockets[ITEM_SOCKET_MAX_NUM];
	TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_MAX_NUM];
};

Change:
struct packet_shop_item
{
	DWORD       vnum;
	DWORD       price;
#ifdef __OFFLINE_SHOP__	
	DWORD       price2;
	DWORD       price3;
	DWORD       price4;
#endif
	BYTE        count;
	BYTE		display_pos;
	long	alSockets[ITEM_SOCKET_MAX_NUM];
	TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_MAX_NUM];
#ifdef __OFFLINE_SHOP__
	int			isSold;
#endif
};

https://puu.sh/sgHfV/a3a1a92432.png

---

Search:
typedef struct packet_shop_start
{
	DWORD   owner_vid;
	struct packet_shop_item	items[SHOP_HOST_ITEM_MAX_NUM];
} TPacketGCShopStart;

Change:
typedef struct packet_shop_start
{
#ifdef __OFFLINE_SHOP__
	DWORD	vid;
	DWORD	grid_type;
#endif
	DWORD   owner_vid;
	struct packet_shop_item	items[SHOP_HOST_ITEM_MAX_NUM];
} TPacketGCShopStart;

https://puu.sh/sgHho/3359c9b329.png
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
		packet_shop_item items[SHOP_HOST_ITEM_MAX_NUM];
	} TSubPacketShopTab;
#ifdef __OFFLINE_SHOP__
	DWORD	vid;
#endif
	DWORD owner_vid;
	BYTE shop_tab_count;
} TPacketGCShopStartEx;

https://puu.sh/sgHiU/812c1ecbb2.png
---

Search:
typedef struct command_safebox_money
{
	BYTE        bHeader;
	BYTE        bState;
	long	lMoney;
} TPacketCGSafeboxMoney;

typedef struct packet_safebox_money_change
{
	BYTE	bHeader;
	long	lMoney;
} TPacketGCSafeboxMoneyChange;

Change:
typedef struct command_safebox_money
{
	BYTE        bHeader;
	BYTE        bState;
#ifdef __OFFLINE_SHOP__
	int64_t		lMoney;
#else
	long		lMoney;
#endif
} TPacketCGSafeboxMoney;

typedef struct packet_safebox_money_change
{
	BYTE		bHeader;
#ifdef __OFFLINE_SHOP__
	int64_t		lMoney;
#else
	long		lMoney;
#endif
} TPacketGCSafeboxMoneyChange;

https://puu.sh/sgHjS/25c3447b3e.png

---

Search:
typedef struct SPacketCGMyShop
{
	BYTE	bHeader;
	char	szSign[SHOP_SIGN_MAX_LEN + 1];
	BYTE	bCount;
} TPacketCGMyShop;

Change:
typedef struct SPacketCGMyShop
{
	BYTE	bHeader;
	char	szSign[SHOP_SIGN_MAX_LEN + 1];
#ifdef __OFFLINE_SHOP__
	BYTE    bType;
	BYTE	bSize;
	BYTE	bColor;
#endif
	BYTE	bCount;
} TPacketCGMyShop;

https://puu.sh/sgHlU/73344ad647.png