#ifndef __INC_TABLES_H__
#define __INC_TABLES_H__
#include "service.h"
#include "length.h"

typedef	DWORD IDENT;

enum
{
	HEADER_GD_LOGIN = 1,
	[..]
	HEADER_GD_REQUEST_CHANNELSTATUS=140,
#ifdef OFFLINE_SHOP
	HEADER_GD_SHOP_NAME = 143,
	HEADER_GD_SHOP_CLOSE = 144,
	HEADER_GD_SHOP_UPDATE_ITEM = 145,
#endif

	HEADER_GD_SETUP = 0xff,

	///////////////////////////////////////////////
	HEADER_DG_NOTICE = 1,
	
[..]

	HEADER_DG_UPDATE_LAND = 142,
#ifdef OFFLINE_SHOP
	HEADER_DG_SHOP_NAME = 143,
	HEADER_DG_SHOP_CLOSE = 144,
	HEADER_DG_SHOP_UPDATE_ITEM = 145,
#endif
	HEADER_DG_MARRIAGE_ADD = 150,


};
#ifdef OFFLINE_SHOP
typedef struct SShopPrice
{
	int days;
	int time;
	long long price;
} TShopCost;
typedef struct command_shop_name
{
	DWORD shop_id;
	char szSign[SHOP_SIGN_MAX_LEN + 1];
} TPacketShopName;
typedef struct command_shop_close
{
	DWORD shop_id;
	DWORD pid;
} TPacketShopClose;
typedef struct command_shop_update_item
{
	DWORD shop_id;
	bool	shop_locked;
} TPacketShopUpdateItem;
#endif

typedef struct SShopItemTable
{
	DWORD		vnum;
	BYTE		count;

    TItemPos	pos;			// PC »óÁˇżˇ¸¸ ŔĚżë
	#ifdef FULL_YANG
	long long		price;	// PC, shop_table_ex.txt »óÁˇżˇ¸¸ ŔĚżë
	#else
	DWORD		price;	// PC, shop_table_ex.txt »óÁˇżˇ¸¸ ŔĚżë
	#endif
	BYTE		display_pos; // PC, shop_table_ex.txt »óÁˇżˇ¸¸ ŔĚżë, ş¸ŔĎ Ŕ§Äˇ.
} TShopItemTable;
[..]