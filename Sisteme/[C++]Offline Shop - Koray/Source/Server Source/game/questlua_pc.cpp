Search:
#include "mob_manager.h"

Add it under:
#include "shop_manager.h"
#include "shop.h"

---

Search:
		lua_pushnumber(L, ch->ChangeEmpire((unsigned char)lua_tonumber(L, 1)));

Add it upper:
#ifdef __OFFLINE_SHOP__
		if (ch && ch->CanChangeEmpireOfflineShopCheck() == false) {
			ch->ChatPacket(CHAT_TYPE_INFO, "You can't change your empire while you have an offline shop in your account.");
			lua_pushnumber(L, 4);
			return 0;
		}
#endif

https://puu.sh/sgHrq/02d5bda947.png

---

Search:
		if ( check_name(szName) == false )
		{
			lua_pushnumber(L, 2);
			return 1;
		}

Add it under:
#ifdef __OFFLINE_SHOP__
		if (CShopManager::instance().GetOfflineShopCount(ch->GetPlayerID()) > 0)
		{
			lua_pushnumber(L, 5);
			return 1;
		}
#endif

https://puu.sh/sgHsJ/d6cf30d9a3.png

---

Search:
int pc_is_dead(lua_State* L)
{
	...
}

Add it upper:
#ifdef __OFFLINE_SHOP__
	int pc_has_offlineshop(lua_State* L)
	{
		LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();
		if (ch == NULL)
		{
			lua_pushboolean(L, false);
			return 1;
		}

		if (ch && ch->GetMyShop() && ch->GetMyShop()->GetPCShop() && !ch->GetMyShop()->GetPCShop()->IsPC())
		{
			lua_pushboolean(L, true);
			return 1;
		}

		lua_pushboolean(L, false);
		return 1;
	}

	int pc_get_offlineshop_count(lua_State* L)
	{
		LPCHARACTER ch = CQuestManager::instance().GetCurrentCharacterPtr();
		if (ch == NULL)
		{
			lua_pushnumber(L, 0);
			return 1;
		}

		if (ch && ch->GetMyShop() && ch->GetMyShop()->GetPCShop() && !ch->GetMyShop()->GetPCShop()->IsPC())
		{
			lua_pushnumber(L, CShopManager::instance().GetOfflineShopCount(ch->GetPlayerID()));
			return 1;
		}

		lua_pushnumber(L, 0);
		return 1;
	}
#endif

https://puu.sh/sgHwl/789659dc89.png

---

Search:
			{ NULL,										NULL									}
		};

		CQuestManager::instance().AddLuaFunctionTable("pc", pc_functions);

Add it upper:
#ifdef __OFFLINE_SHOP__
			{ "has_offlineshop",						pc_has_offlineshop						},
			{ "get_offlineshop_count",					pc_get_offlineshop_count				},
#endif

https://puu.sh/sgHxO/cdd4b29f1d.png