
[..]
#ifdef GIFT_SYSTEM
ACMD(do_gift_refresh);
ACMD(do_gift_get);
#endif
#ifdef OFFLINE_SHOP
ACMD(do_shop_refresh);
ACMD(do_shop_yang);
ACMD(do_set_name_shop);
ACMD(do_shop_refresh_items);
ACMD(do_shop_update);
ACMD(do_shop_delete);
ACMD(do_shop_update_item);
#endif
[..]

struct command_info cmd_info[] =
{
	{ "!RESERVED!",	NULL,			0,			POS_DEAD,	GM_IMPLEMENTOR	}, /* 반드시 이 것이 처음이어야 한다. */
#ifdef GIFT_SYSTEM
	{ "gift_refresh",	do_gift_refresh,	0,	POS_DEAD,	GM_PLAYER },
	{ "gift_get", do_gift_get, 0, POS_DEAD,	GM_PLAYER },
#endif
#ifdef OFFLINE_SHOP
	{ "update_shop_item",			do_shop_update_item,				0,	POS_DEAD,	GM_PLAYER },
	{ "refresh_shop_items",			do_shop_refresh_items,				0,	POS_DEAD,	GM_PLAYER },
	{ "refresh_shop",				do_shop_refresh,				0,	POS_DEAD,	GM_PLAYER },
	{ "shop_yang",					do_shop_yang,				0,	POS_DEAD,	GM_PLAYER },
	{ "shop_name",					do_set_name_shop,				0,	POS_DEAD,	GM_PLAYER },
	{ "delete_shop",				do_shop_delete,				0,	POS_DEAD,	GM_IMPLEMENTOR },
	{ "update_shop",				do_shop_update,				0,	POS_DEAD,	GM_IMPLEMENTOR },
#endif
	[..]
};
[..]