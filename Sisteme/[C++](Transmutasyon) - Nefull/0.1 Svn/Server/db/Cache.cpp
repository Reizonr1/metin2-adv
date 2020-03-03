// Search for:
		int iLen = snprintf(szColumns, sizeof(szColumns), "id, owner_id, window, pos, count, vnum");

// Replace with:
#ifdef __CHANGE_LOOK_SYSTEM__
		int iLen = snprintf(szColumns, sizeof(szColumns), "id, owner_id, window, pos, count, vnum, dwVnum");
#else
		int iLen = snprintf(szColumns, sizeof(szColumns), "id, owner_id, window, pos, count, vnum");
#endif

// Search for:
		int iValueLen = snprintf(szValues, sizeof(szValues), "%u, %u, %d, %d, %u, %u",
				p->id, p->owner, p->window, p->pos, p->count, p->vnum);

// Replace with:
#ifdef __CHANGE_LOOK_SYSTEM__
		int iValueLen = snprintf(szValues, sizeof(szValues), "%u, %u, %d, %d, %u, %u, %u",
				p->id, p->owner, p->window, p->pos, p->count, p->vnum, p->dwVnum);
#else
		int iValueLen = snprintf(szValues, sizeof(szValues), "%u, %u, %d, %d, %u, %u",
				p->id, p->owner, p->window, p->pos, p->count, p->vnum);
#endif

// Search for:
		int iUpdateLen = snprintf(szUpdate, sizeof(szUpdate), "owner_id=%u, window=%d, pos=%d, count=%u, vnum=%u",
				p->owner, p->window, p->pos, p->count, p->vnum);

// Replace with:
#ifdef __CHANGE_LOOK_SYSTEM__
		int iUpdateLen = snprintf(szUpdate, sizeof(szUpdate), "owner_id=%u, window=%d, pos=%d, count=%u, vnum=%u, dwVnum=%u",
				p->owner, p->window, p->pos, p->count, p->vnum, p->dwVnum);
#else
		int iUpdateLen = snprintf(szUpdate, sizeof(szUpdate), "owner_id=%u, window=%d, pos=%d, count=%u, vnum=%u",
				p->owner, p->window, p->pos, p->count, p->vnum);
#endif