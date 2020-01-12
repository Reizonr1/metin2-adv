#ifndef __INC_METIN_II_GAME_OFFLINE_SHOP_CONFIG_H__
#define __INC_METIN_II_GAME_OFFLINE_SHOP_CONFIG_H__

void offlineshop_config_init();


extern BYTE g_bOfflineShopSaveTime;
extern bool g_bNeedMoney;
extern DWORD g_dwNeedMoney;
extern int g_iTotalOfflineShopCount;

extern bool g_bNeedItem;
extern int g_iItemVnum;
extern BYTE g_bItemCount;
extern bool g_bOfflineShopMapAllowLimit;
extern bool g_bEnableRespawnOfflineShop;
extern BYTE g_bOfflineShopSocketMax;

#endif