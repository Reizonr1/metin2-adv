// Search for:
			thecore_memcpy(pack2.items[i].alSockets, item.pkItem->GetSockets(), sizeof(pack2.items[i].alSockets));
			thecore_memcpy(pack2.items[i].aAttr, item.pkItem->GetAttributes(), sizeof(pack2.items[i].aAttr));

// Add Under:
#ifdef __CHANGE_LOOK_SYSTEM__
			pack2.items[i].dwLookVnum = item.pkItem->GetItemLook();
#endif
