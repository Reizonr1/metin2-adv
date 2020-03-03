// Search for:
			pack.header = HEADER_GC_ITEM_SET;
			pack.Cell = Cell;

// Add Under:
#ifdef __CHANGE_LOOK_SYSTEM__
			pack.dwVnum = pItem->GetItemLook();
#endif

// Search for:
			pack.header = HEADER_GC_ITEM_DEL;
			pack.Cell = Cell;

// Add Under:
#ifdef __CHANGE_LOOK_SYSTEM__
			pack.dwVnum = 0;
#endif

// Search for:
					case USE_BAIT:

// Add Before:
#ifdef __CHANGE_LOOK_SYSTEM__
						case USE_RESET_LOOK_VNUM:
						{
							LPITEM item2;
							if (!IsValidItemPosition(DestCell) || !(item2 = GetItem(DestCell)))
								return false;

							if (item2->IsEquipped())
							{
								BuffOnAttr_RemoveBuffsFromItem(item2);
							}

							if (item2->IsExchanging() || item2->IsEquipped())
								return false;

							if (item2->GetItemLook())
							{
								item2->SetItemLook(0);
								item->SetCount(item->GetCount() - 1);
							}
						}
						break;
#endif

// Go to the end of the file and paste this:
#ifdef __CHANGE_LOOK_SYSTEM__
static bool IsAntiFlag(DWORD dwFlag, DWORD dwAntiFlags)
{
	return (dwFlag & dwAntiFlags) != 0;
}

static bool ExcludeItems(DWORD dwVnum)
{
	if (dwVnum == 11901 || dwVnum == 11902 ||
		dwVnum == 11903	|| dwVnum == 11904 ||
		dwVnum == 11905 || dwVnum == 11906 ||
		dwVnum == 11907 || dwVnum == 11908 ||
		dwVnum == 11909	|| dwVnum == 11910 ||
		dwVnum == 11911	|| dwVnum == 11912 ||
		dwVnum == 11913	|| dwVnum == 11914 ||
		dwVnum == 50201	|| dwVnum == 50202
	)
		return true;
	else
		return false;
}

bool CHARACTER::SameItem(LPITEM item1, LPITEM item2)
{
	TItemTable const* table1 = item1->GetProto();
	TItemTable const* table2 = item2->GetProto();

	bool a[2] = {IsAntiFlag(ITEM_ANTIFLAG_WARRIOR, table1->dwAntiFlags), IsAntiFlag(ITEM_ANTIFLAG_WARRIOR, table2->dwAntiFlags)};
	bool b[2] = {IsAntiFlag(ITEM_ANTIFLAG_ASSASSIN, table1->dwAntiFlags), IsAntiFlag(ITEM_ANTIFLAG_ASSASSIN, table2->dwAntiFlags)};
	bool c[2] = {IsAntiFlag(ITEM_ANTIFLAG_SURA, table1->dwAntiFlags), IsAntiFlag(ITEM_ANTIFLAG_SURA, table2->dwAntiFlags)};
	bool d[2] = {IsAntiFlag(ITEM_ANTIFLAG_SHAMAN, table1->dwAntiFlags), IsAntiFlag(ITEM_ANTIFLAG_SHAMAN, table2->dwAntiFlags)};
#ifdef ENABLE_WOLFMAN_CHARACTER
	bool e[2] = {IsAntiFlag(ITEM_ANTIFLAG_WOLFMAN, table1->dwAntiFlags), IsAntiFlag(ITEM_ANTIFLAG_WOLFMAN, table2->dwAntiFlags)};
#endif

	if (ExcludeItems(item1->GetVnum()) || ExcludeItems(item2->GetVnum()))
		return false;

	if (item1->GetType() == ITEM_WEAPON && item2->GetType() == ITEM_WEAPON && item1->GetSubType() == item2->GetSubType() 
#ifdef __QUIVER_SYSTEM__
	&& item1->GetSubType() != WEAPON_ARROW && item2->GetSubType() != WEAPON_ARROW && item1->GetSubType() != WEAPON_QUIVER && item2->GetSubType() != WEAPON_QUIVER 
#else
	&& item1->GetSubType() != WEAPON_ARROW && item2->GetSubType() != WEAPON_ARROW 
#endif
	&& table1->bSize == table2->bSize 
	&& ((!a[1] && !a[2])
	|| (!b[1] && !b[2])
	|| (!c[1] && !c[2])
	|| (!d[1] && !d[2])
#ifdef ENABLE_WOLFMAN_CHARACTER
	|| (!e[1] && !e[2])
#endif
	))
		return true;
	else if (item1->GetType() == ITEM_ARMOR && item2->GetType() == ITEM_ARMOR && item1->GetSubType() == ARMOR_BODY && ARMOR_BODY == item2->GetSubType()
	&& table1->bSize == table2->bSize
	&& ((!a[1] && !a[2])
	|| (!b[1] && !b[2])
	|| (!c[1] && !c[2])
	|| (!d[1] && !d[2])
#ifdef ENABLE_WOLFMAN_CHARACTER
	|| (!e[1] && !e[2])
#endif
	))
		return true;
	else
		return false;
}
#endif
