Search:
enum EWindows
{
	RESERVED_WINDOW,
	INVENTORY,				// ±âº» ÀÎº¥Åä¸®. (45Ä­ Â¥¸®°¡ 2ÆäÀÌÁö Á¸Àç = 90Ä­)
	EQUIPMENT,
	SAFEBOX,
	MALL,
	DRAGON_SOUL_INVENTORY,
	GROUND,					// NOTE: 2013³â 2¿ù5ÀÏ ÇöÀç±îÁö unused.. ¿Ö ÀÖ´Â°ÅÁö???
	BELT_INVENTORY,			// NOTE: W2.1 ¹öÀü¿¡ »õ·Î Ãß°¡µÇ´Â º§Æ® ½½·Ô ¾ÆÀÌÅÛÀÌ Á¦°øÇÏ´Â º§Æ® ÀÎº¥Åä¸®

	WINDOW_TYPE_MAX,
};

Change:
enum EWindows
{
	RESERVED_WINDOW,
	INVENTORY,				// ±âº» ÀÎº¥Åä¸®. (45Ä­ Â¥¸®°¡ 2ÆäÀÌÁö Á¸Àç = 90Ä­)
	EQUIPMENT,
	SAFEBOX,
	MALL,
	DRAGON_SOUL_INVENTORY,
#ifdef __OFFLINE_SHOP__
	OFFLINE_SHOP,
	SAFEBOX_OFFLINE_SHOP,
#endif
	BELT_INVENTORY,			// NOTE: W2.1 ¹öÀü¿¡ »õ·Î Ãß°¡µÇ´Â º§Æ® ½½·Ô ¾ÆÀÌÅÛÀÌ Á¦°øÇÏ´Â º§Æ® ÀÎº¥Åä¸®
	GROUND,
	WINDOW_TYPE_MAX,
};

https://puu.sh/sgKbU/0392c0c588.png

---

Search:
typedef struct packet_shop_item
{
    DWORD       vnum;
    DWORD       price;
    BYTE        count;
	BYTE		display_pos;
	long		alSockets[ITEM_SOCKET_SLOT_MAX_NUM];
    TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_SLOT_MAX_NUM];
} TShopItemData;

Change:
typedef struct packet_shop_item
{
    DWORD       vnum;
    DWORD       price;
#ifdef __OFFLINE_SHOP__
	DWORD		price2;
	DWORD		price3;
	DWORD		price4;
#endif
    BYTE        count;
	BYTE		display_pos;
	long		alSockets[ITEM_SOCKET_SLOT_MAX_NUM];
    TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_SLOT_MAX_NUM];
#ifdef __OFFLINE_SHOP__
	int			isSold;
#endif
} TShopItemData;

https://puu.sh/sgKcP/55cc8fdcaf.png