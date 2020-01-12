Arat ;
	HEADER_CG_MYSHOP                            = 55,

	
Altına Ekle ;
	HEADER_CG_OFFLINE_SHOP						= 56,
	HEADER_CG_MY_OFFLINE_SHOP					= 57,

	
	
	
	
Arat ;
   HEADER_GC_QUEST_CONFIRM                     = 46,

Altına Ekle ;
	HEADER_GC_OFFLINE_SHOP						= 47,
	HEADER_GC_OFFLINE_SHOP_SIGN					= 48,

	
	
	
Arat ;
	SHOP_HOST_ITEM_MAX_NUM = 40,

Altına Ekle ;
	OFFLINE_SHOP_HOST_ITEM_MAX_NUM = 120,

	
	
	
Arat ;
enum
{
    SHOP_SUBHEADER_CG_END,
	SHOP_SUBHEADER_CG_BUY,
	SHOP_SUBHEADER_CG_SELL,
	SHOP_SUBHEADER_CG_SELL2,
};

Değiştir ;
enum
{
	SHOP_SUBHEADER_CG_END,
	SHOP_SUBHEADER_CG_BUY,
	SHOP_SUBHEADER_CG_SELL,
	SHOP_SUBHEADER_CG_SELL2,
	SHOP_SUBHEADER_CG_CHANGE_EDIT_TIME,
	SHOP_SUBHEADER_CG_ADD_ITEM,
	SHOP_SUBHEADER_CG_REMOVE_ITEM,
	SHOP_SUBHEADER_CG_CHANGE_PRICE,
	SHOP_SUBHEADER_CG_DESTROY_OFFLINE_SHOP,
	SHOP_SUBHEADER_CG_REFRESH,
	SHOP_SUBHEADER_CG_REFRESH_MONEY,
	SHOP_SUBHEADER_CG_WITHDRAW_MONEY,
};





Arat ;
typedef struct SShopItemTable
{
    DWORD		vnum;
    BYTE		count;

    TItemPos	pos;			// PC »óÁ¡¿¡¸¸ ÀÌ¿ë
    DWORD		price;			// PC »óÁ¡¿¡¸¸ ÀÌ¿ë
    BYTE		display_pos;	//	PC »óÁ¡¿¡¸¸ ÀÌ¿ë, º¸ÀÏ À§Ä¡.
} TShopItemTable;

Altına Ekle ;
// Offline Shop
typedef struct SOfflineShopItemTable
{
	BYTE		bDisplayPos;
	BYTE		bPos;
	long		lPrice;
} TOfflineShopItemTable;





Arat ;
typedef struct SPacketCGMyShop
{
    BYTE        bHeader;
    char        szSign[SHOP_SIGN_MAX_LEN + 1];
    BYTE        bCount;	// count of TShopItemTable, max 39
} TPacketCGMyShop;

Altına Ekle ;
typedef struct TPacketCGMyOfflineShop
{
	BYTE	bHeader;
	char	szSign[SHOP_SIGN_MAX_LEN + 1];
	BYTE	bCount;
	BYTE	bTime;
} TPacketCGMyOfflineShop;





Arat ;
typedef struct packet_shop_start
{
	struct packet_shop_item		items[SHOP_HOST_ITEM_MAX_NUM];
} TPacketGCShopStart;


Altına Ekle ;
typedef struct packet_offline_shop_start
{
	struct packet_shop_item		items[OFFLINE_SHOP_HOST_ITEM_MAX_NUM];
} TPacketGCOfflineShopStart;




Arat ;
typedef struct packet_shop_update_item
{
	BYTE						pos;
	struct packet_shop_item		item;
} TPacketGCShopUpdateItem;


Altına Ekle ;
typedef struct packet_offline_shop_money
{
	DWORD		dwMoney;
} TPacketGCOfflineShopMoney;





Arat ;
enum EPacketShopSubHeaders
{
	SHOP_SUBHEADER_GC_START,
    SHOP_SUBHEADER_GC_END,
	SHOP_SUBHEADER_GC_UPDATE_ITEM,
	SHOP_SUBHEADER_GC_UPDATE_PRICE,
    SHOP_SUBHEADER_GC_OK,
    SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY,
    SHOP_SUBHEADER_GC_SOLDOUT,
    SHOP_SUBHEADER_GC_INVENTORY_FULL,
    SHOP_SUBHEADER_GC_INVALID_POS,
	SHOP_SUBHEADER_GC_SOLD_OUT,
	SHOP_SUBHEADER_GC_START_EX,
	SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_EX,
};

Değiştir ;
enum EPacketShopSubHeaders
{
	SHOP_SUBHEADER_GC_START,
	SHOP_SUBHEADER_GC_END,
	SHOP_SUBHEADER_GC_UPDATE_ITEM,
	SHOP_SUBHEADER_GC_UPDATE_PRICE,
	SHOP_SUBHEADER_GC_OK,
	SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY,
	SHOP_SUBHEADER_GC_SOLDOUT,
	SHOP_SUBHEADER_GC_INVENTORY_FULL,
	SHOP_SUBHEADER_GC_INVALID_POS,
	SHOP_SUBHEADER_GC_SOLD_OUT,
	SHOP_SUBHEADER_GC_START_EX,
	SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_EX,
	SHOP_SUBHEADER_GC_UPDATE_ITEM2,
	SHOP_SUBHEADER_GC_REFRESH_MONEY,
};
