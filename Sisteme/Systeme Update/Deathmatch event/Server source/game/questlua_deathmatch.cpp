#include "stdafx.h"

#include "questlua.h"
#include "questmanager.h"
#include "char.h"
#include "char_manager.h"
#include "Deathmatch.h"
#include "config.h"
#include "locale_service.h"
#include "gm.h"

#undef sys_err
#ifndef __WIN32__
#define sys_err(fmt, args...) quest::CQuestManager::instance().QuestError(__FUNCTION__, __LINE__, fmt, ##args)
#else
#define sys_err(fmt, ...) quest::CQuestManager::instance().QuestError(__FUNCTION__, __LINE__, fmt, __VA_ARGS__)
#endif

namespace quest
{
	int deathmatch_get_status(lua_State* L)
	{
		DeathMatchStatus ret = CDeathMatchManager::instance().GetStatus();
		lua_pushnumber(L, (int)ret);

		return 1;
	}

	int deathmatch_get_mapindex(lua_State* L)
	{
		lua_pushnumber(L, (int)DEATMATCH_MAP_INDEX);

		return 1;
	}

	int deathmatch_open(lua_State* L)
	{
		CDeathMatchManager::instance().SetStatus(DEATHMATCH_OPEN);

		return 1;
	}
	
	int deathmatch_start_event(lua_State* L)
	{
		CDeathMatchManager::instance().SetStatus(DEATHMATCH_STARTED);
		CDeathMatchManager::instance().StartEvent();
		CDeathMatchManager::instance().RemoveStuns();

		return 0;
	}

	int deathmatch_end_event(lua_State* L)
	{
		CDeathMatchManager::instance().SetHighScore(0,0);
		CDeathMatchManager::instance().CloseEvent();
		CDeathMatchManager::instance().SetStatus(DEATHMATCH_FINISH);

		return 0;
	}

	int deathmatch_join_spectator(lua_State* L)
	{
		LPCHARACTER pChar = CQuestManager::instance().GetCurrentCharacterPtr();
		if (pChar)
			CDeathMatchManager::instance().EnterSpectator(pChar);

		return 0;
	}

	int deathmatch_get_attender_count(lua_State* L)
	{
		lua_pushnumber(L, (int)CDeathMatchManager::instance().GetAttenderCount());
		return 1;
	}

	int deathmatch_get_spectator_count(lua_State* L)
	{
		lua_pushnumber(L, (int)CDeathMatchManager::instance().GetSpectatorCount());
		return 1;
	}

	int deathmatch_get_score(lua_State* L)
	{
		if (lua_isnumber(L, 1))
			lua_pushnumber(L, (int)CDeathMatchManager::instance().GetScore((int)lua_tonumber(L, 1)));

		return 1;
	}

	int deathmatch_get_high_score(lua_State* L)
	{
		lua_pushnumber(L, CDeathMatchManager::instance().GetHighScore());
		return 1;
	}

	int deathmatch_get_high_score_owner(lua_State* L)
	{
		DWORD dwOwnerPID = CDeathMatchManager::instance().GetHighScoreOwner();
		if (!dwOwnerPID){
			lua_pushnumber(L, 0);
			return 0;
		}

		LPCHARACTER pkHighScoreOwner = CHARACTER_MANAGER::instance().FindByPID(dwOwnerPID);
		if (!pkHighScoreOwner){
			lua_pushnumber(L, 0);
			return 0;
		}

		lua_pushstring(L, pkHighScoreOwner->GetName());
		return 1;
	}

	int deathmatch_give_item(lua_State* L)
	{
		if (lua_isnumber(L, 1) && lua_isnumber(L, 2))
			CDeathMatchManager::instance().GiveItemToAttender((int)lua_tonumber(L, 1), (int)lua_tonumber(L, 2));

		return 0;
	}

	int deathmatch_check_status(lua_State* L)
	{
		//CDeathMatchManager::instance().CheckEventStatus();
		if (CDeathMatchManager::instance().GetStatus() == DEATHMATCH_FINISH)
		{
			CDeathMatchManager::instance().SetStatus(DEATHMATCH_CLOSE);
			//CDeathMatchManager::instance().CloseEvent();

			SendNotice("Deathmatch etkinligi bitti");

			std::vector<std::string> gm_list = get_gm_list();
			std::vector<std::string>::const_iterator iter;

			for (iter = gm_list.begin(); iter != gm_list.end(); ++iter)
			{
				std::string charn = *iter;
				if (!charn.empty())
				{
					LPCHARACTER receiver = CHARACTER_MANAGER::instance().FindPC(charn.c_str());
					if (receiver != NULL)
						receiver->ChatPacket(CHAT_TYPE_INFO, "Etkinlik bitti lutfen panelden sonlandirin");
				}
			}
		}

		return 0;
	}
	
	void RegisterDeathMatchFunctionTable()
	{
		luaL_reg deathmatch_functions[] =
		{
			{	"get_status",				deathmatch_get_status				},
			{	"get_mapindex",				deathmatch_get_mapindex				},
			{	"check_status",				deathmatch_check_status				},

			{	"open",						deathmatch_open						},
			{	"start_event",				deathmatch_start_event				},
			{	"end_event",				deathmatch_end_event				},

			{	"join_spectator",			deathmatch_join_spectator			},

			{	"get_attender_count",		deathmatch_get_attender_count		},
			{	"get_spectator_count",		deathmatch_get_spectator_count		},

			{	"get_score",				deathmatch_get_score				},
			{	"get_high_score",			deathmatch_get_high_score			},
			{	"get_high_score_owner",		deathmatch_get_high_score_owner		},

			{	"give_item",				deathmatch_give_item				},

			{	NULL,						NULL								}
		};

		CQuestManager::instance().AddLuaFunctionTable("deathmatch", deathmatch_functions);
	}
}

