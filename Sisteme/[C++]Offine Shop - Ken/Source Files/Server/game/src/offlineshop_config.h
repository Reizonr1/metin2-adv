//=============================================================================
//    File : offlineshop_config.h
//     Use : Use special offline-shop config commands for offline-shop.
//  Author : Ken Kaneki
//    Date : 9/28/2015 - 5:41 PM
//=============================================================================

#ifndef __INC_METIN_II_GAME_OFFLINE_SHOP_CONFIG_H__
#define __INC_METIN_II_GAME_OFFLINE_SHOP_CONFIG_H__


void offlineshop_config_init();


extern BYTE g_bOfflineShopSaveTime;			// Offline-shop save time for MySQL
extern bool g_bNeededMoney;					// Enable required money for open offline-shop
extern DWORD g_dwNeedMoney;					// Required money for open offline-shop

extern int g_iTotalOfflineShopCount;		// If total offline-shop equals to maximum, the system won't allow to open new offline-shop anymore.

extern bool g_bNeededItem;					// Enable required item for open offline-shop
extern int g_iItemVnum;						// Required item vnum for open offline-shop
extern BYTE g_bItemCount;					// Required item count for open offline-shop
extern bool g_bNeedMinLevel;				// Enable requried min level for open an offline-shop
extern BYTE g_bMinLevel;					// Required min level for open an offline-shop

extern WORD g_wCoinsForUnlimited;			// Required coins for open an offline shop.

extern bool g_bOfflineShopMapAllowLimit;	// Enable map allow limit for offline-shop

extern BYTE g_bOfflineShopSocketMax;		// This option would be helpful for who uses more sockets for weapons, armors and accessories
extern bool g_bEnableEmpireLimit;			// This option provides you the player can't build in shinsoo or chunjo if the player is coming from jinno.
#endif