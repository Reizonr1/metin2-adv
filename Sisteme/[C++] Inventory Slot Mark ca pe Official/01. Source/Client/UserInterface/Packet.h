// 1. Replace this packet-struct:
// ********************************* BEGIN ********************************* //
typedef struct packet_exchange
{
    BYTE        header;
    BYTE        subheader;
    BYTE        is_me;
    DWORD       arg1;
    TItemPos       arg2;
    DWORD       arg3;
	long		alValues[ITEM_SOCKET_SLOT_MAX_NUM];
    TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_SLOT_MAX_NUM];
} TPacketGCExchange;
// ********************************** END ********************************** //
// With this:
// ********************************* BEGIN ********************************* //
typedef struct packet_exchange
{
    BYTE        header;
    BYTE        subheader;
    BYTE        is_me;
    DWORD       arg1;
    TItemPos       arg2;
    DWORD       arg3;
#ifdef WJ_ENABLE_TRADABLE_ICON
    TItemPos       arg4;
#endif
	long		alValues[ITEM_SOCKET_SLOT_MAX_NUM];
    TPlayerItemAttribute aAttr[ITEM_ATTRIBUTE_SLOT_MAX_NUM];
} TPacketGCExchange;
// ********************************** END ********************************** //
