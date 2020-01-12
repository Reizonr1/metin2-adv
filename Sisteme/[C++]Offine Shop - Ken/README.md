# Metin2 Offline-shop project by Ken

## 1/7/2016 - Hotfix
1. Fixed a few small problem with Add Item in the current offline shop.
2. Added a sql file. This sql file is only for who uses gold_max in the server.

## 1/6/2016 - Changelogs
1. Fixed non-virtual descructor in offline_shop.cpp
2. Fixed a few small problem about automatic destroy offline shop.
3. Fixed useless function and variables.

## 12/1/2015 - Changelogs
1. Fixed a few small problems
2. Small crash problems solved.
3. Title bug is totally fixed.
4. Fixed a few problem in dynamic buy mechanism.
5. The entered number will be zero when you withdraw your money.
6. Offline shop's pointer color is changed. Also, color of offline shop npc's too. [Default color is orange]
7. You can withdraw your all money.

## 11/27/2015 - Changelogs
1. Added empire limit (You can't build in shinsoo if you're coming from jinno (Empire flag))
2. COfflineShopManager::DestroyOfflineShop function was re-written.
3. Overflow problems solved.

## 11/25/2015 - Changelogs
1. This error is completely fixed (CInputLogin::Analyze: login phase does not handle this packet! header 56)
2. Added a new mechanism for offline shop. You can't open those windows if you don't have an offline shop.
	1. Add Item
	2. Remove Item
	3. Change Price of the item
	4. Change time
3. Get back window is only open when you close your offline shop.

## 11/15/2015 - Changelogs
1. You can now increase maximum gold for the offline shop. You just need to write this in your service.h file and Locale_Inc.h file.
- #define ENABLE_MAXIMUM_YANG_FOR_OFFLINE_SHOP
2. Multi-buy mechanism activated.
3. A few query changed via new one.
4. Offline shop button's location is changed.
5. When your character dead, offline shop window will close itself.
6. If there is no offline-shop name like you enter, the system is not try to destroy offline shop. It will give an error.

## 11/6/2015 - Changelogs
1. Fixed small bugs
2. Added a new gm command to kick the bad offline shop in the game (/kick_offlineshop <owner name of offline shop>)

### 11/5/2015 - Changelogs
1. Added two new config commands.


### 11/2/2015 - Changelogs
1. Added new button inside for Get back the items in the game.
2. You can get your items even If your offline-shop timer is over.
3. Changed icon.tga

This project made by Ken. Anyone has right to re-sell the files on somewhere.

## Offline-shop Change Log 10/16/2015
1. Offline-shop bank's limit is increased. (New limit is 9.223.372.036.854.775.807 yang)
2. OFFLINE_SHOP_MAP_ALLOW_LIMIT is changed via ENABLE_OFFLINE_SHOP_MAP_ALLOW_LIMIT
3. OFFLINE_SHOP_SOCKET_MAX works fine. (This option is not recommend for Soul Binding. Default is 3)

### Offline-shop features
1. You can manage to your offline-shop from the different channels.
2. You can change the item of the price in your offline-shop from the different channels.
3. You can add new item in your offline-shop from the different channels.
4. You can remove the item in your offline-shop from the different channels.
5. You can change the time of your offline-shop from the different channels.
6. You can use special offline-shop config commands for change something before compile the files.

### Warning : You have to create a file in every channels and game99.
1. This file name is OFFLINE_SHOP_CONFIG.
2. Those commands only works in OFFLINE_SHOP_CONFIG.

### How to usage offline-shop config commands?
- OFFLINE_SHOP_SAVE_TIME : Default value is 5. The system will save offline-shop informations in every 5 minutes. (You can change if you want. Maximum value is 10)
- OFFLINE_SHOP_NEED_MONEY : This option provides to you open an offline-shop with required money.
- OFFLINE_SHOP_NEED_ITEM : This option provides to you open an offline-shop with required item.
- OFFLINE_SHOP_TOTAL_COUNT : This option provides to limit offline-shop.
- ENABLE_OFFLINE_SHOP_MAP_ALLOW_LIMIT : This is a boolean. You just use enable/disable or 1/0
- OFFLINE_SHOP_MAP_ALLOW : You can put any limit for open an offline-shop.
- OFFLINE_SHOP_SOCKET_MAX : This is only for who's using socket more than 3.
- MIN_LEVEL: You can put a limit to open an offline-shop for level.
- COINS_FOR_UNLIMITED: You can want some coins to change offline-shop via unlimited.
- EMPIRE_LIMIT: 0/1 (I explainded the feature at top.)

### Offline-shop CONFIG Examples:
- OFFLINE_SAVE_TIME: 5
- OFFLINE_SHOP_NEED_MONEY: enable 500000(yang)
- OFFLINE_SHOP_NEED_MONEY: 1 500000
- OFFLINE_SHOP_NEED_ITEM: enable 11499(item_vnum) 2(count)
- OFFLINE_SHOP_NEED_ITEM: 1 11499(item_vnum) 2(count)
- OFFLINE_SHOP_TOTAL_COUNT: 500
- ENABLE_OFFLINE_SHOP_MAP_ALLOW_LIMIT: enable or disable
- OFFLINE_SHOP_MAP_ALLOW_LIMIT: 0 or 1
- OFFLINE_SHOP_MAP_ALLOW: 1 21 41 (mapIndex)
- OFFLINE_SHOP_SOCKET_MAX: 3
- MIN_LEVEL: enable 5(minimum level)
- MIN_LEVEL: disable 0
- MIN_LEVEL: 1 5(minimum level)
- MIN_LEVEL: 0 0
- COINS_FOR_UNLIMITED: 500
- EMPIRE_LIMIT: 1