// 1) Search:
			char itemlink[256];
// 2) Replace with:
#ifdef ENABLE_CHANGELOOK_SYSTEM
			char itemlink[256 + 12];
#else
			char itemlink[256];
#endif


// 1) Search:
			len = snprintf(itemlink, sizeof(itemlink), "item:%x:%x:%x:%x:%x", htoi(results[1].c_str()), htoi(results[2].c_str()), htoi(results[3].c_str()), htoi(results[4].c_str()), htoi(results[5].c_str()));
// 2) After this make a new line and paste:
#ifdef ENABLE_CHANGELOOK_SYSTEM
			len += snprintf(itemlink + len, sizeof(itemlink) - len, ":%x", htoi(results[6].c_str()));
#endif


// 1) Search:
			if (results.size() >= 8)
// 2) Replace with:
#ifdef ENABLE_CHANGELOOK_SYSTEM
			if (results.size() >= 9)
#else
			if (results.size() >= 8)
#endif


// 1) Search:
				for (int i = 6; i < results.size(); i += 2)
// 2) Replace with:
#ifdef ENABLE_CHANGELOOK_SYSTEM
				for (int i = 7; i < results.size(); i += 2)
#else
				for (int i = 6; i < results.size(); i += 2)
#endif