[..]
#include "Locale_inc.h"
// Private Shop
typedef struct SShopItemTable
{
    DWORD		vnum;
    BYTE		count;

    TItemPos	pos;			// PC 상점에만 이용
#ifdef ENABLE_FULL_YANG
	long long	price;			// PC 상점에만 이용
#else
	DWORD		price;
#endif
    BYTE		display_pos;	//	PC 상점에만 이용, 보일 위치.
} TShopItemTable;

typedef struct SPacketCGMyShop
{
    BYTE        bHeader;
    char        szSign[SHOP_SIGN_MAX_LEN + 1];
    BYTE        bCount;	// count of TShopItemTable, max 39
#ifdef ENABLE_OFFLINE_SHOP
	BYTE		days;
#endif
} TPacketCGMyShop;

[..]