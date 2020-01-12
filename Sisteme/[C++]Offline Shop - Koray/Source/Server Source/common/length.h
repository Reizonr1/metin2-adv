If have not add it:
#include "service.h"

---

Search:
	SHOP_SIGN_MAX_LEN		= 32,

Add it under:
#ifdef __OFFLINE_SHOP__
	OFFLINE_SHOP_MAX_COUNT	= 2, /* For every player */
	OFFLINE_SHOP_CHANNEL_LIMIT = 500,
#endif

http://i.imgur.com/URnTZMq.png
---

Search:
	SHOP_HOST_ITEM_MAX_NUM	= 40,	/* È£½ºÆ®ÀÇ ÃÖ´ë ¾ÆÀÌÅÛ °³¼ö */
	SHOP_GUEST_ITEM_MAX_NUM = 18,	/* °Ô½ºÆ®ÀÇ ÃÖ´ë ¾ÆÀÌÅÛ °³¼ö */

	SHOP_PRICELIST_MAX_NUM	= 40,	///< °³ÀÎ»óÁ¡ °¡°İÁ¤º¸ ¸®½ºÆ®¿¡¼­ À¯ÁöÇÒ °¡°İÁ¤º¸ÀÇ ÃÖ´ë °¹¼ö

Change:
#ifdef __OFFLINE_SHOP__
	SHOP_HOST_ITEM_MAX_NUM = 90,	/* È£½ºÆ®ÀÇ ÃÖ´ë ¾ÆÀÌÅÛ °³¼ö */
#else
	SHOP_HOST_ITEM_MAX_NUM	= 40,	/* È£½ºÆ®ÀÇ ÃÖ´ë ¾ÆÀÌÅÛ °³¼ö */
#endif
	SHOP_GUEST_ITEM_MAX_NUM = 18,	/* °Ô½ºÆ®ÀÇ ÃÖ´ë ¾ÆÀÌÅÛ °³¼ö */

#ifdef __OFFLINE_SHOP__
	SHOP_PRICELIST_MAX_NUM = 90,	///< °³ÀÎ»óÁ¡ °¡°İÁ¤º¸ ¸®½ºÆ®¿¡¼­ À¯ÁöÇÒ °¡°İÁ¤º¸ÀÇ ÃÖ´ë °¹¼ö
#else
	SHOP_PRICELIST_MAX_NUM	= 40,	///< °³ÀÎ»óÁ¡ °¡°İÁ¤º¸ ¸®½ºÆ®¿¡¼­ À¯ÁöÇÒ °¡°İÁ¤º¸ÀÇ ÃÖ´ë °¹¼ö
#endif

http://i.imgur.com/3f5Y4HR.png
---

Search:
	DRAGON_SOUL_INVENTORY,

Add it under:
#ifdef __OFFLINE_SHOP__
	OFFLINE_SHOP,
	SAFEBOX_OFFLINE_SHOP,
#endif

http://i.imgur.com/JyskMbu.png