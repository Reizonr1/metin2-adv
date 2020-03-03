// Search for:
	CPythonSafeBox::Instance().SetItemData(kItemSet.Cell.cell, kItemData);

// Add Before:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	kItemData.dwVnum = kItemSet.dwVnum;
#endif

// Search for:
	CPythonSafeBox::Instance().SetMallItemData(kItemSet.Cell.cell, kItemData);

// Add Before:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	kItemData.dwVnum = kItemSet.dwVnum;
#endif

// Search for: On bool CPythonNetworkStream::RecvItemSetPacket()
	rkPlayer.SetItemData(packet_item_set.Cell, kItemData);

// Add Before:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	kItemData.dwVnum = packet_item_set.dwVnum;
#endif

// Search for: bool CPythonNetworkStream::RecvItemSetPacket2()
	rkPlayer.SetItemData(packet_item_set.Cell, kItemData);

// Add Before:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	kItemData.dwVnum = packet_item_set.dwVnum;
#endif

// Search for: On bool CPythonNetworkStream::RecvItemUpdatePacket()
	rkPlayer.SetItemCount(packet_item_update.Cell, packet_item_update.count);

// Add Under:
#ifdef ENABLE_CHANGE_LOOK_SYSTEM
	rkPlayer.SetItemLook(packet_item_update.Cell, packet_item_update.dwVnum);
#endif
