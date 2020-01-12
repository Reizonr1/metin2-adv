

[..]
//find typedef struct packet_shop_item and replace with this
struct packet_shop_item
{   
	DWORD       vnum;
#ifdef FULL_YANG
	long long	price;
#else
	DWORD       price;
#endif
    BYTE        count;
	BYTE		display_pos;
	long	alSockets[ITEM_SOCKET_MAX_NUM];
	TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_MAX_NUM];
};
//find typedef struct SPacketCGMyShop and replace with this
typedef struct SPacketCGMyShop
{
	BYTE	bHeader;
	char	szSign[SHOP_SIGN_MAX_LEN + 1];
	BYTE	bCount;
	#ifdef OFFLINE_SHOP
	BYTE	days;
	#endif
} TPacketCGMyShop;


[..]