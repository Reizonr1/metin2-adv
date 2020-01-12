Arat ;
typedef struct SQuickslot
{
	BYTE	type;
	BYTE	pos;
} TQuickslot;


Üstüne Ekle ;
typedef struct SPlayerItem2
{
	BYTE	bPos;
	BYTE	bCount;

	DWORD	dwVnum;
	long	alSockets[ITEM_SOCKET_MAX_NUM];
	TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_MAX_NUM];
	DWORD	dwPrice;
} TPlayerItem2;



Arat ;
typedef struct SShopTable
{
	DWORD		dwVnum;
	DWORD		dwNPCVnum;

	BYTE		byItemCount;
	TShopItemTable	items[SHOP_HOST_ITEM_MAX_NUM];
} TShopTable;

Üstüne Ekle ;
typedef struct SSOfflineShopItemTable
{
	BYTE		bPos;
	BYTE		bDisplayPos;
	long		lPrice;
} TOfflineShopItemTable;




Arat ;
typedef struct SPacketGDChangeName
{
	DWORD pid;
	char name[CHARACTER_NAME_MAX_LEN + 1];
} TPacketGDChangeName;

Üstüne Ekle ;
typedef struct SSpawnOfflineShopTable
{
	BYTE	bChannel;
	char	szSign[SHOP_SIGN_MAX_LEN + 1];
	long	lMapIndex, x, y;
	int		iTime;
} TSpawnOfflineShopTable;