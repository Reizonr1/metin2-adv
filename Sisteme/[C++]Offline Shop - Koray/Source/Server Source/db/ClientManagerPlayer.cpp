Search:
			while (it != pSet->end())
			{
				CItemCache * c = *it++;
				TPlayerItem * p = c->Get();

				if (p->vnum) // vnumÀÌ ¾øÀ¸¸é »èÁ¦µÈ ¾ÆÀÌÅÛÀÌ´Ù.
					thecore_memcpy(&s_items[dwCount++], p, sizeof(TPlayerItem));
			}

			if (g_test_server)
				sys_log(0, "ITEM_CACHE: HIT! %s count: %u", pTab->name, dwCount);

Change:
			while (it != pSet->end())
			{
				CItemCache * c = *it++;
				TPlayerItem * p = c->Get();

#ifdef __OFFLINE_SHOP__
				if (p->vnum && (p->window == INVENTORY || p->window == EQUIPMENT))
#else
				if (p->vnum) // vnumÀÌ ¾øÀ¸¸é »èÁ¦µÈ ¾ÆÀÌÅÛÀÌ´Ù.
#endif
					thecore_memcpy(&s_items[dwCount++], p, sizeof(TPlayerItem));
			}

			if (g_test_server)
				sys_log(0, "ITEM_CACHE: HIT! %s count: %u", pTab->name, dwCount);


http://i.imgur.com/zE5VF4o.png