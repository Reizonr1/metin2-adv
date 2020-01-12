Arat ;
	HEADER_CG_MYSHOP				= 55,

Altına Ekle ;
	HEADER_CG_OFFLINE_SHOP			= 56,
	HEADER_CG_MY_OFFLINE_SHOP		= 57,

	
	
	
	
Arat ;
	HEADER_GC_QUEST_CONFIRM			= 46,

Altına Ekle ;
	HEADER_GC_OFFLINE_SHOP			= 47,
	HEADER_GC_OFFLINE_SHOP_SIGN		= 48,

	
	
	

Arat ;
	HEADER_GG_CHECK_AWAKENESS		= 29,

Altına Ekle ;
	HEADER_GG_REMOVE_OFFLINE_SHOP           = 30,
    HEADER_GG_CHANGE_OFFLINE_SHOP_TIME      = 31,
    HEADER_GG_OFFLINE_SHOP_BUY              = 32,

	
	
	
Arat ;
typedef struct SPacketGGBlockChat
{
	BYTE	bHeader;
	char	szName[CHARACTER_NAME_MAX_LEN + 1];
	long	lBlockDuration;
} TPacketGGBlockChat;

Altına Ekle ;
typedef struct SPacketGGRemoveOfflineShop
{
	BYTE	bHeader;
	long	lMapIndex;
	char	szNpcName[CHARACTER_NAME_MAX_LEN + 1];
} TPacketGGRemoveOfflineShop;

typedef struct SPacketGGChangeOfflineShopTime
{
	BYTE	bHeader;
	BYTE	bTime;
	long	lMapIndex;
	DWORD	dwOwnerPID;
} TPacketGGChangeOfflineShopTime;

typedef struct SPacketGGOfflineShopBuy
{
	BYTE	bHeader;
	DWORD	dwMoney;
	char	szBuyerName[CHARACTER_NAME_MAX_LEN + 1];        
} TPacketGGOfflineShopBuy;





Arat ;
enum
{
	SHOP_SUBHEADER_CG_END,
	SHOP_SUBHEADER_CG_BUY,
	SHOP_SUBHEADER_CG_SELL,
	SHOP_SUBHEADER_CG_SELL2
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
	SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_EX,
	
Altına Ekle ;
	SHOP_SUBHEADER_GC_UPDATE_ITEM2,
	SHOP_SUBHEADER_GC_REFRESH_MONEY,
	
	
	
	
Arat ;
typedef struct packet_shop_start
{
	DWORD   owner_vid;
	struct packet_shop_item	items[SHOP_HOST_ITEM_MAX_NUM];
} TPacketGCShopStart;

Altına Ekle ;
typedef struct packet_offline_shop_start
{
	DWORD	owner_vid;
	struct packet_shop_item items[OFFLINE_SHOP_HOST_ITEM_MAX_NUM];
} TPacketGCOfflineShopStart;





Arat ;
typedef struct packet_shop_update_price
{
	int				iPrice;
} TPacketGCShopUpdatePrice;


Değiştir ;
typedef struct packet_shop_update_price
{
	BYTE			bPos;
	int				iPrice;
} TPacketGCShopUpdatePrice;






Arat ;
typedef struct packet_shop	// °¡º¯ ÆĞÅ¶
{
	BYTE        header;
	WORD	size; 
	BYTE        subheader;
} TPacketGCShop;

Altına Ekle ;
typedef struct packet_offline_shop_money
{
    DWORD   dwMoney;
} TPacketGCOfflineShopMoney;






Arat ;
typedef struct SPacketCGMyShop
{
	BYTE	bHeader;
	char	szSign[SHOP_SIGN_MAX_LEN + 1];
	BYTE	bCount;
} TPacketCGMyShop;


Altına Ekle ;
typedef struct TPacketCGMyOfflineShop
{
	BYTE	bHeader;
	char	szSign[SHOP_SIGN_MAX_LEN + 1];
	BYTE	bCount;
	BYTE	bTime;
} TPacketCGMyOfflineShop;