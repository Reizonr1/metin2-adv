// 1) Search:
			thecore_memcpy(pack2.items[i].aAttr, item.pkItem->GetAttributes(), sizeof(pack2.items[i].aAttr));
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
			pack2.items[i].transmutation = item.pkItem->GetTransmutation();
#endif