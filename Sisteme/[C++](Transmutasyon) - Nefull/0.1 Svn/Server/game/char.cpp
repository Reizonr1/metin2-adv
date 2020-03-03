// Search for:
			if (!m_pkSafebox->IsValidPosition(pItems->pos))
				continue;

			LPITEM item = ITEM_MANAGER::instance().CreateItem(pItems->vnum, pItems->count, pItems->id);

// Replace their function with:
			if (!m_pkSafebox->IsValidPosition(pItems->pos))
				continue;

#ifdef __CHANGE_LOOK_SYSTEM__
			LPITEM item = ITEM_MANAGER::instance().CreateItem(pItems->vnum, pItems->count, pItems->id, false, -1, false, pItems->dwVnum);
#else
			LPITEM item = ITEM_MANAGER::instance().CreateItem(pItems->vnum, pItems->count, pItems->id);
#endif

// Search for:
			if (!m_pkMall->IsValidPosition(pItems->pos))
				continue;

			LPITEM item = ITEM_MANAGER::instance().CreateItem(pItems->vnum, pItems->count, pItems->id);

// Replace their function with:
			if (!m_pkMall->IsValidPosition(pItems->pos))
				continue;

#ifdef __CHANGE_LOOK_SYSTEM__
			LPITEM item = ITEM_MANAGER::instance().CreateItem(pItems->vnum, pItems->count, pItems->id, false, -1, false, pItems->dwVnum);
#else
			LPITEM item = ITEM_MANAGER::instance().CreateItem(pItems->vnum, pItems->count, pItems->id);
#endif
