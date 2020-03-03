// 1) Search:
typedef struct packet_item
// 2) Inside this struct search:
    BYTE	count;
// 3) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	DWORD	transmutation;
#endif


// 1) Search:
typedef struct packet_shop_item
// 2) Inside this struct search:
    TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_SLOT_MAX_NUM];
// 3) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	DWORD	transmutation;
#endif