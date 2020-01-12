#ifndef __INC_SERVICE_H__
#define __INC_SERVICE_H__

#define _IMPROVED_PACKET_ENCRYPTION_ // 패킷 암호화 개선
//#define __AUCTION__
#define __PET_SYSTEM__
#define __UDP_BLOCK__

//#define __OFFLINE_SHOP__
#ifdef __OFFLINE_SHOP__
/* For the disable any option change 1 value as 0 */
#define __OFFLINE_SHOP_ALLOW_COIN__		1
#define __OFFLINE_SHOP_ALLOW_GOLDBAR__	1
#define __OFFLINE_SHOP_ALLOW_WON__		1
#endif
#endif
