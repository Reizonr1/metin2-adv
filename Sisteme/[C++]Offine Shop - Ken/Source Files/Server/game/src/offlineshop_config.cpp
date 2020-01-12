#include "stdafx.h"
#include "utils.h"
#include "log.h"
#include "config.h"
#include "offlineshop_config.h"
#include <sstream>

enum
{
	GOLD_MAX = 2000000000,
	ITEM_MAX_COUNT = 200,
	ITEM_SOCKET_MAX_NUM = 3,
};

using namespace std;

BYTE g_bOfflineShopSaveTime = 5;

bool g_bNeededMoney = false;
DWORD g_dwNeedMoney = 0;

bool g_bNeededItem = false;
int g_iItemVnum = 0;
BYTE g_bItemCount = 0;

bool g_bOfflineShopMapAllowLimit = false;
static set<int> s_set_offlineshop_map_allows;

BYTE g_bOfflineShopSocketMax = 3;

int g_iTotalOfflineShopCount = 1000;

bool g_bNeedMinLevel = false;
BYTE g_bMinLevel = 10;

WORD g_wCoinsForUnlimited = 0;
bool g_bEnableEmpireLimit = false;

bool offlineshop_map_allow_find(int iMapIndex)
{
	if (g_bAuthServer)
		return false;

	if (s_set_offlineshop_map_allows.find(iMapIndex) == s_set_offlineshop_map_allows.end())
		return false;

	return true;
}

void offlineshop_map_allow_add(int iMapIndex)
{
	if (offlineshop_map_allow_find(iMapIndex))
	{
		sys_err("Multiple map allow detected in OFFLINE_SHOP_CONFIG [iMapIndex:%d]", iMapIndex);
		exit(1);
	}

	fprintf(stdout, "OFFLINSHOP_MAP_ALLOW: %d\n", iMapIndex);
	s_set_offlineshop_map_allows.insert(iMapIndex);
}

