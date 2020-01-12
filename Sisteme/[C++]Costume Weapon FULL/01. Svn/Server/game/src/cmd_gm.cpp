// 1) Search: ACMD(do_item_purge)
// 2) At the end of their function before close it paste:
#ifdef __WEAPON_COSTUME_SYSTEM__
	if (ch)
	{
		ch->SetPart(PART_WEAPON, 0);
		ch->UpdatePacket();
	}
#endif