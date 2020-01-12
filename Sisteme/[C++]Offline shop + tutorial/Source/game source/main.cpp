Arat ;
#include <boost/bind.hpp>

Altına Ekle ;
#include "offlineshop_manager.h"
#include "offlineshop_config.h"





Arat ;
CShopManager	shop_manager;

Altına Ekle ;
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
	COfflineShopManager offlineshop_manager;
#endif




Arat ;
	// LOCALE_SERVICE
	config_init(st_localeServiceName);
	// END_OF_LOCALE_SERVICE

Altına Ekle ;
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
	// OFFLINE_SHOP_CONFIG
	offlineshop_config_init();
	// END_OF_OFFLINE_SHOP_CONFIG
#endif