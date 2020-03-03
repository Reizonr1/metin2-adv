// 1) Search:
bool CPythonNetworkStream::RecvSafeBoxSetPacket()
// 2) Inside this func search:
	kItemData.count = kItemSet.count;
// 3) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	kItemData.transmutation = kItemSet.transmutation;
#endif


// 1) Search:
bool CPythonNetworkStream::RecvMallItemSetPacket()
// 2) Inside this func search:
	kItemData.count = kItemSet.count;
// 3) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	kItemData.transmutation = kItemSet.transmutation;
#endif


// 1) Search:
bool CPythonNetworkStream::RecvItemSetPacket()
// 2) Inside this func search:
	kItemData.count	= packet_item_set.count;
// 3) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	kItemData.transmutation = packet_item_set.transmutation;
#endif


// 1) Search:
bool CPythonNetworkStream::RecvItemSetPacket2()
// 2) Inside this func search:
	kItemData.count	= packet_item_set.count;
// 3) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	kItemData.transmutation = packet_item_set.transmutation;
#endif


// 1) Search:
bool CPythonNetworkStream::RecvItemUpdatePacket()
// 2) Inside this func search:
	rkPlayer.SetItemCount(packet_item_update.Cell, packet_item_update.count);
// 3) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
	rkPlayer.SetItemTransmutation(packet_item_update.Cell, packet_item_update.transmutation);
#endif