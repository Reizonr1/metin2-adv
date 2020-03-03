// 1) Search:
		thecore_memcpy(&pack_exchg.aAttr, ((LPITEM) pvData)->GetAttributes(), sizeof(pack_exchg.aAttr));
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
		pack_exchg.dwTransmutation = ((LPITEM) pvData)->GetTransmutation();
#endif


// 1) Search:
		memset(&pack_exchg.aAttr, 0, sizeof(pack_exchg.aAttr));
// 2) After this make a new line and paste:
#ifdef __CHANGELOOK_SYSTEM__
		pack_exchg.dwTransmutation = 0;
#endif