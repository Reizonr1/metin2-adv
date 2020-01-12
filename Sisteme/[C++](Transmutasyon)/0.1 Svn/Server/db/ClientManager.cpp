// Search for:
				"SELECT id, window+0, pos, count, vnum, socket0, socket1, socket2, "

// Replace with:
#ifdef __CHANGE_LOOK_SYSTEM__
				"SELECT id, window+0, pos, count, vnum, dwVnum, socket0, socket1, socket2, "
#else
				"SELECT id, window+0, pos, count, vnum, socket0, socket1, socket2, "
#endif

// Search for:
			"REPLACE INTO item%s (id, owner_id, window, pos, count, vnum, socket0, socket1, socket2, "

// Replace with:
#ifdef __CHANGE_LOOK_SYSTEM__
			"REPLACE INTO item%s (id, owner_id, window, pos, count, vnum, dwVnum, socket0, socket1, socket2, "
#else
			"REPLACE INTO item%s (id, owner_id, window, pos, count, vnum, socket0, socket1, socket2, "
#endif

// Search for:
			"VALUES(%u, %u, %d, %d, %u, %u, %ld, %ld, %ld, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)",

// Replace with:
#ifdef __CHANGE_LOOK_SYSTEM__
			"VALUES(%u, %u, %d, %d, %u, %u, %u, %ld, %ld, %ld, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)",
#else
			"VALUES(%u, %u, %d, %d, %u, %u, %ld, %ld, %ld, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)",
#endif

// Search for:
			p->vnum,

// Add Under:
#ifdef __CHANGE_LOOK_SYSTEM__
			p->dwVnum,
#endif