void offlineshop_config_init()
{
	if (g_bAuthServer)
		return;

	FILE * file;
	char buf[256], token_string[256], value_string[256];

	if (!(file = fopen("OFFLINE_SHOP_CONFIG", "r")))
	{
		fprintf(stderr, "Cannot open [OFFLINE_SHOP_CONFIG]\n");
		exit(1);
	}

	while (fgets(buf, sizeof(buf), file))
	{
		parse_token(buf, token_string, value_string);

		TOKEN("OFFLINE_SHOP_SAVE_TIME")
		{
			str_to_number(g_bOfflineShopSaveTime, value_string);
			g_bOfflineShopSaveTime = MINMAX(1, g_bOfflineShopSaveTime, 10);
			fprintf(stdout, "OFFLINE_SHOP_SAVE_TIME: %d", g_bOfflineShopSaveTime);
		}

		TOKEN("OFFLINE_SHOP_NEED_MONEY")
		{
			char arg1[256], arg2[256];
			two_arguments(value_string, arg1, sizeof(arg1), arg2, sizeof(arg2));

			if (!*arg1 || !*arg2)
			{
				fprintf(stderr, "OFFLINE_SHOP_NEED_MONEY syntax: offline_shop_need_money <disable or enable> <money>");
				exit(1);
			}
			else if (!isnhdigit(*arg2))
			{
				fprintf(stderr, "Second argument must be an integer!");
				exit(1);
			}

			g_bNeededMoney = isnhdigit(*arg1) ? str_to_number(g_bNeededMoney, arg1) : strcmp(arg1, "enable");
			
			str_to_number(g_dwNeedMoney, arg2);
			g_dwNeedMoney = MINMAX(1, g_dwNeedMoney, GOLD_MAX);

			fprintf(stderr, "OFFLINE_SHOP_NEED_MONEY: %s - Money %u", g_bNeededMoney ? "Enabled" : "Disabled", g_dwNeedMoney);
		}

		TOKEN("OFFLINE_SHOP_TOTAL_COUNT")
		{
			str_to_number(g_iTotalOfflineShopCount, value_string);
			fprintf(stderr, "OFFLINE_SHOP_TOTAL_COUNT: %d", g_iTotalOfflineShopCount);
			continue;
		}

		TOKEN("OFFLINE_SHOP_NEED_ITEM")
		{
			char arg1[256], arg2[256], arg3[256];
			three_arguments(value_string, arg1, sizeof(arg1), arg2, sizeof(arg2), arg3, sizeof(arg3));

			if (!*arg1 || !*arg2 || !*arg3)
			{
				fprintf(stderr, "OFFLINE_SHOP_NEED_ITEM syntax: offline_shop_need_item <enable or disable> <item_vnum> <item_count>");
				exit(1);
			}
			else if (!isnhdigit(*arg2) || !isnhdigit(*arg3))
			{
				fprintf(stderr, "Second argument and third argument must be an integer!");
				exit(1);
			}

			g_bNeededItem = isnhdigit(*arg1) ? str_to_number(g_bNeededItem, arg1) : strcmp(arg1, "enable");
			
			str_to_number(g_iItemVnum, arg2);
			str_to_number(g_bItemCount, arg3);
			fprintf(stderr, "OFFLINE_SHOP_NEED_ITEM: %s %d %d", g_bNeededItem ? "Enabled" : "Disabled", g_iItemVnum, g_bItemCount);			
		}

		TOKEN("ENABLE_OFFLINE_SHOP_MAP_ALLOW_LIMIT")
		{
			char arg1[256];
			one_argument(value_string, arg1, sizeof(arg1));

			if (!*arg1)
			{
				fprintf(stderr, "OFFLINE_SHOP_MAP_ALLOW_LIMIT syntax: offline_shop_map_allow_limit <enable or disable> or < 0 or 1 >");
				exit(1);
			}

			if (!strcmp(arg1, "enable"))
				g_bOfflineShopMapAllowLimit = true;
			else if (!strcmp(arg1, "disable"))
				g_bOfflineShopMapAllowLimit = false;
			else if (isnhdigit(*arg1))
				str_to_number(g_bOfflineShopMapAllowLimit, arg1);
		}

		TOKEN("OFFLINE_SHOP_MAP_ALLOW")
		{
			if (!g_bOfflineShopMapAllowLimit)
			{
				fprintf(stderr, "ENABLE_OFFLINE_SHOP_MAP_ALLOW_LIMIT must be enable for this option!");
				exit(1);
			}

			char * p = value_string;
			string stNum;

			for (; *p; p++)
			{
				if (isnhspace(*p))
				{
					if (stNum.length())
					{
						int index = 0;
						str_to_number(index, stNum.c_str());
						offlineshop_map_allow_add(index);
						stNum.clear();
					}
				}
				else
					stNum += *p;
			}

			if (stNum.length())
			{
				int index = 0;
				str_to_number(index, stNum.c_str());
				offlineshop_map_allow_add(index);
			}

			continue;
		}

		TOKEN("OFFLINE_SHOP_SOCKET_MAX")
		{
			str_to_number(g_bOfflineShopSocketMax, value_string);
			g_bOfflineShopSocketMax = MINMAX(ITEM_SOCKET_MAX_NUM, g_bOfflineShopSocketMax, 6);
			fprintf(stderr, "OFFLINE_SHOP_SOCKET_MAX: %d", g_bOfflineShopSocketMax);
		}

		TOKEN("MIN_LEVEL")
		{
			char arg1[256], arg2[256];
			two_arguments(value_string, arg1, sizeof(arg1), arg2, sizeof(arg2));

			if (!*arg1 || !*arg2)
			{
				fprintf(stderr, "Syntax error! MIN_LEVEL: <enable or disable> <min level>");
				exit(1);
			}

			if (!isnhdigit(*arg2))
			{
				fprintf(stderr, "Min level must be an integer!");
				exit(2);
			}

			g_bNeedMinLevel = isnhdigit(*arg1) ? str_to_number(g_bNeedMinLevel, arg1) : strcmp(arg1, "enable");
			str_to_number(g_bMinLevel, arg2);

			fprintf(stderr, "OFFLINE_SHOP_NEED_MIN_LEVEL: %d", g_bMinLevel);
		}

		TOKEN("COINS_FOR_UNLIMITED")
		{
			char arg1[256];
			one_argument(value_string, arg1, sizeof(arg1));

			if (!isnhdigit(*arg1))
			{
				fprintf(stderr, "First argument must be an integer!");
				exit(2);
			}

			str_to_number(g_wCoinsForUnlimited, arg1);
			fprintf(stderr, "COINS_FOR_UNLIMTED: %d", g_wCoinsForUnlimited);
		}

		TOKEN("EMPIRE_LIMIT")
		{
			str_to_number(g_bEnableEmpireLimit, value_string);
			fprintf(stderr, "EMPIRE_LIMIT: %s", g_bEnableEmpireLimit ? "enabled" : "disabled");			
		}
	}
}