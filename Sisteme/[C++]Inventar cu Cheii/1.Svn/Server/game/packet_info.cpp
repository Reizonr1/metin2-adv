//Find
Set(HEADER_CG_ITEM_MOVE, sizeof(TPacketCGItemMove), "ItemMove", true);

///Add
#ifdef NEW_ADD_INVENTORY
	Set(ENVANTER_BLACK, sizeof(TPacketCGEnvanter), "Envanter", true);
#endif