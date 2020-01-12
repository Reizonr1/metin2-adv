If have not add it:
#include "service.h"

---

Search:
	HEADER_GD_REQUEST_CHANNELSTATUS	= 140,

Add it under:
#ifdef __OFFLINE_SHOP__
	HEADER_GD_SAFEBOX_MONEY = 150,

	HEADER_GD_COLLECT_OFFLINE_SHOP_ITEM = 151,

	HEADER_GD_OFFLINE_SHOP_ENTRY = 152,
	HEADER_GD_OFFLINE_SHOP_REMOVE = 153,
#endif

http://i.imgur.com/M76RGlB.png
---

Search:
	HEADER_DG_RESPOND_CHANNELSTATUS		= 181,

Add it under:
#ifdef __OFFLINE_SHOP__
	HEADER_DG_SAFEBOX_MONEY = 190,
	HEADER_DG_COLLECT_OFFLINE_SHOP_ITEM = 191,
#endif

http://i.imgur.com/zCpJflm.png
---

Search:
typedef struct SShopItemTable
{
	DWORD		vnum;
	BYTE		count;

    TItemPos	pos;			// PC »óÁ¡¿¡¸¸ ÀÌ¿ë
	DWORD		price;	// PC, shop_table_ex.txt »óÁ¡¿¡¸¸ ÀÌ¿ë
	BYTE		display_pos; // PC, shop_table_ex.txt »óÁ¡¿¡¸¸ ÀÌ¿ë, º¸ÀÏ À§Ä¡.
} TShopItemTable;

Change:
typedef struct SShopItemTable
{
	DWORD		vnum;
	BYTE		count;

    TItemPos	pos;			// PC »óÁ¡¿¡¸¸ ÀÌ¿ë
	DWORD		price;	// PC, shop_table_ex.txt »óÁ¡¿¡¸¸ ÀÌ¿ë
#ifdef __OFFLINE_SHOP__
	DWORD		price2;
	DWORD		price3;
	DWORD		price4;
#endif
	BYTE		display_pos; // PC, shop_table_ex.txt »óÁ¡¿¡¸¸ ÀÌ¿ë, º¸ÀÏ À§Ä¡.
} TShopItemTable;

http://i.imgur.com/6qnUhZf.png
---

Search:
typedef struct SShopTable
{
	DWORD		dwVnum;
	DWORD		dwNPCVnum;

	BYTE		byItemCount;
	TShopItemTable	items[SHOP_HOST_ITEM_MAX_NUM];
} TShopTable;

Add it under:
#ifdef __OFFLINE_SHOP__
typedef struct SOfflineShopTable
{
	DWORD		dwAID;
	DWORD		dwPID;

	DWORD		dwX;
	DWORD		dwY;
	DWORD		dwMapIndex;

	DWORD		dwChannel;

	DWORD		dwDuration;
	DWORD		dwInstallTime;

	uint64_t	ullMoney;

	char		szName[CHARACTER_NAME_MAX_LEN + 1];
	char		szSign[SHOP_SIGN_MAX_LEN + 1];

	TPlayerItem	items[SHOP_HOST_ITEM_MAX_NUM]; /* Game standard struct based */
	DWORD		items2[SHOP_HOST_ITEM_MAX_NUM]; /* DB formatted item array */

	DWORD		price[SHOP_HOST_ITEM_MAX_NUM];
	DWORD		price2[SHOP_HOST_ITEM_MAX_NUM]; /* Alternative price array, default coin */
	DWORD		price3[SHOP_HOST_ITEM_MAX_NUM]; /* Alternative price array 2, default gold bar */
	DWORD		price4[SHOP_HOST_ITEM_MAX_NUM]; /* Alternative price array 3, default won */

	DWORD		dwSize; /* Grid size of shop */

	DWORD		dwColor; /* Shop style */
} TOfflineShopTable;
#endif

http://i.imgur.com/65q7Abq.png
---

Search:
typedef struct SSafeboxTable
{
	DWORD	dwID;
	BYTE	bSize;
	DWORD	dwGold;
	WORD	wItemCount;
} TSafeboxTable;

Change:
typedef struct SSafeboxTable
{
	DWORD	dwID;
	BYTE	bSize;
#ifdef __OFFLINE_SHOP__
	uint64_t dwGold;
#else
	DWORD	dwGold;
#endif
	WORD	wItemCount;
} TSafeboxTable;

http://i.imgur.com/LJz5tQh.png
---

Search:
typedef struct SChannelStatus
{
	short nPort;
	BYTE bStatus;
} TChannelStatus;

Add it under:
#ifdef __OFFLINE_SHOP__
typedef struct SSafeboxMoney
{
	DWORD dwAID;
	BYTE bType;
	int64_t llAmount;
} TSafeboxMoney;
#endif

http://i.imgur.com/pmwnBnA.png