Arat ;
ACMD (do_clear_affect);

Altına ekle ;
ACMD (do_open_offline_shop);




Arat ;
	{ "do_clear_affect", do_clear_affect, 	0, POS_DEAD,		GM_LOW_WIZARD},

	
Altına ekle ;
#ifdef ENABLE_OFFLINE_SHOP_SYSTEM
	{ "open_offlineshop", do_open_offline_shop, 0, POS_DEAD, GM_PLAYER		},
#endif